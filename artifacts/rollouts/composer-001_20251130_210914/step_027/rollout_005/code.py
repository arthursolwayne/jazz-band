
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
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # G
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # G
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # G
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
