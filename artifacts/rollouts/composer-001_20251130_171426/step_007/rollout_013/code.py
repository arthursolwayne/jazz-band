
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm
bass_notes = [
    (64, 1.5, 1.5),  # F
    (63, 1.5, 1.5),  # Eb
    (62, 1.5, 1.5),  # D
    (60, 1.5, 1.5),  # C
    (62, 1.5, 1.5),  # D
    (63, 1.5, 1.5),  # Eb
    (64, 1.5, 1.5),  # F
    (65, 1.5, 1.5)   # Gb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Diane: Comp on 2 and 4, 7th chords
piano_notes = [
    (64, 1.5, 1.5),  # Fm7 (F, Ab, C, Eb)
    (67, 1.5, 1.5),
    (69, 1.5, 1.5),
    (65, 1.5, 1.5),
    (64, 2.25, 2.25),  # Fm7 again
    (67, 2.25, 2.25),
    (69, 2.25, 2.25),
    (65, 2.25, 2.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.5),  # Kick on 1
    (42, 1.5, 1.5),  # Hihat on 1
    (38, 1.875, 1.875),  # Snare on 2
    (42, 1.875, 1.875),  # Hihat on 2
    (36, 2.25, 2.25),  # Kick on 3
    (42, 2.25, 2.25),  # Hihat on 3
    (38, 2.625, 2.625),  # Snare on 4
    (42, 2.625, 2.625)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante: Sax motif (start on 1.5s)
# Motif: F (64), Ab (66), C (67), Bb (62)
sax_notes = [
    (64, 1.5, 1.75),
    (66, 1.75, 2.0),
    (67, 2.0, 2.25),
    (62, 2.25, 2.5)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    (64, 3.0, 3.0),  # F
    (63, 3.0, 3.0),  # Eb
    (62, 3.0, 3.0),  # D
    (60, 3.0, 3.0),  # C
    (62, 3.0, 3.0),  # D
    (63, 3.0, 3.0),  # Eb
    (64, 3.0, 3.0),  # F
    (65, 3.0, 3.0)   # Gb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Diane: Comp on 2 and 4, 7th chords
piano_notes = [
    (64, 3.0, 3.0),  # Fm7
    (67, 3.0, 3.0),
    (69, 3.0, 3.0),
    (65, 3.0, 3.0),
    (64, 3.75, 3.75),  # Fm7 again
    (67, 3.75, 3.75),
    (69, 3.75, 3.75),
    (65, 3.75, 3.75)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 3.0),  # Kick on 1
    (42, 3.0, 3.0),  # Hihat on 1
    (38, 3.375, 3.375),  # Snare on 2
    (42, 3.375, 3.375),  # Hihat on 2
    (36, 3.75, 3.75),  # Kick on 3
    (42, 3.75, 3.75),  # Hihat on 3
    (38, 4.125, 4.125),  # Snare on 4
    (42, 4.125, 4.125)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante: Sax motif (start on 3.0s)
# Motif: F (64), Ab (66), C (67), Bb (62)
sax_notes = [
    (64, 3.0, 3.25),
    (66, 3.25, 3.5),
    (67, 3.5, 3.75),
    (62, 3.75, 4.0)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    (64, 4.5, 4.5),  # F
    (63, 4.5, 4.5),  # Eb
    (62, 4.5, 4.5),  # D
    (60, 4.5, 4.5),  # C
    (62, 4.5, 4.5),  # D
    (63, 4.5, 4.5),  # Eb
    (64, 4.5, 4.5),  # F
    (65, 4.5, 4.5)   # Gb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Diane: Comp on 2 and 4, 7th chords
piano_notes = [
    (64, 4.5, 4.5),  # Fm7
    (67, 4.5, 4.5),
    (69, 4.5, 4.5),
    (65, 4.5, 4.5),
    (64, 5.25, 5.25),  # Fm7 again
    (67, 5.25, 5.25),
    (69, 5.25, 5.25),
    (65, 5.25, 5.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 4.5),  # Kick on 1
    (42, 4.5, 4.5),  # Hihat on 1
    (38, 4.875, 4.875),  # Snare on 2
    (42, 4.875, 4.875),  # Hihat on 2
    (36, 5.25, 5.25),  # Kick on 3
    (42, 5.25, 5.25),  # Hihat on 3
    (38, 5.625, 5.625),  # Snare on 4
    (42, 5.625, 5.625)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante: Sax motif (start on 4.5s)
# Motif: F (64), Ab (66), C (67), Bb (62)
sax_notes = [
    (64, 4.5, 4.75),
    (66, 4.75, 5.0),
    (67, 5.0, 5.25),
    (62, 5.25, 5.5)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
