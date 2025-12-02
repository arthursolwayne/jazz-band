
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth note
hihat_times = [bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125, bar1_start + 1.5]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line (Marcus)
# D2-G2, roots and fifths with chromatic approaches
# Bar 2: D2 (root) -> D#2 (chromatic approach) -> G2 (fifth)
bass_notes_bar2 = [38, 39, 43]
bass_times_bar2 = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75]
for i, pitch in enumerate(bass_notes_bar2):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times_bar2[i], end=bass_times_bar2[i] + 0.25)
    bass.notes.append(note)

# Bar 3: A2 (chromatic) -> B2 (root of D7) -> F#2 (fifth of D7)
bass_notes_bar3 = [41, 42, 46]
bass_times_bar3 = [bar3_start + 0.0, bar3_start + 0.375, bar3_start + 0.75]
for i, pitch in enumerate(bass_notes_bar3):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times_bar3[i], end=bass_times_bar3[i] + 0.25)
    bass.notes.append(note)

# Bar 4: D2 (root) -> D#2 (chromatic) -> G2 (fifth)
bass_notes_bar4 = [38, 39, 43]
bass_times_bar4 = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75]
for i, pitch in enumerate(bass_notes_bar4):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times_bar4[i], end=bass_times_bar4[i] + 0.25)
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (G, B, D, F#)
piano_notes_bar2 = [67, 71, 74, 76]
piano_times_bar2 = [bar2_start + 0.75]
for pitch in piano_notes_bar2:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=piano_times_bar2[0], end=piano_times_bar2[0] + 0.5)
    piano.notes.append(note)

# Bar 3: Bm7 (D, F#, A, B)
piano_notes_bar3 = [62, 66, 69, 71]
piano_times_bar3 = [bar3_start + 0.75]
for pitch in piano_notes_bar3:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=piano_times_bar3[0], end=piano_times_bar3[0] + 0.5)
    piano.notes.append(note)

# Bar 4: Gmaj7 (B, D, F#, G)
piano_notes_bar4 = [67, 71, 76, 77]
piano_times_bar4 = [bar4_start + 0.75]
for pitch in piano_notes_bar4:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=piano_times_bar4[0], end=piano_times_bar4[0] + 0.5)
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 -> E4 -> C4 -> D4
sax_notes = [62, 64, 60, 62]
sax_times = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=sax_times[i], end=sax_times[i] + 0.25)
    sax.notes.append(note)

# Repeat motif in bar 4
sax_notes_bar4 = [62, 64, 60, 62]
sax_times_bar4 = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125]
for i, pitch in enumerate(sax_notes_bar4):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=sax_times_bar4[i], end=sax_times_bar4[i] + 0.25)
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3
kick_times_bar2 = [bar2_start + 0.375, bar2_start + 1.125]
for time in kick_times_bar2:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

kick_times_bar3 = [bar3_start + 0.375, bar3_start + 1.125]
for time in kick_times_bar3:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

kick_times_bar4 = [bar4_start + 0.375, bar4_start + 1.125]
for time in kick_times_bar4:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times_bar2 = [bar2_start + 0.75, bar2_start + 1.5]
for time in snare_times_bar2:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times_bar3 = [bar3_start + 0.75, bar3_start + 1.5]
for time in snare_times_bar3:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times_bar4 = [bar4_start + 0.75, bar4_start + 1.5]
for time in snare_times_bar4:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth note
hihat_times_bar2 = [bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125, bar2_start + 1.5]
for time in hihat_times_bar2:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times_bar3 = [bar3_start + 0.375, bar3_start + 0.75, bar3_start + 1.125, bar3_start + 1.5]
for time in hihat_times_bar3:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times_bar4 = [bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125, bar4_start + 1.5]
for time in hihat_times_bar4:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
