
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody (1.5 - 3.0s)
# Sax melody: C (60), E (64), G (67), B (71), then back to C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),
]

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2: C, B, C#, D
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),
    # Bar 3: E, D#, E, F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5),
    # Bar 4: G, F#, G, A
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    # Bar 3: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),
]

# Bar 3 & 4: Drums
# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Add all the notes to their respective instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
