
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass (root and fifth with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, resolve on last bar)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=78, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=95, pitch=82, start=1.875, end=2.25),  # G
    # Bar 4: Cm7
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),  # Bb
    # Resolve on last bar
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=95, pitch=74, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Little Ray on drums (same pattern as bar 1)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Dante on sax (short motif, make it sing, start it, leave it hanging, finish it)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Ab
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
