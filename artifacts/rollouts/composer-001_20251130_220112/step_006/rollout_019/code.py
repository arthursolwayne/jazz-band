
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    # Bar 2, beat 4: Bm7 (B D F# A)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, start on beat 2
sax_notes = [
    # Start of the motif (beat 2)
    pretty_midi.Note(velocity=105, pitch=66, start=1.875, end=2.0625),  # E
    pretty_midi.Note(velocity=105, pitch=64, start=2.0625, end=2.25),   # D
    # Then leave it hanging, come back on beat 3
    pretty_midi.Note(velocity=105, pitch=66, start=2.625, end=2.8125),  # E
    pretty_midi.Note(velocity=105, pitch=64, start=2.8125, end=3.0),    # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Continue with full quartet (3.0 - 4.5s)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    # Bar 3, beat 4: Em7 (E G B D)
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: continue the motif
sax_notes = [
    # Bar 3, beat 1: F
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.1875),
    # Bar 3, beat 2: G
    pretty_midi.Note(velocity=105, pitch=67, start=3.375, end=3.5625),
    # Bar 3, beat 3: A
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=3.9375),
    # Bar 3, beat 4: B
    pretty_midi.Note(velocity=105, pitch=71, start=4.125, end=4.3125),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Continue with full quartet (4.5 - 6.0s)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    # Bar 4, beat 4: Fmaj7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: complete the motif and end on a high note
sax_notes = [
    # Bar 4, beat 1: C
    pretty_midi.Note(velocity=105, pitch=60, start=4.5, end=4.6875),
    # Bar 4, beat 2: D
    pretty_midi.Note(velocity=105, pitch=62, start=4.875, end=5.0625),
    # Bar 4, beat 3: E
    pretty_midi.Note(velocity=105, pitch=64, start=5.25, end=5.4375),
    # Bar 4, beat 4: F
    pretty_midi.Note(velocity=105, pitch=65, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=105, pitch=67, start=5.8125, end=6.0),  # E again
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    # Hi-hat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
