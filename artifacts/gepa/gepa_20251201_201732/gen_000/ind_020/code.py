
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif (D4 - F4 - G4 - E4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line (D2 - F2 - G2 - E2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, Dm (F, A, D) + F7 (A, C#, F, G#) + Gm7 (Bb, D, F, G) + E7 (G#, B, D, F#)
# Bar 2: Dm (F, A, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
]

# Bar 3: F7 (A, C#, F, G#)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
]

# Bar 4: E7 (G#, B, D, F#)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Sax (3.0 - 4.5s)
# Repeat the motif but with a twist (D4 - F4 - G4 - E4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass (3.0 - 4.5s)
# Walking line: D2 -> F2 -> G2 -> E2 again
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=41, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Piano (3.0 - 4.5s)
# Resolve on the last bar with Dm again
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
