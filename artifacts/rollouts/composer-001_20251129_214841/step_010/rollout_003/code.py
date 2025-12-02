
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),  # C
    (1.875, 61), # Bb
    (2.25, 63),  # C#
    (2.625, 64), # D
    (3.0, 65),   # D#
    (3.375, 67), # E
    (3.75, 66),  # F
    (4.125, 64), # D
    (4.5, 62),   # C
    (4.875, 61), # Bb
    (5.25, 63),  # C#
    (5.625, 64)  # D
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 71),  # C7
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 71),  # C7
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 71),  # C7
    (3.75, 60), (3.75, 64), (3.75, 67), (3.75, 71),  # C7
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71),  # C7
    (5.25, 60), (5.25, 64), (5.25, 67), (5.25, 71)   # C7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65),  # E
    (1.75, 67),  # G
    (2.0, 65),  # E
    (2.25, 67),  # G
    (2.5, 69),  # A
    (2.75, 67),  # G
    (3.0, 65),  # E
    (3.25, 67),  # G
    (3.5, 69),  # A
    (3.75, 71),  # B
    (4.0, 69),  # A
    (4.25, 67),  # G
    (4.5, 65),  # E
    (4.75, 67),  # G
    (5.0, 69),  # A
    (5.25, 71),  # B
    (5.5, 69),  # A
    (5.75, 67),  # G
    (6.0, 65)   # E
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
