
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.0625, end=2.25),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.4375, end=2.625), # G#
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.8125, end=3.0),   # A#
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.5625), # C#
    pretty_midi.Note(velocity=80, pitch=76, start=3.5625, end=3.75),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0),  # D7
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.1875),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.8125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
]
drums.notes.extend(drum_notes)

# Sax: Dante's melody (Bar 2: start on 1, short motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),   # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
