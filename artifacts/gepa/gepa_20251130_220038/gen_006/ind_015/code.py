
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
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),   # Eb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),   # D
    # Bar 3: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # D
    # Bar 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: Motif
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Eb
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
