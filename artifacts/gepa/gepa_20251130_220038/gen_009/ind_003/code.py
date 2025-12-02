
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on beat 1 and 3
kick_notes = [36, 36]
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on beat 2 and 4
snare_notes = [38, 38]
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth
hihat_notes = [42] * 8
hihat_times = [bar1_start + i * 0.375 for i in range(8)]
for note, time in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)

# Marcus: Walking bass line in Dm
# Dm: D, F, A, C
# Walking line with chromatic approaches

bass_notes = [50, 49, 50, 52, 53, 52, 50, 48]
bass_times = [1.5 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Comp on beat 2 and 4

piano_notes = [50, 50, 55, 50, 50, 60, 50, 50]
piano_times = [1.5 + i * 0.375 for i in range(8)]
for note, time in zip(piano_notes, piano_times):
    if time == 1.5 + 0.75 or time == 1.5 + 1.5 or time == 1.5 + 2.25 or time == 1.5 + 3.0:
        piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(piano_note)

# Dante: Melody in Dm
# Motif: D - F - A - C (4th interval, then 3rd)
# Start it, leave it hanging, come back and finish it

sax_notes = [50, 52, 55, 57]
sax_times = [1.5 + i * 0.375 for i in range(4)]
for note, time in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Bar 3 (3.0 - 4.5s)

# Marcus: Walking bass line in Dm
bass_notes = [50, 49, 50, 52, 53, 52, 50, 48]
bass_times = [3.0 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4

piano_notes = [50, 50, 55, 50, 50, 60, 50, 50]
piano_times = [3.0 + i * 0.375 for i in range(8)]
for note, time in zip(piano_notes, piano_times):
    if time == 3.0 + 0.75 or time == 3.0 + 1.5 or time == 3.0 + 2.25 or time == 3.0 + 3.0:
        piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(piano_note)

# Dante: Motif resolution, repeat or variation

sax_notes = [57, 55, 52, 50]
sax_times = [3.0 + i * 0.375 for i in range(4)]
for note, time in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Bar 4 (4.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [50, 49, 50, 52, 53, 52, 50, 48]
bass_times = [4.5 + i * 0.375 for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4

piano_notes = [50, 50, 55, 50, 50, 60, 50, 50]
piano_times = [4.5 + i * 0.375 for i in range(8)]
for note, time in zip(piano_notes, piano_times):
    if time == 4.5 + 0.75 or time == 4.5 + 1.5 or time == 4.5 + 2.25 or time == 4.5 + 3.0:
        piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(piano_note)

# Dante: Motif variation or resolution

sax_notes = [50, 52, 55, 57]
sax_times = [4.5 + i * 0.375 for i in range(4)]
for note, time in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar2_start = 1.5
bar2_end = 3.0

# Kick on beat 1 and 3
kick_notes = [36, 36]
kick_times = [bar2_start + 0.0, bar2_start + 0.75]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on beat 2 and 4
snare_notes = [38, 38]
snare_times = [bar2_start + 0.375, bar2_start + 1.125]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth
hihat_notes = [42] * 8
hihat_times = [bar2_start + i * 0.375 for i in range(8)]
for note, time in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

bar3_start = 3.0
bar3_end = 4.5

# Kick on beat 1 and 3
kick_notes = [36, 36]
kick_times = [bar3_start + 0.0, bar3_start + 0.75]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on beat 2 and 4
snare_notes = [38, 38]
snare_times = [bar3_start + 0.375, bar3_start + 1.125]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth
hihat_notes = [42] * 8
hihat_times = [bar3_start + i * 0.375 for i in range(8)]
for note, time in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

bar4_start = 4.5
bar4_end = 6.0

# Kick on beat 1 and 3
kick_notes = [36, 36]
kick_times = [bar4_start + 0.0, bar4_start + 0.75]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on beat 2 and 4
snare_notes = [38, 38]
snare_times = [bar4_start + 0.375, bar4_start + 1.125]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth
hihat_notes = [42] * 8
hihat_times = [bar4_start + i * 0.375 for i in range(8)]
for note, time in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
