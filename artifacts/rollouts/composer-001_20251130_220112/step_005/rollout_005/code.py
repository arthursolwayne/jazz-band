
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
hihat_times = [bar1_start + i * 0.375 for i in range(8)]

for note, time in zip(kick_notes, kick_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)
for note, time in zip(snare_notes, snare_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)
for note, time in zip(hihat_notes, hihat_times):
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Fm7 chord (F, Ab, C, Eb)
bass_notes = [65, 64, 63, 66, 68, 67, 69, 71]
bass_times = [1.5 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4, Fm7 (F, Ab, C, Eb)
piano_notes = [
    65, 76, 72, 69,  # Fm7 on beat 2
    65, 76, 72, 69   # Fm7 on beat 4
]
piano_times = [
    1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125, 1.5 + 1.5,
    1.5 + 2.375, 1.5 + 2.75, 1.5 + 3.125, 1.5 + 3.5
]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# The motif is F - Ab - C - Eb - F
sax_notes = [65, 68, 72, 69, 65]
sax_times = [1.5, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125, 1.5 + 1.5]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
