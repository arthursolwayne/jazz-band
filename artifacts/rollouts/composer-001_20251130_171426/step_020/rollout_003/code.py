
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),       # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),      # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),          # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),       # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),       # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),      # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),          # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),       # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),       # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),      # F#
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),      # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),       # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-2.25): Root 7th chord on 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),       # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),       # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),       # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),       # D
    # Bar 2 (2.25-3.0): Root 7th chord on 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),      # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),      # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),      # C
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),      # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),       # G (F7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),      # G#
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),      # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),       # G (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),       # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),      # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),          # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),       # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),       # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),      # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),      # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),       # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0-3.75): Root 7th chord on 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),       # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),       # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),       # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),       # D
    # Bar 3 (3.75-4.5): Root 7th chord on 4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),      # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),      # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),      # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),      # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),       # G#
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),      # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),      # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),       # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),       # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),      # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),          # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),       # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),       # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),      # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),      # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),       # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 (4.5-5.25): Root 7th chord on 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),       # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),       # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),       # C
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),       # D
    # Bar 4 (5.25-6.0): Root 7th chord on 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),      # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),      # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),      # C
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),      # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),       # G#
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),      # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),      # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),       # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
