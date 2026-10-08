# Swimlane

**Best for:** cross-functional processes, RACI-style flows, vendor handoffs, multi-team shipping workflows.

## Layout conventions
- Horizontal lanes (or vertical columns) — one per actor/team. Label each lane in the left margin (or top) with a 12px sans label (`style-guide.md`, Japanese labels).
- Lane dividers: 1px hairlines.
- Process steps are rectangles placed inside the lane of the actor performing them; arrows show flow.
- Handoffs (arrows crossing lane boundaries) are the most important edges. Mark the handback or the handoff that introduces the most coupling or latency with the ink headline arrow (2px, `arrow-ink`, dashed for a handback), not with the accent.
- Don't force equal step count per lane; a lane with one step is fine.

## Anti-patterns
- Lanes without labels.
- A step drawn across two lanes (pick one owner).
- Arrows that snake back and forth — reorder steps so the flow is mostly straight.

## html-explainer notes
- This type gives no formulas. Route handoffs with the elbow path in `type-architecture.md` (`H … Q … V …`); a handback that returns left and up is the same path with the signs flipped.
- Do not tint the lane bands: label masks would need a different fill per band. Lanes are hairline-separated; the lane label column is about 80–160px wide and lane height at least 88.
- All steps are the same box; hierarchy comes from lane position and the ink headline arrow, not from box styles.
- Step boxes at least 48px high (56 with two lines of 12px text); fan attach points per index.md §4 rule 4.
