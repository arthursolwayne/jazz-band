
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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
# Sax: short motif, start on beat 1, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),  # A#
    pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    # Bar 3: D7 (D, F#, C#, E)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend([note for note in drum_notes if note not in drums.notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
