
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

# Bass line - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Bb
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # C
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Motif: C - Eb - G - Bb (C7), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.0),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.25, end=4.5),  # A#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 3 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # C
    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Return and finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
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

# Bass line - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.75),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.5),  # C#
    pretty_midi.Note(velocity=80, pitch=74, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    # Bar 4 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # Bb
    # Bar 4 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Wrap up with a strong note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=5.125, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.875, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")
