
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
# Sax: A motif starting on F (65) with a chromatic approach
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0),  # D
    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but transposed up a 3rd
sax_notes_2 = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # A#
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=110, pitch=70, start=4.25, end=4.5),  # A
]
sax.notes.extend(sax_notes_2)

# Bass: Walking line in F
bass_notes_2 = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes_2)

# Piano: 7th chords on 2 and 4
piano_notes_2 = [
    # Bar 3 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.5),  # D
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.5),  # D
]
piano.notes.extend(piano_notes_2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a resolution on F
sax_notes_3 = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes_3)

# Bass: Walking line in F
bass_notes_3 = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes_3)

# Piano: 7th chords on 2 and 4
piano_notes_3 = [
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.0),  # D
    # Bar 4 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.5),  # D
]
piano.notes.extend(piano_notes_3)

# Drums for bar 3 (3.0 - 4.5s)
drum_notes_2 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes_2)

# Drums for bar 4 (4.5 - 6.0s)
drum_notes_3 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes_3)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
