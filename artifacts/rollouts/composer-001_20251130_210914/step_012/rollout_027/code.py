
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
# Sax melody
sax_notes = [
    # Dm7 - D F A C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # C
    # End on C, leave it hanging
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=54, start=2.125, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=56, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=2.375, end=2.5),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats the motif, but with a chromatic passing tone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=54, start=3.625, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=3.875, end=4.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax concludes the motif with a chromatic resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.125, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=90, pitch=54, start=5.125, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.625),  # A#
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=5.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.875, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.875, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
