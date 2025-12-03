
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (Bass): Walking line in Fm (F, Ab, D, C)
# D2 (MIDI 38), G2 (43), chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),  # C2
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=2.75, end=3.0),  # Ab2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (Piano): Open voicings, resolve on bar 4
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = []

# Bar 2
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # D4
])

# Bar 3
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # Ab4
])

# Bar 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # D4
])

for note in piano_notes:
    piano.notes.append(note)

# Dante (Sax): One short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, A, Bb
# Start it, leave it hanging. Come back and finish it.

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # Ab5
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # A5
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.5),  # Bb5
]

# Bar 3 (leave it hanging)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.125),  # F5
])

# Bar 4 (come back and finish it)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # Ab5
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),  # A5
    pretty_midi.Note(velocity=110, pitch=70, start=5.0, end=5.25),  # Bb5
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # C5
])

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
