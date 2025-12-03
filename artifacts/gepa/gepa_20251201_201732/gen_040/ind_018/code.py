
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
    snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [43, 42, 43, 45, 45, 43, 42, 43]
bass_durations = [0.375] * 8
for i, note in enumerate(bass_notes):
    start = bar2_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [62, 64, 67, 69]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar2_start, end=bar2_end)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [62, 64, 62]
sax_durations = [0.375, 0.375, 0.375]
for i, note in enumerate(sax_notes):
    start = bar2_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + sax_durations[i])
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [43, 42, 43, 45, 45, 43, 42, 43]
for i, note in enumerate(bass_notes):
    start = bar3_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: G7 (B, D, G, B)
piano_notes = [69, 71, 74, 76]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar3_start, end=bar3_end)
    piano.notes.append(piano_note)

# Sax: Continue motif, leave it hanging
sax_notes = [64, 62]
sax_durations = [0.375, 0.375]
for i, note in enumerate(sax_notes):
    start = bar3_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + sax_durations[i])
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [43, 42, 43, 45, 45, 43, 42, 43]
for i, note in enumerate(bass_notes):
    start = bar4_start + i * 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: Cm7 (E, G, C, E)
piano_notes = [64, 67, 72, 74]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar4_start, end=bar4_end)
    piano.notes.append(piano_note)

# Sax: Finish the motif
sax_notes = [62]
sax_durations = [0.375]
for i, note in enumerate(sax_notes):
    start = bar4_start + i * 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + sax_durations[i])
    sax.notes.append(sax_note)

# Drums in Bar 2-4
for bar_start in [1.5, 3.0, 4.5]:
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        start = bar_start + i * 0.75
        kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        start = bar_start + i * 0.75 + 0.1875
        snare = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        start = bar_start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
