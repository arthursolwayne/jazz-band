
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax motif: F (65), A (69), Bb (70), F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bass line: F, Gb, G, A (chromatic walk)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2 - on 2 (1.75s): F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0)
]

# Bar 3 - on 2 (2.75s): Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0)
])

# Bar 4 - on 2 (3.75s): G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0)
])

piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax repeats the motif an octave higher: F (77), A (81), Bb (82), F (77)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=81, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=82, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=4.0)
]
sax.notes.extend(sax_notes)

# Bass line: F, Gb, G, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3 - on 2 (3.25s): Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5)
]

# Bar 4 - on 2 (4.25s): G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5)
])

piano.notes.extend(piano_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax repeats the motif again, but now with a slight variation: F (65), Bb (70), A (69), F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=70, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Bass line: F, Gb, G, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4 - on 2 (5.5s): F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75)
]

piano.notes.extend(piano_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
