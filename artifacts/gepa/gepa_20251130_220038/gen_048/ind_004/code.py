
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
    # Hi-hat on every eighth
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
# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.4375, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=2.8125),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.8125, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.8125),  # F
    # Bar 4: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5625),  # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.8125),# Snare on 4
    # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.8125),
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.8125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5625), # Snare on 4
    # Hi-hat
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

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.3125), # Snare on 4
    # Hi-hat
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

# Sax: Bar 2
# Whispering motif - start with a rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),   # G (sustained)
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.125),  # E
]
sax.notes.extend(sax_notes)

# Bar 3: sax continues with implied rhythm
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.125),  # E
]
sax.notes.extend(sax_notes)

# Bar 4: sax resolves with emotional clarity
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),   # E
    pretty_midi.Note(velocity=110, pitch=58, start=4.0, end=4.25),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
