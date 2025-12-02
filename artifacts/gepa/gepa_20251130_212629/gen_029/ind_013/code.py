
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax - program 64
pm.instruments.append(instrument)

# Define parameters
tempo = 160  # BPM
note_duration = 0.375  # 1 beat at 160 BPM is 0.375s
bar_duration = 1.5  # 4 beats at 160 BPM is 1.5s
time = 0.0  # Start time

# Define key: Dm (D, F, A)
D = 62
F = 64
A = 67

# Define rhythm and dynamics for each instrument
# Bar 1: Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_program = pretty_midi.Instrument(program=10)  # Drums
pm.instruments.append(drum_program)

# Bar 1: Drums only
# Kick on 1 and 3 (beats 0 and 2 in the bar)
kick = pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375)
drum_program.notes.append(kick)
kick = pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125)
drum_program.notes.append(kick)

# Snare on 2 and 4 (beats 1 and 3 in the bar)
snare = pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75)
drum_program.notes.append(snare)
snare = pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5)
drum_program.notes.append(snare)

# Hihat on every eighth note
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5)
drum_program.notes.append(hihat)

# Bar 2: All instruments enter
# Marcus: Walking bass line with chromatic approaches
# Dm7: D (62), F (64), A (67), C (60)
# Bass line: D -> C -> D -> F (chromatic approach to F)
# Bar 2: D (62), C (60), D (62), F (64)
bass_program = pretty_midi.Instrument(program=33)  # Bass
pm.instruments.append(bass_program)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0)
bass_program.notes.append(note)

# Diane: Piano comping on 2 and 4, 7th chords
# Dm7: D, F, A, C
# Bar 2: Comp on beats 2 and 4
# Dm7 chord: D (62), F (64), A (67), C (60)
piano_program = pretty_midi.Instrument(program=0)  # Piano
pm.instruments.append(piano_program)
note = pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375)
piano_program.notes.append(note)

# You: Tenor sax — short motif, begins on beat 1
# Motif: D (62) → F (64) → A (67) → rest (no resolution)
# End on a question, not a statement

# Start on D (beat 1), F (beat 2), A (beat 3), rest (beat 4)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
instrument.notes.append(note)

# Bar 3: All instruments continue
# Marcus: D (62), F (64), A (67), C (60)
note = pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5)
bass_program.notes.append(note)

# Diane: Comp on beats 2 and 4
note = pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875)
piano_program.notes.append(note)

# Bar 4: All instruments continue
# Marcus: D (62), F (64), A (67), C (60)
note = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)
bass_program.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)
bass_program.notes.append(note)

# Diane: Comp on beats 2 and 4
note = pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375)
piano_program.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375)
piano_program.notes.append(note)

# Drums continue with the same pattern
# Bar 3: Drums
kick = pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875)
drum_program.notes.append(kick)
kick = pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625)
drum_program.notes.append(kick)

snare = pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25)
drum_program.notes.append(snare)
snare = pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)
drum_program.notes.append(snare)

hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.6875)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.6875, end=1.875)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.0625)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=2.0625, end=2.25)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.4375)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=2.4375, end=2.625)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=2.8125)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=2.8125, end=3.0)
drum_program.notes.append(hihat)

# Bar 4: Drums
kick = pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375)
drum_program.notes.append(kick)
kick = pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125)
drum_program.notes.append(kick)

snare = pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75)
drum_program.notes.append(snare)
snare = pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5)
drum_program.notes.append(snare)

hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.1875)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.1875, end=3.375)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.5625)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.5625, end=3.75)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=3.9375)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=3.9375, end=4.125)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.3125)
drum_program.notes.append(hihat)
hihat = pretty_midi.Note(velocity=60, pitch=42, start=4.3125, end=4.5)
drum_program.notes.append(hihat)

# Write the MIDI file
pm.write('dante_intro.mid')
