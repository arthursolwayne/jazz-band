
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 72), (1.875, 71), (2.25, 74), (2.625, 72),
    # Bar 3
    (3.0, 71), (3.375, 72), (3.75, 74), (4.125, 72),
    # Bar 4
    (4.5, 71), (4.875, 72), (5.25, 74), (5.625, 72)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 65), (1.5, 69), (1.5, 72), (1.5, 76),  # F7
    (2.25, 65), (2.25, 69), (2.25, 72), (2.25, 76),
    # Bar 3
    (3.0, 65), (3.0, 69), (3.0, 72), (3.0, 76),
    (3.75, 65), (3.75, 69), (3.75, 72), (3.75, 76),
    # Bar 4
    (4.5, 65), (4.5, 69), (4.5, 72), (4.5, 76),
    (5.25, 65), (5.25, 69), (5.25, 72), (5.25, 76)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 motif: F, A, Bb, D
# Bar 2: F (start), A (end of bar 2)
note = pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=1.5 + 1.125, end=1.5 + 1.5)
sax.notes.append(note)

# Repeat motif with variation in Bar 4
note = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=4.5 + 0.375, end=4.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
