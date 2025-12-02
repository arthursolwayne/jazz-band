
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

# Marcus on bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=44, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=95, pitch=44, start=2.625, end=2.999),  # Bb
    pretty_midi.Note(velocity=95, pitch=48, start=2.625, end=2.999),  # D
    pretty_midi.Note(velocity=95, pitch=50, start=2.625, end=2.999),  # Eb
    pretty_midi.Note(velocity=95, pitch=55, start=2.625, end=2.999),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, make it sing
# Fm scale: F, Gb, A, Bb, C, Db, E
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=2.625, end=3.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # Ab
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=95, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=50, start=4.125, end=4.499),  # Eb
    pretty_midi.Note(velocity=95, pitch=52, start=4.125, end=4.499),  # F
    pretty_midi.Note(velocity=95, pitch=55, start=4.125, end=4.499),  # G
    pretty_midi.Note(velocity=95, pitch=60, start=4.125, end=4.499),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=4.125, end=4.5),   # Ab
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # Db
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=57, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=57, start=5.625, end=5.999),  # Ab
    pretty_midi.Note(velocity=95, pitch=60, start=5.625, end=5.999),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=5.999),  # C
    pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=5.999),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
