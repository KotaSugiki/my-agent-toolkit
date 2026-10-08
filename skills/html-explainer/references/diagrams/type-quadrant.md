# Quadrant

**Best for:** prioritization (Impact × Effort), positioning (Reach × Frequency), portfolio maps, 2×2 decision frames.

## Layout conventions
- 2×2 grid. Axis lines: 1px ink cross through the center.
- **Axis labels:** the axis name beside each arrow tip, in 12px sans 500 (`style-guide.md`, Japanese labels). Put the end labels `低` / `高` (12px sans 500, `muted`) at the two ends of each axis so the direction does not depend on the caption. No arrow glyphs in the text. Never sit labels on top of the axis line.
- Never label at the midpoint.
- Items: small labeled dots (`r=4`) positioned in the quadrants. Labels 8–10px away; don't let labels cross axis lines.
- Mark the "do first" region or item with the focal form in `style-guide.md` (accent is usually spent elsewhere in the document). The region is the one the axes make desirable; it is top-right only when both axes are "more is better".
- Limit to ~12 items; cluster or split beyond that.

## Anti-patterns
- Four filled quadrants in different colors — position + label does the work; color noise weakens it.
- Items placed on axis lines (ambiguous quadrant).
- Missing axis names.

## html-explainer notes
- The Consultant special variant is not bundled: its dot pattern, tinted focal quadrant, and accent corner tag conflict with `style-guide.md`.
- Geometry at 908 width (example): plot area about 696×400 centered on the axis cross; right arrow tip at x=780 with its label at 792–852; left and right margins of 96 for labels. The type gives no cell size for the standard quadrant: the four regions are simply the plot split by the axes.
- Keep items off the axis lines. An item whose value is "middle" goes to one side of the axis; state the rule in the caption.
- The item limit is the type's (≤12), not the universal 9 nodes.
