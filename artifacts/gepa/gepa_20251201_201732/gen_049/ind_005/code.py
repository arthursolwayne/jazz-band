
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),  # Kick on 1
    (38, 0.5, 1.0),  # Snare on 2
    (36, 1.0, 1.0),  # Kick on 3
    (38, 1.5, 1.0),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Hihat on every eighth note
for i in range(8):
    start = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

# BAR 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, C, Ab, Eb
# Bar 2: F -> Eb -> D -> C (chromatic approach)
bass_notes = [
    (38, 1.5, 0.5),  # F2 (root)
    (36, 2.0, 0.5),  # Eb2 (chromatic approach)
    (35, 2.5, 0.5),  # D2 (chromatic approach)
    (33, 3.0, 0.5),  # C2 (fifth of Fm)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicing, Fm7 -> Bb7 -> Cm7 -> Eb7
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    (53, 1.5, 1.5),  # F (C4)
    (50, 1.5, 1.5),  # Ab (E4)
    (52, 1.5, 1.5),  # C (D4)
    (51, 1.5, 1.5),  # Db (E4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody starts, short motif
# F (C4) -> Ab (E4) -> C (D4) -> rest
sax_notes = [
    (53, 1.5, 0.25),  # F (C4)
    (50, 1.75, 0.25),  # Ab (E4)
    (52, 2.0, 0.25),  # C (D4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# BAR 3: (3.0 - 4.5s)
# Bass: C -> Bb -> A -> Ab (chromatic approach)
bass_notes = [
    (33, 3.0, 0.5),  # C2
    (32, 3.5, 0.5),  # Bb2
    (31, 4.0, 0.5),  # A2
    (30, 4.5, 0.5),  # Ab2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Bb7 -> Cm7 -> Eb7 -> Fm7
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (54, 3.0, 1.5),  # Bb (D4)
    (51, 3.0, 1.5),  # D (F4)
    (53, 3.0, 1.5),  # F (G4)
    (50, 3.0, 1.5),  # Ab (F4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody continues, incomplete
# Rest -> F (C4) -> Eb (E4) -> rest
sax_notes = [
    (53, 3.5, 0.25),  # F (C4)
    (50, 3.75, 0.25),  # Eb (E4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# BAR 4: (4.5 - 6.0s)
# Bass: Ab -> G -> F -> E (chromatic approach)
bass_notes = [
    (30, 4.5, 0.5),  # Ab2
    (29, 5.0, 0.5),  # G2
    (38, 5.5, 0.5),  # F2
    (28, 6.0, 0.5),  # E2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Eb7 -> Fm7 -> Bb7 -> Cm7
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    (50, 4.5, 1.5),  # Eb (F4)
    (52, 4.5, 1.5),  # G (G4)
    (51, 4.5, 1.5),  # Bb (F4)
    (49, 4.5, 1.5),  # Db (E4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody returns, incomplete again
# Rest -> F (C4) -> Ab (E4) -> rest
sax_notes = [
    (53, 5.0, 0.25),  # F (C4)
    (50, 5.25, 0.25),  # Ab (E4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Same pattern as Bar 1
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

# Hihat on every eighth note
for i in range(8):
    start = 3.0 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
