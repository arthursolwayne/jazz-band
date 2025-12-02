
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D

    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),

    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),

    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),

# Sax: Dante's motif - short, simple, haunting
# Motif: D (62) - F (65) - C (60) - D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
