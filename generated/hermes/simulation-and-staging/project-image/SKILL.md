---
name: project-image
description: "In D&D, Project Image creates an illusory copy of yourself at a distant location — you can see through its eyes, speak through its mouth, and cast spells through it. The real-world version is remote presence: avatars, recorded video stand-ins, bot representations, asynchronous video messages. Project Image is the spell for being in two places at once — attending a meeting via avatar while working on something else, leaving a recorded presence in a channel, or deploying an automated representative that speaks with your voice and authority within defined limits."
version: "1.0.0"
author: "Wizards of the Ghosts"
license: "CC0-1.0"
compatibility: "Hermes Agent skills system"
metadata:
  hermes:
    tags:
      - spell
      - shipping-now
      - hybrid
      - simulation-and-staging
      - simulation
      - staging
      - mockup
      - testing
---
# Project Image
Project a version of yourself into a place you cannot physically be.
## What This Skill Does
In D&D, Project Image creates an illusory copy of yourself at a distant location — you can see through its eyes, speak through its mouth, and cast spells through it. The real-world version is remote presence: avatars, recorded video stand-ins, bot representations, asynchronous video messages. Project Image is the spell for being in two places at once — attending a meeting via avatar while working on something else, leaving a recorded presence in a channel, or deploying an automated representative that speaks with your voice and authority within defined limits.
In this grimoire, Project Image is treated as a hybrid spell with a shipping-now delivery profile.
Canonical reference input: Project Image (spell).
## When To Use

- You need presence in a meeting, channel, or space you cannot physically attend.
- A recorded or automated stand-in can represent you for routine interactions.
- Remote participation requires more presence than text but less commitment than live attendance.

## Prerequisites

- No extra runtime dependencies beyond Hermes Agent and the normal toolset for this session.

## Procedure

1. Restate the target, the success condition, and any no-touch boundaries before taking action.
2. Determine what kind of presence is needed: live avatar, recorded message, or automated representative.
3. Define the scope of authority: what can the projection say or do on your behalf?
4. Create and deploy the projection: join the meeting, post the recording, or activate the bot.
5. Monitor for situations that exceed the projection's authority and require your real presence.
6. Debrief on what the projection handled and what required escalation.
7. Package the result as the deliverables below, with confidence, assumptions, and unresolved risk called out explicitly.

## Deliverables

- A deployed remote presence: avatar, recording, or automated representative.
- Clear authority boundaries: what the projection can and cannot do.
- An escalation path for situations that require the real person.

## Pitfalls / Guardrails

- Keep the theatrical framing, but name the concrete mechanism that makes the skill useful right now.
- Remote projections must be disclosed as projections. Pretending a bot or recording is a live human is deception.
- Authority limits must be explicit. A projection that agrees to commitments outside its scope creates real obligations.
- Do not use projected presence to avoid accountability. If a situation requires your real attention, be present.

## Verification

- Check that the result includes every deliverable promised above.
- Check that confirmed facts, assumptions, and inferences are visibly separated.
- Check which parts are concrete actions versus framing, so the user can tell what is real now.

## Example Invocation
```text
/project-image set up remote presence — an avatar, recorded stand-in, or automated representative — that projects you into a space you cannot physically attend
```
