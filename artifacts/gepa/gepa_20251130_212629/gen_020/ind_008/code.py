
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=85, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=85, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=85, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=85, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=85, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=85, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=85, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=85, pitch=42, start=1.3125, end=1.5),
]

drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.6875),  # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),   # Eb
]

sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=85, pitch=39, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=85, pitch=37, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=85, pitch=40, start=2.0, end=2.1875),  # Gb (Ab)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.6875, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=1.6875, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=1.6875, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.6875),   # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.6875),   # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=2.6875),   # A
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.6875),   # Eb
]

piano.notes.extend(piano_notes)

# Drums: same pattern but shifted
drums_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=85, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=85, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=85, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=85, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=85, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=85, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=85, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=85, pitch=42, start=2.8125, end=3.0),
]

drums.notes.extend(drums_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with subtle variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=60, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.5),
]

sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=40, start=3.0, end=3.1875),   # Gb (Ab)
    pretty_midi.Note(velocity=85, pitch=41, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=85, pitch=39, start=3.375, end=3.5),   # F#
    pretty_midi.Note(velocity=85, pitch=42, start=3.5, end=3.6875),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=59, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=55, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=57, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.1875),
]

piano.notes.extend(piano_notes)

# Drums: same pattern but shifted
drums_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=85, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=85, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=85, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=85, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=85, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=85, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=85, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=85, pitch=42, start=4.3125, end=4.5),
]

drums.notes.extend(drums_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif with subtle variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=100, pitch=55, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=100, pitch=57, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=55, start=5.75, end=6.0),
]

sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=42, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=85, pitch=43, start=4.6875, end=4.875), # A#
    pretty_midi.Note(velocity=85, pitch=41, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=85, pitch=44, start=5.0, end=5.1875),  # Bb
    pretty_midi.Note(velocity=85, pitch=43, start=5.1875, end=5.375), # A#
    pretty_midi.Note(velocity=85, pitch=42, start=5.375, end=5.5625), # A
    pretty_midi.Note(velocity=85, pitch=44, start=5.5625, end=5.75), # Bb
    pretty_midi.Note(velocity=85, pitch=45, start=5.75, end=6.0),    # B
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=59, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=55, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=57, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=59, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.6875),
]

piano.notes.extend(piano_notes)

# Drums: same pattern but shifted
drums_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=85, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=85, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=85, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=85, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=85, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=85, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=85, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=85, pitch=42, start=5.8125, end=6.0),
]

drums.notes.extend(drums_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('intro.mid')
