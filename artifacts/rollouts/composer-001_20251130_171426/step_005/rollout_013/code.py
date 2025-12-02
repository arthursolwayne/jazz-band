
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
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
hihat_times = [bar1_start + i * 0.375 for i in range(8)]
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar_start = 1.5

# Marcus: Walking line, chromatic approaches, Fm7 chord tones: F, Ab, Bb, D
# Bar 2: F -> Gb -> Ab -> A
# Bar 3: Bb -> C -> Db -> D
# Bar 4: F -> Gb -> Ab -> A
bass_notes = [78, 77, 76, 77, 71, 72, 71, 72, 78, 77, 76, 77]
bass_times = [bar_start + i * 0.375 for i in range(12)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4 (F, A, Bb, D)
# Bar 3: F7 on 2 and 4
# Bar 4: F7 on 2 and 4
piano_notes = []
piano_times = []
for bar in range(2, 5):
    bar_time = bar_start + (bar - 2) * 1.5
    for beat in [1, 3]:  # 2 and 4
        time = bar_time + (beat - 1) * 0.75
        chords = [76, 81, 80, 79]
        for note in chords:
            piano_notes.append(note)
            piano_times.append(time)

for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_time = bar_start + (bar - 2) * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8
    kick_times = [bar_time + 0.0, bar_time + 0.75]
    snare_times = [bar_time + 0.375, bar_time + 1.125]
    hihat_times = [bar_time + i * 0.375 for i in range(8)]
    for note, time in zip(kick_notes, kick_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(snare_notes, snare_times):
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(hihat_notes, hihat_times):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, short motif, Fm7 -> Ab7 -> Bb7 -> D7
# F (76), Ab (78), Bb (80), D (79)
# Start on bar 2, beat 1
sax_notes = [76, 78, 80, 79]
sax_times = [bar_start + 0.0, bar_start + 0.375, bar_start + 0.75, bar_start + 1.125]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
