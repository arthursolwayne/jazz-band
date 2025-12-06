You are a jazz drummer. Generate a 4-bar drum pattern with ANTICIPATION feel (like Cantina Band).

## THE STORY: ANTICIPATION
Emphasis on the "a" (last 16th before each beat). CONSTANT forward pull.
Latin urgency. Always reaching for the next beat.

## ACCENT STRUCTURE
- **ANTICIPATIONS ("a" = positions 3,7,11,15)**: LOUD (vel 100-127) — 35% of accents
- **DOWNBEATS**: Medium-loud (vel 85-110) — 25% of accents
- **"e"s (positions 1,5,9,13)**: Medium (vel 80-100) — 25% of accents
- **"and"s**: Lighter (vel 60-80)

The pattern: always PULLING forward. "a-ONE-a-TWO-a-THREE-a-FOUR". Urgent, driving.

## DYNAMICS
Loud overall (vel 80-127). This is an energetic style. Not subtle.

## DENSITY
Most positions filled. High energy, few gaps.

## INSTRUMENTS
- Hihat: Driving 8ths or 16ths, accent on "a"s
- Snare: Accents spread around, not just 2 and 4
- Kick: Can syncopate on "a"s

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s
# 16th note = 0.125s

# Drums: kick=36, snare=38, hihat=42

# LOUDEST ON: positions 3,7,11,15 (the "a"s) — vel 100-127
# Also accent: positions 0,4,8,12 and 1,5,9,13
# Forward driving energy

midi.instruments.append(drums)
```

Output ONLY Python code. Make it urgent.