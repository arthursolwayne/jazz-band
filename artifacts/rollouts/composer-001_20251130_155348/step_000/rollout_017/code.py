
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approach to F7
bass_notes = [
    # F -> Eb -> D -> C
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),
    # F7 chord (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.125),
    # Sax: Melody starts (F, G, Ab, Bb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),
    # Piano: 7th chords on 2 and 4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.25),
]
bass.notes.extend(bass_notes)
sax.notes.extend(bass_notes[8:12])
piano.notes.extend(bass_notes[12:])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approach to Bb7
bass_notes = [
    # Bb -> A -> G -> F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5),
    # Bb7 chord (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.625),
    # Sax: Melody continues (C, Bb, A, G)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),
    # Piano: 7th chords on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.75),
]
bass.notes.extend(bass_notes)
sax.notes.extend(bass_notes[8:12])
piano.notes.extend(bass_notes[12:])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approach to F7
bass_notes = [
    # F -> Eb -> D -> C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=63, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),
    # F7 chord (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.125),
    # Sax: Melody ends (F, G, Ab, Bb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.5),
    # Piano: 7th chords on 2 and 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),
]
bass.notes.extend(bass_notes)
sax.notes.extend(bass_notes[8:12])
piano.notes.extend(bass_notes[12:])

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
