
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

# Bass line - Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane (7th chords on 2 and 4)
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # Bb
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # Bb
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante (melody)
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=115, pitch=64, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=59, start=2.625, end=3.0),   # F
    # Bar 3: Repeat the motif, but with a slight variation
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=115, pitch=64, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=105, pitch=60, start=4.125, end=4.5),   # Eb
    # Bar 4: Return to Bb, leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=115, pitch=64, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=59, start=5.625, end=6.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
