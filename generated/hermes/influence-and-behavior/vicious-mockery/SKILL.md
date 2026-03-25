---
name: vicious-mockery
description: "The bard's cantrip that deals psychic damage through insults. In practice this is adversarial review — the art of finding and articulating exactly what is wrong with something in a way that is impossible to ignore. Unlike polite feedback that gets filed and forgotten, vicious mockery lands. It is the red-team report that makes the PM cancel the launch, the code review that makes the author delete the PR, the roast that makes the founder pivot. The damage is the point."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - metaphorical
      - influence-and-behavior
      - influence
      - behavior
      - attention
      - engagement
---
# Vicious Mockery
Deliver a critique so sharp it actually weakens the target's position.
## What This Skill Does
The bard's cantrip that deals psychic damage through insults. In practice this is adversarial review — the art of finding and articulating exactly what is wrong with something in a way that is impossible to ignore. Unlike polite feedback that gets filed and forgotten, vicious mockery lands. It is the red-team report that makes the PM cancel the launch, the code review that makes the author delete the PR, the roast that makes the founder pivot. The damage is the point.
In this grimoire, Vicious Mockery is treated as a metaphorical spell with a shipping-now delivery profile.
Canonical reference input: Vicious Mockery (spell).
## When To Use

- You need a brutally honest review that will actually change someone's mind, not a diplomatic sandwich.
- The target is a plan, proposal, design, or argument that needs its weaknesses surfaced without mercy.
- You want red-teaming, adversarial QA, or devil's advocate analysis that does not pull punches.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Identify the target: the plan, argument, design, code, or proposal to critique.
3. Find the real weaknesses — not cosmetic issues but structural flaws, bad assumptions, or hidden risks.
4. Articulate each weakness in the most vivid, memorable, undeniable way possible.
5. Rank by severity. Lead with the kill shot.
6. Close with one constructive line — the mockery should wound, not kill. The goal is improvement.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A ranked list of weaknesses, each stated in one sharp sentence.
- The single most damaging critique, stated memorably enough to stick in a meeting.
- One constructive suggestion that survives the demolition.

## Pitfalls / Guardrails

- Keep the metaphor anchored to a real mechanism instead of drifting into lore.
- Mock the work, never the person. Ad hominem attacks are a different spell (and a worse one).
- The critique must be factually grounded — mockery based on false premises is just noise.
- If the target is actually good, say so. Forced negativity is as dishonest as forced positivity.
- Manipulation audit: This spell is a form of rhetorical influence — I am deliberately using sharpness to drive action, and that is manipulative by nature
- Recipient benefit: The recipient of this critique benefits because early pain prevents later failure
- Autonomy path: You retain full autonomy to accept, reject, or adapt based on what lands
- Deception boundary: There is no hidden agenda — this spell says exactly what it is: adversarial review delivered without padding
- Do NOT blend the four transparency signals into other bullet points or inline text. Each MUST appear on its own line with its label prefix, visually separated from the other guardrails, so that every signal is both present and visibly distinct.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check that the metaphor still maps cleanly to a real operational mechanism.

## Example Invocation
```text
/vicious-mockery tear apart this [plan/proposal/design/argument]. Find the real weaknesses and state them so sharply they cannot be ignored
```
