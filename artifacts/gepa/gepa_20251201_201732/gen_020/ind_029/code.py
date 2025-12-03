
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # G2
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # F#2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # D3 (resolve)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5s): Dmaj7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D5
    # Bar 3 (3.0s): Bm7b5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # G5
    # Bar 4 (4.5s): F#7
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # G5
    # Bar 4 (4.875s): Resolve to Dmaj7
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5s): Start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G4
    # Bar 3 (3.0s): Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # F#4
    # Bar 4 (4.5s): Come back and finish the motif
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875), # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25), # E4
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fills for the rest of the piece
drum_fill_notes = [
    # Bar 2 - fill on 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
    # Bar 3 - fill on 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5),
    # Bar 4 - fill on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75),
]

for note in drum_fill_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
