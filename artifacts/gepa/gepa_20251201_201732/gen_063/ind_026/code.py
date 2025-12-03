
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F#2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),  # B2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # F3
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),  # E3
]

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C#5

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5

    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
]

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts (D4, F4, Bb4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # A4

    # Bar 3: Motif continues (Bb4, G4, E4)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F4

    # Bar 4: Motif resolves (Bb4, D4, F4)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # A4
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

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
