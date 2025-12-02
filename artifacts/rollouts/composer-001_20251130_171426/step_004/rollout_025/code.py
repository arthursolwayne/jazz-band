
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5s)
    (59, 1.5, 1.75),  # D
    (60, 1.75, 2.0),  # Eb
    (58, 2.0, 2.25),  # C
    (59, 2.25, 2.5),  # D
    # Bar 3 (2.5s)
    (60, 2.5, 2.75),  # Eb
    (61, 2.75, 3.0),  # F
    (60, 3.0, 3.25),  # Eb
    (59, 3.25, 3.5),  # D
    # Bar 4 (3.5s)
    (58, 3.5, 3.75),  # C
    (59, 3.75, 4.0),  # D
    (61, 4.0, 4.25),  # F
    (62, 4.25, 4.5),  # G
    # Bar 4 continuation
    (61, 4.5, 4.75),  # F
    (60, 4.75, 5.0),  # Eb
    (59, 5.0, 5.25),  # D
    (58, 5.25, 5.5),  # C
    (57, 5.5, 5.75),  # Bb
    (59, 5.75, 6.0),  # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Diane on piano: 7th chords, comp on 2 and 4, moving, angry
piano_notes = [
    # Bar 2 (1.5s)
    (62, 1.75, 2.0),  # F7: F, A, C, Eb
    (64, 1.75, 2.0),
    (65, 1.75, 2.0),
    (67, 1.75, 2.0),
    # Bar 3 (2.5s)
    (62, 2.75, 3.0),
    (64, 2.75, 3.0),
    (65, 2.75, 3.0),
    (67, 2.75, 3.0),
    # Bar 4 (3.5s)
    (62, 4.75, 5.0),
    (64, 4.75, 5.0),
    (65, 4.75, 5.0),
    (67, 4.75, 5.0),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5s)
    (36, 1.5, 1.875),
    (36, 2.625, 2.875),
    (38, 1.875, 2.125),
    (38, 3.125, 3.375),
    # Bar 3 (2.5s)
    (36, 2.5, 2.875),
    (36, 3.625, 3.875),
    (38, 2.875, 3.125),
    (38, 4.125, 4.375),
    # Bar 4 (3.5s)
    (36, 3.5, 3.875),
    (36, 4.625, 4.875),
    (38, 3.875, 4.125),
    (38, 5.125, 5.375),
    # Hi-hats on all eighths
    (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875),
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante on sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Motif (Dm7)
    (62, 1.5, 1.625),  # F
    (60, 1.625, 1.75),  # D
    (64, 1.75, 1.875),  # G
    (62, 1.875, 2.0),  # F
    # Pause and return
    (62, 3.0, 3.125),  # F
    (60, 3.125, 3.25),  # D
    (64, 3.25, 3.375),  # G
    (62, 3.375, 3.5),  # F
    # End with a twist
    (65, 3.5, 3.75),  # A
    (62, 3.75, 4.0),  # F
    (64, 4.0, 4.25),  # G
    (62, 4.25, 4.5),  # F
    (60, 4.5, 4.75),  # D
    (62, 4.75, 5.0),  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
