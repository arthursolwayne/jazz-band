
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define F major scale
F_MAJOR = [65, 67, 69, 72, 74, 76, 79]  # F, G, A, C, D, E, F#

# Function to convert note name to MIDI note number
def note_to_midi(note, octave=4):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return 12 * (octave + 1) + note_names.index(note)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Drums')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Add instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Time per bar = 1.5 seconds
bar_length = 1.5
bar = 0

### 🎤 Saxophone: Tenor motif (starts, leaves it hanging, comes back)
sax_notes = [
    (note_to_midi('G', 4), 0.25),  # G4 (start)
    (note_to_midi('A', 4), 1.0),   # A4 (wait)
    (note_to_midi('G', 4), 0.1),   # G4 (return)
    (note_to_midi('F', 4), 0.3)    # F4 (end with question)
]

for note, duration in sax_notes:
    start_time = bar_length * bar
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

### 🥁 Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    ('Kick', 0.0),  # Bar 0, beat 1
    ('Hi-Hat', 0.375),  # 8th note
    ('Hi-Hat', 0.75),   # 8th note
    ('Snare', 1.0),     # Bar 0, beat 2
    ('Kick', 1.5),      # Bar 1, beat 1
    ('Hi-Hat', 1.875),  # 8th note
    ('Hi-Hat', 2.25),   # 8th note
    ('Snare', 2.5),     # Bar 1, beat 2
    ('Kick', 3.0),      # Bar 2, beat 1
    ('Hi-Hat', 3.375),
    ('Hi-Hat', 3.75),
    ('Snare', 4.0),     # Bar 2, beat 2
    ('Kick', 4.5),
    ('Hi-Hat', 4.875),
    ('Hi-Hat', 5.25),
    ('Snare', 5.5)      # Bar 3, beat 2
]

for note_type, time in drum_notes:
    if note_type == 'Kick':
        pitch = 36
        velocity = 100
    elif note_type == 'Snare':
        pitch = 38
        velocity = 110
    elif note_type == 'Hi-Hat':
        pitch = 42
        velocity = 70
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

### 🎻 Piano: 7th chords on 2 and 4, with expressive dynamics
def chord_notes(chord, octave):
    return [note_to_midi(note, octave) for note in chord]

for bar in range(4):
    if bar == 0:
        # F7 (F, A, C, E) on beat 2
        chord = chord_notes(['F', 'A', 'C', 'E'], 4)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=chord[0], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=chord[1], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=chord[2], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=chord[3], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
    elif bar == 1:
        # C7 on beat 2
        chord = chord_notes(['C', 'E', 'G', 'B'], 4)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=chord[0], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=chord[1], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=chord[2], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=chord[3], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
    elif bar == 2:
        # G7 on beat 2
        chord = chord_notes(['G', 'B', 'D', 'F#'], 4)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=chord[0], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=chord[1], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=chord[2], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=chord[3], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
    elif bar == 3:
        # C7 on beat 2
        chord = chord_notes(['C', 'E', 'G', 'B'], 4)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=chord[0], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=chord[1], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=chord[2], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=chord[3], start=bar_length * bar + 0.75, end=bar_length * bar + 1.0))

### 🎸 Bass: Walking line with chromatic approaches
# Walking bass line in F major
bass_notes = [
    (note_to_midi('F', 3), 0.0),   # F3
    (note_to_midi('G', 3), 0.375),  # G3
    (note_to_midi('A', 3), 0.75),   # A3
    (note_to_midi('Bb', 3), 1.125), # Bb3 (chromatic)
    (note_to_midi('C', 3), 1.5),    # C3
    (note_to_midi('D', 3), 1.875),  # D3
    (note_to_midi('E', 3), 2.25),   # E3
    (note_to_midi('F', 3), 2.625),  # F3
    (note_to_midi('G', 3), 3.0),    # G3
    (note_to_midi('A', 3), 3.375),  # A3
    (note_to_midi('Bb', 3), 3.75),  # Bb3
    (note_to_midi('C', 3), 4.125),  # C3
    (note_to_midi('D', 3), 4.5),    # D3
    (note_to_midi('E', 3), 4.875),  # E3
    (note_to_midi('F', 3), 5.25),   # F3
    (note_to_midi('G', 3), 5.625)   # G3
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Save the MIDI file
pm.write("jazz_intro.mid")
