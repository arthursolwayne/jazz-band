
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

# Bar 2: Full ensemble starts (1.5 - 3.0s)
# Bass: Fm walking line, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Continue with the same pattern, but slightly altered
# Bass: Walking line, chromatic approach to Ab
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.875, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, finish it with resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Continue with the same pattern, but slightly altered
# Bass: Walking line, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.375),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=5.375, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.875, end=6.0),  # C#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, finish it with resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to a file
midi.write("intro.mid")
