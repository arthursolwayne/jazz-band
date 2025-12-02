
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Short motif: D (D4), Bb (Bb4), F (F4), G (G4) -> D (D4), Bb (Bb4), F (F4), G (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.25),  # C3
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.5),  # D3
    pretty_midi.Note(velocity=100, pitch=47, start=2.5, end=2.75),  # E3
    pretty_midi.Note(velocity=100, pitch=45, start=2.75, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # C5

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 3: Little Ray (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif but resolve on G (G4) at end
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=100, pitch=46, start=4.75, end=5.0),  # Eb3
    pretty_midi.Note(velocity=100, pitch=44, start=5.0, end=5.25),  # C3
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.5),  # D3
    pretty_midi.Note(velocity=100, pitch=47, start=5.5, end=5.75),  # E3
    pretty_midi.Note(velocity=100, pitch=45, start=5.75, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # C5

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Little Ray (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
