
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]

kick_times = [0.0, 0.75, 1.5, 2.25]
snare_times = [0.375, 1.125, 1.875, 2.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif

sax_notes = [62, 64, 65, 67]
sax_times = [1.5, 1.75, 2.0, 2.25]
for note, time in zip(sax_notes, sax_times):
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking line in C)
bass_notes = [60, 62, 63, 64, 65, 67, 68, 69]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25]
for note, time in zip(bass_notes, bass_times):
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords (7th chords on 2 and 4)
piano_notes = [60, 64, 67, 71, 60, 64, 67, 71]
piano_times = [1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25]
for note, time in zip(piano_notes, piano_times):
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif again

sax_notes = [62, 64, 65, 67]
sax_times = [3.0, 3.25, 3.5, 3.75]
for note, time in zip(sax_notes, sax_times):
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking line in C)
bass_notes = [60, 62, 63, 64, 65, 67, 68, 69]
bass_times = [3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
for note, time in zip(bass_notes, bass_times):
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords (7th chords on 2 and 4)
piano_notes = [60, 64, 67, 71, 60, 64, 67, 71]
piano_times = [3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25, 6.75]
for note, time in zip(piano_notes, piano_times):
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif again with resolution

sax_notes = [62, 64, 65, 67, 69]
sax_times = [4.5, 4.75, 5.0, 5.25, 5.5]
for note, time in zip(sax_notes, sax_times):
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking line in C)
bass_notes = [60, 62, 63, 64, 65, 67, 68, 69]
bass_times = [4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
for note, time in zip(bass_notes, bass_times):
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano chords (7th chords on 2 and 4)
piano_notes = [60, 64, 67, 71, 60, 64, 67, 71]
piano_times = [4.75, 5.25, 5.75, 6.25, 6.75, 7.25, 7.75, 8.25]
for note, time in zip(piano_notes, piano_times):
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums continue with same pattern for bars 2-4
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]

kick_times = [1.5, 2.25, 3.0, 3.75]
snare_times = [1.875, 2.625, 3.375, 4.125]
hihat_times = [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

kick_times = [3.0, 3.75, 4.5, 5.25]
snare_times = [3.375, 4.125, 4.875, 5.625]
hihat_times = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

kick_times = [4.5, 5.25, 6.0, 6.75]
snare_times = [4.875, 5.625, 6.375, 7.125]
hihat_times = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro.mid')
