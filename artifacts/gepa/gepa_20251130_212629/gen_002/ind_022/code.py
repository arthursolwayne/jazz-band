
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Marcus
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),  # D

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # 7th chords on 2 and 4
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=2.0),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=85, pitch=61, start=1.5, end=2.0),

    pretty_midi.Note(velocity=85, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=85, pitch=64, start=2.5, end=3.0),
    pretty_midi.Note(velocity=85, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=85, pitch=61, start=2.5, end=3.0),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=85, pitch=61, start=3.0, end=3.5),

    pretty_midi.Note(velocity=85, pitch=62, start=4.0, end=4.5),
    pretty_midi.Note(velocity=85, pitch=64, start=4.0, end=4.5),
    pretty_midi.Note(velocity=85, pitch=60, start=4.0, end=4.5),
    pretty_midi.Note(velocity=85, pitch=61, start=4.0, end=4.5),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=60, start=4.5, end=5.0),
    pretty_midi.Note(velocity=85, pitch=61, start=4.5, end=5.0),

    pretty_midi.Note(velocity=85, pitch=62, start=5.5, end=6.0),
    pretty_midi.Note(velocity=85, pitch=64, start=5.5, end=6.0),
    pretty_midi.Note(velocity=85, pitch=60, start=5.5, end=6.0),
    pretty_midi.Note(velocity=85, pitch=61, start=5.5, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)

# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(4):  # 4 eighths per bar
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
