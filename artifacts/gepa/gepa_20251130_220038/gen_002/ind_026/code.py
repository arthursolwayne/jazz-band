
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
# Bass line in F: F, G#, A, Bb, B, C#, D, Eb, E, F#, G, Ab, etc.
bass_notes = [78, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91]
for i in range(3):  # 3 bars
    for j in range(4):  # 4 beats per bar
        time = 1.5 + i * 1.5 + j * 0.375
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[(i * 4 + j) % len(bass_notes)], start=time, end=time + 0.25)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7, Bb7, C7, Eb7
chords = [ [78, 82, 87, 90], [82, 86, 91, 93], [78, 82, 87, 92], [82, 86, 91, 95] ]
for bar in range(3):  # Bars 2-4
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            for pitch in chords[bar]:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
                piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, E (F Eb Bb G)
motif = [78, 81, 82, 87]
for i, note in enumerate(motif):
    start_time = 1.5 + 0.375 * i
    end_time = start_time + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start_time, end=end_time)
    sax.notes.append(sax_note)

# Repeat the last note of the motif to hang
sax_note = pretty_midi.Note(velocity=110, pitch=motif[-1], start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
sax.notes.append(sax_note)

# Repeat the motif again at the end to complete it
for i, note in enumerate(motif):
    start_time = 1.5 + 3.0 + 0.375 * i
    end_time = start_time + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start_time, end=end_time)
    sax.notes.append(sax_note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):  # Bars 2-4
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
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

midi.write("wayne_intro.mid")
