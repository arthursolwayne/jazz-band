
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Tenor sax, short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # G (Fm scale)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Eb
    # Bar 4: Eb7 (Eb, G, Bb, Db) on beat 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Tenor sax, motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Eb
    # Bar 4: Eb7 (Eb, G, Bb, Db) on beat 4
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Tenor sax, resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
