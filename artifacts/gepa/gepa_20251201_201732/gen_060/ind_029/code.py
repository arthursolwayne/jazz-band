
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
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on &1
    (1.0, 38, 100),   # Snare on 2
    (1.25, 42, 100),  # Hihat on &2
    (1.5, 36, 100),   # Kick on 3
    (1.75, 42, 100),  # Hihat on &3
    (2.0, 38, 100),   # Snare on 4
    (2.25, 42, 100),  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (root) -> E2 (fifth with chromatic approach from D#2)
# Piano: Dmaj7 (D-F#-A-C#) -> G7 (G-B-D-F) -> A7 (A-C#-E-G)
# Sax: Motif: D (1.5s) -> F# (1.75s) -> A (2.0s) -> (rest)
# Drums: Kick on 1, Snare on 2, Hihat on &1, &2, &3, &4

# Bass
bass_notes = [
    (1.5, 38, 100),  # D2
    (1.75, 40, 100), # D#2 (chromatic approach)
    (2.0, 43, 100),  # E2 (fifth)
    (2.25, 38, 100), # D2
    (2.5, 40, 100),  # D#2
    (2.75, 43, 100), # E2
    (3.0, 38, 100),  # D2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano
piano_notes = [
    (1.5, 55, 100),  # D (root)
    (1.5, 59, 100),  # F#
    (1.5, 64, 100),  # A
    (1.5, 67, 100),  # C#
    (2.0, 62, 100),  # G
    (2.0, 67, 100),  # B
    (2.0, 64, 100),  # D
    (2.0, 69, 100),  # F
    (2.5, 65, 100),  # A
    (2.5, 69, 100),  # C#
    (2.5, 72, 100),  # E
    (2.5, 76, 100),  # G
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax
sax_notes = [
    (1.5, 62, 100),  # D (1.5s)
    (1.75, 66, 100), # F#
    (2.0, 69, 100),  # A
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums Bar 2
drum_notes = [
    (1.5, 36, 100),   # Kick on 1
    (1.75, 42, 100),  # Hihat on &1
    (2.0, 38, 100),   # Snare on 2
    (2.25, 42, 100),  # Hihat on &2
    (2.5, 36, 100),   # Kick on 3
    (2.75, 42, 100),  # Hihat on &3
    (3.0, 38, 100),   # Snare on 4
    (3.25, 42, 100),  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 -> F2 (chromatic approach from E2) -> G2 (fifth) -> A2 (chromatic)
# Piano: G7 (G-B-D-F) -> A7 (A-C#-E-G) -> Dmaj7 (D-F#-A-C#)
# Sax: (rest) -> D (3.5s) -> F# (3.75s) -> A (4.0s)
# Drums: same pattern

# Bass
bass_notes = [
    (3.0, 38, 100),  # D2
    (3.25, 43, 100), # E2
    (3.5, 44, 100),  # F2
    (3.75, 43, 100), # E2
    (4.0, 45, 100),  # G2
    (4.25, 47, 100), # A2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano
piano_notes = [
    (3.0, 62, 100),  # G
    (3.0, 67, 100),  # B
    (3.0, 64, 100),  # D
    (3.0, 69, 100),  # F
    (3.5, 65, 100),  # A
    (3.5, 69, 100),  # C#
    (3.5, 72, 100),  # E
    (3.5, 76, 100),  # G
    (4.0, 55, 100),  # D
    (4.0, 59, 100),  # F#
    (4.0, 64, 100),  # A
    (4.0, 67, 100),  # C#
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax
sax_notes = [
    (3.5, 62, 100),  # D
    (3.75, 66, 100), # F#
    (4.0, 69, 100),  # A
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums Bar 3
drum_notes = [
    (3.0, 36, 100),   # Kick on 1
    (3.25, 42, 100),  # Hihat on &1
    (3.5, 38, 100),   # Snare on 2
    (3.75, 42, 100),  # Hihat on &2
    (4.0, 36, 100),   # Kick on 3
    (4.25, 42, 100),  # Hihat on &3
    (4.5, 38, 100),   # Snare on 4
    (4.75, 42, 100),  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 -> F2 (chromatic approach from E2) -> G2 -> A2
# Piano: Dmaj7 (D-F#-A-C#) -> G7 (G-B-D-F) -> A7 (A-C#-E-G)
# Sax: (rest) -> D (5.0s) -> F# (5.25s) -> A (5.5s) -> (rest)
# Drums: same pattern

# Bass
bass_notes = [
    (4.5, 38, 100),  # D2
    (4.75, 43, 100), # E2
    (5.0, 44, 100),  # F2
    (5.25, 43, 100), # E2
    (5.5, 45, 100),  # G2
    (5.75, 47, 100), # A2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano
piano_notes = [
    (4.5, 55, 100),  # D
    (4.5, 59, 100),  # F#
    (4.5, 64, 100),  # A
    (4.5, 67, 100),  # C#
    (5.0, 62, 100),  # G
    (5.0, 67, 100),  # B
    (5.0, 64, 100),  # D
    (5.0, 69, 100),  # F
    (5.5, 65, 100),  # A
    (5.5, 69, 100),  # C#
    (5.5, 72, 100),  # E
    (5.5, 76, 100),  # G
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax
sax_notes = [
    (5.0, 62, 100),  # D
    (5.25, 66, 100), # F#
    (5.5, 69, 100),  # A
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums Bar 4
drum_notes = [
    (4.5, 36, 100),   # Kick on 1
    (4.75, 42, 100),  # Hihat on &1
    (5.0, 38, 100),   # Snare on 2
    (5.25, 42, 100),  # Hihat on &2
    (5.5, 36, 100),   # Kick on 3
    (5.75, 42, 100),  # Hihat on &3
    (6.0, 38, 100),   # Snare on 4
    (6.25, 42, 100),  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
