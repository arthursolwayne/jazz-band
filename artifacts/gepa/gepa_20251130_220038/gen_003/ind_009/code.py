
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bass line: Walking in Dm, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=54, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=54, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),   # G
]
piano.notes.extend(piano_notes)

# Saxophone: Motif in Dm, start it, leave it hanging, come back and finish it
# Motif: D (E), Eb (F), F (G), D (E) -> question, suspension, resolution
# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D (E)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Eb (F)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F (G)
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D (E)
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # Eb (F)
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F (G)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D (E)
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # Eb (F)
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F (G)
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D (E)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # Eb (F)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),   # F (G)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
