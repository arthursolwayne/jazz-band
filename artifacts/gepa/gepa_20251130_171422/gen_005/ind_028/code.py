
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax melody (1.5 - 3.0s)
# Dm7, F, G, C, Bb, A, G, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Marcus bass line (chromatic walk)
# D, C#, D, E, F, E, D, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Diane piano comping (7th chords, on 2 and 4)
# Dm7 on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),
    # Bar 2: Dm7 on 4 (2.75 - 3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full ensemble
# Sax melody (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Marcus bass line (chromatic walk)
# D, C#, D, E, F, E, D, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Diane piano comping (7th chords, on 2 and 4)
# Dm7 on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.5),
    # Bar 3: Dm7 on 4 (4.25 - 4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=70, start=4.25, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full ensemble
# Sax melody (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=100, pitch=65, start=6.25, end=6.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Marcus bass line (chromatic walk)
# D, C#, D, E, F, E, D, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=62, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=60, start=6.25, end=6.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Diane piano comping (7th chords, on 2 and 4)
# Dm7 on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=5.0),
    # Bar 4: Dm7 on 4 (5.75 - 6.0)
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=70, start=5.75, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
