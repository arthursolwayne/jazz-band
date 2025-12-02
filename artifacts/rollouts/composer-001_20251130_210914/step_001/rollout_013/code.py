
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # D
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.875),  # D
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.625),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.625),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.625),  # D
    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.375),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.375),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.375),  # D
    # Bar 4 (4.5 - 5.25s)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.125),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.125),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.125),  # D
    # Bar 4 (5.25 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=5.875),  # E
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=5.875),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Fm7 (F Ab Bb C) - motif: F Ab Bb F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
