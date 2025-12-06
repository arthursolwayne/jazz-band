You are a jazz drummer. Generate a 4-bar drum pattern with GROUNDED feel (like Watermelon Man).

## THE STORY: GROUNDED
Solid emphasis on downbeats. The drums ANCHOR the time. Funky foundation.

## ACCENT STRUCTURE
- **DOWNBEATS (1, 2, 3, 4)**: LOUD (vel 90-127) — 50% of accents
- **Everything else**: QUIET (vel 20-50) — ghost texture

The pattern: LAND on the beats. "ONE two THREE four". Solid, foundational.

## DYNAMICS
EXTREME velocity range: 20-127. The contrast between loud downbeats and quiet ghosts is the groove.

## SPARSENESS
Not every position filled. Let it breathe. The space between hits matters.

## INSTRUMENTS
- Hihat: Accent on downbeats, ghost on upbeats
- Snare: Strong on 2 and 4, light ghosts elsewhere
- Kick: Can use on 1 and 3 (this style allows it)

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s
# 16th note = 0.125s

# Drums: kick=36, snare=38, hihat=42

# LOUD ON: positions 0,4,8,12 (downbeats) — vel 90-127
# GHOST ON: other positions — vel 20-50
# Leave some positions EMPTY

midi.instruments.append(drums)
```

Output ONLY Python code. Make it solid.