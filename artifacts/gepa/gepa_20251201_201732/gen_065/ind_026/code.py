
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
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F2, G2, D2, C2, E2, D2, C2, Bb2)
bar2_start = 1.5
bass_notes = [70, 71, 67, 68, 71, 67, 68, 70]
bass_times = [bar2_start + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar, resolve on the last
def add_piano_notes(chord, time):
    for note in chord:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note_obj)

bar2_chords = [64, 68, 67, 69]  # Fm7
bar3_chords = [65, 69, 68, 71]  # Gm7
bar4_chords = [67, 71, 70, 72]  # Am7
bar2_time = bar2_start
bar3_time = bar2_start + 1.5
bar4_time = bar2_start + 3.0

add_piano_notes(bar2_chords, bar2_time)
add_piano_notes(bar3_chords, bar3_time)
add_piano_notes(bar4_chords, bar4_time)

# Dante: Saxophone motif (F, Ab, Bb, F)
sax_notes = [65, 67, 68, 65]
sax_times = [bar2_start, bar2_start + 0.5, bar2_start + 1.0, bar2_start + 1.5]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Little Ray: Full kit on bars 2-4
bar2_4_start = bar2_start
bar2_4_end = 6.0

kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 16
kick_times = [bar2_4_start + i * 1.5 for i in range(4)]
snare_times = [bar2_4_start + i * 1.5 + 0.75 for i in range(4)]
hihat_times = [bar2_4_start + i * 0.375 for i in range(16)]

for note, time in zip(kick_notes, kick_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
