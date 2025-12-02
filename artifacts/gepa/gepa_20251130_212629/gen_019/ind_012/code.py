
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=2.875),  # F
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),    # E
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),    # G
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.0),    # B
]
for note in piano_notes:
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F# (D7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # G (G7)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # F (C7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.75), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add drum fills for rhythm and energy
drum_fill_1 = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
]
for note in drum_fill_1:
    drums.notes.append(note)

# Final silence or rest
# Silence in the last half of bar 4 to leave it hanging
# No notes in sax, bass, or piano in the last 0.375s of bar 4

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
