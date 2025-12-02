
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
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [57, 59, 60, 62, 63, 62, 60, 59, 57, 55, 57, 59, 60, 62, 63, 62, 60, 59, 57]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (50, 0.0), (53, 0.0), (62, 0.0), (60, 0.0),
    # Bar 3: G7 (G, B, D, F)
    (67, 1.5), (71, 1.5), (62, 1.5), (53, 1.5),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0), (63, 3.0), (67, 3.0), (58, 3.0)
]
for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (D, Eb, F, G)
    (50, 1.5), (51, 1.5), (52, 1.5), (53, 1.5),
    # Bar 3: Continue the motif (Ab, G, F, Eb)
    (57, 3.0), (53, 3.0), (52, 3.0), (51, 3.0),
    # Bar 4: Resolve (D, F, A)
    (50, 4.5), (53, 4.5), (62, 4.5)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
