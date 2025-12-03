
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
# Bass line: F - Ab - Bb - B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),   # B2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: F7 - Bb7 - Cm7 - F7
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=85, start=2.25, end=2.625),
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=2.625, end=3.0),
    # Bar 2: F7 (resolve on 4)
    pretty_midi.Note(velocity=100, pitch=87, start=2.625, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging
# F - Ab - Bb - (leave it hanging on Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=80, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=82, start=1.875, end=2.0625),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: F - Ab - Bb - B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),   # B2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: F7 - Bb7 - Cm7 - F7
# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=85, start=3.0, end=3.375),
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=4.125),
    # Bar 4: F7 (resolve on 4)
    pretty_midi.Note(velocity=100, pitch=87, start=4.125, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    # Kick on 1 and 3 (3.0 and 4.125)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 (3.375 and 4.5)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat every eighth
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

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: F - Ab - Bb - B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),   # B2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Fm7 - Bbm7 - Cm7 - Fm7
# Bar 4: Fm7 (F Ab C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Come back and finish the motif
# Bb - F - Ab - F (resolve on F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=82, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=77, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=80, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=77, start=5.0625, end=5.25),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
