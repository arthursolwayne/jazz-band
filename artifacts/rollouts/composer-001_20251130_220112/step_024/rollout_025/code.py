
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - Dm7
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.25),  # D
    # Bar 3 - G7
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0),  # B
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - G7
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75),  # B
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.75),  # F
    # Bar 4 - Cm7
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.5),  # E
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif (repeat)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - Cm7
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),  # E
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.25),  # Bb
    # Bar 5 - Dm7 (off the beat, just a hint)
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=75, pitch=67, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=65, pitch=71, start=5.625, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (final pass)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
