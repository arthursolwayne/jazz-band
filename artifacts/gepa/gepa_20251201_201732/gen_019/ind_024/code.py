
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
    time = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar1_start + i * 0.75
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    38, 41, 43, 42,  # Bar 2
    43, 45, 47, 46,  # Bar 3
    46, 48, 50, 49   # Bar 4
]
bass_durations = [0.375] * 12
bass_times = [1.5 + i * 0.375 for i in range(12)]

for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=bass_times[i], end=bass_times[i] + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: C#m7 (C# E G B)
piano_notes = [
    # Bar 2: D7
    50, 53, 55, 57,  # D, F#, A, C#
    # Bar 3: Gm7
    55, 57, 59, 61,  # G, Bb, D, F
    # Bar 4: C#m7
    58, 61, 64, 66   # C#, E, G, B
]
piano_durations = [0.375] * 4 + [0.375] * 4 + [0.375] * 4
piano_times = [1.5 + i * 0.375 for i in range(12)]

for i, note in enumerate(piano_notes):
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=piano_times[i], end=piano_times[i] + piano_durations[i])
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (F#), E (F#), F# (G), D (F#)
sax_notes = [50, 51, 52, 50]
sax_durations = [0.375, 0.375, 0.375, 0.375]
sax_times = [1.5, 1.875, 2.25, 2.625]

for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=sax_times[i], end=sax_times[i] + sax_durations[i])
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    time = bar2_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar2_start + i * 0.75
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar2_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

# Bar 3
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    time = bar3_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar3_start + i * 0.75
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar3_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

# Bar 4
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    time = bar4_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar4_start + i * 0.75
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar4_start + i * 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
