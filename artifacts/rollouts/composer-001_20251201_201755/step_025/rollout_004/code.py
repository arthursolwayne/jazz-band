
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
bar_duration = 1.5
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [0.0, 0.75]
# Snare on 2 and 4
snare_times = [0.375, 1.125]
# Hihat on every eighth
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5]

for note, time in zip(kick_notes * len(kick_times), kick_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note)

for note, time in zip(snare_notes * len(snare_times), snare_times):
    note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note)

for note, time in zip(hihat_notes * len(hihat_times), hihat_times):
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [38, 40, 41, 43, 41, 40, 38, 37]
bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]
for pitch, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [62, 65, 67, 70]
piano_times = [1.5]
for pitch, time in zip(piano_notes, piano_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: motif - start it, leave it hanging
sax_notes = [64, 67, 69]
sax_times = [1.5, 1.75, 2.0]
for pitch, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [37, 38, 40, 43, 41, 40, 38, 37]
bass_times = [3.0 + i * 0.375 for i in range(len(bass_notes))]
for pitch, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A C E G)
piano_notes = [69, 72, 74, 77]
piano_times = [3.0]
for pitch, time in zip(piano_notes, piano_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: motif - continue and resolve
sax_notes = [71, 74, 76]
sax_times = [3.0, 3.25, 3.5]
for pitch, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [37, 38, 40, 43, 41, 40, 38, 37]
bass_times = [4.5 + i * 0.375 for i in range(len(bass_notes))]
for pitch, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
piano_notes = [71, 74, 76, 70]
piano_times = [4.5]
for pitch, time in zip(piano_notes, piano_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: motif - finish it
sax_notes = [76, 74, 71]
sax_times = [4.5, 4.75, 5.0]
for pitch, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: same pattern
for note, time in zip(kick_notes * len(kick_times), [4.5, 5.25]):
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

for note, time in zip(snare_notes * len(snare_times), [4.875, 5.625]):
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

for note, time in zip(hihat_notes * len(hihat_times), [4.5, 4.875, 5.25, 5.625, 6.0]):
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
