
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
    pretty_midi.Note(127, 36, 0.0, 0.375),    # Kick on 1
    pretty_midi.Note(127, 42, 0.375, 0.75),   # Hihat on 2
    pretty_midi.Note(127, 38, 0.75, 1.125),   # Snare on 3
    pretty_midi.Note(127, 42, 1.125, 1.5),    # Hihat on 4
    pretty_midi.Note(127, 36, 1.5, 1.875),    # Kick on 1 of next bar (overlap)
    pretty_midi.Note(127, 42, 1.875, 2.25),   # Hihat on 2 of next bar (overlap)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches

bass_notes = [
    pretty_midi.Note(100, 38, 1.5, 1.875),    # D2 (root)
    pretty_midi.Note(100, 41, 1.875, 2.25),   # F#2 (chromatic approach to G2)
    pretty_midi.Note(100, 43, 2.25, 2.625),   # G2 (fifth)
    pretty_midi.Note(100, 42, 2.625, 3.0),    # F2 (chromatic approach to E2)
]

# Piano: Open voicings, different chord each bar
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(100, 62, 1.5, 2.0),    # D (D4)
    pretty_midi.Note(100, 67, 1.5, 2.0),    # F# (F#4)
    pretty_midi.Note(100, 71, 1.5, 2.0),    # A (A4)
    pretty_midi.Note(100, 69, 1.5, 2.0),    # C# (C#5)
]

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(100, 67, 1.5, 1.875),    # F (F4)
    pretty_midi.Note(100, 69, 1.875, 2.25),   # A (A4)
    pretty_midi.Note(100, 67, 2.25, 2.625),   # F (F4)
    pretty_midi.Note(100, 65, 2.625, 3.0),    # D (D4)
]

# Add bar 2 notes
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend([
    pretty_midi.Note(127, 36, 1.5, 1.875),    # Kick on 1
    pretty_midi.Note(127, 42, 1.875, 2.25),   # Hihat on 2
    pretty_midi.Note(127, 38, 2.25, 2.625),   # Snare on 3
    pretty_midi.Note(127, 42, 2.625, 3.0),    # Hihat on 4
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches

bass_notes = [
    pretty_midi.Note(100, 42, 3.0, 3.375),    # E2 (chromatic approach to F#2)
    pretty_midi.Note(100, 43, 3.375, 3.75),   # G2 (fifth)
    pretty_midi.Note(100, 41, 3.75, 4.125),   # F#2 (chromatic approach to G2)
    pretty_midi.Note(100, 38, 4.125, 4.5),    # D2 (root)
]

# Piano: Open voicings, different chord each bar
# Bar 3: G7 (G-B-D-F#)
piano_notes = [
    pretty_midi.Note(100, 67, 3.0, 3.5),    # G (G4)
    pretty_midi.Note(100, 71, 3.0, 3.5),    # B (B4)
    pretty_midi.Note(100, 69, 3.0, 3.5),    # D (D5)
    pretty_midi.Note(100, 71, 3.0, 3.5),    # F# (F#5)
]

# Sax: Continue motif, resolve on bar end
sax_notes = [
    pretty_midi.Note(100, 62, 3.0, 3.375),    # D (D4)
    pretty_midi.Note(100, 67, 3.375, 3.75),   # F (F4)
    pretty_midi.Note(100, 69, 3.75, 4.125),   # A (A4)
    pretty_midi.Note(100, 67, 4.125, 4.5),    # F (F4)
]

# Add bar 3 notes
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend([
    pretty_midi.Note(127, 36, 3.0, 3.375),    # Kick on 1
    pretty_midi.Note(127, 42, 3.375, 3.75),   # Hihat on 2
    pretty_midi.Note(127, 38, 3.75, 4.125),   # Snare on 3
    pretty_midi.Note(127, 42, 4.125, 4.5),    # Hihat on 4
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches

bass_notes = [
    pretty_midi.Note(100, 43, 4.5, 4.875),    # G2 (fifth)
    pretty_midi.Note(100, 42, 4.875, 5.25),   # E2 (chromatic approach to F#2)
    pretty_midi.Note(100, 43, 5.25, 5.625),   # G2 (fifth)
    pretty_midi.Note(100, 38, 5.625, 6.0),    # D2 (root)
]

# Piano: Open voicings, different chord each bar
# Bar 4: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(100, 71, 4.5, 5.0),    # B (B4)
    pretty_midi.Note(100, 69, 4.5, 5.0),    # D (D5)
    pretty_midi.Note(100, 71, 4.5, 5.0),    # F# (F#5)
    pretty_midi.Note(100, 74, 4.5, 5.0),    # A (A5)
]

# Sax: Resolve motif
sax_notes = [
    pretty_midi.Note(100, 69, 4.5, 4.875),    # A (A4)
    pretty_midi.Note(100, 71, 4.875, 5.25),   # C (C5)
    pretty_midi.Note(100, 69, 5.25, 5.625),   # A (A4)
    pretty_midi.Note(100, 67, 5.625, 6.0),    # F (F4)
]

# Add bar 4 notes
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend([
    pretty_midi.Note(127, 36, 4.5, 4.875),    # Kick on 1
    pretty_midi.Note(127, 42, 4.875, 5.25),   # Hihat on 2
    pretty_midi.Note(127, 38, 5.25, 5.625),   # Snare on 3
    pretty_midi.Note(127, 42, 5.625, 6.0),    # Hihat on 4
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
