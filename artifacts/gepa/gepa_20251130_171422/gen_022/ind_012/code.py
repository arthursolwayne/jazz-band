
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm, chromatic approach to Bb
# Diane: 7th chords comp on 2 and 4
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Dante: Melody starts, one short motif, leave it hanging

# Marcus bass line (Dm7 chord: D F A C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # Ab (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane piano comp (Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante sax melody: short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D (lower)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane piano comp (Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=4.125, end=4.5),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante sax motif: Continue the melody with variation, leave it unresolved
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane piano comp (Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=5.625, end=6.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante sax motif: Finish the phrase, leave it open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
