
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

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=1.5, end=1.875),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody - short motif, make it sing. Start it, leave it hanging.
# Melody: F, Bb, D, F (Motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # Ab
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=4.875),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody - repeat motif, but finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=80, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # G
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=4.875),  # B
    # Bar 4: End with a quick F7
    pretty_midi.Note(velocity=95, pitch=79, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=5.875),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=5.875),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=5.625, end=5.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody - repeat motif, but finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=86, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
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
