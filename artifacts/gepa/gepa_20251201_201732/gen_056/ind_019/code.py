
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_note_1 = pretty_midi.Note(
    velocity=100, pitch=36, start=0.0, end=0.375
)
drum_note_2 = pretty_midi.Note(
    velocity=100, pitch=42, start=0.375, end=0.75
)
drum_note_3 = pretty_midi.Note(
    velocity=100, pitch=36, start=0.75, end=1.125
)
drum_note_4 = pretty_midi.Note(
    velocity=100, pitch=42, start=1.125, end=1.5
)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # Gb2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano - Diane (Open voicings, different chord each bar, resolve on last)
# Bar 2: Fm7 (F, Ab, C, Eb) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
]
# Bar 3: Bb7b5 (Bb, D, F, Ab) open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb) open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
])
# Bar 4: Resolving to Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Eb4
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D4
])
# Bar 4 continuation
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D4
])
piano.notes.extend(piano_notes)

# Drums continue with fill
# Bar 2
drum_note_5 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_note_6 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_note_7 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drum_note_8 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
drums.notes.extend([drum_note_5, drum_note_6, drum_note_7, drum_note_8])

# Bar 3
drum_note_9 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_note_10 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_note_11 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_note_12 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
drums.notes.extend([drum_note_9, drum_note_10, drum_note_11, drum_note_12])

# Bar 4 (Fill)
drum_note_13 = pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0)
drum_note_14 = pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125)
drum_note_15 = pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.25)
drum_note_16 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.5)
drum_note_17 = pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.625)
drum_note_18 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75)
drum_note_19 = pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.0)
drums.notes.extend([drum_note_13, drum_note_14, drum_note_15, drum_note_16, drum_note_17, drum_note_18, drum_note_19])

# Saxophone - Dante (Motif: One short phrase, haunting, incomplete)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # C4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
