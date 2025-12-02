
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
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [0.0, 0.75]
snare_times = [0.375, 1.125]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: short motif, make it sing
# Dm7 - G7 - Cm7 - F7 (in D minor key)
# Melody: D - F - G - Bb

sax_notes = [62, 65, 67, 69]
sax_times = [1.5, 1.75, 2.0, 2.25]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [62, 63, 64, 67, 69, 71, 72, 71]
bass_times = [1.5, 1.625, 1.75, 1.875, 2.0, 2.125, 2.25, 2.375]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [62, 67, 72, 74, 67, 72, 76, 79]
piano_times = [1.5, 1.625, 1.75, 1.875, 2.0, 2.125, 2.25, 2.375]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: same pattern
kick_times = [1.5, 2.25]
snare_times = [1.875, 2.625]
hihat_times = [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat motif, but with variation
sax_notes = [62, 65, 67, 69]
sax_times = [3.0, 3.25, 3.5, 3.75]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [62, 63, 64, 67, 69, 71, 72, 71]
bass_times = [3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [62, 67, 72, 74, 67, 72, 76, 79]
piano_times = [3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: same pattern
kick_times = [3.0, 3.75]
snare_times = [3.375, 4.125]
hihat_times = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: resolve the motif
sax_notes = [62, 65, 67, 62]
sax_times = [4.5, 4.75, 5.0, 5.25]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line, chromatic approaches
bass_notes = [62, 63, 64, 67, 69, 71, 72, 71]
bass_times = [4.5, 4.625, 4.75, 4.875, 5.0, 5.125, 5.25, 5.375]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [62, 67, 72, 74, 67, 72, 76, 79]
piano_times = [4.5, 4.625, 4.75, 4.875, 5.0, 5.125, 5.25, 5.375]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: same pattern
kick_times = [4.5, 5.25]
snare_times = [4.875, 5.625]
hihat_times = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
