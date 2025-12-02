
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Gb, Ab, Bb, B, C, Db, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (F7, Bb7, F7, Bb7)
piano_notes = [
    # Bar 2 - F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=68, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),
    # Bar 3 - Bb7 (Bb, D, Eb, F)
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),
    # Bar 4 - F7 again
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),
    # Bar 4 - Bb7 again
    pretty_midi.Note(velocity=85, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Dante: Motif starting at bar 2
# Fm motive: F, Ab, Bb, Gb (half-step up to Gb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.75),  # Gb
    # Repeat the motif with slight variation
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
