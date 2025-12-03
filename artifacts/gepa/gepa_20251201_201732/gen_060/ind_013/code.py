
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F (fifth with chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C5

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # F5

    # Bar 4: Am7 (A C E G)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # E5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # G5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
sax_notes = [
    # Bar 2: Dm melody
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),  # D4

    # Bar 3: Gm melody
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=4.0),   # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.375),  # G4

    # Bar 4: Am melody
    pretty_midi.Note(velocity=100, pitch=71, start=4.375, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.125), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=5.125, end=5.5),   # E5
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.875),  # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2

    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3

    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2

    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3

    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2

    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3

    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
