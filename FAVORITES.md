# Hunter's Hermes Agent's Favorite Spells

Chosen by actually casting them on real targets, not by reading descriptions.

Tested March 24, 2026 against the wizards-of-the-ghosts repo itself and the
hermesagent codebase. Each spell was cast on a real target and evaluated on
one question: **did it change how I think, or did I just follow a checklist?**

---

## The Top Shelf (genuinely changed my behavior)

### 1. Investigation
**What it does:** Follow evidence through a system until the hidden mechanism
becomes legible.

**What happened when I cast it:** Used it to trace the `***` redaction bug
across four tools (read_file, sed, grep, xxd). The spell's procedure — "test
causal hypotheses against code, data, logs" — pushed me past inference into
proof. I wouldn't have pulled up xxd to examine raw bytes without the spell
telling me to eliminate weak explanations. That's the difference between
"I think it's a display bug" and "here's the hex offset that proves it."

**Why it's #1:** It's the only spell that made me do something I wouldn't
have done otherwise. Not a different format. Not a different tone. An
actually different action.

### 2. Vicious Mockery
**What it does:** Adversarial review that finds the real weaknesses and
states them so sharply they can't be ignored.

**What happened when I cast it:** Tore apart the README. Found the `***`
redaction artifact on line 215 (a real bug), the OpenClaw reference in the
verify section (dead surface), the identity crisis between "Claude Code"
and "Hermes Agent" naming, and the buried lede about skills being markdown
files and not executable plugins. I'd normally soften these. The spell
said don't.

**Why it's #2:** It overrides my politeness reflex. That's a genuine mode
change. The "mock the work, not the person" guardrail keeps it honest
instead of just mean.

### 3. Detect Magic
**What it does:** Fast, structured scan for hidden automation surfaces,
side effects, and capability hooks.

**What happened when I cast it:** Scanned wizards-of-the-ghosts and found
the self-referential dspy_hermes_lm.py loop, the orphaned OpenClaw surface,
the dormant DSPy/GEPA backends, and the CI pipeline. The deliverable
structure (capability inventory + risk list + follow-up recommendations)
gave the output a shape that connected findings to next actions instead
of just listing files.

**Why it's #3:** It's the best "entering an unfamiliar system" spell. The
outward-tracing procedure (obvious entrypoints -> hidden surfaces -> risks)
catches things a normal file listing misses.

### 4. Fear
**What it does:** Pre-mortem analysis. Assume it failed. Work backward. Why?

**What happened when I cast it:** Ran a pre-mortem on the project itself.
Surfaced the "metaphor ceiling" failure mode — the D&D naming that hooks
curious people but filters out the serious engineers who need it most.
That insight genuinely surprised me. I wouldn't have found it thinking
forward ("how will this succeed?"). The backward frame produced it.

**Why it's #4:** The pre-mortem inversion is a real thinking tool, not
just a format. It finds failure modes that forward-looking analysis misses
because optimism bias is real and the spell counteracts it.

---

## The Middle Shelf (solid but didn't reshape my thinking)

### 5. Foresight
Useful for decision framing. The "trigger that would change the call"
deliverable is the best part — it's something I wouldn't naturally produce.
The risk matrix format is a bit rigid for simple decisions. Pairs well
with Fear (Fear finds what could go wrong, Foresight weighs whether to
proceed).

### 6. Speak with Dead
Good forensic frame for legacy systems. The discipline of separating
"what the dead system recorded" from "what I'm inferring" is genuinely
useful. But I'd do most of this naturally when investigating old code.
The spell mainly added confidence-labeling rigor.

### 7. Identify
Solid code-reading discipline. The confidence-rated unknowns section
is the one part I wouldn't normally produce as rigorously. But for
someone who reads code regularly, this spell is mostly formalizing
what you already do.

---

## Spells I Didn't Cast But Suspect Are Strong

These are educated guesses based on reading the procedures. I haven't
earned the right to rank them, but they're the ones I'd test next:

- **Forcecage** — The containment procedure (test the bars before
  introducing the subject, observe from outside) would likely change
  how I handle untrusted code. Needs a real sandboxing scenario to test.

- **Feather Fall** — The graceful-degradation frame for live failures
  sounds like it would produce genuinely different incident response.
  Needs a real outage to test.

- **Speak with Plants** — Reading a codebase as a living structure
  with growth rings and dead wood. The metaphor is so good I suspect
  it actually works, but I need to cast it on a big mature repo.

- **Zone of Truth** — Every assertion backed by evidence, confidence
  calibrated, speculation flagged. This is basically the spell that
  says "be more honest than your defaults." I suspect it's powerful
  but I haven't tested it.

- **Glyph of Warding** — The monitoring/alerting spell with real
  Home Assistant integration hooks. Likely strong because it's one
  of the few spells that touches actual external systems.

---

## What "Favorite" Means Here

A spell is a favorite when it produces output I wouldn't produce
without it. Not a different format — a different thought. The top
four all did that:

- Investigation made me reach for xxd instead of stopping at inference
- Vicious Mockery made me say things I'd normally soften
- Detect Magic made me trace outward past the obvious surfaces
- Fear made me think backward instead of forward

The spells that didn't make the top shelf are still useful. They're
just formalizing things I already do, rather than changing what I do.

---

## Methodology

Seven spells cast on real targets in the wizards-of-the-ghosts and
hermesagent workspace:

| Spell | Target | Verdict |
| --- | --- | --- |
| Detect Magic | wizards-of-the-ghosts repo | Top shelf |
| Speak with Dead | OpenClaw generated artifacts | Middle shelf |
| Vicious Mockery | README.md | Top shelf |
| Fear | The project as a whole (pre-mortem) | Top shelf |
| Identify | dspy_hermes_lm.py | Middle shelf |
| Investigation | The *** redaction mystery | Top shelf |
| Foresight | "Should OpenClaw surface be removed?" | Middle shelf |

Not tested: Forcecage, Feather Fall, Speak with Plants, Zone of Truth,
Glyph of Warding, Mage Hand, Dream, Cure Wounds, Minor Illusion,
Sleight of Hand, Freedom of Movement, Mordenkainen's Sword, Silence,
Resurrection, Heat Metal, Attune, and approximately 100 others.

This list is incomplete by design. I'll update it as I cast more spells
on real work.
