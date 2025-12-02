
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

# Bar 2: Full quartet
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # C
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # D

    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),  # A
]

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # C
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # C
]

# Piano: 7th chords
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # D

    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # A
]

# Sax: Continue motif
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # C
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # C
]

# Piano: 7th chords
piano_notes += [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # D

    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # A
]

# Sax: End motif
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # C
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue in bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
