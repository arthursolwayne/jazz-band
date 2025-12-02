
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = Program(33)  # Electric Bass
piano_program = Program(0)  # Acoustic Grand Piano
drums_program = Program(0)  # Acoustic Grand Piano (used for percussion)
sax_program = Program(65)   # Tenor Saxophone

# Bass instrument
bass = Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano instrument
piano = Instrument(program=piano_program)
pm.instruments.append(piano)

# Drums instrument (using piano for percussion)
drums = Instrument(program=drums_program)
pm.instruments.append(drums)

# Sax instrument
sax = Instrument(program=sax_program)
pm.instruments.append(sax)

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 6.0 / 4  # seconds per bar
note_duration = bar_length / 8  # 8th note

# Kick on 1 and 3
drums.notes.append(Note(36, 60, 0, note_duration))
drums.notes.append(Note(36, 60, 2 * note_duration, note_duration))

# Snare on 2 and 4
drums.notes.append(Note(38, 60, 1 * note_duration, note_duration))
drums.notes.append(Note(38, 60, 3 * note_duration, note_duration))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(Note(42, 60, i * note_duration, note_duration / 2))

# Bar 2: Everyone enters
# Bass: Walking line, chromatic approaches
bass_notes = [
    (36, 0), (37, note_duration), (38, 2 * note_duration), (39, 3 * note_duration),
    (38, 4 * note_duration), (37, 5 * note_duration), (36, 6 * note_duration), (35, 7 * note_duration)
]
for pitch, start in bass_notes:
    bass.notes.append(Note(pitch, 100, start, note_duration))

# Piano: 7th chords on 2 and 4
# Bar 2, beat 2: D7 (D, F#, A, C)
piano.notes.append(Note(62, 100, 1 * note_duration, note_duration))
piano.notes.append(Note(67, 100, 1 * note_duration, note_duration))
piano.notes.append(Note(71, 100, 1 * note_duration, note_duration))
piano.notes.append(Note(69, 100, 1 * note_duration, note_duration))

# Bar 2, beat 4: G7 (G, B, D, F)
piano.notes.append(Note(67, 100, 3 * note_duration, note_duration))
piano.notes.append(Note(71, 100, 3 * note_duration, note_duration))
piano.notes.append(Note(62, 100, 3 * note_duration, note_duration))
piano.notes.append(Note(65, 100, 3 * note_duration, note_duration))

# Sax: Melody - sparse, expressive
# Bar 2, beat 1: D (62), quarter note
sax.notes.append(Note(62, 100, 0, 2 * note_duration))

# Bar 2, beat 3: Bb (60), eighth note
sax.notes.append(Note(60, 100, 3 * note_duration, note_duration))

# Bar 3: Continue the melody - sparse, with space
# Bar 3, beat 2: F# (67), eighth note
sax.notes.append(Note(67, 100, 1 * note_duration, note_duration))

# Bar 3, beat 4: rest
# Bar 4: Continue the melody, finish the motif
# Bar 4, beat 1: D (62), quarter note
sax.notes.append(Note(62, 100, 4 * note_duration, 2 * note_duration))

# Bar 4, beat 3: Bb (60), eighth note
sax.notes.append(Note(60, 100, 7 * note_duration, note_duration))

# Add some dynamic variation
for note in sax.notes:
    if note.start >= 0 and note.start < bar_length:
        note.velocity = 100
    elif note.start >= bar_length and note.start < 2 * bar_length:
        note.velocity = 80
    elif note.start >= 2 * bar_length and note.start < 3 * bar_length:
        note.velocity = 90
    else:
        note.velocity = 100

# Save the MIDI file
pm.write("jazz_intro.mid")
