
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

for i in range(2):
    kick_time = bar_1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in range(2):
    snare_time = bar_1_start + i * 0.75 + 0.1
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = bar_1_start + i * 0.125
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F (F2, G2, A2, Bb2, C3, D3, E3, F3)
bass_notes = [78, 80, 82, 83, 85, 87, 89, 91]
bass_durations = [0.25] * 8
bass_start = 1.5
for i in range(8):
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=bass_start + i * 0.25, end=bass_start + i * 0.25 + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E) -> F, A, C, E
# Bar 3: Dm7 (D, F, A, C) -> D, F, A, C
# Bar 4: G7 (G, B, D, F) -> G, B, D, F
# Comp on 2 and 4
bar_2_start = 1.5
bar_3_start = 2.25
bar_4_start = 3.0

# Bar 2: Fmaj7
for i, pitch in enumerate([78, 83, 85, 90]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_2_start + 0.5, end=bar_2_start + 0.5 + 0.25)
    piano.notes.append(note)

# Bar 3: Dm7
for i, pitch in enumerate([82, 85, 87, 90]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_3_start + 0.5, end=bar_3_start + 0.5 + 0.25)
    piano.notes.append(note)

# Bar 4: G7
for i, pitch in enumerate([87, 91, 89, 85]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_4_start + 0.5, end=bar_4_start + 0.5 + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, A, F (motif), then rest, then repeat
sax_notes = [78, 80, 82, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78]
sax_durations = [0.125] * 16
sax_start = 1.5

for i in range(4):
    note = pretty_midi.Note(velocity=115, pitch=sax_notes[i], start=sax_start + i * 0.125, end=sax_start + i * 0.125 + 0.125)
    sax.notes.append(note)

for i in range(4, 16):
    note = pretty_midi.Note(velocity=115, pitch=sax_notes[i], start=sax_start + i * 0.125, end=sax_start + i * 0.125 + 0.125)
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar_1_end + (bar - 2) * 1.5
    for i in range(2):
        kick_time = bar_start + i * 0.75
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick)

    for i in range(2):
        snare_time = bar_start + i * 0.75 + 0.1
        snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare)

    for i in range(8):
        hihat_time = bar_start + i * 0.125
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
