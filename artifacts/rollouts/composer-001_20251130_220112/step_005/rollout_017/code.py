
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

# Marcus: Walking bass line in Fm (F, Gb, Ab, Bb, C, Db, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (Fm7 on 2, Bbm7 on 4)
# Bar 2: Fm7 on beat 2 (1.875 - 2.25)
# Bar 2: Bbm7 on beat 4 (2.625 - 3.0)
piano_notes = [
    # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25),
    # Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif (F, Gb, Ab, Bb) in Fm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (F, Gb, Ab, Bb, C, Db, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (Fm7 on 2, Bbm7 on 4)
# Bar 3: Fm7 on beat 2 (3.375 - 3.75)
# Bar 3: Bbm7 on beat 4 (4.125 - 4.5)
piano_notes = [
    # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75),
    # Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif variation (Ab, Bb, C, Db)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),   # Db
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (F, Gb, Ab, Bb, C, Db, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (Fm7 on 2, Bbm7 on 4)
# Bar 4: Fm7 on beat 2 (4.875 - 5.25)
# Bar 4: Bbm7 on beat 4 (5.625 - 6.0)
piano_notes = [
    # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),
    # Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: End the motif (F, Gb, Ab, Bb) with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
