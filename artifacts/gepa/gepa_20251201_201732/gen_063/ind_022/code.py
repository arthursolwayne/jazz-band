
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

# Drums: Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (root), F2 (flat 3), G2 (5), C2 (flat 7)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=3.0),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (start at 1.5s), then return at 3.0s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=52, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=52, start=3.0, end=3.375),  # D4 (return)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm
# Bar 3: C2 (flat 7), D2 (root), F2 (flat 3), G2 (5)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 -> Gm7 -> Cm7 -> Fm7 (open voicings)
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # F5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=57, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=52, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=110, pitch=57, start=4.125, end=4.5),   # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm
# Bar 4: G2 (5), C2 (flat 7), D2 (root), F2 (flat 3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.25),  # C2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Fm7 (F-Ab-C-Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # F5
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Ab5
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # C6
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0),  # Eb6
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolution of motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=55, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=52, start=5.625, end=6.0),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
