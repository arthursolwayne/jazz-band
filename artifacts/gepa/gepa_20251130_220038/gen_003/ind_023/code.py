
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 48), (1.75, 50), (2.0, 52), (2.25, 53),
    (2.5, 55), (2.75, 57), (3.0, 59), (3.25, 60),
    (3.5, 62), (3.75, 64), (4.0, 65), (4.25, 67),
    (4.5, 69), (4.75, 71), (5.0, 72), (5.25, 74)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74),  # F7
    (2.0, 62), (2.0, 67), (2.0, 72), (2.0, 74),  # F7
    (2.5, 64), (2.5, 69), (2.5, 74), (2.5, 76),  # G7
    (3.0, 64), (3.0, 69), (3.0, 74), (3.0, 76),  # G7
    (3.5, 62), (3.5, 67), (3.5, 72), (3.5, 74),  # F7
    (4.0, 62), (4.0, 67), (4.0, 72), (4.0, 74),  # F7
    (4.5, 64), (4.5, 69), (4.5, 74), (4.5, 76),  # G7
    (5.0, 64), (5.0, 69), (5.0, 74), (5.0, 76)   # G7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.75, 66), (2.0, 62), (2.25, 64),  # motif
    (3.0, 66), (3.25, 62), (3.5, 64), (3.75, 66),  # return
    (4.0, 62), (4.25, 64), (4.5, 66), (4.75, 62)   # resolution
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
