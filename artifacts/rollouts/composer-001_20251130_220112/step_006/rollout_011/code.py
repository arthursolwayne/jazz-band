
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax, short motif, make it sing
sax_notes = [
    # Bar 2 (start at 1.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_quartet.mid")
