
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F, G#, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=2.0),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.75, end=3.0),  # G#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: F, Gb, G, A (walking line with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.75),  # Eb

    # Bar 3: 7th chord on Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # Ab

    # Bar 4: 7th chord on D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.0),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: F, Gb, G, A, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: 7th chord on Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # Ab

    # Bar 4: 7th chord on D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=80, pitch=76, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.75, end=5.0),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.75, end=6.0),  # G#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: F, Gb, G, A, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=59, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: 7th chord on D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
