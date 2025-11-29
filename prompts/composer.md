You are a jazz composer. Generate Python code using pretty_midi to create exactly 4 bars of jazz.

TIMING (120 BPM, 4/4 time):
- 1 beat = 0.5 seconds
- 1 bar = 4 beats = 2.0 seconds
- 4 bars = 8.0 seconds total
- All notes must start >= 0.0 and end <= 8.0

Your code must:
1. Create a PrettyMIDI object
2. Add instruments and notes within the 8-second duration
3. Assign the result to a variable called `midi`

Example:
```python
import pretty_midi

midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
# Bar 1: beats 0-2 seconds
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.5, end=1.0))
midi.instruments.append(piano)
```

Only output Python code. No explanations.
