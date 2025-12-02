
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (D4), F# (F#4), A (A4), C (C5), D (D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.375),
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.625),  # D (D3)
    pretty_midi.Note(velocity=80, pitch=44, start=1.625, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.125),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.125, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.375, end=2.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),  # D7: F#

    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5),  # D7: F#
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=3.125, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.625),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=3.625, end=3.875),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=3.875, end=4.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),  # D7: F#

    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # D7: F#
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a descending resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.375),
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=4.625, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.125),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=5.125, end=5.375),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.375, end=5.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625),  # D7: F#

    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.5),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=5.375, end=5.5),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),  # D7: B
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5),  # D7: F#
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
