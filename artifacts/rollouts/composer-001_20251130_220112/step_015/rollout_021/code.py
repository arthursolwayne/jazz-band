
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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (bass) - walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.625, end=1.75),   # F#
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.125, end=2.25),   # F#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),   # F
    pretty_midi.Note(velocity=90, pitch=63, start=2.375, end=2.5),   # E
]
bass.notes.extend(bass_notes)

# Diane (piano) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),   # E♭
    # Bar 3 - 7th chord on B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # B♭
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),   # A♭
    # Bar 4 - 7th chord on E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),   # E
    pretty_midi.Note(velocity=90, pitch=74, start=2.875, end=3.0),   # G#
    pretty_midi.Note(velocity=90, pitch=76, start=2.875, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Little Ray (drums) - same pattern as bar 1, shifted
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Dante (sax) - motif
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # B♭
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # G
    # Bar 3: Silence
    # Bar 4: Resume motif
    pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0),   # A
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25),   # B♭
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
