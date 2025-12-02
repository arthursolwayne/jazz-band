
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus)
# Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),   # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=49, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=52, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=85, pitch=49, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
# Motif: F - Bb - D - rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    # Rest until 2.75
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus)
# Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),   # F7
    pretty_midi.Note(velocity=85, pitch=49, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # F7
    pretty_midi.Note(velocity=85, pitch=49, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
# Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=60, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=95, pitch=60, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus)
# Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),   # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),   # F7
    pretty_midi.Note(velocity=85, pitch=49, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # F7
    pretty_midi.Note(velocity=85, pitch=49, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
# End with question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
