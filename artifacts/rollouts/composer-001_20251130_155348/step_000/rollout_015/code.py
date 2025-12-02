
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
    # Time (s), note
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.75, 63), (2.0, 60), (2.25, 61),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62), (3.25, 63), (3.5, 60), (3.75, 61),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.75, 63), (5.0, 60), (5.25, 61),
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 71), (1.75, 74), (1.75, 76), (1.75, 79),
    (2.25, 71), (2.25, 74), (2.25, 76), (2.25, 79),
    # Bar 3 (3.0 - 4.5s)
    (3.25, 69), (3.25, 72), (3.25, 74), (3.25, 79),
    (3.75, 69), (3.75, 72), (3.75, 74), (3.75, 79),
    # Bar 4 (4.5 - 6.0s)
    (4.75, 71), (4.75, 74), (4.75, 76), (4.75, 79),
    (5.25, 71), (5.25, 74), (5.25, 76), (5.25, 79),
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3 (3.0 - 4.5s)
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42),
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D7 - G7 - A7 - D7 (Motif: D, F#, A, C#)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.625, 67), (1.75, 69), (1.875, 64),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62), (3.125, 67), (3.25, 69), (3.375, 64),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.625, 67), (4.75, 69), (4.875, 64),
    (5.0, 62), (5.125, 67), (5.25, 69), (5.375, 64),
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
