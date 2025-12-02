
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=70, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=70, pitch=48, start=2.625, end=3.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.25),  # D
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Motif starts here (1.5 - 3.0s)
# Motif: F, Bb, G, F (melodic minor)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=48, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=70, pitch=49, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=70, pitch=50, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=52, start=4.125, end=4.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # D
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Motif variation (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=52, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=53, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=70, pitch=55, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=70, pitch=57, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # D
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Motif variation (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
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
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
