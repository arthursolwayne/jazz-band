
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.0, end=4.25),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.5),  # D#
    pretty_midi.Note(velocity=80, pitch=76, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=5.75, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C7
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax - motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on every 8th
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
