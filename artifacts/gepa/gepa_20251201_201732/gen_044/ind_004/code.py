
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (bass) - walking line in Dm: D2, F2, G2, C2, D2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # C2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano) - Open voicings, resolve on the last chord
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F5
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (sax) - Motif: D4 - F4 - G4 - D4 (starts on 2, leaves it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Drum fill at the end of bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),   # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
