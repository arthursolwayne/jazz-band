
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

# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=3.0),  # C

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.25, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),

    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),

    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, start it, leave it hanging, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.65, end=1.8),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.8, end=2.0),   # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.15),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=2.15, end=2.3),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.3, end=2.5),   # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.65),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.65, end=2.8),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.8, end=3.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Add the drum fills
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.75),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=3.0),  # Hihat

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.25),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),  # Hihat

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.75),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),  # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
