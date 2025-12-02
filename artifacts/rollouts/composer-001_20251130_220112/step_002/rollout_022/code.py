
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
    # Kick on 1 and 3
    (36, 0.0, 0.375),
    (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375),
    (38, 2.25, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (62, 1.5, 1.5),  # D
    (63, 1.5, 1.5),  # Eb
    (64, 1.5, 1.5),  # E
    (62, 1.5, 1.5),  # D
    # Bar 3
    (60, 3.0, 3.0),  # B
    (61, 3.0, 3.0),  # C
    (62, 3.0, 3.0),  # D
    (60, 3.0, 3.0),  # B
    # Bar 4
    (64, 4.5, 4.5),  # E
    (65, 4.5, 4.5),  # F
    (67, 4.5, 4.5),  # G
    (64, 4.5, 4.5),  # E
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.5, 1.5),  # G7
    (66, 1.5, 1.5),
    (69, 1.5, 1.5),
    (71, 1.5, 1.5),
    # Bar 3
    (67, 3.0, 3.0),  # G7
    (66, 3.0, 3.0),
    (69, 3.0, 3.0),
    (71, 3.0, 3.0),
    # Bar 4
    (67, 4.5, 4.5),  # G7
    (66, 4.5, 4.5),
    (69, 4.5, 4.5),
    (71, 4.5, 4.5),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Short motif, make it sing
sax_notes = [
    # Bar 2
    (64, 1.5, 1.75),  # E
    (66, 1.75, 2.0),  # G
    # Bar 3
    (62, 3.0, 3.25),  # D
    (64, 3.25, 3.5),  # E
    # Bar 4
    (66, 4.5, 4.75),  # G
    (64, 4.75, 5.0),  # E
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bars 2-4
drum_notes_2_4 = [
    # Kick on 1 and 3
    (36, 1.5, 1.875),
    (36, 2.625, 2.875),
    (36, 3.75, 4.0),
    (36, 4.875, 5.125),
    # Snare on 2 and 4
    (38, 2.25, 2.5),
    (38, 3.375, 3.625),
    (38, 4.5, 4.75),
    # Hi-hat on every eighth
    (42, 1.5, 1.6875),
    (42, 1.6875, 1.875),
    (42, 1.875, 2.0625),
    (42, 2.0625, 2.25),
    (42, 2.25, 2.4375),
    (42, 2.4375, 2.625),
    (42, 2.625, 2.8125),
    (42, 2.8125, 3.0),
    (42, 3.0, 3.1875),
    (42, 3.1875, 3.375),
    (42, 3.375, 3.5625),
    (42, 3.5625, 3.75),
    (42, 3.75, 3.9375),
    (42, 3.9375, 4.125),
    (42, 4.125, 4.3125),
    (42, 4.3125, 4.5),
    (42, 4.5, 4.6875),
    (42, 4.6875, 4.875),
    (42, 4.875, 5.0)
]
for note in drum_notes_2_4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
