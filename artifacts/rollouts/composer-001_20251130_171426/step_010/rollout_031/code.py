
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)     # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Dm7 -> F7 -> Bb7 -> G7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),    # G
]
sax.notes.extend(sax_notes)

# Bass line: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),     # D7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),    # D7
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, now with a slight syncopation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),    # G
]
sax.notes.extend(sax_notes)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),     # D7
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),    # D7
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),    # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a tritone resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),    # G
]
sax.notes.extend(sax_notes)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),     # D7
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),    # D7
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),    # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
