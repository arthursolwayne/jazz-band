
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

# Kick on 1 and 3 (0.0 and 0.75s)
kick_times = [0.0, 0.75]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4 (0.375 and 1.125s)
snare_times = [0.375, 1.125]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hihat on every eighth note
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line with chromatic approaches
bass_notes = [60, 61, 62, 63, 64, 62, 60, 59]
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [64, 67, 71, 72]
piano_times = [1.875, 2.625, 4.125, 4.875]
for note, time in zip(piano_notes, piano_times):
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Drums: same pattern, shifted by 1.5s
kick_times = [1.5, 2.25]
for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

snare_times = [1.875, 2.625]
for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

hihat_times = [i * 0.375 + 1.5 for i in range(8)]
for time in hihat_times:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(hihat)

# Sax: Dante - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [62, 64, 62, 60]  # "C" -> "D" -> "C" -> "B"
sax_times = [1.5, 1.75, 1.875, 2.0]

for note, time in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Repeat motif at the end (bar 4)
sax_notes_end = [62, 64, 62, 60]
sax_times_end = [4.5, 4.75, 4.875, 5.0]

for note, time in zip(sax_notes_end, sax_times_end):
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
