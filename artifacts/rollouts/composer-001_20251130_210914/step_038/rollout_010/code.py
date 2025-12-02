
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
# Sax motif: F, Ab, Bb, F (F7 no 3rd)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F, Gb, G, A)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=90, pitch=50, start=2.0625, end=2.25), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=95, pitch=53, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=57, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),  # E
    # Bb7 on beat 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=95, pitch=50, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=85, pitch=55, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=2.75),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation (F, Bb, Ab, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=3.5625, end=3.75), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (Bb, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.5625, end=3.75), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Bb7 on 2, Eb7 on 4)
piano_notes = [
    # Bb7 on beat 2 (3.375 - 3.5)
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=85, pitch=55, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.5),  # Ab
    # Eb7 on beat 4 (4.125 - 4.25)
    pretty_midi.Note(velocity=95, pitch=48, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=85, pitch=53, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.25),  # Db
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3 (3.0 - 3.375, 4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 (3.75 - 3.875, 4.5 - 4.625)
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
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
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif resolution (F, Eb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (Eb, E, F, G)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.0625, end=5.25), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Eb7 on 2, A7 on 4)
piano_notes = [
    # Eb7 on beat 2 (4.875 - 5.0)
    pretty_midi.Note(velocity=95, pitch=48, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=85, pitch=53, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0),  # Db
    # A7 on beat 4 (5.625 - 5.75)
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=85, pitch=74, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=5.625, end=5.75),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3 (4.5 - 4.875, 5.625 - 6.0)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4 (5.25 - 5.375, 6.0 - 6.125)
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
