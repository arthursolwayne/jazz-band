
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [36, 37, 38, 39, 37, 36, 35, 34, 36, 37, 38, 39, 37, 36, 35, 34]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i % 4) * 0.375
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Ebm7 = Eb, Gb, Bb, Db
# Abm7 = Ab, B, Eb, Gb
piano_notes = [
    # Bar 2
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 64),  # Fm7
    # Bar 3
    (2.0, 64), (2.0, 67), (2.0, 69), (2.0, 71),  # Bbm7
    # Bar 4
    (2.5, 64), (2.5, 67), (2.5, 69), (2.5, 71),  # Bbm7 again
    # Voicing on 2 and 4
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 64),
    (3.5, 62), (3.5, 67), (3.5, 69), (3.5, 64)
]
for time, pitch in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, sing, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, Eb (Fm7 arpeggio)
sax_notes = [
    (1.5, 62), (1.5 + 0.1875, 67), (1.5 + 0.375, 67), (1.5 + 0.5625, 64),  # First phrase
    (2.0, 62), (2.0 + 0.1875, 67), (2.0 + 0.375, 67), (2.0 + 0.5625, 64),  # Repeat
    (3.0, 62), (3.0 + 0.1875, 67), (3.0 + 0.375, 67), (3.0 + 0.5625, 64),  # Repeat again
    (4.0, 62), (4.0 + 0.1875, 67), (4.0 + 0.375, 67), (4.0 + 0.5625, 64),  # Finish it
]
for time, pitch in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
