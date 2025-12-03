
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 2), (1.875, 4), (2.25, 5), (2.625, 7),
    (3.0, 7), (3.375, 9), (3.75, 11), (4.125, 12)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note + 36, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    (1.5, 65), (1.5, 69), (1.5, 72), (1.5, 74),
    # Bar 3: Gm7 (G Bb D F)
    (3.0, 71), (3.0, 73), (3.0, 76), (3.0, 78),
    # Bar 4: Bb7 (Bb D F A)
    (4.5, 70), (4.5, 74), (4.5, 77), (4.5, 79)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax: Melody - one short motif, make it sing, leave it hanging
# Start on D (62), go to F# (67), back to D (62), rest on beat 3
sax_notes = [
    (1.5, 62), (1.875, 67), (2.25, 62), (2.625, 62),
    (3.0, 67), (3.375, 62), (3.75, 62), (4.125, 62),
    (4.5, 62), (4.875, 67), (5.25, 62), (5.625, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (3.0, 7), (3.375, 9), (3.75, 11), (4.125, 12),
    (4.5, 12), (4.875, 14), (5.25, 16), (5.625, 17)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note + 36, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Gm7
piano_notes = [
    (3.0, 71), (3.0, 73), (3.0, 76), (3.0, 78),
    (3.375, 71), (3.375, 73), (3.375, 76), (3.375, 78)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (4.5, 12), (4.875, 14), (5.25, 16), (5.625, 17),
    (6.0, 17), (6.375, 19), (6.75, 21), (7.125, 22)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note + 36, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: Bb7
piano_notes = [
    (4.5, 70), (4.5, 74), (4.5, 77), (4.5, 79),
    (4.875, 70), (4.875, 74), (4.875, 77), (4.875, 79)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Sax: Continue the motif, resolve on the last note
sax_notes = [
    (4.5, 62), (4.875, 67), (5.25, 62), (5.625, 62),
    (6.0, 67), (6.375, 62), (6.75, 62), (7.125, 62)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
