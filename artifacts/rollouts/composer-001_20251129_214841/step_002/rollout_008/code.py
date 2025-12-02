
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - Marcus (walking line, chromatic approaches, never the same note twice)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),   # C7 (C, E, B)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),   # D7 (D, F#, C#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante (motif: C, D#, F, G, leave it hanging, then finish on the 4th bar)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.25), # D#
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5

    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)

    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - Marcus
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),   # D7 (D, F#, C#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),   # E7 (E, G#, D)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante (continuing motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5

    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)

    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),   # F7 (F, A, E)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=6.0),   # G7 (G, B, F#)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.25), # D#
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5

    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)

    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
