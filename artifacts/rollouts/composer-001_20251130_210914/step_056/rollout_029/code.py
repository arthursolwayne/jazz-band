
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D (D4), F# (F#4), A (A4), C (C5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0625, end=2.25), # C5
]
sax.notes.extend(sax_notes)

# Bass line: walking line in D (D, F#, A, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),  # D3
    pretty_midi.Note(velocity=80, pitch=66, start=1.6875, end=1.875), # F#3
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0625), # A3
    pretty_midi.Note(velocity=80, pitch=72, start=2.0625, end=2.25), # C4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # C5
]
# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),  # F#4
])
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 3: Sax melody (D, F#, A, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5625, end=3.75), # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Bass line (D, F#, A, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),  # D3
    pretty_midi.Note(velocity=80, pitch=66, start=3.1875, end=3.375), # F#3
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625), # A3
    pretty_midi.Note(velocity=80, pitch=72, start=3.5625, end=3.75), # C4
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (7th chords on 2 and 4)
# Bar 3: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # C5
]
# Bar 4: B7 (B, D#, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # D#5
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A4
])
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),  # Out of range, adjust
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax melody (D, F#, A, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.0625, end=5.25), # C5
]
sax.notes.extend(sax_notes)

# Bar 4: Bass line (D, F#, A, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.6875),  # D3
    pretty_midi.Note(velocity=80, pitch=66, start=4.6875, end=4.875), # F#3
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625), # A3
    pretty_midi.Note(velocity=80, pitch=72, start=5.0625, end=5.25), # C4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (7th chords on 2 and 4)
# Bar 4: B7 (B, D#, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),  # D#5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A4
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
