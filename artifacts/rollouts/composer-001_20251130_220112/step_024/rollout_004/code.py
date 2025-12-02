
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 to 1.5s)
    # Kick on 1 (0.0s), snare on 2 (0.75s), hihat on 0.375, 0.75, 1.125, 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F (G6), Bb (A6), C (B6), D (C7) - 16th notes, start on beat 1, end on beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
# F (F3), G (G3), Ab (Ab3), A (A3), Bb (Bb3), B (B3), C (C4), Db (Db4)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=73, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 (F, A, C, Eb) on beat 2 (1.875s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),
    # Bar 3: F7 on beat 4 (3.0s)
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Bar 3: Drums
# Kick on 1 (3.0s), snare on 2 (3.75s), hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 3: Sax (3.0 - 4.5s)
# Repeat the motif, but start on beat 2 (3.0s), end on beat 3 (3.75s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Bass
# Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=75, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Bar 3: Piano
# 7th chord on beat 4 (4.5s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
# Kick on 1 (4.5s), snare on 2 (5.25s), hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax (4.5 - 6.0s)
# End the motif on beat 4 (5.625s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Bass
# Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=80, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Bar 4: Piano
# 7th chord on beat 4 (6.0s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=69, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=72, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=68, start=6.0, end=6.375),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
