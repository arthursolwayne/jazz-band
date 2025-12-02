
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Sax: motif starting on Fm (F, Ab, Bb, D)
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F (1), Ab (2), Bb (3), D (4) - but with syncopation and space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Fm (chromatic approach)
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),   # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=2.75, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),   # Db
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db
# 2nd beat: Fm7
# 4th beat: Bb7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=2.0, end=2.25),  # Db

    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),  # Gb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation with space and syncopation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.625),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),    # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=90, pitch=61, start=3.25, end=3.5),    # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.75),    # B
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),    # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),    # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=61, start=3.5, end=3.75),  # Db

    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a question, not a statement. Leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),    # A
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),    # B
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.5),    # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=5.5, end=5.75),    # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),    # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),  # Db

    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

midi.write("intro.mid")
