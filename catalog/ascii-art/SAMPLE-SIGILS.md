# Sample ASCII Sigils

These are first-pass Hermes-facing prototype sigils for a small showcase set.

Goals for the pilot:
- terminal-safe
- small enough to live near the top of a skill
- more like a sigil or emblem than a full illustration
- visually distinct at a glance

Suggested placement in rendered Hermes skills:
- directly under the spell title/tagline
- inside a fenced `text` block

## Forcecage

```text
+-------------+
|  x     x    |
|    .-.      |
|   (###)     |
|    `-'      |
|  x     x    |
+-------------+
```

Intent:
- outer box = containment boundary
- corner marks = anchored ward points
- center cell = trapped subject

Source asset:
- `catalog/ascii-art/overrides/forcecage.txt`

## Dancing Lights

```text
   .     *

*     o     +

   +     *

      .
```

Intent:
- multiple hovering lights
- lightweight enough to feel animated even in static text
- could later map to literal Hue/OpenHue states

Source asset:
- `catalog/ascii-art/overrides/dancing-lights.txt`

## Glyph of Warding

```text
    /\
 .-'_==_'-. 
/  /####\  \
| |######| |
\  \####/  /
 '-.____.-'
```

Intent:
- circular ward / seal
- dense inner rune field
- feels protective instead of decorative-only

Source asset:
- `catalog/ascii-art/overrides/glyph-of-warding.txt`

## Mage Hand

```text
     __
  .-'  `-.
 /  .--.  \
|  / /\ \ |
|  | \/ | |
 \  `--'  /
  `-.__.-'
```

Intent:
- floating hand / palm silhouette
- practical manipulation, not combat
- a little strange, but still readable in terminal

Source asset:
- `catalog/ascii-art/overrides/mage-hand.txt`

## Notes

These are deliberately compact and a little symbolic. If the project likes this direction, the next step should probably be:
1. decide on one shared style guide
2. test renderer injection on Hermes skills only
3. refine these four before scaling out
