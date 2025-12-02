
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
bar_1_start = 0.0
bar_1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8
kick_times = [bar_1_start + 0.0, bar_1_start + 0.75]
snare_times = [bar_1_start + 0.375, bar_1_start + 1.125]
hihat_times = [bar_1_start + i * 0.375 for i in range(8)]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5
bar_4_end = 6.0

bass_notes = [
    62, 63, 64, 63,  # Dm7 -> G7
    67, 68, 69, 67,  # G7 -> Cm7
    60, 61, 62, 61   # Cm7 -> Dm7 (resolve)
]
bass_times = [bar_2_start + i * 0.375 for i in range(12)]

for note, time in zip(bass_notes, bass_times):
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D - F - A - C)
    62, 64, 67, 69,
    # Bar 3: G7 (G - B - D - F)
    67, 71, 69, 64,
    # Bar 4: Cm7 (C - Eb - G - Bb)
    60, 63, 67, 68
]
piano_times = [
    bar_2_start + 0.75, bar_2_start + 1.125, bar_2_start + 1.5, bar_2_start + 1.875,
    bar_3_start + 0.75, bar_3_start + 1.125, bar_3_start + 1.5, bar_3_start + 1.875,
    bar_4_start + 0.75, bar_4_start + 1.125, bar_4_start + 1.5, bar_4_start + 1.875
]

for note, time in zip(piano_notes, piano_times):
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [67, 69, 71, 69, 71, 72, 71, 69]
sax_times = [bar_2_start + 0.0, bar_2_start + 0.375, bar_2_start + 0.75, bar_2_start + 1.125,
             bar_2_start + 2.0, bar_2_start + 2.375, bar_2_start + 2.75, bar_2_start + 3.125]

for note, time in zip(sax_notes, sax_times):
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
