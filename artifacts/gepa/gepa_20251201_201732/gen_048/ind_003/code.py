
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Piano comping, open voicings, resolve on the last bar
piano_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    # Bar 3 (G7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    # Bar 4 (Dm7) - last bar
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F4
    # Bar 4 (Dm7) - final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax, one short motif, make it sing
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F4
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # F4
    # Bar 4: Resolve motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    # Repeat motif with slight variation to develop
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
