
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 36, 100), (1.125, 42, 100),
    (1.5, 38, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Marcus: Walking line, chromatic approach to D
bass_notes = [
    (1.5, 62, 100), (1.75, 61, 100), (2.0, 63, 100), (2.25, 65, 100),
    (2.5, 67, 100), (2.75, 65, 100), (3.0, 64, 100), (3.25, 62, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 in 2nd half
    (2.0, 67, 100), (2.0, 69, 100), (2.0, 71, 100), (2.0, 72, 100),  # D7
    # Bar 3: D7 in 2nd half
    (3.0, 67, 100), (3.0, 69, 100), (3.0, 71, 100), (3.0, 72, 100),  # D7
    # Bar 4: D7 in 2nd half
    (4.0, 67, 100), (4.0, 69, 100), (4.0, 71, 100), (4.0, 72, 100)   # D7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 36, 100), (2.625, 42, 100),
    (3.0, 38, 100), (3.375, 42, 100),
    (3.75, 38, 100), (4.125, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax - Dante: Motif in D, start it, leave it hanging
# D (62), F# (64), G (65), B (67), then repeat from F#
sax_notes = [
    (1.5, 62, 100), (1.75, 64, 100), (2.0, 65, 100), (2.25, 67, 100),
    (2.5, 64, 100), (2.75, 65, 100), (3.0, 67, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Marcus: Walking line, chromatic approach to G
bass_notes = [
    (3.0, 67, 100), (3.25, 65, 100), (3.5, 66, 100), (3.75, 68, 100),
    (4.0, 70, 100), (4.25, 68, 100), (4.5, 67, 100), (4.75, 65, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: G7 in 2nd half
    (3.5, 67, 100), (3.5, 69, 100), (3.5, 71, 100), (3.5, 72, 100),  # G7
    # Bar 4: G7 in 2nd half
    (4.5, 67, 100), (4.5, 69, 100), (4.5, 71, 100), (4.5, 72, 100)   # G7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100), (3.375, 42, 100),
    (3.75, 36, 100), (4.125, 42, 100),
    (4.5, 38, 100), (4.875, 42, 100),
    (5.25, 38, 100), (5.625, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax - Dante: Continue the motif, finish it
sax_notes = [
    (3.5, 67, 100), (3.75, 65, 100), (4.0, 67, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Marcus: Walking line, chromatic approach to D
bass_notes = [
    (4.5, 67, 100), (4.75, 65, 100), (5.0, 66, 100), (5.25, 68, 100),
    (5.5, 70, 100), (5.75, 68, 100), (6.0, 67, 100), (6.25, 65, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: D7 in 2nd half
    (5.0, 67, 100), (5.0, 69, 100), (5.0, 71, 100), (5.0, 72, 100),  # D7
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 36, 100), (5.625, 42, 100),
    (6.0, 38, 100), (6.375, 42, 100),
    (6.75, 38, 100), (7.125, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax - Dante: End of motif, leave a lingering note
sax_notes = [
    (5.0, 67, 100), (5.25, 65, 100), (5.5, 67, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
