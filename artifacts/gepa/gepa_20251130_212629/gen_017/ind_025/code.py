
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=2.25),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=3.0),   # F7 - Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, one phrase, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.5),   # F7 - Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: second phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
]

for note in drum_notes:
    drums.notes.append(note)

# Bass line: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.25),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=6.0),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=6.0),   # F7 - A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=6.0),   # F7 - C
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=6.0),   # F7 - Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: end with an open question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
