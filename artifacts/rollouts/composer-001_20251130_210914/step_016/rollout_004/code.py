
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start, leave hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.1875, end=2.375),# D
    pretty_midi.Note(velocity=100, pitch=66, start=2.375, end=2.5625),# F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5625, end=2.75), # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.9375)  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=1.875),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),
    # A (7th)
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),
    # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=2.125, end=2.25),
    # C (root)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.375),
    # Db (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=61, start=2.375, end=2.5),
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=2.75),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=2.75, end=2.875),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.125),
    # Bar 2, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),
    # Bar 3, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875),
    # Bar 3, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),
    # Bar 4, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.625),
    # Bar 4, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=67, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=69, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=60, start=6.25, end=6.375)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif, but incomplete
sax_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.5)   # D
]
sax.notes.extend(sax_notes_2)

# Bass: walking line, chromatic approaches
bass_notes_2 = [
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=3.125, end=3.25),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.375),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.5),
    # A (7th)
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),
    # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=3.625, end=3.75),
    # C (root)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875),
    # Db (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=61, start=3.875, end=4.0),
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.25),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=4.25, end=4.375),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=4.375, end=4.5)
]
bass.notes.extend(bass_notes_2)

# Piano: 7th chords on 2 and 4
piano_notes_2 = [
    # Bar 3, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875),
    # Bar 3, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),
    # Bar 4, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.625),
    # Bar 4, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=67, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=69, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=60, start=6.25, end=6.375)
]
piano.notes.extend(piano_notes_2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.1875, end=5.375), # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.375, end=5.5625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5625, end=5.75), # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=5.9375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.9375, end=6.0)   # A
]
sax.notes.extend(sax_notes_3)

# Bass: walking line, chromatic approaches
bass_notes_3 = [
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=4.625, end=4.75),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=4.875),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.0),
    # A (7th)
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),
    # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=5.125, end=5.25),
    # C (root)
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.375),
    # Db (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=61, start=5.375, end=5.5),
    # D (root)
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.625),
    # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=5.75),
    # F (3rd)
    pretty_midi.Note(velocity=80, pitch=66, start=5.75, end=5.875),
    # G (5th)
    pretty_midi.Note(velocity=80, pitch=68, start=5.875, end=6.0)
]
bass.notes.extend(bass_notes_3)

# Piano: 7th chords on 2 and 4
piano_notes_3 = [
    # Bar 4, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.625),
    # Bar 4, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=67, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=69, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=60, start=6.25, end=6.375)
]
piano.notes.extend(piano_notes_3)

# Drums: Bar 3 (3.0 - 4.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes_2)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes_3 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes_3)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
