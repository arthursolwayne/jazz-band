
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + 0.375 * i for i in range(8)]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line, chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: Motif, start and finish

bar2_start = 1.5
bar2_end = 3.0

# Bass line (Dm7 -> Gm7 -> Cm7 -> F7)
# Dm7: D F A C
# Gm7: G Bb D F
# Cm7: C Eb G Bb
# F7: F A C Eb

bass_notes = [50, 53, 55, 57, 58, 60, 62, 64]
bass_times = [bar2_start + 0.375 * i for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1))

# Piano chords on 2 and 4
# Dm7: D F A C
# Gm7: G Bb D F
# Cm7: C Eb G Bb
# F7: F A C Eb

chords = [
    (50, 53, 57, 60),  # Dm7
    (55, 58, 60, 64),  # Gm7
    (52, 55, 59, 62),  # Cm7
    (55, 58, 60, 64)   # F7
]
chord_times = [bar2_start + 0.75, bar2_start + 1.5, bar2_start + 2.25, bar2_start + 3.0]

for chord, time in zip(chords, chord_times):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Sax: Motif - Dm scale, start and finish
# Dm: D F G A Bb C
# Motif: D -> F -> G -> A -> Bb -> C -> D

motif = [50, 53, 55, 57, 58, 60, 50]
motif_times = [bar2_start + 0.375 * i for i in range(len(motif))]
for note, time in zip(motif, motif_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line, chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: Motif variation

bar3_start = 3.0
bar3_end = 4.5

# Bass line (Dm7 -> Gm7 -> Cm7 -> F7)
bass_notes = [50, 53, 55, 57, 58, 60, 62, 64]
bass_times = [bar3_start + 0.375 * i for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1))

# Piano chords on 2 and 4
chords = [
    (50, 53, 57, 60),  # Dm7
    (55, 58, 60, 64),  # Gm7
    (52, 55, 59, 62),  # Cm7
    (55, 58, 60, 64)   # F7
]
chord_times = [bar3_start + 0.75, bar3_start + 1.5, bar3_start + 2.25, bar3_start + 3.0]

for chord, time in zip(chords, chord_times):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Sax: Motif variation
# D -> F -> G -> A -> Bb -> C -> D -> F -> G -> A -> Bb -> C -> D

motif = [50, 53, 55, 57, 58, 60, 50, 53, 55, 57, 58, 60, 50]
motif_times = [bar3_start + 0.375 * i for i in range(len(motif))]
for note, time in zip(motif, motif_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line, chromatic approaches
# Piano: 7th chords on 2 and 4
# Sax: Motif variation

bar4_start = 4.5
bar4_end = 6.0

# Bass line (Dm7 -> Gm7 -> Cm7 -> F7)
bass_notes = [50, 53, 55, 57, 58, 60, 62, 64]
bass_times = [bar4_start + 0.375 * i for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1))

# Piano chords on 2 and 4
chords = [
    (50, 53, 57, 60),  # Dm7
    (55, 58, 60, 64),  # Gm7
    (52, 55, 59, 62),  # Cm7
    (55, 58, 60, 64)   # F7
]
chord_times = [bar4_start + 0.75, bar4_start + 1.5, bar4_start + 2.25, bar4_start + 3.0]

for chord, time in zip(chords, chord_times):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Sax: Motif variation
# D -> F -> G -> A -> Bb -> C -> D -> F -> G -> A -> Bb -> C -> D -> F -> G -> A -> Bb -> C -> D

motif = [50, 53, 55, 57, 58, 60, 50, 53, 55, 57, 58, 60, 50, 53, 55, 57, 58, 60, 50]
motif_times = [bar4_start + 0.375 * i for i in range(len(motif))]
for note, time in zip(motif, motif_times):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_start = 4.5
bar4_end = 6.0
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8
kick_times = [bar4_start + 0.375, bar4_start + 1.125]
snare_times = [bar4_start + 0.75, bar4_start + 1.5]
hihat_times = [bar4_start + 0.375 * i for i in range(8)]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
