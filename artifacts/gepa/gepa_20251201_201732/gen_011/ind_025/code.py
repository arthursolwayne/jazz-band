
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

# Marcus: Walking line (Fm), roots and fifths with chromatic approaches
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        notes = [(24, 1.5), (26, 1.5), (24, 1.5), (22, 1.5)]  # F, Ab, F, D
    elif bar == 3:
        notes = [(26, 1.5), (24, 1.5), (26, 1.5), (25, 1.5)]  # Ab, F, Ab, Gb
    else:
        notes = [(22, 1.5), (24, 1.5), (22, 1.5), (20, 1.5)]  # D, F, D, C
    for i, (pitch, duration) in enumerate(notes):
        note_start = time + i * 0.375
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=note_start, end=note_start + duration)
        bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Fm7 (F, Ab, C, D)
        notes = [(24, 1.5), (26, 1.5), (28, 1.5), (29, 1.5)]
    elif bar == 3:
        # Bbm7 (Bb, Db, F, G)
        notes = [(23, 1.5), (25, 1.5), (28, 1.5), (29, 1.5)]
    else:
        # Eb7 (Eb, G, Bb, D)
        notes = [(22, 1.5), (27, 1.5), (25, 1.5), (29, 1.5)]
    for i, (pitch, duration) in enumerate(notes):
        note_start = time + i * 0.375
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + duration)
        piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    for beat in range(4):
        beat_time = time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=beat_time, end=beat_time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=beat_time, end=beat_time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=beat_time + eighth * 0.1875, end=beat_time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Gb, F (bar 2)
# Leave it hanging on Gb, then resolve back on the last beat of bar 4
motif = [24, 26, 25, 24]
for i, pitch in enumerate(motif):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)
# Gb in bar 3, no resolution yet
note = pretty_midi.Note(velocity=110, pitch=25, start=3.0, end=3.25)
sax.notes.append(note)
# Resolve back on F in bar 4
note = pretty_midi.Note(velocity=110, pitch=24, start=4.5, end=4.75)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
