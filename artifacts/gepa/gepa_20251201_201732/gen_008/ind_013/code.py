
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: D2 (D2), F2 (F2), G2 (G2), A2 (A2) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A2 on 4
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # G4
]
# Bar 3: Gm7 (Bb, D, G, B)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # B4
]
# Bar 4: Cm7 (Eb, G, C, E)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # C4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # E4
]
piano.notes.extend(piano_notes)

# Bar 2: Sax motif (Dm scale, but not scales)
# D, Eb, F, G (Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G4
]
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75), # D4 (return)
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Sax (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.75), # C4
]
sax.notes.extend(sax_notes)

# Bar 4: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # D4 (hold on 1 and 2)
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # F4 (on 3)
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # G4 (on 4)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # D4 (hold on 4)
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (3.0 - 4.5s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Eb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # D5
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
