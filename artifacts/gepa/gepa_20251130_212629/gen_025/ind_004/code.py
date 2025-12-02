
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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
# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # E
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # D
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s) - Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # C
    # Bar 3 (3.0-4.5s) - G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F
    # Bar 4 (4.5-6.0s) - Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one short phrase, sing it, leave it hanging
sax_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),   # F
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
