
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, C, Ab, Eb, Bb, F, C, Ab, etc.
bass_notes = [
    (1.5, 53), (1.875, 51), (2.25, 53), (2.625, 55),
    (3.0, 55), (3.375, 53), (3.75, 51), (4.125, 53),
    (4.5, 53), (4.875, 51), (5.25, 53), (5.625, 55)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 64), (1.5, 69), (1.5, 72), (1.5, 67),
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    (3.0, 62), (3.0, 66), (3.0, 72), (3.0, 69),
    # Bar 4: Ebm7 (Eb, Gb, Bb, Db)
    (4.5, 67), (4.5, 71), (4.5, 62), (4.5, 66)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 1.5))

# Sax: Haunting motif, incomplete, with rests
# Start at 1.5s with a short phrase that ends on a rest
sax_notes = [
    # Bar 2: F (65), Ab (67), rest
    (1.5, 65), (1.875, 67),
    # Bar 3: rest, Bb (62)
    (3.0, 62),
    # Bar 4: rest, Eb (67)
    (4.5, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Add rests to sax in the remaining time
# Bar 2: rest from 2.25s to 3.0s
sax.notes.append(pretty_midi.Note(velocity=0, pitch=60, start=2.25, end=3.0))
# Bar 3: rest from 3.375s to 4.5s
sax.notes.append(pretty_midi.Note(velocity=0, pitch=60, start=3.375, end=4.5))
# Bar 4: rest from 5.25s to 6.0s
sax.notes.append(pretty_midi.Note(velocity=0, pitch=60, start=5.25, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
