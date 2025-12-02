
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.4375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.4375, end=2.625),  # F
]
sax.notes.extend(sax_notes)

# Bass walking line (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0625),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=2.0625, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.4375, end=2.625),  # G
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4 (7th chords: F7, A7)
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # Bb
    # Bar 3: A7 on beat 4
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=54, start=2.625, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125),  # F
]
sax.notes.extend(sax_notes)

# Bass walking line (Bb, C, D, E)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=3.1875, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=3.5625, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=3.9375, end=4.125),  # C
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4 (7th chords: Bb7, D7)
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.5625),  # C
    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=54, start=4.125, end=4.25),  # F#
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.25),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625),  # F
]
sax.notes.extend(sax_notes)

# Bass walking line (E, F, G, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=80, pitch=54, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=80, pitch=56, start=5.0625, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.4375),  # E
    pretty_midi.Note(velocity=80, pitch=54, start=5.4375, end=5.625),  # F
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4 (7th chords: E7, G7)
piano_notes = [
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.0625),  # E
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0625),  # B
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.0625),  # A
    # Bar 4: G7 on beat 4
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=5.75),  # C
]
piano.notes.extend(piano_notes)

# Drums continue (Bar 2-4)
# Bar 2: 1.5 - 3.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
