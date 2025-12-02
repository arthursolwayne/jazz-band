
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax starts motif (1.5 - 3.0s)
# D7 chord: D F# A C#
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.125),  # F#
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.375, end=2.5),  # F#
    pretty_midi.Note(velocity=80, pitch=49, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (1.5 - 3.0s)
piano_notes = [
    # Bar 2, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C#
    # Bar 2, beat 4: G7
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # F#
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # C#
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.375),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=80, pitch=49, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.875, end=4.0),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.125),  # C#
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.375),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=4.375, end=4.5),  # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # F#
    # Bar 3, beat 4: C7
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # C#
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.625),  # C#
    pretty_midi.Note(velocity=80, pitch=57, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=54, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=5.125, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=80, pitch=54, start=5.875, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Same pattern as bar 1
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
