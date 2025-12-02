
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.5),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=37, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=36, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=35, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=33, start=3.25, end=3.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=34, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=4.75, end=5.0),  # Db
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - F7 on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # D
    # Bar 3 - Bb7 on 2
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.25),  # G
    # Bar 4 - Eb7 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.25),  # B
    # Bar 4 - F7 on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # D
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=63, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # E
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
