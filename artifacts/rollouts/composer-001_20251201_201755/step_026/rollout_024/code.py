
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
# Bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (chromatic approach to G) on 2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),
    # G2 (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # D2 (root) on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - C4 (E4), D4 (F#4), E4 (G4), F#4 (A4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.6875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0625),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0625, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.8125),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F (chromatic approach to G) on 1
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.1875),
    # G2 (fifth) on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.1875, end=3.5),
    # Bb (chromatic approach to A) on 3
    pretty_midi.Note(velocity=90, pitch=46, start=3.5, end=3.6875),
    # A2 (root of Dm7) on 4
    pretty_midi.Note(velocity=90, pitch=45, start=3.6875, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A-C-E-G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=4.5),  # G5
]
piano.notes.extend(piano_notes)

# Sax: Motif - A4 (C5), Bb4 (D5), C5 (E5), D5 (F#5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.9375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=76, start=3.9375, end=4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.3125),  # C5
    pretty_midi.Note(velocity=100, pitch=77, start=4.3125, end=4.5),  # E5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # A2 (root of Am7) on 1
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),
    # Bb (chromatic approach to A) on 2
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.0),
    # A2 (root of Am7) on 3
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.375),
    # D2 (root of Dm7) on 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - D4 (F#4), E4 (G4), F#4 (A4), G4 (Bb4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.4375),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.4375, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.8125, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 2: 1.5 - 3.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
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

# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
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

# Bar 4: 4.5 - 6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hi-hat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
