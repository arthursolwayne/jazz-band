
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hi-hat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax starts with a short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # E (Bb7)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # G (Bb7)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.25, end=4.5),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes motif, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F (Bb7)
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # E (Bb7)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hi-hat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hi-hat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
