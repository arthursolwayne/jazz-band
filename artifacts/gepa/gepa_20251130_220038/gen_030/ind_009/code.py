
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# D Dorian scale: D, E, F#, G, A, B, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25),  # A#
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=5.25),
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=5.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D, F#, A, C, D, B, A, F#
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
]

# Bar 3 (3.0 - 4.5s)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
]

# Bar 4 (4.5 - 6.0s)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
