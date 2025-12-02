
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C7 (D7)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C7 (D7)
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
]

# Sax - Dante (melodic motif, one short phrase, start it, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # D
]

# Add notes to instruments
for note in drum_notes:
    drums.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
