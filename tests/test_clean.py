"""
Tests for scripts/clean.py — diffable cleanup.

Core invariant: every non-blank content line in the cleaned body must appear
verbatim as a full line in the raw body. Cleaning is allowed to *delete*
lines but never to rewrite them.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from clean import (  # noqa: E402
    Cleaned,
    apply_drops,
    clean_markdown,
    extract_json_object,
    heuristic_clean,
    parse_jina_header,
    verify_body_is_subset,
)

# Raw Jina output in the new scheme lives at link_NN.md (cleaned output is
# link_NN.clean.md). The aws-2023-august/link_00 fixture was chosen because
# it exercises a full cookie-banner preamble + real article body.
FIXTURE = ROOT / "data" / "articles" / "aws-2023-august" / "link_00.md"


@pytest.fixture
def raw_text() -> str:
    return FIXTURE.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# extract_json_object: tolerates trailing commentary / code fences
# ---------------------------------------------------------------------------

def test_extract_json_plain():
    assert extract_json_object('{"a": 1}') == {"a": 1}


def test_extract_json_with_code_fence():
    assert extract_json_object('```json\n{"a": 1}\n```') == {"a": 1}


def test_extract_json_with_trailing_commentary():
    """The failure mode we saw on open-exchange-rates-2020-march."""
    raw = (
        '```json\n'
        '{\n  "title": "x",\n  "drop_ranges": [[1, 10]]\n}\n'
        '```\n\n'
        'Wait, let me reconsider. The page is boilerplate...'
    )
    obj = extract_json_object(raw)
    assert obj == {"title": "x", "drop_ranges": [[1, 10]]}


def test_extract_json_with_nested_braces():
    raw = '{"a": {"b": 1}, "c": [{"d": 2}]}'
    assert extract_json_object(raw) == {"a": {"b": 1}, "c": [{"d": 2}]}


def test_extract_json_returns_none_on_garbage():
    assert extract_json_object("not json at all") is None


# ---------------------------------------------------------------------------
# apply_drops: pure line-slicing primitive
# ---------------------------------------------------------------------------

def test_apply_drops_removes_inclusive_ranges():
    body = "a\nb\nc\nd\ne"
    assert apply_drops(body, [(2, 3)]) == "a\nd\ne"


def test_apply_drops_handles_multiple_disjoint_ranges():
    body = "a\nb\nc\nd\ne\nf"
    assert apply_drops(body, [(1, 1), (4, 5)]) == "b\nc\nf"


def test_apply_drops_empty_ranges_returns_body_unchanged():
    body = "a\nb\nc"
    assert apply_drops(body, []) == body


# ---------------------------------------------------------------------------
# verify_body_is_subset: the diffability guarantee
# ---------------------------------------------------------------------------

def test_verify_subset_true_when_clean_lines_all_present_in_raw():
    raw = "junk\nreal line 1\nreal line 2\nfooter junk"
    clean = "real line 1\nreal line 2"
    assert verify_body_is_subset(clean, raw) is True


def test_verify_subset_false_when_a_line_was_rewritten():
    raw = "real line 1\nreal line 2"
    clean = "real line 1\nreal line 2 (edited)"
    assert verify_body_is_subset(clean, raw) is False


def test_verify_subset_ignores_blank_lines():
    raw = "a\nb"
    clean = "\na\n\nb\n"
    assert verify_body_is_subset(clean, raw) is True


def test_clean_preserves_indented_first_line(raw_text: str):
    """
    Regression: apply_drops(...).strip() used to mangle the first content
    line if it had leading whitespace (e.g. indented code block, list
    continuation). That broke the subset check.
    """
    # Build a minimal raw body where the first non-blank line is indented.
    body = "    indented first line\nnormal line\n"
    # Simulate a drop that leaves the full body intact.
    from clean import apply_drops as _apply_drops  # noqa: E402
    from clean import verify_body_is_subset as _verify  # noqa: E402
    out = _apply_drops(body, [])
    # Our cleaner strips *blank* boundary lines but not *within* a line.
    # Exercise the cleaner end-to-end by constructing a synthetic raw.
    synthetic = "Title: x\nURL Source: y\nPublished Time: z\nMarkdown Content:\n\n    indented first line\nnormal line\n"
    result = clean_markdown(synthetic, use_llm=False)
    assert _verify(result.body_md, body)
    assert "    indented first line" in result.body_md


# ---------------------------------------------------------------------------
# heuristic_clean on the real fixture
# ---------------------------------------------------------------------------

def test_heuristic_strips_cookie_banner(raw_text: str):
    body = parse_jina_header(raw_text)["body"]
    cleaned_body = heuristic_clean(body, title="Two real-life examples")
    assert "Select your cookie preferences" not in cleaned_body
    assert "Accept Decline Customize" not in cleaned_body


def test_heuristic_keeps_article_body(raw_text: str):
    body = parse_jina_header(raw_text)["body"]
    cleaned_body = heuristic_clean(body, title="Two real-life examples")
    assert "Welcome to another blog post" in cleaned_body
    assert "Story 1: On the hunt for credentials" in cleaned_body


def test_heuristic_output_is_line_subset_of_raw(raw_text: str):
    body = parse_jina_header(raw_text)["body"]
    cleaned_body = heuristic_clean(body, title="Two real-life examples")
    assert verify_body_is_subset(cleaned_body, body), (
        "heuristic cleaner must not rewrite lines"
    )


# ---------------------------------------------------------------------------
# clean_markdown end-to-end with use_llm=False
# ---------------------------------------------------------------------------

def test_clean_markdown_no_llm_produces_diffable_output(raw_text: str):
    result = clean_markdown(
        raw_text,
        url="https://aws.amazon.com/blogs/security/two-real-life-examples",
        source_type="article",
        use_llm=False,
    )
    assert isinstance(result, Cleaned)
    assert result.cleanup_method == "fallback_heuristic"
    assert result.body_md
    body = parse_jina_header(raw_text)["body"]
    assert verify_body_is_subset(result.body_md, body)


def test_clean_markdown_extracts_title_from_jina_header(raw_text: str):
    result = clean_markdown(raw_text, use_llm=False)
    assert "Two real-life examples" in result.title


def test_clean_markdown_sets_drop_ranges(raw_text: str):
    result = clean_markdown(raw_text, use_llm=False)
    assert result.drop_ranges, "heuristic must record which lines it dropped"
    # ranges must be valid (start <= end, positive)
    for start, end in result.drop_ranges:
        assert 1 <= start <= end


# ---------------------------------------------------------------------------
# Regression: heading titles wrapped in markdown links should not cause the
# heuristic to repeatedly "match" title_needle against URL slug text and
# land start_idx at a late section.
# ---------------------------------------------------------------------------

def test_heuristic_ignores_slug_in_linked_headings():
    body = (
        "Junk preamble line\n"
        "# [Real Article Title](https://site.tld/real-article-title)\n"
        "Body paragraph one.\n"
        "## [Indicators of Compromise](https://site.tld/real-article-title#iocs)\n"
        "IoC content that must not become the sole surviving section.\n"
    )
    cleaned = heuristic_clean(body, title="Real Article Title")
    assert "Body paragraph one." in cleaned, (
        "linked section heading must not hijack start_idx away from the "
        "real title heading"
    )
    assert "Real Article Title" in cleaned


# ---------------------------------------------------------------------------
# Regression: re-running clean on a file that already has frontmatter must
# be idempotent — no nested `---` frontmatter blocks.
# ---------------------------------------------------------------------------

def test_clean_markdown_already_clean_is_idempotent():
    already = (
        "---\n"
        'title: "Something"\n'
        'url: "https://example.com/x"\n'
        "---\n"
        "\n"
        "Real body text.\n"
    )
    result = clean_markdown(already, use_llm=False)
    assert result.cleanup_method == "already_clean"
    rendered = result.to_markdown()
    assert rendered.count("---\n") == 2, (
        f"expected exactly one frontmatter block, got: {rendered!r}"
    )
    # Round-trip: rendering then re-cleaning yields the same output.
    result2 = clean_markdown(rendered, use_llm=False)
    assert result2.to_markdown() == rendered
