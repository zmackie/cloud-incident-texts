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
    heuristic_clean,
    parse_jina_header,
    verify_body_is_subset,
)

FIXTURE = ROOT / "data" / "articles" / "aws-2023-august" / "link_00.raw.md"


@pytest.fixture
def raw_text() -> str:
    return FIXTURE.read_text(encoding="utf-8")


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
