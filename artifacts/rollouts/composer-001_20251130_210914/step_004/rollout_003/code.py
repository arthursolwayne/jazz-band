
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 1.5),     # D (root)
    (63, 1.875, 1.875), # Eb (chromatic)
    (60, 2.25, 2.25),   # Bb (5th)
    (61, 2.625, 2.625), # B (chromatic)
    (62, 3.0, 3.0),     # D
    (63, 3.375, 3.375), # Eb
    (60, 3.75, 3.75),   # Bb
    (61, 4.125, 4.125), # B
    (62, 4.5, 4.5),     # D
    (63, 4.875, 4.875), # Eb
    (60, 5.25, 5.25),   # Bb
    (61, 5.625, 5.625)  # B
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 1.875), # D7 (D, F#, A, C)
    (64, 1.875, 1.875),
    (69, 1.875, 1.875),
    (60, 1.875, 1.875),
    # Bar 3
    (62, 3.375, 3.375),
    (64, 3.375, 3.375),
    (69, 3.375, 3.375),
    (60, 3.375, 3.375),
    # Bar 4
    (62, 4.875, 4.875),
    (64, 4.875, 4.875),
    (69, 4.875, 4.875),
    (60, 4.875, 4.875)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 1.5),     # Kick on 1
    (42, 1.5, 1.5),     # Hihat on 1
    (38, 1.875, 1.875), # Snare on 2
    (42, 1.875, 1.875), # Hihat on 2
    (36, 2.25, 2.25),   # Kick on 3
    (42, 2.25, 2.25),   # Hihat on 3
    (38, 2.625, 2.625), # Snare on 4
    (42, 2.625, 2.625)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 3.0),     # Kick on 1
    (42, 3.0, 3.0),     # Hihat on 1
    (38, 3.375, 3.375), # Snare on 2
    (42, 3.375, 3.375), # Hihat on 2
    (36, 3.75, 3.75),   # Kick on 3
    (42, 3.75, 3.75),   # Hihat on 3
    (38, 4.125, 4.125), # Snare on 4
    (42, 4.125, 4.125)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 4.5),     # Kick on 1
    (42, 4.5, 4.5),     # Hihat on 1
    (38, 4.875, 4.875), # Snare on 2
    (42, 4.875, 4.875), # Hihat on 2
    (36, 5.25, 5.25),   # Kick on 3
    (42, 5.25, 5.25),   # Hihat on 3
    (38, 5.625, 5.625), # Snare on 4
    (42, 5.625, 5.625)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    (62, 1.5, 1.75),     # D
    (64, 1.75, 2.0),     # Eb
    (65, 2.0, 2.25),     # F
    (67, 2.25, 2.5),     # G
    (69, 2.5, 2.75),     # A
    (60, 2.75, 3.0),     # Bb
    (62, 3.0, 3.25),     # D
    (64, 3.25, 3.5),     # Eb
    (65, 3.5, 3.75),     # F
    (67, 3.75, 4.0),     # G
    (69, 4.0, 4.25),     # A
    (60, 4.25, 4.5),     # Bb
    (62, 4.5, 4.75),     # D
    (64, 4.75, 5.0),     # Eb
    (65, 5.0, 5.25),     # F
    (67, 5.25, 5.5),     # G
    (69, 5.5, 5.75),     # A
    (60, 5.75, 6.0)      # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
