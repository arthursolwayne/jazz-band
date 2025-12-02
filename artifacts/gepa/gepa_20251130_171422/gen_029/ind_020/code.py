
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.0),  # F

    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=44, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.375, end=2.5),  # F

    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=2.875, end=3.0),  # G

    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.5),  # F

    pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=3.875, end=4.0),  # E

    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.125),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=4.25, end=4.375),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=4.375, end=4.5),  # G

    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.0),  # F

    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=80, pitch=49, start=5.375, end=5.5),  # A

    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.875, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.625),  # Eb

    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.125),  # Bb

    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.5, end=2.625),  # A

    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.125),  # G

    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.625),  # B

    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.125),  # G

    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.625),  # A

    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.125),  # G
]
piano.notes.extend(piano_notes)

# Sax - Dante: sparse, expressive, one short motif
sax_notes = [
    # Start motif (Bar 2, 1.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D

    # Echo and resolve (Bar 3, 2.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # C

    # Final phrase (Bar 4, 3.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D

    # Final resolution
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI to file
midi.write("jazz_intro.mid")
