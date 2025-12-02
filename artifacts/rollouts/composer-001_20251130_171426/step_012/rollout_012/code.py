
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if bar == 2:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=48, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=49, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=50, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=51, start=time, end=time + 0.125)
                bass.notes.append(note)
        elif bar == 3:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=51, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=52, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=54, start=time, end=time + 0.125)
                bass.notes.append(note)
        elif bar == 4:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=54, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=52, start=time, end=time + 0.125)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=51, start=time, end=time + 0.125)
                bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            if bar == 2:
                # F7 (F, A, C, E)
                for pitch in [71, 74, 76, 79]:
                    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                    piano.notes.append(note)
            elif bar == 3:
                # Bb7 (Bb, D, F, Ab)
                for pitch in [70, 73, 76, 78]:
                    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                    piano.notes.append(note)
            elif bar == 4:
                # F7 again
                for pitch in [71, 74, 76, 79]:
                    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                    piano.notes.append(note)

# Drums continue for bars 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - G - A - F (F6, G6, A6, F6)
# Play first 2 notes, leave it hanging, then play the last 2 on the next bar
for beat in range(2):
    time = 1.5 + beat * 0.375
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.125)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=72, start=time, end=time + 0.125)
        sax.notes.append(note)

for beat in range(2, 4):
    time = 3.0 + beat * 0.375
    if beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.125)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=72, start=time, end=time + 0.125)
        sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo_intro.mid')
