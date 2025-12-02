
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),  # D#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # B
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # B
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # B
]
piano.notes.extend(piano_notes)

# Saxophone - Dante (one short motif, start it, leave it hanging, come back and finish it)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),   # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
