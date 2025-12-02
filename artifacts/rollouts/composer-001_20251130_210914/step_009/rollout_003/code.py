
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
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.75, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=46, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.875, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    # Bar 3: Dm7 again
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    # Bar 4: Dm7 again
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=46, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=4.375, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    # Bar 4: Dm7 again
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a strong note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=46, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=5.875),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=5.875, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
