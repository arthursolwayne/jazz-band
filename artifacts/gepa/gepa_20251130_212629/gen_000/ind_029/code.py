
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

bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar1_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: short motif, start it, leave it hanging

bar2_start = 1.5
bar2_end = 3.0

# Bass line (walking, chromatic)
bass_notes = [37, 39, 40, 38, 37, 39, 40, 38]
for i, note in enumerate(bass_notes):
    start = bar2_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = []
chord1 = [60, 64, 67, 71]  # C7
chord2 = [62, 66, 69, 73]  # D7

for i, chord in enumerate([chord2, chord1]):
    start = bar2_start + i * 1.5 + 0.75
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.75)
        piano.notes.append(piano_note)

# Sax: short motif, start it, leave it hanging
sax_notes = [62, 64, 65]
for i, note in enumerate(sax_notes):
    start = bar2_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: continue motif, then resolve

bar3_start = 3.0
bar3_end = 4.5

# Bass line (walking, chromatic)
bass_notes = [37, 39, 40, 38, 37, 39, 40, 38]
for i, note in enumerate(bass_notes):
    start = bar3_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
chord1 = [60, 64, 67, 71]  # C7
chord2 = [62, 66, 69, 73]  # D7

for i, chord in enumerate([chord2, chord1]):
    start = bar3_start + i * 1.5 + 0.75
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.75)
        piano.notes.append(piano_note)

# Sax: continue motif, then resolve
sax_notes = [67, 65, 64, 62]
for i, note in enumerate(sax_notes):
    start = bar3_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: resolve motif and end

bar4_start = 4.5
bar4_end = 6.0

# Bass line (walking, chromatic)
bass_notes = [37, 39, 40, 38, 37, 39, 40, 38]
for i, note in enumerate(bass_notes):
    start = bar4_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
chord1 = [60, 64, 67, 71]  # C7
chord2 = [62, 66, 69, 73]  # D7

for i, chord in enumerate([chord2, chord1]):
    start = bar4_start + i * 1.5 + 0.75
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.75)
        piano.notes.append(piano_note)

# Sax: resolve motif and end
sax_notes = [62, 64, 65, 62]
for i, note in enumerate(sax_notes):
    start = bar4_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar4_kick_notes = [36, 36]
bar4_snare_notes = [38, 38]
bar4_hihat_notes = [42] * 8

for i, note in enumerate(bar4_kick_notes):
    start = bar4_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(bar4_snare_notes):
    start = bar4_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(bar4_hihat_notes):
    start = bar4_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
