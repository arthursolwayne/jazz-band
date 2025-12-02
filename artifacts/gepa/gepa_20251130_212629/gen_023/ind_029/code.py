
import pretty_midi
import numpy as np

# Create a PrettyMIDI object at 160 BPM in F major
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Time in seconds per bar: 160 BPM -> 60/160 = 0.375 sec per beat, 1.5 sec per bar
bar_length = 1.5  # seconds
beat_length = 0.375  # seconds
note_length = beat_length * 0.5  # half note
rest = beat_length * 0.5  # half rest

# Define the key: F major
F_MAJOR = [65, 67, 69, 72, 74, 76, 77]  # MIDI notes for F, G, A, C, D, E, F#

# Bar 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: Time 0.0 to 1.5 sec
# Kick on 0.0 and 0.75
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0.0, end=0.0 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0.75, end=0.75 + 0.125))

# Snare on 0.375 and 1.125
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.125 + 0.125))

# Hi-hats on every eighth
for i in range(8):
    start = i * 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.0625))

# Bar 2: Everyone in
# Bass: Walking line, chromatic, in F major
# Start at bar 1.5 (time 1.5)

# Bass line: F, Gb, G, A, Bb, B, C, Db
bass_notes = [65, 66, 67, 69, 70, 71, 72, 73]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * beat_length
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: start at 1.5, comp on beat 2 and 4 (0.375 and 0.75 from bar start)

# Bar 2 Chord: F7 = F, A, C, Eb
root = 65
third = 68
fifth = 72
seventh = 69  # Eb
chord = [root, third, fifth, seventh]

# Play the 7th chord on beat 2 (0.375) and beat 4 (0.75) of the bar
for beat_offset in [0.375, 0.75]:
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.5 + beat_offset, end=1.5 + beat_offset + 0.125))

# Sax: Motif — one short phrase, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: F, Ab, Bb, F (half note, half rest, half note, half rest)
note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + note_length)
note2 = pretty_midi.Note(velocity=110, pitch=69, start=1.5 + note_length + rest, end=1.5 + note_length + rest + note_length)

sax.notes.append(note1)
sax.notes.append(note2)

# Bar 3: Everyone continues
# Bass: Next walking line
# Use same pattern but shifted up by a half step
bass_notes_shifted = [note + 1 for note in bass_notes]
for i, note in enumerate(bass_notes_shifted):
    start = 1.5 + i * beat_length + 1.5  # Bar 3 (start at 3.0)
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Bar 3 Chord: Bb7 = Bb, D, F, Ab
root = 70
third = 74
fifth = 65
seventh = 69
chord = [root, third, fifth, seventh]

for beat_offset in [0.375, 0.75]:
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.0 + beat_offset, end=3.0 + beat_offset + 0.125))

# Sax: Continue the motif — repeat phrase
note3 = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.0 + note_length)
note4 = pretty_midi.Note(velocity=110, pitch=69, start=3.0 + note_length + rest, end=3.0 + note_length + rest + note_length)

sax.notes.append(note3)
sax.notes.append(note4)

# Bar 4: Everyone in
# Bass: Next walking line
bass_notes_shifted = [note + 1 for note in bass_notes_shifted]
for i, note in enumerate(bass_notes_shifted):
    start = 1.5 + i * beat_length + 3.0  # Bar 4 (start at 4.5)
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Bar 4 Chord: E7 = E, G#, B, D
root = 76
third = 79
fifth = 71
seventh = 70
chord = [root, third, fifth, seventh]

for beat_offset in [0.375, 0.75]:
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5 + beat_offset, end=4.5 + beat_offset + 0.125))

# Sax: End the motif — resolve it
note5 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.5 + note_length)
note6 = pretty_midi.Note(velocity=110, pitch=65, start=4.5 + note_length + rest, end=4.5 + note_length + rest + note_length)

sax.notes.append(note5)
sax.notes.append(note6)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
