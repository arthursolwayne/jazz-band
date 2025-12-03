
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # G2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # G2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: G7 (G, B, D, F)
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=2.25),  # C#4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # F4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # B4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25),   # F4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.625),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),   # F4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.125),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.25),   # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),   # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 (1.5 - 3.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Drums: Bar 3 (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.6875, end=5.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
