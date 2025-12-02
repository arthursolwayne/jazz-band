
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=3.0),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=48, start=4.25, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.75, end=6.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=55, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.75),  # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=55, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.0, end=4.25),  # A
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=55, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=85, pitch=46, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.75),  # A
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.1875, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.6875, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.1875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.1875, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.6875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.6875, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
