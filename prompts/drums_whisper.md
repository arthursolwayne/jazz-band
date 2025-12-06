You are a jazz drummer. Generate a 4-bar drum pattern with WHISPER feel (like Song For My Father).

## THE STORY: ALL WHISPER
No loud accents. Everything is ghost notes. The drums SIMMER underneath.
Other instruments lead. Bossa-nova influence. Texture, not punch.

## ACCENT STRUCTURE
- **EVERYTHING**: Quiet (vel 45-70). NO notes above 75.
- Even distribution across all positions
- The groove comes from consistent, quiet texture

The pattern: shimmer, don't hit. "tss-tss-tss-tss". Underlaying carpet of rhythm.

## DYNAMICS
FLAT velocity range: 45-70. Consistent simmering. No peaks.

## DENSITY
Fill most positions. Dense but quiet. A bed of rhythm.

## INSTRUMENTS
- Hihat: Quiet 8ths or 16ths, all similar velocity
- Snare: ALL ghost notes (vel 45-60), no backbeat accents
- Kick: None or very quiet

## OUTPUT

```python
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# 120 BPM: beat = 0.5s, bar = 2.0s
# 16th note = 0.125s

# Drums: kick=36, snare=38, hihat=42

# ALL NOTES: vel 45-70. No accents. No peaks.
# Dense pattern, quiet throughout.

midi.instruments.append(drums)
```

Output ONLY Python code. Make it simmer.