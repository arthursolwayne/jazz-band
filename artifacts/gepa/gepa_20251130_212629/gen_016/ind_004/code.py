
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
    # Hi-hat on every eighth
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

# Bass line - Marcus: chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),  # F
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0),    # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),    # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),    # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Dm (D, F, Bb)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625), # Bb
    # Bar 3: Rest
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.8125), # Bb
    # Bar 4: Return with Dm
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.3125, end=4.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
