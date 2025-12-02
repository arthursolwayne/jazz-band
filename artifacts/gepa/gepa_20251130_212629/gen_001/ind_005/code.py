
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # B

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # F7
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # F7
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody
# Bar 2 (1.5 - 3.0s)
# Motif: F (D# in Fm), Gb, E, Ab (start on 1, end on 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),   # Gb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # Gb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),   # Gb
]
sax.notes.extend(sax_notes)

# Drums: Fill for bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
]
drums.notes.extend(drum_notes)

# Drums: Full bar for bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
]
drums.notes.extend(drum_notes)

# Drums: Full bar for bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("intro_in_fm.mid")
