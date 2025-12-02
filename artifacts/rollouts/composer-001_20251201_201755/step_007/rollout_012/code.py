
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) -> F2 (MIDI 41) -> G2 (MIDI 43) -> C2 (MIDI 36)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - D4 (62) -> F4 (65) -> D4 (62) -> G4 (67) (hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) -> Bb2 (MIDI 40) -> C2 (MIDI 36) -> F2 (MIDI 41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif - G4 (67) -> D4 (62) -> F4 (65) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) -> C2 (MIDI 36) -> D2 (MIDI 38) -> G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Complete motif - D4 (62) -> G4 (67) -> D4 (62) -> F4 (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
