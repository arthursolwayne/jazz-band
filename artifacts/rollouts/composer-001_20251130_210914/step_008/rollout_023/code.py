
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
