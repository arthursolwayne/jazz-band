
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
# Fm7 -> Bb7 -> Eb7 -> Am7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=3.0),  # A2
]

piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Db4
]

# Sax motif: F, Ab, Bb, C (start on beat 1, leave hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # C4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (Bb2, B2, C2, Db2, D2, Eb2, E2, F2)
# Bb7 -> Eb7 -> Am7 -> Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),  # Db2
]

piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab4
]

# Sax motif: F, Ab, Bb, C (start on beat 1, leave hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75), # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # C4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2, Eb2, E2, F2, G2, Ab2, A2, Bb2)
# Eb7 -> Am7 -> Dm7 -> Gm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # F2
]

piano_notes = [
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Db4
]

# Sax motif: F, Ab, Bb, C (resolve on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # C4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Add drum fill in bar 4
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
