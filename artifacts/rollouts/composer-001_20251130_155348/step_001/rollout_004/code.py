
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
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D7: G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # D7: Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D7: F#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G7: B
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G7: D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G7: F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G7: G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G7: B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G7: D
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G7: F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G7: G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax solo: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F#
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]
for note in drums_notes:
    drums.notes.append(note)

# Bar 3
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
for note in drums_notes:
    drums.notes.append(note)

# Bar 4
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drums_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
