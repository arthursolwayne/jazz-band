
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.375, end=2.5),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.625),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=2.875, end=3.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=3.875, end=4.0),  # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=4.375, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=4.375, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.5),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, build it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.125, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.375, end=5.5),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.375),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
