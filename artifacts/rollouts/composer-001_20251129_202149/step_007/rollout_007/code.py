
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
]

# Sax: Motif
sax_notes = [
    # Bar 2, beat 1: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 2, beat 2: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Bar 2, beat 3: F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    # Bar 2, beat 4: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]

# Bar 3 (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
])

# Piano: 7th chords, comp on 2 and 4
piano_notes.extend([
    # Bar 3, beat 2: G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75),
    # Bar 3, beat 4: C7
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
])

# Sax: Motif again, but transposed
sax_notes.extend([
    # Bar 3, beat 1: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 3, beat 2: D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Bar 3, beat 3: F
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    # Bar 3, beat 4: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
])

# Bar 4 (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # E
])

# Piano: 7th chords, comp on 2 and 4
piano_notes.extend([
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    # Bar 4, beat 4: G7
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),
])

# Sax: Motif again, but ending on C
sax_notes.extend([
    # Bar 4, beat 1: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    # Bar 4, beat 2: D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    # Bar 4, beat 3: F
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    # Bar 4, beat 4: C
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
])

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
