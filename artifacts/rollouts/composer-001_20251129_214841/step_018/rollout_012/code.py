
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Bar 2: Full band enters
# Sax: 4-note motif starting on C (60), E (64), Bb (62), D (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # D
]

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=70, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=70, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=70, pitch=64, start=2.625, end=3.0),   # E
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, Bb, D)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),
    # Bar 3: C7 again
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    # Bar 4: C7 again
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),
]

# Add notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
