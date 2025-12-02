
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D (root)
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),   # C
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # B
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, motif: D (62) -> Bb (60) -> A (69) -> D (62) -> rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),           # D
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),           # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),           # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),           # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),           # D (short rest)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),           # D (rest)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),           # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),           # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),           # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),           # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),      # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_intro.mid")
