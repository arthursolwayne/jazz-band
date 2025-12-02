
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
