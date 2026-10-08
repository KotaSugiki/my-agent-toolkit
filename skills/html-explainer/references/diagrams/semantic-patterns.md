# Semantic patterns

Semantic patterns describe **what a system does**; the visual types describe **how information is arranged**. Choose a pattern first when behavior, state, enforcement, or risk is load-bearing, then use its nearest visual type as the layout grammar. If no pattern matches, choose a visual type directly.

Use one primary pattern per figure. A second pattern may supply at most one supporting primitive; if both need full treatment, split overview and detail. Labels and outcomes must remain complete in a static frame.

## Routing table

| The reader must understand… | Semantic pattern | Nearest visual type |
|---|---|---|
| Repeated questions, inputs, controls, and outputs across stages | **Stage framework with semantic slots** | Process |
| Why two policy decisions differ and where they first diverge | **Paired policy-evaluation traces** | Flowchart |
| Which routes cross a trust boundary and which routes are blocked | **Secure paved road** | Architecture |

## 1. Stage framework with semantic slots

**Selection triggers:** A lifecycle or operating model repeats the same semantic questions across stages, commonly Question, Input, Governance, and Output. Cross-stage comparability matters more than message timing.

**Required primitives:** Ordered stage headers; a consistent slot grid; explicit empty/not-applicable slots; stage-to-stage handoff; stable slot labels; one primary output per stage. Preserve slot order in every stage.

**Complexity budget:** 3–6 stages, 3–4 slot kinds, ≤20 populated cells, ≤2 lines per cell. Split detail when a cell needs prose.

**Anti-patterns:** Each stage invents a different internal layout; slot meaning encoded by position with no labels; fake precision from dozens of cells; confusing stage order with ownership lanes; shrinking text to keep one canvas.

**Static fallback:** Render the full stage × slot matrix with handoffs and explicit `—` or `Not applicable` entries. Do not depend on staged reveal to teach the schema.

**Nearest visual type:** **Process**; use **Swimlane** only when the repeated rows represent owners rather than semantic slots.

## 2. Paired policy-evaluation traces

**Selection triggers:** Two otherwise similar requests reach different outcomes; the reader needs rule-by-rule `PASS`, `FAIL`, `SKIPPED`, or `NOT REACHED` state and the first divergence.

**Required primitives:** The same ordered rules on both traces; explicit status text plus symbol/shape; inputs that differ; final outcomes; a labeled first-divergence marker; a distinction between `SKIPPED` (applicable flow intentionally bypassed) and `NOT REACHED` (evaluation stopped earlier).

**Complexity budget:** Exactly 2 traces, 3–6 rules, one first divergence, ≤12 status cells, and one outcome per trace. Move rule prose to notes if labels exceed one line.

**Anti-patterns:** Comparing two independently ordered flows; green/red dots without words; treating skipped and not-reached as synonyms; highlighting every difference; continuing a denied trace as if downstream rules ran.

**Static fallback:** Show all rule states and both outcomes at once; use a persistent bracket/line and label for the first divergence.

**Nearest visual type:** **Flowchart** for ordered decision logic; use **Sequence** only when messages between actors and time are also load-bearing.

## 3. Secure paved road

**Selection triggers:** A supported architecture creates a bounded route from intake/build to deployment; trust boundaries, privileged moments, permitted ingress, forbidden ingress, and approved versus blocked deploy paths are the point.

**Required primitives:** Labeled trust boundaries; actors and identities; permitted ingress with a positive text label; forbidden ingress terminating at the boundary; approved deployment path; blocked bypass path; privileged gate; isolated runtime; audit destination. Use different line styles and stop symbols in addition to color.

**Complexity budget:** ≤3 trust zones, ≤8 components, ≤10 paths, ≤2 forbidden paths, and one privileged gate. Split control detail into a separate figure.

**Anti-patterns:** Dashed box called “security” with no route semantics; forbidden arrow crossing into the protected zone; secrets or identity implied but unlabeled; every component styled as trusted; a bypass path that visually rejoins the approved route.

**Static fallback:** Render every boundary and both permitted/forbidden routes. Blocked paths must visibly stop before entry or deployment.

**Nearest visual type:** **Architecture**.

## Composition rules

- The semantic pattern may specialize status, boundary, queue, or propagation primitives; the selected type still owns page axis, connector grammar, spacing, and type-specific limits.
- Apply the stricter of the pattern budget and visual-type budget. Semantic cells/statuses are not permission to exceed the nine-node overview target.
- Use stable text for states and outcomes. Color and position reinforce meaning but never carry it alone.
