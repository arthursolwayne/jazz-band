
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
kick_times = [bar1_start + 0.0, bar1_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.375, bar1_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar1_start + 0.0, bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Bar 2 (Dm7): D2, F2, A2, C2, chromatic approach to D2
bass_notes = [38, 40, 43, 45, 37, 38]
bass_times = [bar2_start + 0.0, bar2_start + 0.25, bar2_start + 0.5, bar2_start + 0.75, bar2_start + 1.0, bar2_start + 1.25]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_times[i], end=bass_times[i] + 0.25)
    bass.notes.append(note)

# Bar 3 (G7): G2, B2, D3, F2, chromatic approach to G2
bass_notes = [43, 45, 47, 40, 42, 43]
bass_times = [bar3_start + 0.0, bar3_start + 0.25, bar3_start + 0.5, bar3_start + 0.75, bar3_start + 1.0, bar3_start + 1.25]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_times[i], end=bass_times[i] + 0.25)
    bass.notes.append(note)

# Bar 4 (Cm7): C2, Eb2, G2, Bb2, chromatic approach to C2
bass_notes = [36, 39, 42, 44, 35, 36]
bass_times = [bar4_start + 0.0, bar4_start + 0.25, bar4_start + 0.5, bar4_start + 0.75, bar4_start + 1.0, bar4_start + 1.25]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_times[i], end=bass_times[i] + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [50, 52, 55, 57]
piano_times = [bar2_start + 0.0, bar2_start + 0.0, bar2_start + 0.0, bar2_start + 0.0]
for i in range(len(piano_notes)):
    note = pretty_midi.Note(velocity=100, pitch=piano_notes[i], start=piano_times[i], end=bar2_end)
    piano.notes.append(note)

# Bar 3: G7 (G, B, D, F)
piano_notes = [55, 57, 59, 52]
piano_times = [bar3_start + 0.0, bar3_start + 0.0, bar3_start + 0.0, bar3_start + 0.0]
for i in range(len(piano_notes)):
    note = pretty_midi.Note(velocity=100, pitch=piano_notes[i], start=piano_times[i], end=bar3_end)
    piano.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [52, 54, 57, 50]
piano_times = [bar4_start + 0.0, bar4_start + 0.0, bar4_start + 0.0, bar4_start + 0.0]
for i in range(len(piano_notes)):
    note = pretty_midi.Note(velocity=100, pitch=piano_notes[i], start=piano_times[i], end=bar4_end)
    piano.notes.append(note)

# Sax: Motif in Dm. Start it, leave it hanging. Come back and finish it.
# Motif: D (50), F (52), D (50), E (51)
sax_notes = [50, 52, 50, 51]
sax_times = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125]
for i in range(len(sax_notes)):
    note = pretty_midi.Note(velocity=110, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.25)
    sax.notes.append(note)

# Repeat the motif in bar 3, shifted up a half step for variation
sax_notes = [51, 53, 51, 52]
sax_times = [bar3_start + 0.0, bar3_start + 0.375, bar3_start + 0.75, bar3_start + 1.125]
for i in range(len(sax_notes)):
    note = pretty_midi.Note(velocity=110, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.25)
    sax.notes.append(note)

# Repeat the motif in bar 4, resolving on D
sax_notes = [50, 52, 50, 50]
sax_times = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125]
for i in range(len(sax_notes)):
    note = pretty_midi.Note(velocity=110, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.25)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
kick_times = [bar2_start + 0.0, bar2_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times = [bar2_start + 0.375, bar2_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times = [bar2_start + 0.0, bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 3
kick_times = [bar3_start + 0.0, bar3_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times = [bar3_start + 0.375, bar3_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times = [bar3_start + 0.0, bar3_start + 0.375, bar3_start + 0.75, bar3_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 4
kick_times = [bar4_start + 0.0, bar4_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times = [bar4_start + 0.375, bar4_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times = [bar4_start + 0.0, bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125]
for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
