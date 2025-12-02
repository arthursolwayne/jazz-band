
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
bar_duration = 1.5
for bar in range(1):
    time = bar * bar_duration
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.375, end=time + 0.75)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.75, end=time + 1.125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.append(hihat)

# Bars 2-4 (1.5 - 6.0s)
# Start with saxophone motif

# Dm7 chord: D, F, A, C
# Sax motif: D, F, G, D (melodic gesture)
note_lengths = [0.5, 0.5, 0.5, 0.5]
time = 1.5
for i, note in enumerate([62, 65, 67, 62]):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + i * 0.5, end=time + (i + 1) * 0.5))

# Marcus - walking bass line in Dm
# Dm scale: D, Eb, F, G, A, Bb, C
# Chromatic line: D, Eb, D#, F, E, F#, G, A, Ab, Bb, A#, C, B, C#, D
bass_notes = [62, 63, 64, 65, 67, 68, 71, 67, 66, 69, 70, 68, 70, 71, 62]
bass_time = 1.5
for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=bass_time + i * 0.375, end=bass_time + (i + 1) * 0.375))

# Diane - 7th chords on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, E
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # 2nd beat: Dm7
    (62, 65, 67, 69, 1.5 + 0.375, 1.5 + 0.75),
    # 4th beat: G7
    (67, 71, 62, 69, 1.5 + 1.125, 1.5 + 1.5),
    # Bar 3 (3.0 - 4.5s)
    # 2nd beat: Cm7
    (60, 63, 67, 71, 3.0 + 0.375, 3.0 + 0.75),
    # 4th beat: F7
    (65, 69, 60, 72, 3.0 + 1.125, 3.0 + 1.5),
    # Bar 4 (4.5 - 6.0s)
    # 2nd beat: Dm7
    (62, 65, 67, 69, 4.5 + 0.375, 4.5 + 0.75),
    # 4th beat: G7
    (67, 71, 62, 69, 4.5 + 1.125, 4.5 + 1.5)
]
for note_info in piano_notes:
    for pitch in note_info[0:4]:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=note_info[4], end=note_info[5]))

# Little Ray - same pattern as bar 1
for bar in range(2, 4):
    time = bar * bar_duration
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.375, end=time + 0.75)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.75, end=time + 1.125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
