# Practical Wix & HTML Skills

Two focused skills for Claude Code and other agents that support `SKILL.md` instructions, adapted from workflows used to maintain Villa Caunedo's website in Asturias, Spain.

| Skill | Purpose |
| --- | --- |
| `hero-readability` | Improve text readability over hero images with scoped CSS, keeping links and image loading behavior intact. |
| `ordered-photo-captions` | Map supplied images to captions in an explicit order and prevent responsive gallery overflow. |

## Install in Claude Code

Clone `https://github.com/villacaunedo/practical-wix-html-skills.git`, then copy either skill directory from `skills/` into `~/.claude/skills/` (for all projects) or `.claude/skills/` (for one project). Do not replace an existing directory without reviewing it first.

Each skill includes a self-contained HTML/CSS example in `assets/`. No customer data, external images, desktop paths, browser extension, credentials, or additional skills are required to read the instructions or open the examples. Applying them to your own project requires access to its HTML/CSS and images. A browser is needed for visual checks.

Example requests:

- "Use hero-readability to improve this page's white title over its bright hero photograph. Preserve the photo and links."
- "Use ordered-photo-captions to insert these three image URLs and exact captions in the supplied order; check the mobile gallery."

## Scope and limitations

These skills operate on HTML/CSS. A Wix HTML embed is distinct from native Wix text. These examples do not implement native Wix components or demonstrate indexing improvements. CSS classes must be adapted to the target document. Readability must be checked with the actual image at the relevant breakpoints; a shadow or gradient alone does not establish WCAG compliance.

## Validation

Run `python scripts/check_examples.py` (Python 3 standard library only) for structural checks and `python scripts/serve_examples.py`, then open the printed local address for visual review. Structural checks do not assess browser layout, accessibility compliance, or production Wix behavior. See `VALIDATION.md` for what was actually checked.

## Contributing

Report the skill, a minimal reproducible HTML/CSS example, viewport size, expected behavior, and actual behavior. Remove personal data and use images you have permission to redistribute. Preserve source attribution. Proposals should include relevant checks and clearly state remaining limitations.

## Origin and license

Maintainer: Miguel Palacio Hurle (GitHub: villacaunedo). Adapted from `hero-contraste-legibilidad` and `optimizacion-fotos` workflows in the private Villa Caunedo collection. This release candidate contains two newly generalized instruction sets and synthetic examples; it does not include Humanizer or other third-party skills. Released under MIT; see `LICENSE`.

Status: initial public release candidate, 21 November 2026. No independent user adoption metrics are available yet.
