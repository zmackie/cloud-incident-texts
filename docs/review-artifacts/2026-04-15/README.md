# Review Artifacts - 2026-04-15

Validation run summary:

- Corpus analyzed: `134` incidents
- Unique ATT&CK techniques in corpus: `178`
- Total attack-chain steps: `974`
- Browser validation target: `http://127.0.0.1:4321/cloud-incident-texts`

Captured screenshots:

- `home.png`: heatmap homepage rendered from generated `site/public/data`
- `incidents.png`: incidents index rendered from generated corpus
- `graph.png`: cross-incident attack graph rendered from generated corpus
- `incident-cloudflare.png`: incident detail page for a previously empty-chain case
- `incident-google-unc4899.png`: incident detail page for the UNC4899 case-study outlier
- `browser-check.json`: rendered-page counts captured via Playwright

Key commands used:

- `uv run scripts/analyze.py --workers 4 --ensure-attack-data`
- `uv run scripts/build_site_data.py`
- `npm run build`
- `npm run preview -- --host 127.0.0.1 --port 4321`
