
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
    # Hihat on every eighth
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
# Marcus: Walking line, chromatic approaches, never the same note twice.
# Key is F major, so bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),  # G (C#4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # A (D4)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # Bb (D#4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # A (D4)
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),  # G (C#4)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4 (1.5 - 3.0s)
# F7 on 1, Am7 on 2, C7 on 3, E7 on 4
piano_notes = []
# Bar 2, beat 1: F7 = F, A, C, E
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F (E4)
    pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.75),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.75),  # E (B4)
])

# Bar 2, beat 2: Am7 = A, C, E, G
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=2.0),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=1.75, end=2.0),  # G (C5)
])

# Bar 2, beat 3: C7 = C, E, G, Bb
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.25),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=2.0, end=2.25),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=80, start=2.0, end=2.25),  # Bb (C#5)
])

# Bar 2, beat 4: E7 = E, G, B, D
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=2.25, end=2.5),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=82, start=2.25, end=2.5),  # B (E5)
    pretty_midi.Note(velocity=80, pitch=84, start=2.25, end=2.5),  # D (F5)
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches, never the same note twice.
# Key is F major, so bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # A (D4)
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # G (C#4)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25),  # G (C#4)
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # A (D4)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4 (3.0 - 4.5s)
# F7 on 1, Am7 on 2, C7 on 3, E7 on 4
piano_notes = []
# Bar 3, beat 1: F7 = F, A, C, E
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F (E4)
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25),  # E (B4)
])

# Bar 3, beat 2: Am7 = A, C, E, G
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=68, start=3.25, end=3.5),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=3.25, end=3.5),  # G (C5)
])

# Bar 3, beat 3: C7 = C, E, G, Bb
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=3.5, end=3.75),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=3.5, end=3.75),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=80, start=3.5, end=3.75),  # Bb (C#5)
])

# Bar 3, beat 4: E7 = E, G, B, D
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.0),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.0),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=82, start=3.75, end=4.0),  # B (E5)
    pretty_midi.Note(velocity=80, pitch=84, start=3.75, end=4.0),  # D (F5)
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches, never the same note twice.
# Key is F major, so bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # A (D4)
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25),  # G (C#4)
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.75),  # G (C#4)
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # A (D4)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4 (4.5 - 6.0s)
# F7 on 1, Am7 on 2, C7 on 3, E7 on 4
piano_notes = []
# Bar 4, beat 1: F7 = F, A, C, E
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F (E4)
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.75),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.75),  # E (B4)
])

# Bar 4, beat 2: Am7 = A, C, E, G
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # A (G4)
    pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=4.75, end=5.0),  # G (C5)
])

# Bar 4, beat 3: C7 = C, E, G, Bb
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # C (A4)
    pretty_midi.Note(velocity=80, pitch=76, start=5.0, end=5.25),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=5.0, end=5.25),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=80, start=5.0, end=5.25),  # Bb (C#5)
])

# Bar 4, beat 4: E7 = E, G, B, D
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.5),  # E (B4)
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.5),  # G (C5)
    pretty_midi.Note(velocity=80, pitch=82, start=5.25, end=5.5),  # B (E5)
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.5),  # D (F5)
])

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # E (B4)
]
sax.notes.extend(sax_notes)

# Bar 3: Leave it hanging
# Bar 4: Come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),  # E (B4)
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # C (A4)
]
sax.notes.extend(sax_notes)

# Add all notes to the instruments
piano.notes.extend(piano_notes)
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
