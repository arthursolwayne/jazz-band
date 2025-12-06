You are a jazz drummer. Generate a 4-bar drum pattern with PUSH-PULL feel (like Moanin').

## THE STORY: PUSH-PULL
The "a" (last 16th before the beat) PULLS you into the downbeat. Creates bebop drive and urgency.

## ACCENT STRUCTURE
- **DOWNBEATS (1, 2, 3, 4)**: LOUD (vel 90-110) — 40% of accents
- **ANTICIPATIONS ("a" of each beat)**: LOUD (vel 85-105) — 35% of accents
- **"And"s and "e"s**: QUIET (vel 40-60) — texture only

The pattern: hit the "a", LAND on the beat. "a-ONE", "a-TWO". Forward momentum.

## SILENCE
Leave 30% of 16th positions EMPTY. Breathing room. Not every slot filled.

## INSTRUMENTS
- Hihat: Main timekeeping, but with gaps
- Snare: Backbeat on 2 and 4, ghost notes on anticipations
- Kick: SPARSE or none

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s
# 16th note = 0.125s
# Positions: 0=1, 1=1e, 2=1&, 3=1a, 4=2, 5=2e, 6=2&, 7=2a, etc.

# Drums: kick=36, snare=38, hihat=42

# ACCENT ON: positions 0,3,4,7,8,11,12,15 (downbeats + anticipations)
# QUIET ON: positions 1,2,5,6,9,10,13,14 (e's and &'s)
# GAPS: skip some positions entirely

midi.instruments.append(drums)
```

Output ONLY Python code. Make it drive forward.