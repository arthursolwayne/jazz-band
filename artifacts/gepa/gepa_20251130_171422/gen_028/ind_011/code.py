
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor
key = 'F'
scale_degrees = [0, 2, 3, 5, 7, 8, 10]  # F, Gb, G, A, Bb, B, C
note_numbers = [note + 64 for note in [36, 38, 39, 41, 43, 44, 46]]  # F3, Gb3, G3, A3, Bb3, B3, C4
note_names = ['F3', 'Gb3', 'G3', 'A3', 'Bb3', 'B3', 'C4']

# Instrument setup
# Tenor Sax (program 64)
tenor_sax_program = 64
tenor_sax = pretty_midi.Instrument(program=tenor_sax_program)
pm.instruments.append(tenor_sax)

# Bass (program 33)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (program 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (program 128)
drums = pretty_midi.Instrument(program=128)
pm.instruments.append(drums)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Tempo is already set at 160 BPM via initial_tempo

# Define beat length in seconds
beat_length = 0.375  # 160 BPM = 60 / 160 = 0.375s per beat
bar_length = beat_length * 4  # 1.5 seconds per bar

# Bar 1: Little Ray (Drums) - mysterious, sparse
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# But with a subtle rubato feel
# 0.0 to 1.5 seconds
drum_notes = [
    (0.0, pretty_midi.note_number_to_name(36), 80),  # Kick on 1
    (0.25, pretty_midi.note_number_to_name(38), 70),  # Snare on 2
    (0.5, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 3
    (0.75, pretty_midi.note_number_to_name(38), 75),  # Snare on 4
    (0.9375, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 4 &
    (1.0, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 4
    (1.125, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 4 +
    (1.25, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 4 ++
    (1.375, pretty_midi.note_number_to_name(42), 60),  # Hi-hat on 4 +++

    # End of bar 1
]

for time, note_name, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2: Everyone comes in
# Tenor sax melody (sparse, expressive, with rests)
# Fm scale: F, Gb, G, A, Bb, B, C
# Three-note motif: G, A, Bb — spaced out, with rests in between
# Start at 1.5s
tenor_notes = [
    (1.5, 41, 90),  # G3
    (1.75, 44, 100),  # Bb3
    (2.0, 41, 90),  # G3
    (2.25, 40, 110),  # Ab3 (slightly outside scale, but expressive)
    (2.5, 44, 100),  # Bb3
    (2.75, 46, 90),  # C4
    (3.0, 44, 95),  # Bb3
    (3.25, 41, 90),  # G3
    (3.5, 44, 100),  # Bb3
    (3.75, 41, 90),  # G3
]

for time, pitch, velocity in tenor_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    tenor_sax.notes.append(note)

# Bass line (Marcus)
# Walking line, chromatic approaches, anchor
# Start at 1.5s
bass_notes = [
    (1.5, 40, 70),  # G3
    (1.875, 39, 65),  # Gb3
    (2.25, 41, 75),  # A3
    (2.625, 40, 70),  # G3
    (3.0, 38, 65),  # F3
    (3.375, 40, 70),  # G3
    (3.75, 41, 75),  # A3
    (4.125, 39, 65),  # Gb3
]

for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano (Diane)
# 7th chords, comp on 2 and 4
# F7, Bb7
piano_notes = [
    (1.5, pretty_midi.note_name_to_number('F3'), 80),
    (1.5, pretty_midi.note_name_to_number('A3'), 80),
    (1.5, pretty_midi.note_name_to_number('C4'), 80),
    (1.5, pretty_midi.note_name_to_number('E3'), 80),  # F7

    (2.5, pretty_midi.note_name_to_number('Bb3'), 80),
    (2.5, pretty_midi.note_name_to_number('D3'), 80),
    (2.5, pretty_midi.note_name_to_number('F4'), 80),
    (2.5, pretty_midi.note_name_to_number('A3'), 80),  # Bb7

    (3.5, pretty_midi.note_name_to_number('F3'), 80),
    (3.5, pretty_midi.note_name_to_number('A3'), 80),
    (3.5, pretty_midi.note_name_to_number('C4'), 80),
    (3.5, pretty_midi.note_name_to_number('E3'), 80),  # F7 again

    (4.5, pretty_midi.note_name_to_number('Bb3'), 80),
    (4.5, pretty_midi.note_name_to_number('D3'), 80),
    (4.5, pretty_midi.note_name_to_number('F4'), 80),
    (4.5, pretty_midi.note_name_to_number('A3'), 80),  # Bb7
]

for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Bar 3: Tension, glimmer of resolution
# Tenor sax: A, Bb, C
# More space, more dynamic
tenor_notes_bar3 = [
    (3.75, 41, 95),  # A3
    (4.0, 44, 100),  # Bb3
    (4.25, 46, 95),  # C4
    (4.5, 44, 90),  # Bb3
    (4.75, 41, 90),  # A3
    (5.0, 44, 85),  # Bb3
]

for time, pitch, velocity in tenor_notes_bar3:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    tenor_sax.notes.append(note)

# Bass line: Smooth chromatic descent
bass_notes_bar3 = [
    (3.75, 41, 70),  # A3
    (4.125, 40, 65),  # G3
    (4.5, 39, 60),  # Gb3
    (4.875, 38, 65),  # F3
]

for time, pitch, velocity in bass_notes_bar3:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano: Flurried comp, more color
piano_notes_bar3 = [
    (3.75, pretty_midi.note_name_to_number('A3'), 85),
    (3.75, pretty_midi.note_name_to_number('C4'), 80),
    (3.75, pretty_midi.note_name_to_number('E3'), 80),
    (3.75, pretty_midi.note_name_to_number('G3'), 80),

    (4.0, pretty_midi.note_name_to_number('Bb3'), 90),
    (4.0, pretty_midi.note_name_to_number('D3'), 85),
    (4.0, pretty_midi.note_name_to_number('F4'), 80),
    (4.0, pretty_midi.note_name_to_number('A3'), 80),

    (4.25, pretty_midi.note_name_to_number('A3'), 85),
    (4.25, pretty_midi.note_name_to_number('C4'), 80),
    (4.25, pretty_midi.note_name_to_number('E3'), 80),
    (4.25, pretty_midi.note_name_to_number('G3'), 80),

    (4.5, pretty_midi.note_name_to_number('Bb3'), 90),
    (4.5, pretty_midi.note_name_to_number('D3'), 85),
    (4.5, pretty_midi.note_name_to_number('F4'), 80),
    (4.5, pretty_midi.note_name_to_number('A3'), 80),
]

for time, pitch, velocity in piano_notes_bar3:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Bar 4: Lingering question
# Tenor sax: Ends on a rest, unresolved
# A glimmer, then silence
tenor_notes_bar4 = [
    (5.25, 44, 85),  # Bb3
    (5.5, 44, 75),  # Bb3
    (5.75, 44, 65),  # Bb3
    (6.0, 44, 50),  # Bb3 (fading)
]

for time, pitch, velocity in tenor_notes_bar4:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    tenor_sax.notes.append(note)

# Bass: Resolves down to F
bass_notes_bar4 = [
    (5.25, 38, 60),  # F3
    (5.625, 38, 55),  # F3
    (6.0, 38, 50),  # F3 (fading)
]

for time, pitch, velocity in bass_notes_bar4:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Piano: Last chord on F7, unresolved
piano_notes_bar4 = [
    (5.25, pretty_midi.note_name_to_number('F3'), 80),
    (5.25, pretty_midi.note_name_to_number('A3'), 80),
    (5.25, pretty_midi.note_name_to_number('C4'), 80),
    (5.25, pretty_midi.note_name_to_number('E3'), 80),

    (5.5, pretty_midi.note_name_to_number('F3'), 70),
    (5.5, pretty_midi.note_name_to_number('A3'), 70),
    (5.5, pretty_midi.note_name_to_number('C4'), 70),
    (5.5, pretty_midi.note_name_to_number('E3'), 70),

    (5.75, pretty_midi.note_name_to_number('F3'), 60),
    (5.75, pretty_midi.note_name_to_number('A3'), 60),
    (5.75, pretty_midi.note_name_to_number('C4'), 60),
    (5.75, pretty_midi.note_name_to_number('E3'), 60),
]

for time, pitch, velocity in piano_notes_bar4:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Drums: Bar 4 - same pattern, slightly more energetic
drum_notes_bar4 = [
    (5.0, pretty_midi.note_number_to_name(36), 85),  # Kick on 1
    (5.25, pretty_midi.note_number_to_name(38), 75),  # Snare on 2
    (5.5, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 3
    (5.75, pretty_midi.note_number_to_name(38), 80),  # Snare on 4
    (5.9375, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 4 &
    (6.0, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 4
    (6.125, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 4 +
    (6.25, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 4 ++
    (6.375, pretty_midi.note_number_to_name(42), 65),  # Hi-hat on 4 +++

    # End of bar 4
]

for time, note_name, velocity in drum_notes_bar4:
    note = pretty_midi.Note(velocity=velocity, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.05)
    drums.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
