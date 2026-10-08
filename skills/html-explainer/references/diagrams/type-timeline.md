# Timeline

**Best for:** release history, project milestones, incident timelines, roadmaps, changelog visualizations.

## Layout conventions
- Horizontal hairline baseline across the middle (`stroke-width=1`).
- Tick marks at time boundaries (quarters, months, sprints) with date labels below in Ubuntu Mono.
- Events: small filled circles (`r=4`) on the baseline. Labels alternate above and below to prevent collision, connected to the circle with a 1px hairline drop.
- Major milestones (gates): a white ring (`r=6`, stroke 2, `style-guide.md` focal form) + a weight-600 label; accent only when the document's accent is spent here.
- Time scale must be honest: if intervals are non-equal, space the circles non-equally. Don't fake linear spacing for aesthetics. Break the axis visibly if a region is too dense.

## Anti-patterns
- Equal-spacing events that aren't equally spaced in time.
- Missing axis labels ("what unit is this?").
- Crowded labels without vertical offset — illegible.

## html-explainer notes
- Event label: the name in 12px sans 600, with an ISO date (`2026-11-02`) in mono 9px beneath it. Alternate above and below. Month tick labels sit centered inside each month interval below the axis, so drop lines to lower events never cross them.
- Scale: x = x0 + days × px_per_day. Choose x0 so the first event's centered label stays at least 40px from the viewBox edge (example: x0=68 at 5.85px/day for a 133-day span).
- A legend is needed only when more than one marker form is used (dot, ring); say what the ring means.
- The event limit is the type's (about 7), not the universal 9 nodes.
