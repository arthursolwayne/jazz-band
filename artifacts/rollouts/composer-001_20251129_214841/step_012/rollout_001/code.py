
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line in C
bass_notes = [
    (1.5, 60), (1.75, 61), (2.0, 62), (2.25, 63),
    (2.5, 64), (2.75, 65), (3.0, 66), (3.25, 67),
    (3.5, 68), (3.75, 69), (4.0, 70), (4.25, 71),
    (4.5, 72), (4.75, 73), (5.0, 74), (5.25, 75)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2 (C7 on beat 2)
    (2.0, 60), (2.0, 64), (2.0, 67),
    # Bar 3 (F7 on beat 2)
    (3.5, 59), (3.5, 62), (3.5, 66),
    # Bar 4 (G7 on beat 2)
    (5.0, 61), (5.0, 65), (5.0, 67)
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax melody - one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 62), (2.25, 65),
    (2.5, 62), (2.75, 65), (3.0, 62), (3.25, 65),
    (3.5, 62), (3.75, 65), (4.0, 62), (4.25, 65),
    (4.5, 62), (4.75, 65), (5.0, 62), (5.25, 65)
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums continue through bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
