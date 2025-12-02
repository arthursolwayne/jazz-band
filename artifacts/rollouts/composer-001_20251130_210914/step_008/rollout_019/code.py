
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # F
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),   # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
