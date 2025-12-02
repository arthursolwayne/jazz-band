
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
# Marcus: Walking bass line in D
bass_notes = [
    # D (D3) on 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # F# (F#3) on 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),
    # A (A3) on 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    # C (C4) on 4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    # Chromatic approaches
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    # D7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody - start with a motif, leave it hanging
sax_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),
    # F# (F#4) on 2
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),
    # Bb (Bb4) on 3
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.625),
    # D (D5) on 4
    pretty_midi.Note(velocity=110, pitch=82, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    # F# (F#3) on 1
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),
    # A (A3) on 2
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    # C (C4) on 3
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    # D (D4) on 4
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
    # Chromatic approaches
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.25),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # F#7 on 2 (F#, A, C, D)
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # F#7 on 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue the melody
sax_notes = [
    # F# (F#4) on 1
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.375),
    # A (A4) on 2
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.75),
    # D (D5) on 3
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.125),
    # F# (F#5) on 4
    pretty_midi.Note(velocity=110, pitch=85, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    # A (A3) on 1
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    # C (C4) on 2
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    # D (D4) on 3
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    # F# (F#4) on 4
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
    # Chromatic approaches
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=75, start=5.625, end=5.75),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # A7 on 2 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25),
    # A7 on 4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: End the motif
sax_notes = [
    # A (A4) on 1
    pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.875),
    # D (D5) on 2
    pretty_midi.Note(velocity=110, pitch=82, start=4.875, end=5.25),
    # F# (F#5) on 3
    pretty_midi.Note(velocity=110, pitch=85, start=5.25, end=5.625),
    # A (A5) on 4
    pretty_midi.Note(velocity=110, pitch=89, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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

# Save the MIDI file
midi.write("dante_intro.mid")
