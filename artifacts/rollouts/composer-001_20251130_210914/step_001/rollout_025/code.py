
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Marcus: walking line in Fm - F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.6875, end=1.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0625),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.0625, end=2.25),   # A
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.4375),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.4375, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.8125, end=3.0),    # Db
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625),  # Eb
    # Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.8125),  # Ab
]
piano.notes.extend(piano_notes)

# Dante: motif starting at bar 2, 1st beat
# Fm motif: F, Gb, Bb, Ab
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=2.0625, end=2.25),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: walking line in Fm - F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.1875, end=3.375),  # Gb
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.5625, end=3.75),   # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.9375),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.9375, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.3125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.3125, end=4.5),    # Db
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),  # Eb
    # Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.3125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.3125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125),  # Ab
]
piano.notes.extend(piano_notes)

# Dante: continuation of motif
# Fm motif: F, Gb, Bb, Ab
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # Gb
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.5625, end=3.75),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: walking line in Fm - F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.6875, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0625),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.0625, end=5.25),   # A
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.4375),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.4375, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=5.8125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.8125, end=6.0),    # Db
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),  # Eb
    # Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125),  # Ab
]
piano.notes.extend(piano_notes)

# Dante: finish the motif
# Fm motif: F, Gb, Bb, Ab
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # Gb
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.0625, end=5.25),  # Ab
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
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
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.125, end=6.25),
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
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
