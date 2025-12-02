
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 60), (2.25, 61),
    (2.5, 62), (2.75, 63), (3.0, 60), (3.25, 61),
    (3.5, 62), (3.75, 63), (4.0, 60), (4.25, 61),
    (4.5, 62), (4.75, 63), (5.0, 60), (5.25, 61)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 71), (1.5, 76),  # D7
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 76),  # D7
    (2.5, 67), (2.5, 71), (2.5, 76), (2.5, 80),  # G7
    (3.0, 67), (3.0, 71), (3.0, 76), (3.0, 80),  # G7
    (3.5, 64), (3.5, 67), (3.5, 71), (3.5, 76),  # D7
    (4.0, 64), (4.0, 67), (4.0, 71), (4.0, 76),  # D7
    (4.5, 67), (4.5, 71), (4.5, 76), (4.5, 80),  # G7
    (5.0, 67), (5.0, 71), (5.0, 76), (5.0, 80)   # G7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (66), G (67), D (62)
sax_notes = [
    (1.5, 62), (1.5 + 0.125, 66), (1.5 + 0.25, 67), (1.5 + 0.375, 62),
    (2.75, 62), (2.75 + 0.125, 66), (2.75 + 0.25, 67), (2.75 + 0.375, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue in bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
