
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif - D (D4), F# (F#4), A (A4), B (B4), D (D5)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75)   # D5
]
sax.notes.extend(sax_notes)

# Bass - Walking line in D: D, Eb, F, G, A, Bb, B, C, D
# Bar 2: D (D2), Eb (Eb2), F (F2), G (G2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=2.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75)   # A2
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5)   # C5
]
piano.notes.extend(piano_notes)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif - repeat first 4 notes, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25)   # D5
]
sax.notes.extend(sax_notes)

# Bass - Walking line in D: A, Bb, B, C, D, Eb, F, G, A
# Bar 3: A (A2), Bb (Bb2), B (B2), C (C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # A2
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # B2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # C3
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25)   # D3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
# Bar 3: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0)   # C5
]
piano.notes.extend(piano_notes)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif - repeat first 4 notes, resolve to D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=6.0)    # D5
]
sax.notes.extend(sax_notes)

# Bass - Walking line in D: C, D, Eb, F, G, A, Bb, B, C
# Bar 4: C (C3), D (D3), Eb (Eb3), F (F3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # C3
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # D3
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # Eb3
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F3
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0)    # G3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
# Bar 4: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5)   # C5
]
piano.notes.extend(piano_notes)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
