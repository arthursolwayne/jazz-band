
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    (1.5, 45), (1.75, 46), (2.0, 44), (2.25, 43),
    (2.5, 45), (2.75, 46), (3.0, 44), (3.25, 43),
    (3.5, 45), (3.75, 46), (4.0, 44), (4.25, 43),
    (4.5, 45), (4.75, 46), (5.0, 44), (5.25, 43)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: 7th chords on 2 and 4
    (2.0, 65), (2.0, 69), (2.0, 72), (2.0, 74),  # F7
    (2.25, 65), (2.25, 69), (2.25, 72), (2.25, 74),
    (3.0, 65), (3.0, 70), (3.0, 72), (3.0, 74),  # Bb7
    (3.25, 65), (3.25, 70), (3.25, 72), (3.25, 74),
    # Bar 3: 7th chords on 2 and 4
    (4.0, 65), (4.0, 69), (4.0, 72), (4.0, 74),  # F7
    (4.25, 65), (4.25, 69), (4.25, 72), (4.25, 74),
    (5.0, 65), (5.0, 70), (5.0, 72), (5.0, 74),  # Bb7
    (5.25, 65), (5.25, 70), (5.25, 72), (5.25, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Tenor Sax (melody: whisper at first, then a cry)
# Bar 2: Start with a motif
sax_notes = [
    (1.5, 62), (1.75, 64), (2.0, 62),  # Whisper
    (2.25, 66), (2.5, 68), (2.75, 66), (3.0, 64), (3.25, 66),  # Build
    (3.5, 71), (3.75, 69), (4.0, 67), (4.25, 66),  # Cry
    (4.5, 64), (4.75, 62), (5.0, 64), (5.25, 66), (5.5, 68), (5.75, 71)  # Resolve
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
