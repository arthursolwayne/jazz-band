
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
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + 0.375 * i for i in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# D minor scale: D, Eb, F, G, Ab, Bb, C
bass_notes = [50, 49, 52, 53, 51, 50, 48, 49, 52, 53, 51, 50, 48, 49, 52, 53]
bass_times = [1.5 + i * 0.375 for i in range(16)]
for note, t in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=t, end=t + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# D7 chord: D, F#, A, C
# Dm7: D, F, A, C
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Bar 2: D7 on beat 2 and 4
piano_notes = [50, 58, 62, 60]
piano_times = [bar2_start + 0.75, bar2_start + 1.5]
for note, t in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.1)
    piano.notes.append(note_obj)

# Bar 3: Dm7 on beat 2 and 4
piano_notes = [50, 57, 62, 60]
piano_times = [bar3_start + 0.75, bar3_start + 1.5]
for note, t in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.1)
    piano.notes.append(note_obj)

# Bar 4: D7 on beat 2 and 4
piano_notes = [50, 58, 62, 60]
piano_times = [bar4_start + 0.75, bar4_start + 1.5]
for note, t in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.1)
    piano.notes.append(note_obj)

# Drums continue: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_kick_times = [bar2_start + 0.375, bar2_start + 1.125]
bar2_snare_times = [bar2_start + 0.75, bar2_start + 1.5]
bar2_hihat_times = [bar2_start + 0.375 * i for i in range(4)]

for t in bar2_kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar2_snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar2_hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

bar3_kick_times = [bar3_start + 0.375, bar3_start + 1.125]
bar3_snare_times = [bar3_start + 0.75, bar3_start + 1.5]
bar3_hihat_times = [bar3_start + 0.375 * i for i in range(4)]

for t in bar3_kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar3_snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar3_hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

bar4_kick_times = [bar4_start + 0.375, bar4_start + 1.125]
bar4_snare_times = [bar4_start + 0.75, bar4_start + 1.5]
bar4_hihat_times = [bar4_start + 0.375 * i for i in range(4)]

for t in bar4_kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar4_snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in bar4_hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D minor: D, Eb, F, G, Ab, Bb, C
# Motif: D, F, Eb, C
motif = [50, 52, 49, 48]
# Play motif at bar 2, starting on beat 1, leave it hanging
sax_times = [bar2_start + 0.375, bar2_start + 0.75, bar2_start + 1.125, bar2_start + 1.5]
for note, t in zip(motif, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=t, end=t + 0.375)
    sax.notes.append(note_obj)

# Repeat the motif at bar 4, but complete it
sax_times = [bar4_start + 0.375, bar4_start + 0.75, bar4_start + 1.125, bar4_start + 1.5]
for note, t in zip(motif, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=t, end=t + 0.375)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
