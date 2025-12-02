
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2 (1.5-3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # F7: D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F7: A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F7: C
    # Bar 3 (3.0-4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # F7: D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F7: A
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F7: C
    # Bar 4 (4.5-6.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # F7: D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F7: A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F7: C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody. Start with restraint, build with tension, resolve with clarity.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Add hihat on every eighth note
for bar in range(2, 5):
    for i in range(0, 4):
        start = 1.5 + (bar - 2) * 1.5 + i * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
