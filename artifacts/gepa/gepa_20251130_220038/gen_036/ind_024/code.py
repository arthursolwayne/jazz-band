
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=36, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0),  # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=39, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=36, start=4.25, end=4.5),  # Eb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=37, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# Bar 2 (1.5 - 3.0s) - Fm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # D

    # Bar 3 (3.0 - 4.5s) - Fm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # D

    # Bar 4 (4.5 - 6.0s) - Fm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing
# Bar 2 (1.5 - 3.0s) - Start the motif
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D

    # Bar 3 (3.0 - 4.5s) - Leave it hanging, return later
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # D

    # Bar 4 (4.5 - 6.0s) - Finish the motif
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
