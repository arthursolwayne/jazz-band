
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 60), (1.875, 61), (2.25, 62), (2.625, 64),
    # Bar 3
    (3.0, 65), (3.375, 67), (3.75, 69), (4.125, 71),
    # Bar 4
    (4.5, 72), (4.875, 71), (5.25, 69), (5.625, 67)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 60), (1.875, 64), (1.875, 67), (1.875, 71),
    (2.625, 60), (2.625, 64), (2.625, 67), (2.625, 71),
    # Bar 3
    (3.375, 62), (3.375, 66), (3.375, 69), (3.375, 73),
    (4.125, 62), (4.125, 66), (4.125, 69), (4.125, 73),
    # Bar 4
    (4.875, 60), (4.875, 64), (4.875, 67), (4.875, 71),
    (5.625, 60), (5.625, 64), (5.625, 67), (5.625, 71)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue same pattern
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

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C7 -> E7 -> G7 -> D7 -> C7
sax_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 62),
    (1.875, 60), (1.875, 64), (1.875, 67), (1.875, 62),
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
