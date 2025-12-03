
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus - Walking bass line (F2-G2, MIDI 38-43)
bass_notes = [
    # F2 (MIDI 38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # G2 (MIDI 43) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # F2 (MIDI 38)
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.75),
    # G2 (MIDI 43) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hihat on every eighth
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante's sax solo (Bar 2-4)
# One short motif, start it, leave it hanging, come back and finish it
# Motif: F (D#4), A (F4), Bb (G4), D (B4)
# Start on F, leave it hanging, come back on D
sax_notes = [
    # Bar 2 - Start of motif
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.625),  # F (D#4)
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125),  # A (F4)
    # Bar 4 - Come back and finish the motif
    pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=4.625),  # Bb (G4)
    pretty_midi.Note(velocity=110, pitch=71, start=4.625, end=4.75),  # D (B4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
