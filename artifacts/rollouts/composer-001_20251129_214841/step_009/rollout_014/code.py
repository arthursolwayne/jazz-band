
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60) - F (65) - Bb (62) - D (64)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (C - Bb - B - C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: C7 on 2, F7 on 4
piano_notes = [
    # C7: C, E, Bb, B
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),
    # F7: F, A, E, G
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (C - Bb - B - C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3: C7 on 2, F7 on 4
piano_notes = [
    # C7: C, E, Bb, B
    pretty_midi.Note(velocity=95, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),
    # F7: F, A, E, G
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (C - Bb - B - C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4: C7 on 2, F7 on 4
piano_notes = [
    # C7: C, E, Bb, B
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),
    # F7: F, A, E, G
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick=36, snare=38, hihat=42
# Bar 2: 1.5 - 3.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
