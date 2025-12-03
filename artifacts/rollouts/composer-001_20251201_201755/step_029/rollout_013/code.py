
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)   # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - A4 (one bar), then D4 - F4 - G4 - A4 (third bar)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # A4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
