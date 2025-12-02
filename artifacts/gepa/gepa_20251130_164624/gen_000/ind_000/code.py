
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=90, pitch=45, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.375),  # C#
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=2.75),  # D#
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.625),  # E♭
    # Bar 3: B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=2.375),  # B♭
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375),  # A♭
    # Bar 4: F7 again
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=2.875),  # E♭
]
piano.notes.extend(piano_notes)

# Sax line - Dante: one short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # E♭
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # E♭
    # Bar 4: Resolve it
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
