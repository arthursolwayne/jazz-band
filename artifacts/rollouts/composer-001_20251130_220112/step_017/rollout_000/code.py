
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
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F# (third)
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A (fifth)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D (root)
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # E (chromatic)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D, E, F#, G, A, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.906), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.906), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D (root)
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # F# (third)
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A (fifth)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D (root)
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # E (chromatic)
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D, E, F#, G, A, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5),

    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=66, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D (root)
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F# (third)
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # A (fifth)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D (root)
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # E (chromatic)
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D, E, F#, G, A, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=72, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=62, start=6.25, end=6.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
