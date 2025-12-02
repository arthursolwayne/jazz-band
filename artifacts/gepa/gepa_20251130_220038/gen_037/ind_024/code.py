
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
    # Hihat on every eighth
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
# Sax: Short motif, start it, leave it hanging
# D7 -> F#7 -> B7 -> D7 (sax melody)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.625),  # F#

    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # C#
    pretty_midi.Note(velocity=90, pitch=73, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=90, pitch=78, start=1.75, end=1.875),  # G#
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, imply resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=3.125, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.125),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # C#
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.125),  # D#
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.125),  # G#

    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.375),  # F#
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=80, pitch=54, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.625),  # F#

    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=4.875),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=73, start=4.75, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=78, start=4.75, end=4.875),  # G#
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

midi.write('dante_intro.mid')
