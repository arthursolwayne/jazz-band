
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (59, 1.5, 1.5),   # D (root)
    (60, 1.875, 1.875),  # Eb (chromatic up)
    (58, 2.25, 2.25),    # C (b7)
    (62, 2.625, 2.625),  # F (3rd)
    (60, 2.625, 2.625),  # Eb (chromatic down)
    (59, 3.0, 3.0),      # D (root)
    (62, 3.375, 3.375),  # F
    (63, 3.75, 3.75),    # F#
    (60, 4.125, 4.125),  # Eb
    (59, 4.5, 4.5),      # D
    (62, 4.875, 4.875),  # F
    (63, 5.25, 5.25)     # F#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 1.5),    # F (3rd)
    (65, 1.5, 1.5),    # A (7th)
    (60, 1.875, 1.875),  # D
    (64, 1.875, 1.875),  # Bb (b7)
    # Bar 3
    (62, 2.25, 2.25),    # F
    (65, 2.25, 2.25),    # A
    (60, 2.625, 2.625),  # D
    (64, 2.625, 2.625),  # Bb
    # Bar 4
    (62, 3.0, 3.0),    # F
    (65, 3.0, 3.0),    # A
    (60, 3.375, 3.375),  # D
    (64, 3.375, 3.375),  # Bb
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.5),    # F
    (63, 1.625, 1.625),  # F#
    (62, 1.875, 1.875),  # F
    (60, 2.25, 2.25),    # D
    (62, 2.625, 2.625),  # F
    (63, 2.75, 2.75),    # F#
    (62, 3.0, 3.0),    # F
    (60, 3.375, 3.375),  # D
    (62, 3.75, 3.75),    # F
    (63, 3.875, 3.875),  # F#
    (62, 4.125, 4.125),  # F
    (60, 4.5, 4.5)       # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
