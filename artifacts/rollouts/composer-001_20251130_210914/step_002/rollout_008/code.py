
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &1
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &2
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &3
    (42, 1.125, 0.1875),  # Hihat on 4
    (42, 1.3125, 0.1875),  # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (24, 1.5, 1.625),  # F (1)
    (25, 1.625, 1.75),  # F# (2)
    (23, 1.75, 1.875),  # E (3)
    (24, 1.875, 2.0),  # F (4)
    (26, 2.0, 2.125),  # G (1)
    (27, 2.125, 2.25),  # G# (2)
    (25, 2.25, 2.375),  # F# (3)
    (26, 2.375, 2.5),  # G (4)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 1.625, 1.75),  # C7 (2)
    (39, 1.625, 1.75),
    (41, 1.625, 1.75),
    (43, 1.625, 1.75),
    (45, 2.125, 2.25),  # C7 (4)
    (39, 2.125, 2.25),
    (41, 2.125, 2.25),
    (43, 2.125, 2.25),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: short motif on 1 and 3
sax_notes = [
    (46, 1.5, 1.875),  # Bb (1)
    (49, 2.0, 2.375),  # D (3)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (27, 3.0, 3.125),  # G (1)
    (28, 3.125, 3.25),  # G# (2)
    (26, 3.25, 3.375),  # G (3)
    (27, 3.375, 3.5),  # G (4)
    (29, 3.5, 3.625),  # A (1)
    (30, 3.625, 3.75),  # A# (2)
    (28, 3.75, 3.875),  # G# (3)
    (29, 3.875, 4.0),  # A (4)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 3.125, 3.25),  # C7 (2)
    (39, 3.125, 3.25),
    (41, 3.125, 3.25),
    (43, 3.125, 3.25),
    (45, 3.625, 3.75),  # C7 (4)
    (39, 3.625, 3.75),
    (41, 3.625, 3.75),
    (43, 3.625, 3.75),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: continuation of motif, leave it hanging
sax_notes = [
    (49, 3.0, 3.375),  # D (1)
    (51, 3.5, 3.875),  # F (3)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (30, 4.5, 4.625),  # A# (1)
    (31, 4.625, 4.75),  # Bb (2)
    (29, 4.75, 4.875),  # A (3)
    (30, 4.875, 5.0),  # A# (4)
    (32, 5.0, 5.125),  # B (1)
    (33, 5.125, 5.25),  # B# (2)
    (31, 5.25, 5.375),  # Bb (3)
    (32, 5.375, 5.5),  # B (4)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 4.625, 4.75),  # C7 (2)
    (39, 4.625, 4.75),
    (41, 4.625, 4.75),
    (43, 4.625, 4.75),
    (45, 5.125, 5.25),  # C7 (4)
    (39, 5.125, 5.25),
    (41, 5.125, 5.25),
    (43, 5.125, 5.25),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: complete the motif
sax_notes = [
    (51, 4.5, 4.875),  # F (1)
    (46, 5.0, 5.375),  # Bb (3)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 4.875),  # Kick on 1
    (38, 4.875, 5.0),  # Snare on 2
    (42, 4.5, 4.6875),  # Hihat on 1
    (42, 4.6875, 4.875),  # Hihat on &1
    (42, 4.875, 5.0),  # Hihat on 2
    (42, 5.0, 5.1875),  # Hihat on &2
    (36, 5.0, 5.375),  # Kick on 3
    (38, 5.375, 5.5),  # Snare on 4
    (42, 5.0, 5.1875),  # Hihat on 3
    (42, 5.1875, 5.375),  # Hihat on &3
    (42, 5.375, 5.5),  # Hihat on 4
    (42, 5.5, 5.6875),  # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
