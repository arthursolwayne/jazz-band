
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # G#2
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # G#2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # F2
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # G#2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F4
    # Bar 4: Cmaj7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
]
for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F#4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    # Bar 4: Finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F#4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar
drum_notes_continuation = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes_continuation:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
