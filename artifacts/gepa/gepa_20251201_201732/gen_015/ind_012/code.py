
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2) -> G2 (F2) -> A2 (G2) -> B2 (A2) -> C3 (B2) -> D3 (C3) -> F3 (D3) -> F3 (E3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # B2
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # F3
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),  # F3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.25),  # C4
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.25),  # E4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Motif - F4 (1.5), G4 (1.875), E4 (2.25), D4 (2.625), rest (2.625-3.0)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (F2) -> A2 (G2) -> B2 (A2) -> C3 (B2) -> D3 (C3) -> E3 (D3) -> F3 (E3) -> F3 (F3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25), # E3
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625), # F3
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),  # F3
]
bass.notes.extend(bass_notes)

# Piano: Bar 3: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Motif - E4 (3.0), D4 (3.375), F4 (3.75), E4 (4.125), rest (4.125-4.5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # E4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (G2) -> B2 (A2) -> C3 (B2) -> D3 (C3) -> E3 (D3) -> F3 (E3) -> G3 (F3) -> G3 (G3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25), # B2
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=6.0, end=6.375),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=6.375, end=6.75), # F3
    pretty_midi.Note(velocity=80, pitch=50, start=6.75, end=7.125), # G3
    pretty_midi.Note(velocity=80, pitch=50, start=7.125, end=7.5),  # G3
]
bass.notes.extend(bass_notes)

# Piano: Bar 4: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # E5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # G5
]
piano.notes.extend(piano_notes)

# Sax: Motif - D4 (4.5), F4 (4.875), E4 (5.25), F4 (5.625), rest (5.625-6.0)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
