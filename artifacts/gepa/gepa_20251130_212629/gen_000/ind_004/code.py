
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0
# Bass line: walking, chromatic approaches
bass_notes = [37, 39, 41, 42, 43, 41, 39, 40]
bass_times = [bar2_start + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))
# Piano: 7th chords on 2 and 4 (F7, A7, D7, G7)
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    71, 74, 76, 79,
    # Bar 3: A7 (A, C#, E, G#)
    77, 80, 83, 86,
    # Bar 4: D7 (D, F#, A, C#)
    74, 77, 80, 83,
    # Bar 4: G7 (G, B, D, F#)
    78, 81, 84, 87
]
piano_times = [bar2_start + 0.75, bar2_start + 0.75, bar2_start + 0.75, bar2_start + 0.75,
               bar2_start + 1.5, bar2_start + 1.5, bar2_start + 1.5, bar2_start + 1.5,
               bar2_start + 2.25, bar2_start + 2.25, bar2_start + 2.25, bar2_start + 2.25,
               bar2_start + 3.0, bar2_start + 3.0, bar2_start + 3.0, bar2_start + 3.0]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
# Sax: melody - F, G#, Bb, C, E, D, C, F
sax_notes = [71, 73, 76, 77, 80, 78, 77, 71]
sax_times = [bar2_start + i * 0.375 for i in range(8)]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5
# Bass line: walking, chromatic approaches
bass_notes = [37, 39, 41, 42, 43, 41, 39, 40]
bass_times = [bar3_start + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))
# Piano: 7th chords on 2 and 4 (A7, D7)
piano_notes = [
    # Bar 3: A7 (A, C#, E, G#)
    77, 80, 83, 86,
    # Bar 4: D7 (D, F#, A, C#)
    74, 77, 80, 83
]
piano_times = [bar3_start + 0.75, bar3_start + 0.75, bar3_start + 0.75, bar3_start + 0.75,
               bar3_start + 1.5, bar3_start + 1.5, bar3_start + 1.5, bar3_start + 1.5]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
# Sax: melody continuation - F, G#, Bb, C, E, D, C, F
sax_notes = [71, 73, 76, 77, 80, 78, 77, 71]
sax_times = [bar3_start + i * 0.375 for i in range(8)]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0
# Bass line: walking, chromatic approaches
bass_notes = [37, 39, 41, 42, 43, 41, 39, 40]
bass_times = [bar4_start + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))
# Piano: 7th chords on 2 and 4 (G7, F7)
piano_notes = [
    # Bar 4: G7 (G, B, D, F#)
    78, 81, 84, 87,
    # Bar 4: F7 (F, A, C, E)
    71, 74, 76, 79
]
piano_times = [bar4_start + 0.75, bar4_start + 0.75, bar4_start + 0.75, bar4_start + 0.75,
               bar4_start + 1.5, bar4_start + 1.5, bar4_start + 1.5, bar4_start + 1.5]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
# Sax: melody finish - F, G#, Bb, C, E, D, C, F
sax_notes = [71, 73, 76, 77, 80, 78, 77, 71]
sax_times = [bar4_start + i * 0.375 for i in range(8)]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Drums: Bar 3 and 4 (3.0 - 6.0s)
bar3_4_start = 3.0
bar3_4_end = 6.0
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8
kick_times = [bar3_4_start + 0.0, bar3_4_start + 0.75, bar3_4_start + 1.5, bar3_4_start + 2.25, bar3_4_start + 3.0]
snare_times = [bar3_4_start + 0.375, bar3_4_start + 1.125, bar3_4_start + 1.875, bar3_4_start + 2.625]
hihat_times = [bar3_4_start + i * 0.375 for i in range(8)]
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
