
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

# Marcus: Walking bass line (Fm root and fifths with chromatic approaches)
bass_notes = [
    # F2 (MIDI 53) root on 1
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # C2 (MIDI 48) fifth with chromatic approach (E2 = 50)
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.375),
    # F2 again on 3
    pretty_midi.Note(velocity=80, pitch=53, start=2.375, end=2.75),
    # Ab2 (MIDI 50) chromatic approach to G2 (MIDI 49) which is a b7
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Db)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Db4
    # Bar 3: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # G4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.9375),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax motif (Bar 2-4)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # G4
    # Bar 3: Continue the motif with a chromatic approach
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # C4
    # Bar 4: Resolution of the motif
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),   # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.375),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
