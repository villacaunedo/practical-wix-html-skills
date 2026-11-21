---
name: ordered-photo-captions
description: Insert supplied image URLs and exact captions in an explicitly agreed order in existing HTML, and repair responsive captioned galleries. Use for ordered photo placement, figure/figcaption markup, clipped captions, image overflow, or unwanted gaps in mobile grids. Preserve unrelated text, links, metadata, image loading intent, and locale parity.
---

# Ordered photo captions

1. Read the supplied HTML/CSS and ordered image/caption list. Inventory the image slots, existing URLs, classes, dimensions, loading attributes, and any hero. Request missing source or ambiguous mappings rather than inventing URLs or place names. A mismatch between the page topic and captions must be resolved before insertion.
2. Make a mapping table: slot, source URL, exact caption, alt text, caption policy. Follow the user's order and explicit duplicates. A hero can have no visible caption if that is the agreed policy; do not assume the first image is always a hero or the page's LCP. Treat supplied captions as text, escaping HTML special characters.
3. Preserve the layout's intent. Wrap each captioned image in `figure` and add `figcaption`. Transfer a layout class to the wrapper only after reviewing every selector that uses it; keep image-specific styles on the image. Reset the browser's default figure margins. Do not copy fixed example dimensions to unrelated images.

```css
.sample-gallery { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 1rem; }
.sample-gallery__photo {
  margin: 0; min-width: 0; display: flex; flex-direction: column;
  border-radius: .75rem; overflow: hidden; background: #122c23; color: #fff;
}
.sample-gallery__photo img {
  width: 100%; height: 12rem; object-fit: cover; display: block;
}
.sample-gallery__photo figcaption {
  padding: .75rem; overflow-wrap: anywhere; flex: 0 0 auto;
}
@media (max-width: 700px) {
  .sample-gallery { grid-template-columns: repeat(2,minmax(0,1fr)); }
  .sample-gallery__photo:last-child:nth-child(odd) { grid-column: 1 / -1; }
}
@media (max-width: 380px) {
  .sample-gallery { grid-template-columns: minmax(0,1fr); }
}
```

4. Prefer auto-height gallery rows so captions can grow at zoom and in translation. If the original must keep fixed-height cells, reserve enough space for captions and let the image shrink using flex/min-height rules; test long captions rather than clipping them to retain an arbitrary height. Review competing `display`, sizing, and overflow rules. Never globally override all figure/image classes.
5. Preserve hero eager loading/high priority where appropriate; keep known below-fold images lazy. Do not assign priority or lazy loading solely from list position. Preserve or supply truthful intrinsic dimensions; do not invent an aspect ratio. Use descriptive alt text for informative images and empty alt for decorative images; avoid keyword stuffing.
6. If a two-column mobile grid has an unwanted final gap, apply the odd-last-child selector only within that grid's two-column breakpoint. An even number must remain paired. Adapt the rule for a different column count rather than using last-child full width unconditionally.
7. For paired language versions, retain URL order and explicit duplicates. Translate descriptive text but preserve proper names unless the user supplied a conventional translation.
8. Verify image/caption counts against the mapping, compare ordered URLs and captions, confirm no unintended duplication, and diff unrelated links/text/metadata. Preview narrow mobile and desktop sizes, odd/even item counts, long captions, and text zoom. Check for horizontal overflow and clipped captions. If a browser is unavailable, distinguish structural checks from pending visual checks.
9. Deliver a reviewable patch with the mapping, checks actually run, and unresolved issues. Do not publish unless requested.

Use `assets/example.html` as an offline gallery example with synthetic SVG images. It demonstrates three and four items and a long caption; it does not prove behavior inside Wix. Editing an embed does not create native Wix content or establish indexing changes.
