
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
    # Hi-hat on every 8th
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    # Chromatic approach to G2 (43) from F#2 (42)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),

    # Bar 3: G2 (root), Bb2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),
    # Chromatic approach to D3 (50) from C#3 (49)
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),

    # Bar 4: D3 (root), F3 (fifth)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),
    # Chromatic approach to G3 (51) from F#3 (50)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C5,

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # F5

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
