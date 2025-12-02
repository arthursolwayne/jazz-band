
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 85, 86, 88]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        pitch = bass_notes[(bar - 2) * 4 + beat]
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    (64, 0.0), (67, 0.0), (70, 0.0), (72, 0.0),
    # Bar 2: Comp on beat 2
    (67, 0.75),
    # Bar 3: G7 (G B D F)
    (67, 1.5), (71, 1.5), (70, 1.5), (69, 1.5),
    # Bar 3: Comp on beat 2
    (71, 2.25),
    # Bar 4: C7 (C E G B)
    (60, 3.0), (64, 3.0), (67, 3.0), (71, 3.0),
    # Bar 4: Comp on beat 2
    (64, 3.75)
]
for pitch, offset in piano_notes:
    time = 1.5 + offset
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - B - D (D F# B D)
sax_notes = [
    (64, 1.5, 0.25),  # D
    (67, 1.75, 0.25),  # F#
    (70, 2.0, 0.25),   # B
    (64, 2.5, 0.25),   # D (leave it hanging)
    (67, 2.75, 0.25),  # F#
    (70, 3.0, 0.25),   # B
    (64, 3.5, 0.25)    # D (finish it)
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: continue for bars 2-4
for bar in range(2, 5):
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
