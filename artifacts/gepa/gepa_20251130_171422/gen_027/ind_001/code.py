
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define key: F major
key = 'F'

# Define time signature: 4/4
time_signature = (4, 4)

# Create instruments
drums = pretty_midi.Instrument(program=128)  # Drums
bass = pretty_midi.Instrument(program=33)     # Double Bass
piano = pretty_midi.Instrument(program=0)     # Acoustic Piano
sax = pretty_midi.Instrument(program=64)      # Tenor Saxophone

pm.instruments = [drums, bass, piano, sax]

# Set the time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(time_signature[0], time_signature[1], 0)]

# Define note durations based on 160 BPM
beat_duration = pretty_midi.time_functions.bpm_to_tempo(160)
bar_duration = beat_duration * 4  # 4/4 time

# Helper function to get note number from note name
def note_name_to_number(note_name):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = int(note_name[-1])
    note_index = note_names.index(note_name[:-1])
    return note_index + 12 * (octave + 1)

# Bar 1: Drums (Little Ray)
# Subtle, sparse, with space and tension
drum_notes = [
    (pretty_midi.note_number_to_name(36), 0.1, 0.0),  # Kick at start of bar
    (pretty_midi.note_number_to_name(42), 0.1, 0.6),  # Snare on "2"
    (pretty_midi.note_number_to_name(46), 0.05, 0.9), # Hi-hat on "3" and "4"
    (pretty_midi.note_number_to_name(46), 0.05, 1.1), # Hi-hat on "4"
]

for note_name, duration, time in drum_notes:
    note_number = note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + duration)
    drums.notes.append(note)

# Bar 2: Bass (Marcus)
# Walking line with chromatic approach
bass_notes = [
    (note_name_to_number('F'), 0.25, 0.0),     # F
    (note_name_to_number('G'), 0.25, 0.25),    # G
    (note_name_to_number('A'), 0.25, 0.5),     # A
    (note_name_to_number('Bb'), 0.25, 0.75),   # Bb
    (note_name_to_number('B'), 0.25, 1.0),     # B
    (note_name_to_number('C'), 0.25, 1.25),    # C
    (note_name_to_number('D'), 0.25, 1.5),     # D
    (note_name_to_number('Eb'), 0.25, 1.75),   # Eb
]

for note_number, duration, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + duration)
    bass.notes.append(note)

# Bar 2: Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    (note_name_to_number('F'), 0.25, 0.5),
    (note_name_to_number('A'), 0.25, 0.5),
    (note_name_to_number('C'), 0.25, 0.5),
    (note_name_to_number('E'), 0.25, 0.5),

    # Bar 2, beat 4: Bb7
    (note_name_to_number('Bb'), 0.25, 1.0),
    (note_name_to_number('D'), 0.25, 1.0),
    (note_name_to_number('F'), 0.25, 1.0),
    (note_name_to_number('Ab'), 0.25, 1.0),
]

for note_number, duration, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + duration)
    piano.notes.append(note)

# Bar 2-4: Sax (You)
# Short, emotional motif: F - G - Bb - F (melodic minor)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2, beat 1: F (start of motif)
    (note_name_to_number('F'), 0.5, 0.0),
    # Bar 2, beat 2: G
    (note_name_to_number('G'), 0.5, 0.5),
    # Bar 2, beat 3: Bb (hang on this note)
    (note_name_to_number('Bb'), 0.25, 1.0),
    # Bar 3, beat 1: F (return and finish)
    (note_name_to_number('F'), 1.0, 1.25),
]

for note_number, duration, time in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=note_number, start=time, end=time + duration)
    sax.notes.append(note)

# Bar 3: Drums (Little Ray)
# Add more texture, rhythmic interest
drum_notes = [
    (pretty_midi.note_number_to_name(36), 0.1, 1.25), # Kick
    (pretty_midi.note_number_to_name(42), 0.1, 1.5),  # Snare on "3"
    (pretty_midi.note_number_to_name(46), 0.05, 1.6), # Hi-hat
    (pretty_midi.note_number_to_name(46), 0.05, 1.8), # Hi-hat
    (pretty_midi.note_number_to_name(46), 0.05, 2.0), # Hi-hat
    (pretty_midi.note_number_to_name(46), 0.05, 2.2), # Hi-hat
]

for note_name, duration, time in drum_notes:
    note_number = note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + duration)
    drums.notes.append(note)

# Bar 3: Bass (Marcus)
# Continue the walking line with chromatic variation
bass_notes = [
    (note_name_to_number('Eb'), 0.25, 2.0),     # Eb
    (note_name_to_number('F'), 0.25, 2.25),     # F
    (note_name_to_number('G'), 0.25, 2.5),      # G
    (note_name_to_number('A'), 0.25, 2.75),     # A
    (note_name_to_number('Bb'), 0.25, 3.0),     # Bb
    (note_name_to_number('B'), 0.25, 3.25),     # B
    (note_name_to_number('C'), 0.25, 3.5),      # C
    (note_name_to_number('D'), 0.25, 3.75),     # D
]

for note_number, duration, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + duration)
    bass.notes.append(note)

# Bar 3: Piano (Diane)
# Add some movement, comp on 2 and 4 again
piano_notes = [
    # Bar 3, beat 2: F7
    (note_name_to_number('F'), 0.25, 2.5),
    (note_name_to_number('A'), 0.25, 2.5),
    (note_name_to_number('C'), 0.25, 2.5),
    (note_name_to_number('E'), 0.25, 2.5),

    # Bar 3, beat 4: Bb7
    (note_name_to_number('Bb'), 0.25, 3.0),
    (note_name_to_number('D'), 0.25, 3.0),
    (note_name_to_number('F'), 0.25, 3.0),
    (note_name_to_number('Ab'), 0.25, 3.0),
]

for note_number, duration, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + duration)
    piano.notes.append(note)

# Bar 4: Drums (Little Ray)
# End with a clean, open-ended feel
drum_notes = [
    (pretty_midi.note_number_to_name(36), 0.1, 3.5), # Kick
    (pretty_midi.note_number_to_name(42), 0.1, 3.75), # Snare on "4"
    (pretty_midi.note_number_to_name(46), 0.1, 4.0),  # Hi-hat
]

for note_name, duration, time in drum_notes:
    note_number = note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + duration)
    drums.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro.mid')
