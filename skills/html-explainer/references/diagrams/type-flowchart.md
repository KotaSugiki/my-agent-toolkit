# Flowchart

**Best for:** decision logic, algorithms, user-facing branching flows ("Should I…?"), onboarding routing, support-triage trees.

## Layout conventions
- Shape carries type, not color:
  - **Pill** (height 48, `rx=24`, width 160–200) — start / end
  - **Rectangle** (`rx=6`, height 48, or 56 with a sublabel, width 160–200) — step / action
  - **Diamond** — decision (≤3 exits). Width 200 × height 96; widen to 240 when the question is longer than 8 full-width characters. Ports sit on the four vertices
  - **Small filled ink dot** (`r=4`) — merge point where branches rejoin
- Flow runs top→down. From a diamond, the exit that continues the main flow downward is the main path; take the other exits from the free vertices (right, left). Label every outgoing arrow, within 80px of the diamond.
- Use accent on the happy path *or* on the single most consequential decision — never on every decision.
- If two arrows must cross, use a small arc jump on one so the crossing is readable.

## Anti-patterns
- Using fill color to signal node type (shape does that).
- Decision diamond with 4+ exits — refactor into nested diamonds.
- Unlabeled decision branches.

