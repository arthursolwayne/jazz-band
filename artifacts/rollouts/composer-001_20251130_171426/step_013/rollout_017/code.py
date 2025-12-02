
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

# Bar 2: Full band starts
# Sax melody in F minor (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.0625, end=2.25), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=90, pitch=51, start=2.0625, end=2.25),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# F7 on beat 2 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=73, start=1.6875, end=1.875),
])
# F7 on beat 4 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=73, start=2.0625, end=2.25),
])
piano.notes.extend(piano_notes)

# Bar 3: Sax continues melody, bass walks, piano comps, drums fill
# Sax: F, Bb, Ab, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.4375, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=2.8125, end=3.0),    # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.4375, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.8125, end=3.0),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# F7 on beat 2 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=74, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=76, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=73, start=2.4375, end=2.625),
])
# F7 on beat 4 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=73, start=2.8125, end=3.0),
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax ends motif, bass walks, piano comps, drums fill
# Sax: F, Ab, Bb, D (repeat of motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.75),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.1875, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.5625, end=3.75),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# F7 on beat 2 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=73, start=3.1875, end=3.375),
])
# F7 on beat 4 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=73, start=3.5625, end=3.75),
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
