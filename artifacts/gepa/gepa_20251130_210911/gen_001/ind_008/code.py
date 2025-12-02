
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=35, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=34, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=33, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=32, start=2.625, end=3.0),   # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=31, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=30, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=29, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=28, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=27, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=26, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=25, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=24, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, Ab, Bb, F (start at bar 2, leave it hanging, come back and finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=50, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
