You are a jazz drummer. Generate a 4-bar drum pattern with SWING/BOUNCE feel (like So What).

## THE STORY: SWING/BOUNCE
Emphasis on the "and"s creates a lilting, floating feel. Cool modal jazz. The upbeats lift.

## ACCENT STRUCTURE
- **"AND"s (positions 2, 6, 10, 14)**: LOUD (vel 80-100) — 50% of accents
- **DOWNBEATS**: Medium (vel 60-80) — 25% of accents
- **"e"s and "a"s**: QUIET ghost notes (vel 25-45) — texture

The pattern: float on the upbeats. "one-AND-two-AND". Lilting, dancing.

## DYNAMICS
WIDE velocity range: 20-95. Whisper to medium-loud. Ghost notes everywhere.
The snare is mostly ghost notes with occasional pops on 2 and 4.

## DENSITY
Fill most positions BUT with varied velocity. Dense texture, not sparse.

## INSTRUMENTS
- Hihat: Steady 8ths but quiet on downbeats, lift on "and"s
- Snare: 80% ghost notes (vel 25-40), 20% accents
- Kick: Almost none

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s
# 16th note = 0.125s

# Drums: kick=36, snare=38, hihat=42

# LOUD ON: positions 2,6,10,14 (the "and"s)
# MEDIUM ON: positions 0,4,8,12 (downbeats)
# GHOST: positions 1,3,5,7,9,11,13,15 (vel 25-40)

midi.instruments.append(drums)
```

Output ONLY Python code. Make it float.