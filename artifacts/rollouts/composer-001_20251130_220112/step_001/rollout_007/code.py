
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Enter bass, piano, sax
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Introduce the motif
# Bar 2: Start the motif (D, Eb, C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C
    # Bar 3: Let it hang (no note)
    # Bar 4: Return and finish the motif (D, Eb, C)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
# Bar 2 (1.5 - 3.0)
for i in range(1.5, 3.0, 0.375):
    if i % 1.0 == 0.0:
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    if i % 1.0 == 0.75:
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i, end=i+0.125)
    for j in range(0, 1.5, 0.1875):
        # Hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=i + j, end=i + j + 0.1875)

# Bar 3 (3.0 - 4.5)
for i in range(3.0, 4.5, 0.375):
    if i % 1.0 == 0.0:
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    if i % 1.0 == 0.75:
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i, end=i+0.125)
    for j in range(0, 1.5, 0.1875):
        # Hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=i + j, end=i + j + 0.1875)

# Bar 4 (4.5 - 6.0)
for i in range(4.5, 6.0, 0.375):
    if i % 1.0 == 0.0:
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    if i % 1.0 == 0.75:
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i, end=i+0.125)
    for j in range(0, 1.5, 0.1875):
        # Hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=i + j, end=i + j + 0.1875)

# Add the notes to the instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
