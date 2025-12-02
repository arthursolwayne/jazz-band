
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 71, 70, 69]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chord1 = [60, 64, 67, 71]  # C7
chord2 = [60, 64, 67, 71]  # C7
for i, chord in enumerate([chord1, chord2]):
    start = 1.5 + (i + 1) * bar_length / 2
    end = start + 0.5
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, then finish it
motif = [62, 64, 65, 62, 60, 62, 64, 65]
for i, pitch in enumerate(motif):
    start = 1.5 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 59, 60, 61]
for i, pitch in enumerate(bass_notes):
    start = 3.0 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chord1 = [60, 64, 67, 71]  # C7
chord2 = [60, 64, 67, 71]  # C7
for i, chord in enumerate([chord1, chord2]):
    start = 3.0 + (i + 1) * bar_length / 2
    end = start + 0.5
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Sax: Motif continuation
motif = [65, 64, 62, 60, 62, 64, 65, 67]
for i, pitch in enumerate(motif):
    start = 3.0 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 71, 70, 69, 68]
for i, pitch in enumerate(bass_notes):
    start = 4.5 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chord1 = [60, 64, 67, 71]  # C7
chord2 = [60, 64, 67, 71]  # C7
for i, chord in enumerate([chord1, chord2]):
    start = 4.5 + (i + 1) * bar_length / 2
    end = start + 0.5
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Sax: Motif finish
motif = [67, 65, 64, 62, 60, 62, 64, 65]
for i, pitch in enumerate(motif):
    start = 4.5 + (i * bar_length / 4)
    end = start + 0.1
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 4.5 + (beat * bar_length / 4)
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
