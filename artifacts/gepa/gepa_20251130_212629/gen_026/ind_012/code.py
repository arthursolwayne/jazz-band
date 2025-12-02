
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Sax starts with a short motif, leaving it hanging

# Sax motif (F, G#, B, D) - 16th notes with a rest on the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=68, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),
]

sax.notes.extend(sax_notes)

# Bass line: walking line in F, chromatic approaches
# F - G - Ab - A - Bb - B - C - Db - D - Eb - E - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=48, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=52, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=54, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=58, start=2.875, end=3.0),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 (F, A, C, Eb) on 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.0),
    # Bb7 (Bb, D, F, Ab) on 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=2.75),
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif, but with a rest on last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=68, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=68, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.5),
]

sax.notes.extend(sax_notes)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=59, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=63, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=66, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=68, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=69, start=4.375, end=4.5),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 (F, A, C, Eb) on 2 (3.875 - 4.0)
    pretty_midi.Note(velocity=90, pitch=57, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=59, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=61, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),
    # Bb7 (Bb, D, F, Ab) on 4 (4.625 - 4.75)
    pretty_midi.Note(velocity=90, pitch=51, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=54, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=57, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=59, start=4.625, end=4.75),
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax continues the motif, but ends with a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=68, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=68, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),
]

sax.notes.extend(sax_notes)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=70, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=73, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=74, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=76, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=77, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=78, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=79, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=80, start=5.875, end=6.0),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 (F, A, C, Eb) on 2 (5.375 - 5.5)
    pretty_midi.Note(velocity=90, pitch=57, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=59, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=61, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.5),
    # Bb7 (Bb, D, F, Ab) on 4 (6.125 - 6.25)
    pretty_midi.Note(velocity=90, pitch=51, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=54, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=57, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=59, start=6.125, end=6.25),
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
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
midi.write("intro.mid")
