
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=1.875),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.125),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.875, end=3.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.625),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=60, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),
    pretty_midi.Note(velocity=85, pitch=67, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody (Bar 2-4, D minor blues with tension)
sax_notes = [
    # Bar 2: D (start on beat 1)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 2: F# (beat 2)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    # Bar 2: rest (beat 3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.0),  # Grace note
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    # Bar 2: C (beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),
    # Bar 3: Bb (beat 1)
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.75),
    # Bar 3: D (beat 2)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),
    # Bar 3: rest (beat 3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=2.875),  # Grace note
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (1.5 - 3.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=85, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
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

# Bar 4: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=3.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=85, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every eighth
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

# Bar 4: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=63, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=62, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=85, pitch=71, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.625, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: Melody (Bar 4, ends with a question)
sax_notes = [
    # Bar 4: D (beat 1)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 4: F# (beat 2)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    # Bar 4: rest (beat 3)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.5),  # Grace note
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    # Bar 4: Bb (beat 4 - ends on a question)
    pretty_midi.Note(velocity=100, pitch=59, start=3.875, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
