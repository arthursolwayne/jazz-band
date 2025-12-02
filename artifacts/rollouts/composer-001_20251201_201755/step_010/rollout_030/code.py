
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in D (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),    # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),   # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),   # A2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),    # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),    # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),    # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),    # C#4
]
# Bar 3: Bm7 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),   # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),   # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),   # A4
])
# Bar 4: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),    # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),    # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),    # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),    # F#4
])
piano.notes.extend(piano_notes)

# Dante: Motif in D (D4, E4, F#4, G4), start on bar 2, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),   # E4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),    # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),    # D2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),   # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),   # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),    # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),    # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),    # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),    # A4
]
# Bar 4: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),   # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),   # F#4
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),    # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),   # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),   # A2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on last
# Bar 4: G7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),    # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),    # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),    # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),    # F#4
]
piano.notes.extend(piano_notes)

# Dante: Return to motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),    # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),   # E4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),    # G4
]
sax.notes.extend(sax_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
