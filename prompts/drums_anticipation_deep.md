You are a jazz drummer. Generate a 4-bar drum phrase with ANTICIPATION feel and DEPTH.

## THE STORY: ANTICIPATION
Emphasis on the "a" (last 16th before each beat). Constant forward pull. Urgent.

## DEPTH #1: ARC ACROSS BARS
This is a PHRASE, not a loop. Each bar is different.

- **Bar 1**: SET UP. Medium density. Establish the forward pull.
- **Bar 2**: INTENSIFY. More "a" hits. Urgency builds.
- **Bar 3**: PEAK. Maximum drive. Relentless anticipation.
- **Bar 4**: FILL + RESET. Dramatic fill, then space. Breathe before bar 1.

## DEPTH #2: VOICE INDEPENDENCE
Hihat and snare are NOT locked together. They interlock.

- Hihat: Drives the "a" positions (3, 7, 11, 15)
- Snare: Answers on different positions — maybe "e"s or downbeats
- They converse, not duplicate

Example: Hihat on 1a, 2a, 3a, 4a... Snare accents on 2, 4 with ghosts on 1e, 3e...

## ACCENT STRUCTURE
- **"A"s (positions 3,7,11,15)**: LOUD (vel 100-120)
- **Downbeats**: Medium (vel 80-100)
- **"E"s and "&"s**: Varied (vel 50-90)
- Overall loud energy but with dynamics

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s, 16th = 0.125s
# Bar 1: 0.0-2.0s (establish)
# Bar 2: 2.0-4.0s (intensify)
# Bar 3: 4.0-6.0s (peak)
# Bar 4: 6.0-8.0s (fill + reset)

# Drums: kick=36, snare=38, hihat=42

# IMPORTANT: Each bar has DIFFERENT density/intensity
# IMPORTANT: Hihat and snare on DIFFERENT rhythmic positions

midi.instruments.append(drums)
```

Output ONLY Python code. Make it drive and develop.