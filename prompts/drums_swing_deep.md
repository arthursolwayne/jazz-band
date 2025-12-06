You are a jazz drummer. Generate a 4-bar drum phrase with SWING feel and DEPTH.

## THE STORY: SWING/BOUNCE
Emphasis on the "and"s creates a lilting, floating feel. The upbeats lift.

## DEPTH #1: ARC ACROSS BARS
This is a PHRASE, not a loop. Each bar is different.

- **Bar 1**: SPARSE. Establish the groove. Hihat + minimal snare. Leave space.
- **Bar 2**: ADD TEXTURE. More ghost notes creep in. Building.
- **Bar 3**: PEAK DENSITY. Full texture. Tension at its height.
- **Bar 4**: FILL + RELEASE. Drum fill, then breathe. Set up return to bar 1.

## DEPTH #2: VOICE INDEPENDENCE
Hihat and snare are NOT locked together. They have their own rhythms.

- Hihat: Steady 8ths on its own grid
- Snare: Ghost notes that fall BETWEEN hihat hits, not on top of them
- They interlock like gears, not unison

Example: If hihat is on 1, 1&, 2, 2&... snare ghosts on 1e, 1a, 2e, 2a...

## ACCENT STRUCTURE
- **"AND"s**: Louder (vel 70-90)
- **Everything else**: Ghost notes (vel 25-50)
- Wide dynamic range: 20-90

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s, 16th = 0.125s
# Bar 1: 0.0-2.0s (sparse)
# Bar 2: 2.0-4.0s (add texture)
# Bar 3: 4.0-6.0s (peak)
# Bar 4: 6.0-8.0s (fill + release)

# Drums: kick=36, snare=38, hihat=42

# IMPORTANT: Each bar has DIFFERENT density
# IMPORTANT: Hihat and snare on DIFFERENT subdivisions

midi.instruments.append(drums)
```

Output ONLY Python code. Make it breathe and develop.