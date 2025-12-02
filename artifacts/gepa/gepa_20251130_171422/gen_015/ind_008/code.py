
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (1.5)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D (2.25)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D (2.75)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line (chromatic approach, walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (continuation with space)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Eb (rest on 3.75-4.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D (4.0)
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line (chromatic approach, walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Bar 3)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line (chromatic approach, walking)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.5, end=5.75),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Bar 4)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
