
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus)
# Bar 2: Fm7 (F, Ab, C, D)
# Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F (D2)
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Eb (C#2)
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # G (E2)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F (D2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# Bar 2: Fm7 (F, Ab, C, D)
# Open voicing, resolve on the last beat
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),   # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # D

    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # Db
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),   # G

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
# Bar 2: Melody starts
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # Bb

    # Bar 3: Repeat the motif
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # Bb

    # Bar 4: Finish the motif with a run up
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass (Marcus)
# Bar 3: Bbm7 (Bb, Db, F, G)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Ab (G#)
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Eb7 (Eb, G, Bb, D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
# Bar 3: Bbm7 (Bb, Db, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # Db
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),   # G

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
# Bar 3: Repeat the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # Bb

    # Bar 4: Finish the motif with a run up
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
