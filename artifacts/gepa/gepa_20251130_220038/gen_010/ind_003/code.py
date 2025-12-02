
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

# Bar 2 (1.5 - 3.0s): Full quartet
# Sax: Start motif - Fm7 (F, Ab, Bb, D) in 16th notes
# F, Ab, Bb, D
for note, time_offset in zip([59, 60, 62, 65], [0, 0.1875, 0.375, 0.5625]):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5 + time_offset, end=1.5 + time_offset + 0.125))

# Bass: Walking line in Fm
# F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [59, 60, 62, 63, 62, 63, 64, 65]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.125))

# Piano: F7 on beat 2, Ab7 on beat 4
# 2nd beat: F7 (F, A, C, Eb)
for note in [59, 62, 64, 65]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.5 + 0.75, end=1.5 + 0.75 + 0.125))

# 4th beat: Ab7 (Ab, C, Eb, G)
for note in [60, 64, 65, 67]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.5 + 1.5, end=1.5 + 1.5 + 0.125))

# Bar 3 (3.0 - 4.5s)
# Sax: Repeat first motif but start on Ab
for note, time_offset in zip([60, 62, 64, 67], [0, 0.1875, 0.375, 0.5625]):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0 + time_offset, end=3.0 + time_offset + 0.125))

# Bass: Continue walking line
# F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [59, 60, 62, 63, 62, 63, 64, 65]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.125))

# Piano: Cm7 on beat 2, Eb7 on beat 4
# 2nd beat: Cm7 (C, Eb, G, Bb)
for note in [60, 64, 67, 69]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.0 + 0.75, end=3.0 + 0.75 + 0.125))

# 4th beat: Eb7 (Eb, G, Bb, D)
for note in [64, 67, 69, 65]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.0 + 1.5, end=3.0 + 1.5 + 0.125))

# Bar 4 (4.5 - 6.0s)
# Sax: Finish the motif by resolving back to Fm
# F, Ab, Bb, D
for note, time_offset in zip([59, 60, 62, 65], [0, 0.1875, 0.375, 0.5625]):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5 + time_offset, end=4.5 + time_offset + 0.125))

# Bass: Continue walking line
# F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [59, 60, 62, 63, 62, 63, 64, 65]
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.125))

# Piano: F7 on beat 2, Fm7 on beat 4
# 2nd beat: F7 (F, A, C, Eb)
for note in [59, 62, 64, 65]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5 + 0.75, end=4.5 + 0.75 + 0.125))

# 4th beat: Fm7 (F, Ab, Bb, D)
for note in [59, 60, 62, 65]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5 + 1.5, end=4.5 + 1.5 + 0.125))

# Drums continue
for beat in [0, 1, 2, 3]:
    time = 4.5 + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
