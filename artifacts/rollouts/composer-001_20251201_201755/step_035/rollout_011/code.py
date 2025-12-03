
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
# Bass: Walking line with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.6875, end=1.875),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.0625),
    # D2 again
    pretty_midi.Note(velocity=100, pitch=38, start=2.0625, end=2.25),
    # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.4375),
    # F2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=41, start=2.4375, end=2.625),
    # G2 again
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=2.8125),
    # D2
    pretty_midi.Note(velocity=100, pitch=38, start=2.8125, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # C5
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, G4, D4 (hanging on G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # D4
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    # C2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=35, start=4.6875, end=4.875),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.0625),
    # C2 again
    pretty_midi.Note(velocity=100, pitch=36, start=5.0625, end=5.25),
    # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.4375),
    # F2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=41, start=5.4375, end=5.625),
    # G2 again
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=5.8125),
    # C2
    pretty_midi.Note(velocity=100, pitch=36, start=5.8125, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, finish it
# Motif: D4, F4, G4, D4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
