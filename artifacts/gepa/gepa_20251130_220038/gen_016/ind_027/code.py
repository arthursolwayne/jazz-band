
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
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
snare_notes = [38, 38]
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
hihat_notes = [42] * 8
hihat_times = [bar1_start + 0.0, bar1_start + 0.1875, bar1_start + 0.375, bar1_start + 0.5625, bar1_start + 0.75, bar1_start + 0.9375, bar1_start + 1.125, bar1_start + 1.3125]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
# Fm7 -> Bb7 -> Eb7 -> Am7 -> Dm7 -> G7 -> Cm7 -> F7
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

bass_notes = [53, 52, 50, 48, 49, 47, 45, 43, 46, 44, 42, 40, 41, 39, 37, 35, 38, 36, 34, 32, 33, 31, 29, 27, 30, 28, 26, 24, 25, 23, 21, 19]
bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Fm7: F, Ab, Bb, Db (bar 2)
# Bb7: Bb, D, F, Ab (bar 3)
# Eb7: Eb, G, Bb, Db (bar 4)

chord_notes = [
    # Bar 2 (beat 2)
    [53, 56, 57, 59],  # Fm7
    # Bar 3 (beat 2)
    [57, 60, 53, 56],  # Bb7
    # Bar 4 (beat 2)
    [50, 55, 57, 59],  # Eb7
]
chord_times = [1.5 + 0.75, 1.5 + 2.25, 1.5 + 3.75]

for notes, time in zip(chord_notes, chord_times):
    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif starting on bar 2, with a short phrase that sings
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F, Gb, A, Bb (start), leave it hanging, return on bar 4

sax_notes = [53, 51, 56, 57, 56, 54, 53]
sax_times = [1.5 + 0.0, 1.5 + 0.1875, 1.5 + 0.375, 1.5 + 0.5625, 2.5 + 0.0, 2.5 + 0.1875, 2.5 + 0.375]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat every eighth

bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_notes = [36, 36]
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    snare_notes = [38, 38]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_notes = [42] * 8
    hihat_times = [bar_start + 0.0, bar_start + 0.1875, bar_start + 0.375, bar_start + 0.5625, bar_start + 0.75, bar_start + 0.9375, bar_start + 1.125, bar_start + 1.3125]

    for note, time in zip(kick_notes, kick_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(snare_notes, snare_times):
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(hihat_notes, hihat_times):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
