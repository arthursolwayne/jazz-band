
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125), # Hihat on &
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax melody, piano comp, bass walking, drums continue
# Time: 1.5 - 3.0s
# Dm7 -> G7 -> Cm7 -> F7

# Bass line: Dm7 -> G7 -> Cm7 -> F7
# D2 -> F2 -> D2 -> F2 -> Bb2 -> D2 -> C2 -> E2
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),      # D2
    pretty_midi.Note(velocity=70, pitch=41, start=1.875, end=2.25),     # F2
    pretty_midi.Note(velocity=70, pitch=38, start=2.25, end=2.625),     # D2
    pretty_midi.Note(velocity=70, pitch=41, start=2.625, end=3.0),      # F2
    pretty_midi.Note(velocity=70, pitch=44, start=3.0, end=3.375),      # Bb2
    pretty_midi.Note(velocity=70, pitch=38, start=3.375, end=3.75),     # D2
    pretty_midi.Note(velocity=70, pitch=36, start=3.75, end=4.125),     # C2
    pretty_midi.Note(velocity=70, pitch=39, start=4.125, end=4.5),      # E2
]
bass.notes.extend(bass_notes)

# Piano comp: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=70, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.375),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.875),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Motif: D4 -> E4 -> F4 -> D4 (staccato with a half note on the last D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # E4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=3.0),    # D4 (staccato)
]
sax.notes.extend(sax_notes)

# Bar 3: Sax continues with G7 (G4 -> A4 -> B4 -> G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # A4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5625), # B4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.5),    # G4 (staccato)
]
sax.notes.extend(sax_notes)

# Bar 4: Sax continues with Cm7 (C4 -> D4 -> Eb4 -> C4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # D4
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.0625), # Eb4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=6.0),    # C4 (staccato)
]
sax.notes.extend(sax_notes)

# Bars 2-4: Drums continue
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125), # Hihat on &
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125), # Hihat on &
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=6.0, end=6.375),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.1875),   # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.5625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=6.75, end=7.125),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=6.9375),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.3125), # Hihat on &
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
