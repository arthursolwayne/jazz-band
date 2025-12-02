
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = BEAT * 4  # seconds per bar
NOTE_DURATION = BEAT / 4  # quarter note duration in seconds

# Time for each bar (in seconds)
bar_times = [0, BAR, BAR * 2, BAR * 3]

# ----------------------------
# Drums: Little Ray
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same
# ----------------------------

# Bar 1 (0-1.5s)
drum_notes = [
    # Kick on 1 and 3
    (pretty_midi.note_number_to_midi(36), 0.0, NOTE_DURATION),
    (pretty_midi.note_number_to_midi(36), NOTE_DURATION * 2, NOTE_DURATION),
    # Snare on 2 and 4
    (pretty_midi.note_number_to_midi(38), NOTE_DURATION, NOTE_DURATION),
    (pretty_midi.note_number_to_midi(38), NOTE_DURATION * 3, NOTE_DURATION),
    # Hihat on every eighth
    (pretty_midi.note_number_to_midi(42), 0.0, NOTE_DURATION / 2),
    (pretty_midi.note_number_to_midi(42), NOTE_DURATION / 2, NOTE_DURATION / 2),
    (pretty_midi.note_number_to_midi(42), NOTE_DURATION, NOTE_DURATION / 2),
    (pretty_midi.note_number_to_midi(42), NOTE_DURATION * 1.5, NOTE_DURATION / 2)
]

# Bar 2-4 (1.5s to 6s)
for i in range(1, 4):
    for note in drum_notes:
        note_time = note[1] + bar_times[i]
        note_duration = note[2]
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note_time, end=note_time + note_duration))

# ----------------------------
# Bass: Marcus
# Walking line, chromatic approaches, never the same note twice
# Bar 1: Rest
# Bar 2: Dm7 walking line
# Bar 3: Chromatic approach to F
# Bar 4: Chromatic approach to G
# ----------------------------

# Bar 2 (1.5s to 3s)
bass_notes = [
    (pretty_midi.note_number_to_midi(62), 1.5, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(60), 1.875, NOTE_DURATION),  # C
    (pretty_midi.note_number_to_midi(61), 2.25, NOTE_DURATION),  # C#
    (pretty_midi.note_number_to_midi(63), 2.625, NOTE_DURATION)  # D#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2]))

# Bar 3 (3s to 4.5s)
bass_notes = [
    (pretty_midi.note_number_to_midi(62), 3.0, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(61), 3.375, NOTE_DURATION),  # C#
    (pretty_midi.note_number_to_midi(60), 3.75, NOTE_DURATION),  # C
    (pretty_midi.note_number_to_midi(59), 4.125, NOTE_DURATION)  # B
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2]))

# Bar 4 (4.5s to 6s)
bass_notes = [
    (pretty_midi.note_number_to_midi(62), 4.5, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(63), 4.875, NOTE_DURATION),  # D#
    (pretty_midi.note_number_to_midi(64), 5.25, NOTE_DURATION),  # E
    (pretty_midi.note_number_to_midi(65), 5.625, NOTE_DURATION)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2]))

# ----------------------------
# Piano: Diane
# 7th chords, comp on 2 and 4
# Bar 1: Rest
# Bar 2: Dm7 (D F A C)
# Bar 3: F7 (F A C E)
# Bar 4: G7 (G B D F)
# ----------------------------

# Bar 2 (1.5s to 3s)
piano_notes = [
    (pretty_midi.note_number_to_midi(62), 1.875, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(65), 1.875, NOTE_DURATION),  # F
    (pretty_midi.note_number_to_midi(67), 1.875, NOTE_DURATION),  # A
    (pretty_midi.note_number_to_midi(69), 1.875, NOTE_DURATION)   # C
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Bar 3 (3s to 4.5s)
piano_notes = [
    (pretty_midi.note_number_to_midi(65), 3.375, NOTE_DURATION),  # F
    (pretty_midi.note_number_to_midi(67), 3.375, NOTE_DURATION),  # A
    (pretty_midi.note_number_to_midi(69), 3.375, NOTE_DURATION),  # C
    (pretty_midi.note_number_to_midi(71), 3.375, NOTE_DURATION)   # E
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Bar 4 (4.5s to 6s)
piano_notes = [
    (pretty_midi.note_number_to_midi(67), 5.25, NOTE_DURATION),  # G
    (pretty_midi.note_number_to_midi(71), 5.25, NOTE_DURATION),  # B
    (pretty_midi.note_number_to_midi(69), 5.25, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(65), 5.25, NOTE_DURATION)   # F
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# ----------------------------
# Sax: Dante
# Bar 1: Rest
# Bar 2: Start the motif — D, E, F#, D (one short motif, sing, leave it hanging)
# Bar 3: Rest
# Bar 4: Return to complete the motif — D, E, F#, D
# ----------------------------

# Bar 2 (1.5s to 3s)
sax_notes = [
    (pretty_midi.note_number_to_midi(62), 1.5, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(64), 1.875, NOTE_DURATION),  # E
    (pretty_midi.note_number_to_midi(66), 2.25, NOTE_DURATION),  # F#
    (pretty_midi.note_number_to_midi(62), 2.625, NOTE_DURATION)   # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Bar 4 (4.5s to 6s)
sax_notes = [
    (pretty_midi.note_number_to_midi(62), 4.5, NOTE_DURATION),  # D
    (pretty_midi.note_number_to_midi(64), 4.875, NOTE_DURATION),  # E
    (pretty_midi.note_number_to_midi(66), 5.25, NOTE_DURATION),  # F#
    (pretty_midi.note_number_to_midi(62), 5.625, NOTE_DURATION)   # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
