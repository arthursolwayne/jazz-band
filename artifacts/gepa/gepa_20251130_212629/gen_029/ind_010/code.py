
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts with a motif
# Melody: D (D4) - F# (F#4) - B (B4) - D (D5) - rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.375, end=2.5),  # D5
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=70, pitch=41, start=1.75, end=2.0),   # C#3
    pretty_midi.Note(velocity=70, pitch=43, start=2.0, end=2.25),   # D#3
    pretty_midi.Note(velocity=70, pitch=44, start=2.25, end=2.5),   # E3
    pretty_midi.Note(velocity=70, pitch=43, start=2.5, end=2.75),   # D#3
    pretty_midi.Note(velocity=70, pitch=42, start=2.75, end=3.0),   # D3
    pretty_midi.Note(velocity=70, pitch=41, start=3.0, end=3.25),   # C#3
    pretty_midi.Note(velocity=70, pitch=43, start=3.25, end=3.5),   # D#3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping with feel
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),   # D7 chord: D, F#, A, C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75),   # F#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),   # D7 chord again
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),   # D7 chord
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),    # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),   # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),    # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
