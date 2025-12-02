
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # Bb
    # Bar 2 - 4th beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif - short and memorable
# F, G#, Bb, F (1st bar of sax line)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # F
    # Leave it hanging, come back
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.75, end=2.875),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # Bb
    # Bar 3 - 4th beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, variations
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.125, end=3.25),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.625, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.875, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # Bb
    # Bar 4 - 4th beat (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.125, end=5.25),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=5.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=5.875, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
