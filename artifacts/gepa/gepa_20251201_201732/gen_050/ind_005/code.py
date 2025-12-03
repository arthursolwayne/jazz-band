
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: F (G2) -> Bb (A2) -> Ab (G#2) -> D (C#2) -> F (G2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # G2 (F root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # A2 (Bb)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # G#2 (Ab)
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),  # C#2 (D)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Fm7 -> Ab7 -> Bbmaj7 -> D7
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=3.0),  # D
    # Bar 3 (Ab7)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F
    # Bar 4 (Bbmaj7)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Ab
    # Bar 4 (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F# (Gb)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Fm
# Start on F (G4), then Ab (G#4), then D (C#5), then F (G4)
# Leave it hanging on the last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # F (G4)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # Ab (G#4)
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625), # D (C#5)
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # F (G4) - end on the beat
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # F (G4) - hold for a beat
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75), # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125), # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # F (G4)
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # F (G4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
