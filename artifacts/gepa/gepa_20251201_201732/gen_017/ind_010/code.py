
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: C2 (MIDI 36) -> F2 (MIDI 41) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # C#2 approach
    pretty_midi.Note(velocity=85, pitch=36, start=1.875, end=2.25), # C2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 approach
    pretty_midi.Note(velocity=85, pitch=41, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 -> F7 -> Dm7 -> G7
piano_notes = [
    # Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.25),  # E4

    # F7 (F, A, C#, E)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=3.0),  # F4
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0),  # C#5
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=3.0),  # E4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> G (67) -> E (67) -> D (62) -> G (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # E4 (rest)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) -> D2 (MIDI 49) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # A2 approach
    pretty_midi.Note(velocity=85, pitch=43, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # E2 approach
    pretty_midi.Note(velocity=85, pitch=49, start=4.125, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 -> G7 -> Cmaj7 -> Fmaj7
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # A4
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.75),  # C5

    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),  # D5
    pretty_midi.Note(velocity=85, pitch=65, start=3.75, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 41) -> C2 (MIDI 36) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # E2 approach
    pretty_midi.Note(velocity=85, pitch=41, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.625), # B2 approach
    pretty_midi.Note(velocity=85, pitch=36, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 -> Fmaj7 -> Dm7 -> G7
piano_notes = [
    # Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=5.25),  # E5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=5.25),  # B5

    # Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=6.0),  # F4
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0),  # C5
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=6.0),  # E4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=85, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=85, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
