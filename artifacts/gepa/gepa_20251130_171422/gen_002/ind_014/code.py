
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Rest, then repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif again, this time with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
