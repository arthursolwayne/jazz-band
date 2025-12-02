
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
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=44, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=90, pitch=46, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=2.9375),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=2.9375, end=3.125), # C
    pretty_midi.Note(velocity=90, pitch=49, start=3.125, end=3.3125), # C#
    pretty_midi.Note(velocity=90, pitch=50, start=3.3125, end=3.5),   # D
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.6875),   # D#
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Bar 2: comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=75, pitch=76, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=75, pitch=76, start=2.0, end=2.1875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=85, pitch=67, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=71, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=75, pitch=76, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=85, pitch=67, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=71, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=75, pitch=76, start=3.125, end=3.3125),
]
piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # G#
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.1875),  # F (leave hanging)
    # Bar 3: Repeat motif
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5625),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.5625, end=2.75),   # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.9375),   # G#
    pretty_midi.Note(velocity=110, pitch=64, start=2.9375, end=3.125),  # F (leave hanging)
    # Bar 4: Complete the motif
    pretty_midi.Note(velocity=110, pitch=64, start=3.3125, end=3.4375), # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.4375, end=3.625),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.8125),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=3.8125, end=4.0),    # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.1875, end=2.375), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.5625, end=2.75),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.9375, end=3.125), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.3125, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.6875),   # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.8125, end=4.0),   # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
