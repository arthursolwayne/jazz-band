
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: sax starts with a motif
# C - E - G - Bb (C7 no 9)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on C, chromatic approach to E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: C7 (C, E, Bb, G)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.25)
]
piano.notes.extend(piano_notes)

# Bar 3: D7 (D, F#, C, A)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C, E, Bb, G)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.75)
]
piano.notes.extend(piano_notes)

# Bar 4: sax returns to finish the motif
# C - E - G - Bb (C7 no 9)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Bar 4: drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
