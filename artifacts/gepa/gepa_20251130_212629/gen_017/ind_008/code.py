
import pretty_midi

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds per beat at 160 BPM: 60 / 160 = 0.375s per beat
# Bar length = 4 beats = 1.5 seconds

# Fill the bar with hihat on every eighth
for i in range(0, 8):
    note = pretty_midi.Note(velocity=60, pitch=hihat, start=i * 0.375, end=(i + 1) * 0.375)
    drums.notes.append(note)

# Kick on 1 and 3 (beats 0 and 2)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Snare on 2 and 4 (beats 1 and 3)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet enters
# Start with sax, bass, and piano

# Bass line: Walking line in F, chromatic approaches, no repeated notes
# F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F# -> G -> Ab -> A -> Bb

bass_notes = [
    (1.5, 77),   # F (4th fret on E string)
    (1.75, 78),  # G
    (2.0, 76),   # Ab
    (2.25, 77),  # A
    (2.5, 75),   # Bb
    (2.75, 76),  # B
    (3.0, 72),   # C
    (3.25, 71),  # Db
    (3.5, 72),   # D
    (3.75, 71),  # Eb
    (4.0, 72),   # E
    (4.25, 77),  # F# (chromatic approach)
    (4.5, 78),   # G
    (4.75, 76),  # Ab
    (5.0, 77),   # A
    (5.25, 75),  # Bb
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=75, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab), E7 (E, G#, B, D), A7 (A, C#, E, G)

# Bar 2 (1.5 - 3.0)
chord = pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0)  # A
chord = pretty_midi.Note(velocity=100, pitch=81, start=1.75, end=2.0)  # C
chord = pretty_midi.Note(velocity=100, pitch=84, start=1.75, end=2.0)  # E
chord = pretty_midi.Note(velocity=100, pitch=82, start=1.75, end=2.0)  # Bb
piano.notes.append(chord)

# Bar 3 (3.0 - 4.5)
chord = pretty_midi.Note(velocity=100, pitch=80, start=3.25, end=3.5)  # Bb
chord = pretty_midi.Note(velocity=100, pitch=83, start=3.25, end=3.5)  # D
chord = pretty_midi.Note(velocity=100, pitch=84, start=3.25, end=3.5)  # F
chord = pretty_midi.Note(velocity=100, pitch=82, start=3.25, end=3.5)  # Ab
piano.notes.append(chord)

# Bar 4 (4.5 - 6.0)
chord = pretty_midi.Note(velocity=100, pitch=85, start=4.75, end=5.0)  # E
chord = pretty_midi.Note(velocity=100, pitch=87, start=4.75, end=5.0)  # G#
chord = pretty_midi.Note(velocity=100, pitch=89, start=4.75, end=5.0)  # B
chord = pretty_midi.Note(velocity=100, pitch=84, start=4.75, end=5.0)  # D
piano.notes.append(chord)

# Saxophone: One short motif, 3 notes, suspended, then finished in the final bar
# F -> A -> Bb -> B -> A -> G -> F
# Play first three notes in bar 2, leave it hanging, come back in bar 4

note1 = pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=87, start=1.75, end=2.0)  # A
note3 = pretty_midi.Note(velocity=100, pitch=88, start=2.0, end=2.25)  # Bb

sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

note4 = pretty_midi.Note(velocity=100, pitch=89, start=4.75, end=5.0)  # B
note5 = pretty_midi.Note(velocity=100, pitch=87, start=5.0, end=5.25)  # A
note6 = pretty_midi.Note(velocity=100, pitch=86, start=5.25, end=5.5)  # G
note7 = pretty_midi.Note(velocity=100, pitch=84, start=5.5, end=5.75)  # F

sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
