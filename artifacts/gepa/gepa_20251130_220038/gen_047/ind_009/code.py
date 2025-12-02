
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F minor, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # Eb

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # C

    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Melody - short motif, starts, leaves it hanging, comes back
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # C

    # Bar 3 (Rest)
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=3.0),  # Rest (space)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # F

    # Bar 4 (Resolution)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4

    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4

    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("waynes_shot.mid")
