
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
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.75),  # G#
    pretty_midi.Note(velocity=80, pitch=46, start=2.75, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F7 (G)

    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # F7 (G)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A (Fm)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Bb (Fm)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # A (Fm)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # Bb (Fm)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # A (Fm)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # F7 (G)

    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # F7 (G)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # D (Fm)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # C (Fm)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # D (Fm)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # C (Fm)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # A (Fm)
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Bb (Fm)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),  # D#
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=80, pitch=56, start=5.75, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # F7 (G)

    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # F7 (Bb)
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # F7 (E)
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # F7 (D)
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # F7 (G)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Bb (Fm)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # A (Fm)
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # G (Fm)
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.5),  # F (Fm)
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # G (Fm)
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=6.0),  # F (Fm)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
