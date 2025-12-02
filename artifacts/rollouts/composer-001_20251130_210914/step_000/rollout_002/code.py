
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
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + i * 0.375 for i in range(8)]

for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, F7 chord in F
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

bass_notes = [
    # Bar 2: F -> G -> G# -> A
    (45, bar2_start + 0.0, 0.375),
    (47, bar2_start + 0.375, 0.375),
    (48, bar2_start + 0.75, 0.375),
    (49, bar2_start + 1.125, 0.375),
    # Bar 3: A -> Bb -> B -> C
    (50, bar3_start + 0.0, 0.375),
    (51, bar3_start + 0.375, 0.375),
    (52, bar3_start + 0.75, 0.375),
    (53, bar3_start + 1.125, 0.375),
    # Bar 4: C -> C# -> D -> D#
    (54, bar4_start + 0.0, 0.375),
    (55, bar4_start + 0.375, 0.375),
    (56, bar4_start + 0.75, 0.375),
    (57, bar4_start + 1.125, 0.375),
]
for pitch, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (50, bar2_start + 0.75, 0.375),  # F
    (53, bar2_start + 0.75, 0.375),  # A
    (55, bar2_start + 0.75, 0.375),  # C
    (57, bar2_start + 0.75, 0.375),  # D#
    # Bar 3: F7 on beat 2
    (50, bar3_start + 0.75, 0.375),
    (53, bar3_start + 0.75, 0.375),
    (55, bar3_start + 0.75, 0.375),
    (57, bar3_start + 0.75, 0.375),
    # Bar 4: F7 on beat 2
    (50, bar4_start + 0.75, 0.375),
    (53, bar4_start + 0.75, 0.375),
    (55, bar4_start + 0.75, 0.375),
    (57, bar4_start + 0.75, 0.375),
]
for pitch, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start):
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8
    kick_times = [start + 0.375, start + 1.125]
    snare_times = [start + 0.75, start + 1.5]
    hihat_times = [start + i * 0.375 for i in range(8)]

    for note, time in zip(kick_notes, kick_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(snare_notes, snare_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))
    for note, time in zip(hihat_notes, hihat_times):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

add_drums(bar2_start)
add_drums(bar3_start)
add_drums(bar4_start)

# Sax: Melody, one short motif, make it sing. Start it, leave it hanging, finish it.
# F, A, Bb, D, A, Bb, F
sax_notes = [
    (50, bar2_start + 0.0, 0.375),  # F
    (53, bar2_start + 0.375, 0.375), # A
    (52, bar2_start + 0.75, 0.375),  # Bb
    (55, bar2_start + 1.125, 0.375), # D
    (53, bar3_start + 0.375, 0.375), # A
    (52, bar3_start + 0.75, 0.375),  # Bb
    (50, bar4_start + 1.125, 0.375)  # F
]
for pitch, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
