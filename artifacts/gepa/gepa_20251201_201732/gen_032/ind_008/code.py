
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

# Bar 2: Full band enters
# Bass: walking line with roots and fifths
# F - C - G - D - A - E - Bb - F
bass_notes = [78, 71, 76, 72, 77, 73, 78, 71]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [78, 82, 77, 81]
for i, pitch in enumerate(piano_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: motif
# F - Bb - G - E
sax_notes = [78, 74, 77, 81]
for i, pitch in enumerate(sax_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 3: Piano: C7 (C, E, G, B)
piano_notes = [77, 81, 79, 83]
for i, pitch in enumerate(piano_notes):
    time = 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bass: walking line with roots and fifths
# C - G - D - A - E - Bb - F - C
bass_notes = [77, 72, 76, 77, 73, 78, 71, 77]
for i, pitch in enumerate(bass_notes):
    time = 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Sax: motif variation
# G - C - E - Bb
sax_notes = [77, 77, 81, 74]
for i, pitch in enumerate(sax_notes):
    time = 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 4: Piano: G7 (G, B, D, F)
piano_notes = [79, 83, 77, 78]
for i, pitch in enumerate(piano_notes):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Bass: walking line with roots and fifths
# G - D - A - E - Bb - F - C - G
bass_notes = [79, 74, 77, 73, 78, 71, 77, 79]
for i, pitch in enumerate(bass_notes):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Sax: motif finish
# F - Bb - G - E
sax_notes = [78, 74, 77, 81]
for i, pitch in enumerate(sax_notes):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
