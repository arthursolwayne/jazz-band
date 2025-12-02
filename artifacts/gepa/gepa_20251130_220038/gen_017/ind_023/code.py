
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

for i in range(2):
    kick_time = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in range(2):
    snare_time = bar1_start + i * 0.75 + 0.25
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = bar1_start + i * 0.125
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5
bar_end = 6.0

# Bass line in Fm: F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [71, 70, 68, 69, 67, 68, 69, 70]
for i in range(8):
    time = bar2_start + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Bbm7 = Bb, Db, F, Ab
# E7 = E, G#, B, D
# Am7 = A, C, E, G
piano_notes = []
# Bar 2: Fm7 on beat 2, Bbm7 on beat 4
piano_notes.extend([76, 79, 71, 73])  # Fm7
piano_notes.extend([71, 74, 76, 79])  # Bbm7
# Bar 3: E7 on beat 2, Am7 on beat 4
piano_notes.extend([77, 80, 72, 75])  # E7
piano_notes.extend([72, 75, 77, 79])  # Am7
# Bar 4: Fm7 on beat 2, Bbm7 on beat 4
piano_notes.extend([76, 79, 71, 73])  # Fm7
piano_notes.extend([71, 74, 76, 79])  # Bbm7

for i, pitch in enumerate(piano_notes):
    time = bar2_start + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C
# Bar 2: F, Ab (start)
# Bar 3: Bb (hang)
# Bar 4: C (resolve)

sax_notes = [
    # Bar 2
    (76, bar2_start, bar2_start + 0.25),
    (79, bar2_start + 0.25, bar2_start + 0.5),
    # Bar 3
    (71, bar3_start + 0.5, bar3_start + 0.75),
    # Bar 4
    (73, bar4_start + 0.5, bar4_start + 0.75)
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [bar2_start, bar3_start, bar4_start]:
    for i in range(2):
        kick_time = bar_start + i * 0.75
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick)

    for i in range(2):
        snare_time = bar_start + i * 0.75 + 0.25
        snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare)

    for i in range(8):
        hihat_time = bar_start + i * 0.125
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
