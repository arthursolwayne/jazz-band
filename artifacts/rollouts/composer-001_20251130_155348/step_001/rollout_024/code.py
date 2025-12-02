
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

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    (1.5, 46), (1.875, 47), (2.25, 45), (2.625, 44),
    # Bar 3
    (3.0, 43), (3.375, 42), (3.75, 41), (4.125, 40),
    # Bar 4
    (4.5, 39), (4.875, 38), (5.25, 37), (5.625, 36)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (1.875, 60), (1.875, 64), (1.875, 67), (1.875, 71),
    (2.625, 60), (2.625, 64), (2.625, 67), (2.625, 71),
    # Bar 3
    (3.375, 60), (3.375, 64), (3.375, 67), (3.375, 71),
    (4.125, 60), (4.125, 64), (4.125, 67), (4.125, 71),
    # Bar 4
    (4.875, 60), (4.875, 64), (4.875, 67), (4.875, 71),
    (5.625, 60), (5.625, 64), (5.625, 67), (5.625, 71)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue pattern
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

# Sax: Dante (motif, start at bar 2, leave it hanging)
sax_notes = [
    # Bar 2
    (1.5, 62), (1.625, 60), (1.75, 62), (1.875, 60),
    # Bar 3
    (2.25, 62), (2.375, 60), (2.5, 62), (2.625, 60),
    # Bar 4
    (3.0, 62), (3.125, 60), (3.25, 62), (3.375, 60),
    (3.75, 62), (3.875, 60), (4.0, 62), (4.125, 60),
    (4.5, 62), (4.625, 60)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
