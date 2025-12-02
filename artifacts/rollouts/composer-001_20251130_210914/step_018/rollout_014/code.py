
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi>Note(36, 0.0, 1.0, 100))
drums.notes.append(pretty_midi.Note(36, 1.5, 2.5, 100))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(38, 0.75, 1.25, 100))
drums.notes.append(pretty_midi.Note(38, 2.25, 2.75, 100))

# Hi-hat on every eighth
for i in range(0, 6, 0.375):
    drums.notes.append(pretty_midi.Note(42, i, i + 0.125, 100))

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
# Dmin7 = D F A C
# Chromatic approaches: C# -> D, B -> C, A# -> B, G# -> A
notes = [62, 63, 65, 67, 62, 60, 62, 63, 65, 67, 62, 60, 62, 63, 65, 67]
for i, note in enumerate(notes):
    time = 1.5 + (i * 0.375)
    bass.notes.append(pretty_midi.Note(note, time, time + 0.25, 100))

# Piano: Dmin7, 7th chords, comp on 2 and 4
# Bar 2: Dmin7 (D F A C)
# Bar 3: G7 (G B D F)
# Bar 4: Cm7 (C Eb G Bb)
chords = [
    # Bar 2 (1.5 - 2.0s) - Dmin7
    (62, 1.5, 2.0), (64, 1.5, 2.0), (67, 1.5, 2.0), (69, 1.5, 2.0),
    # Bar 3 (2.5 - 3.0s) - G7
    (67, 2.5, 3.0), (69, 2.5, 3.0), (71, 2.5, 3.0), (72, 2.5, 3.0),
    # Bar 4 (3.5 - 4.0s) - Cm7
    (60, 3.5, 4.0), (63, 3.5, 4.0), (67, 3.5, 4.0), (70, 3.5, 4.0)
]
for note, start, end in chords:
    piano.notes.append(pretty_midi.Note(note, start, end, 100))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(36, start, start + 0.25, 100))
    drums.notes.append(pretty_midi.Note(36, start + 0.75, start + 1.0, 100))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(38, start + 0.375, start + 0.625, 100))
    drums.notes.append(pretty_midi.Note(38, start + 1.125, start + 1.375, 100))
    # Hi-hat on every eighth
    for i in range(0, 6, 0.375):
        drums.notes.append(pretty_midi.Note(42, start + i, start + i + 0.125, 100))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), Eb (63), F (64), D (62) - motif
# Play on 1 of bar 2
sax.notes.append(pretty_midi.Note(62, 1.5, 1.75, 100))
sax.notes.append(pretty_midi.Note(63, 1.75, 2.0, 100))
sax.notes.append(pretty_midi.Note(64, 2.0, 2.25, 100))
sax.notes.append(pretty_midi.Note(62, 2.25, 2.5, 100))  # leave it hanging
# Repeat the motif on 1 of bar 3
sax.notes.append(pretty_midi.Note(62, 3.0, 3.25, 100))
sax.notes.append(pretty_midi.Note(63, 3.25, 3.5, 100))
sax.notes.append(pretty_midi.Note(64, 3.5, 3.75, 100))
sax.notes.append(pretty_midi.Note(62, 3.75, 4.0, 100))  # finish it

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
