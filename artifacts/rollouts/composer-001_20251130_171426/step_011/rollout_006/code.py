
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),  # D
    (1.875, 63),  # Eb
    (2.25, 64),  # E
    (2.625, 62),  # D
    (3.0, 60),   # C
    (3.375, 61),  # Db
    (3.75, 62),  # D
    (4.125, 60),  # C
    (4.5, 59),   # Bb
    (4.875, 60),  # Bb
    (5.25, 62),  # D
    (5.625, 63),  # Eb
    (6.0, 64),   # E
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),  # Dm7
    (1.875, 62), (1.875, 67), (1.875, 72), (1.875, 76),  # Dm7
    (2.25, 62), (2.25, 67), (2.25, 72), (2.25, 76),  # Dm7
    (2.625, 62), (2.625, 67), (2.625, 72), (2.625, 76),  # Dm7
    (3.0, 62), (3.0, 67), (3.0, 72), (3.0, 76),  # Dm7
    (3.375, 62), (3.375, 67), (3.375, 72), (3.375, 76),  # Dm7
    (3.75, 62), (3.75, 67), (3.75, 72), (3.75, 76),  # Dm7
    (4.125, 62), (4.125, 67), (4.125, 72), (4.125, 76),  # Dm7
    (4.5, 62), (4.5, 67), (4.5, 72), (4.5, 76),  # Dm7
    (4.875, 62), (4.875, 67), (4.875, 72), (4.875, 76),  # Dm7
    (5.25, 62), (5.25, 67), (5.25, 72), (5.25, 76),  # Dm7
    (5.625, 62), (5.625, 67), (5.625, 72), (5.625, 76),  # Dm7
    (6.0, 62), (6.0, 67), (6.0, 72), (6.0, 76),  # Dm7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 62), (1.875, 64),  # D - E - D - E
    (2.25, 62), (2.375, 64), (2.5, 62), (2.625, 64),  # D - E - D - E
    (3.0, 62), (3.125, 64), (3.25, 62), (3.375, 64),  # D - E - D - E
    (3.75, 62), (3.875, 64), (4.0, 62), (4.125, 64),  # D - E - D - E
    (4.5, 62), (4.625, 64), (4.75, 62), (4.875, 64),  # D - E - D - E
    (5.25, 62), (5.375, 64), (5.5, 62), (5.625, 64),  # D - E - D - E
    (6.0, 62), (6.125, 64), (6.25, 62), (6.375, 64),  # D - E - D - E
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
