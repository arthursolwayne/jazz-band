
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F (41) - 3rd (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.125),
    # G2 (43) - 5th
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),
    # Bar 3 (3.0 - 4.5s)
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    # F (41) - 3rd (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.625),
    # G2 (43) - 5th
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=4.0),
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.375),
    # Bar 4 (4.5 - 6.0s)
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # F (41) - 3rd (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.125),
    # G2 (43) - 5th
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.5),
    # D2 (38) - root
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F5
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.65),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.65, end=1.8),   # F4 (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=67, start=1.8, end=2.0),    # A4
    # Bar 3: G7
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.15),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.15, end=3.3),   # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.3, end=3.45),   # D5
    # Bar 4: Cm7
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.65),  # C4
    pretty_midi.Note(velocity=110, pitch=63, start=4.65, end=4.8),   # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=4.8, end=5.0),    # G4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.15),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
