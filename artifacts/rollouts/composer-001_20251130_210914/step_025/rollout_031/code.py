
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
# Sax: Motif starting at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # Fm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.1875),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=46, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.6875),   # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=1.5, end=1.6875),   # A
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.6875),   # D
    pretty_midi.Note(velocity=95, pitch=46, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=95, pitch=50, start=2.1875, end=2.375), # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=95, pitch=53, start=2.1875, end=2.375), # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Second half of motif (with a chromatic twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.5625, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.1875),   # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=3.9375),  # A
    pretty_midi.Note(velocity=90, pitch=46, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.3125), # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=4.3125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=46, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.1875),   # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=3.0, end=3.1875),   # A
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.1875),   # D
    pretty_midi.Note(velocity=95, pitch=46, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=95, pitch=50, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=4.125, end=4.3125), # A
    pretty_midi.Note(velocity=95, pitch=53, start=4.125, end=4.3125), # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
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
# Sax: Resolution to the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.1875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=5.1875, end=5.375), # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5625), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.5625, end=5.75), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),    # Fm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.6875, end=4.875), # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.1875),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=5.1875, end=5.375), # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.375, end=5.5625), # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=5.5625, end=5.75), # D
    pretty_midi.Note(velocity=90, pitch=45, start=5.75, end=6.0),    # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=46, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=95, pitch=50, start=4.5, end=4.6875),   # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=4.5, end=4.6875),   # A
    pretty_midi.Note(velocity=95, pitch=53, start=4.5, end=4.6875),   # D
    pretty_midi.Note(velocity=95, pitch=46, start=5.5625, end=5.75),  # F
    pretty_midi.Note(velocity=95, pitch=50, start=5.5625, end=5.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=49, start=5.5625, end=5.75),  # A
    pretty_midi.Note(velocity=95, pitch=53, start=5.5625, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
