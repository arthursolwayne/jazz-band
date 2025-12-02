
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
# Sax: motif starts at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=80, pitch=46, start=2.75, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # G
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=46, start=4.25, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # G
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=58, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=80, pitch=46, start=5.75, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # G
    # Bar 4: F7 on beat 4 (same chord, just extended)
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
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

midi.write("jazz_intro.mid")
