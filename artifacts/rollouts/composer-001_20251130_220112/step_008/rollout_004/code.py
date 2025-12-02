
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX - Tenor motif: Fm7 -> Eb7 -> Dm7 -> C7
# Fm7 = F, Ab, Db, Eb
# Eb7 = Eb, G, Bb, Db
# Dm7 = D, F, A, C
# C7 = C, E, G, Bb
sax_notes = [
    (1.5, 87), (1.75, 82), (2.0, 80), (2.25, 79),  # F, Eb, D, C
    (2.5, 79), (2.75, 82), (3.0, 80), (3.25, 79)   # D, Eb, D, C
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# BASS - Walking line: F, Gb, G, A, Bb, B, C, Db
bass_notes = [
    (1.5, 71), (1.75, 70), (2.0, 72), (2.25, 74),
    (2.5, 73), (2.75, 75), (3.0, 76), (3.25, 70)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# PIANO - 7th chords comped on 2 and 4
piano_notes = [
    (1.75, 72), (1.75, 69), (1.75, 67), (1.75, 65),  # Fm7 (C, Eb, F, Ab)
    (2.25, 71), (2.25, 68), (2.25, 66), (2.25, 64),  # Eb7 (Bb, Db, Eb, G)
    (2.75, 71), (2.75, 69), (2.75, 67), (2.75, 65),  # Fm7 again
    (3.25, 72), (3.25, 69), (3.25, 67), (3.25, 65)   # Fm7 again
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX - Repeat motif with slight variation: Fm7 -> Eb7 -> Dm7 -> C7
sax_notes = [
    (3.0, 87), (3.25, 82), (3.5, 80), (3.75, 79),  # F, Eb, D, C
    (4.0, 79), (4.25, 82), (4.5, 80), (4.75, 79)   # D, Eb, D, C
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# BASS - Walking line: F, Gb, G, A, Bb, B, C, Db
bass_notes = [
    (3.0, 71), (3.25, 70), (3.5, 72), (3.75, 74),
    (4.0, 73), (4.25, 75), (4.5, 76), (4.75, 70)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# PIANO - 7th chords comped on 2 and 4
piano_notes = [
    (3.25, 72), (3.25, 69), (3.25, 67), (3.25, 65),  # Fm7 (C, Eb, F, Ab)
    (3.75, 71), (3.75, 68), (3.75, 66), (3.75, 64),  # Eb7 (Bb, Db, Eb, G)
    (4.25, 71), (4.25, 69), (4.25, 67), (4.25, 65),  # Fm7 again
    (4.75, 72), (4.75, 69), (4.75, 67), (4.75, 65)   # Fm7 again
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX - Finale: Fm7 -> Eb7 -> Dm7 -> C7, with resolution to Fm
sax_notes = [
    (4.5, 87), (4.75, 82), (5.0, 80), (5.25, 79),  # F, Eb, D, C
    (5.5, 79), (5.75, 82), (6.0, 80), (6.25, 79)   # D, Eb, D, C
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# BASS - Walking line: F, Gb, G, A, Bb, B, C, Db
bass_notes = [
    (4.5, 71), (4.75, 70), (5.0, 72), (5.25, 74),
    (5.5, 73), (5.75, 75), (6.0, 76), (6.25, 70)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# PIANO - 7th chords comped on 2 and 4
piano_notes = [
    (4.75, 72), (4.75, 69), (4.75, 67), (4.75, 65),  # Fm7 (C, Eb, F, Ab)
    (5.25, 71), (5.25, 68), (5.25, 66), (5.25, 64),  # Eb7 (Bb, Db, Eb, G)
    (5.75, 71), (5.75, 69), (5.75, 67), (5.75, 65),  # Fm7 again
    (6.25, 72), (6.25, 69), (6.25, 67), (6.25, 65)   # Fm7 again
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
