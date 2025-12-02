
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Everyone in
# Bass: walking line with chromatic approaches
# Dm7 = D F A C
bass_notes = [50, 51, 53, 52, 50, 49, 50, 52]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 1, F7 on beat 2
    (50, 1.5), (52, 1.5), (55, 1.5), (57, 1.5),
    (53, 2.0), (55, 2.0), (58, 2.0), (60, 2.0),
    # Bar 3: Gm7 on beat 1, Bb7 on beat 2
    (57, 3.0), (59, 3.0), (62, 3.0), (64, 3.0),
    (60, 3.5), (62, 3.5), (65, 3.5), (67, 3.5),
    # Bar 4: Cm7 on beat 1, Eb7 on beat 2
    (57, 4.5), (59, 4.5), (62, 4.5), (64, 4.5),
    (60, 5.0), (62, 5.0), (65, 5.0), (67, 5.0)
]
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: same pattern as bar 1
for bar in range(2, 4):
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

# Sax: motif in Dm
# Dm = D F A C
# Motif: D - F - A - D (descending triplet with a lift on the last note)
sax_notes = [
    (50, 1.5), (52, 1.6667), (55, 1.8333), (50, 2.0)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.1667)
    sax.notes.append(note)

# Final line: Dm7 chord to wrap it up
sax_notes = [
    (50, 4.5), (52, 4.5), (55, 4.5), (57, 4.5)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
