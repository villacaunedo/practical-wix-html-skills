---
name: hero-readability
description: Improve text readability over hero photographs using scoped HTML/CSS overlays and optional text shadows. Use when a hero title or subtitle is lost against a bright or detailed background. Preserve image URLs, links, layout intent, and unrelated content; verify with the actual image at mobile and desktop sizes.
---

# Hero readability

1. Inspect the supplied HTML/CSS and identify the hero, image/background, existing overlay, text, and calls to action. If the source is missing, request it. Work in the supplied project; never assume a desktop path or another skill exists.
2. Record the image URLs, image loading attributes, text, destinations, and existing dimensions. Preserve them. Scope new CSS to this hero rather than generic headings or every pill on the page. Make a reviewable patch; do not publish unless requested.
3. Identify the text position at each breakpoint. Add a decorative layer between the image and text, preserving the original overlay. Set `aria-hidden="true"` and `pointer-events: none`. Ensure the hero establishes a containing/stacking context, and keep interactive text above both overlays. Avoid negative stacking that can put the image behind the page.
4. Start with a localized radial darkening for light text. Adapt the center to the actual text position and tune opacity for the image. Do not darken or filter the entire image automatically. Use a subtle text shadow only as an additional treatment.

```css
.sample-hero { position: relative; isolation: isolate; }
.sample-hero__shade {
  position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: radial-gradient(ellipse 85% 90% at 40% 55%,
    rgb(0 0 0 / 82%) 0%, rgb(0 0 0 / 62%) 60%, transparent 100%);
}
.sample-hero__content { position: relative; z-index: 2; }
.sample-hero__title, .sample-hero__subtitle {
  text-shadow: 0 1px 3px rgb(0 0 0 / 55%);
}
```

5. For text aligned differently on mobile, adjust the gradient center/extent there. Long text may need a larger dark region or a solid text backing instead of stronger shadows. Keep the layout flexible and avoid fixed heights that crop wrapped content.
6. Do not use canvas pixel sampling unless specifically needed and supported. Cross-origin pixel reads depend on image server CORS settings; do not assume all Wix images permit or forbid them. CSS overlays avoid that dependency.
7. Open the actual page at narrow mobile and desktop sizes and with a long heading. Check readable text over the lightest areas, wrapping, no horizontal scrolling, working links, keyboard focus, and unchanged image behavior. Measure contrast over representative background regions: aim for at least 4.5:1 for normal text and 3:1 for qualifying large text. Do not claim compliance from shadow/overlay presence alone. If visual or contrast tools are unavailable, report those checks as pending.
8. Compare before/after text, image URLs and attributes, and link destinations. Report the patch, checks performed, and unresolved limitations.

Use `assets/example.html` for a synthetic, offline example of the layering pattern. It is not a production photograph contrast test. CSS names are illustrative: map them to the target page instead of adding duplicate heroes. If the page is a Wix embed, do not claim the patch creates native Wix text or improves Google indexing.
