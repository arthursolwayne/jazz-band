
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with sparse, syncopated hits
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth with dynamic variation
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=65, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=75, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=65, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Dm - D F A C)
# Motif: D (1/4), F# (1/8), A (1/8), D (1/8), F (1/8), rest (1/8)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.375)
]
sax.notes.extend(sax_notes)

# Bass line: chromatic walking line with melodic intent
# Dm7: D F A C
# Walking line: D F G A Bb B C D
# Chromatic approach to F and A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with emotional comping
# Dm7 = D F A C
# F7 = F A C E
# A7 = A C E G
# C7 = C E G Bb
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),
    # Inner voice comping
    pretty_midi.Note(velocity=70, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=65, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=65, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=75, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=65, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=65, pitch=64, start=4.875, end=5.25)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
