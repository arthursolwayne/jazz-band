
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Dm7 (F, A, D, G) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # D (F, A, D, G)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Marcus: Walking bass line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # D

    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.75),  # C#
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # D

    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Dante: Sax motif - short, singable, no scale runs
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # G

    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # G

    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
