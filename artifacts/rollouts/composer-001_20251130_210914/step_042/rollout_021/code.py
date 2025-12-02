
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
# Sax: short motif starting on D (D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # F3
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.25),  # G3
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # A3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=95, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),
    # Bar 2, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but transpose up a 3rd
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G4
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=90, pitch=52, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),  # D4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),
    # Bar 3, beat 4: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: return to D, but with a chromatic approach
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.625),  # C#4
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.125),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.375),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.75),  # D4
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=5.0),  # E4
    pretty_midi.Note(velocity=90, pitch=58, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # A4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),
    # Bar 4, beat 4: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=95, pitch=71, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=5.75),
    pretty_midi.Note(velocity=85, pitch=76, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=79, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    # Add these to the drums instrument
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
