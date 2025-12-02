
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),    # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),   # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),    # hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),   # Gb
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),    # Ab
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),    # Ab7 (Ab, C, Eb, Gb)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),     # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),     # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),    # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),   # B
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),    # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),    # Ab7
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),     # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),     # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),    # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),   # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),    # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),    # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),    # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),    # Ab7
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),     # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),     # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),     # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
