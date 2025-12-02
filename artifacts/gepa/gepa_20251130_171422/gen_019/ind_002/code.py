
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody (Dante)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.75, end=3.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (Diane) - 7th chords on 2 and 4
# Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (Dante)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (Diane) - 7th chords on 2 and 4
# Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (Dante)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (Diane) - 7th chords on 2 and 4
# Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.75, end=6.0),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums for bars 2-4
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
