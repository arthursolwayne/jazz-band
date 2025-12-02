
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2: C -> B -> C -> D
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),
    # Bar 3: E -> D -> E -> F
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    # Bar 4: G -> F -> G -> A
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
    # Bar 4: Bb -> A -> Bb -> C
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),
    # Bar 4: D -> C -> D -> Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=64, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=65, start=6.25, end=6.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    # Bar 3: D7 (D, F#, C, E)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=4.0),
    # Bar 4: C7 (C, E, B, D)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),
    # Bar 4: D7 (D, F#, C, E)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
