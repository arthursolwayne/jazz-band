
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),    # Bb
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),    # B
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),    # A
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),    # G
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),    # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),    # F7 root
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),    # E
]
piano.notes.extend(piano_notes)

# Sax: sparse, expressive motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # E (F7 3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # A (7th)
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),   # E again
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),   # F (root)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),    # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),    # A
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),    # B
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),    # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),    # F7 root
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),    # E
]
piano.notes.extend(piano_notes)

# Sax: sparse, expressive motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # D (7th)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),   # F again
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),   # G (question)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),    # B
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),    # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),    # A
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),    # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),    # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),    # F7 root
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),    # E
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),    # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),    # E
]
piano.notes.extend(piano_notes)

# Sax: sparse, expressive motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # G (turn)
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # F (resolution)
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # F (hold)
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # G (question)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
