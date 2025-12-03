
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2) to C3 (root), chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (D2)
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # F#2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 - Open voicing (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E (E5)
]
piano.notes.extend(piano_notes_bar2)

# Sax: Melody - Start with a short motif, leave it hanging
# F (F4) to G (G4) to A (A4) to F (F4), then rest
sax_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes_bar2)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb2 (chromatic approach) to F2 (root)
bass_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # Bb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125),  # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # G2
]
bass.notes.extend(bass_notes_bar3)

# Piano: Dm7 - Open voicing (D, F, A, C)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # C
]
piano.notes.extend(piano_notes_bar3)

# Sax: Repeat motif with variation
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes_bar3)

# Drums: Same pattern
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes_bar3)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Bb2 (chromatic approach) to F2
bass_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes_bar4)

# Piano: C7 - Open voicing (C, E, G, B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # B
]
piano.notes.extend(piano_notes_bar4)

# Sax: Repeat motif on F, then leave it hanging
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes_bar4)

# Drums: Same pattern
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
