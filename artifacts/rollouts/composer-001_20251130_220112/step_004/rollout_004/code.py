
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches, no same note twice)
bass_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # E
    # Bar 3: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # E
    # Bar 4: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody - one short motif, start it, leave it hanging, come back and finish it)
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # F
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # D
    # Bar 4: Finish motif
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
