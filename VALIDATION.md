# Validation record

21 November 2026 — release candidate, not a public adoption report.

## Executed

- Both skill instruction files passed the skill metadata validator (YAML frontmatter, required fields, naming rules).
- `python scripts/check_examples.py` passed for both bundled examples: image counts, intrinsic SVG dimensions, decorative alt policy, caption count/order, unique IDs, local link/label targets, no scripts/iframes, and expected layering/responsive CSS markers.
- An independent agent applied both skills to a new synthetic hero and four-image gallery. Preservation, ordered-source and caption-count checks passed; browser layout and measured contrast were not verified.
- Both example pages returned HTTP 200 through a local Python HTTP server.
- Examples use only newly authored inline synthetic SVGs, system fonts, and local HTML/CSS; no production photographs or user data are included.

## Limits

These are metadata, structural, and serving checks. They do not establish computed browser layout, measured contrast, WCAG compliance, mobile rendering, SEO results, native Wix compatibility, or user adoption.

Before a stable release, visually check actual target pages at 360px, 600px and desktop widths; long headings/captions; odd/even galleries; text zoom; keyboard focus and link usability. Measure contrast over real background photographs. Review patches against original text, URLs and metadata.

## Reproduce structural checks

Python 3, no dependencies: `python scripts/check_examples.py`.
For manual inspection: `python scripts/serve_examples.py`.
