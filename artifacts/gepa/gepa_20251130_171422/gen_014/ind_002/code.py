
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
beat = 0.375  # 160 BPM = 0.375 sec per beat

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar1_start + 0.0, end=bar1_start + 0.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar1_start + beat * 2, end=bar1_start + beat * 2 + 0.1))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar1_start + beat, end=bar1_start + beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar1_start + beat * 3, end=bar1_start + beat * 3 + 0.1))

# Hihat on every eighth (8 notes per bar)
for i in range(8):
    start = bar1_start + i * beat
    end = start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5

# Marcus on bass: walking line in Fm (F, Gb, Ab, Bb) with chromatic approaches
# Bassline: F, Gb, Ab, Bb, Bb, C, D, Eb
bass_notes = [77, 76, 74, 72, 72, 73, 75, 73]
for i, note in enumerate(bass_notes):
    start = bar2_start + i * beat
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane on piano: 7th chords on 2 and 4, with comping
# Fm7 = F, Ab, Bb, C
# Gm7 = G, Bb, C, D
# Am7 = A, C, D, E
# Bbm7 = Bb, Db, Eb, F
chords = [
    # Bar 2: Fm7 (beat 2)
    (77, 74, 72, 73, bar2_start + beat, bar2_start + beat + 0.25),
    # Bar 3: Gm7 (beat 2)
    (78, 72, 73, 74, bar2_start + beat * 3, bar2_start + beat * 3 + 0.25),
    # Bar 4: Am7 (beat 2)
    (79, 73, 74, 75, bar2_start + beat * 5, bar2_start + beat * 5 + 0.25),
]

for note in chords:
    pitch, _, _, _, start, end = note
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# Dante on sax: short motif, start, leave it hanging, come back
# Motif: F (77), Ab (74), Bb (72), F (77)
# Play F (beat 1), Ab (beat 2), Bb (beat 3), rest on beat 4
sax_notes = [
    (77, bar2_start, bar2_start + 0.25),
    (74, bar2_start + beat, bar2_start + beat + 0.25),
    (72, bar2_start + beat * 2, bar2_start + beat * 2 + 0.25)
]

for note in sax_notes:
    pitch, start, end = note
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 3 and 4: Full quartet (3.0 - 6.0s)
bar3_start = 3.0

# Marcus: continue walking line
bass_notes = [72, 73, 75, 73, 73, 74, 76, 74]
for i, note in enumerate(bass_notes):
    start = bar3_start + i * beat
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane: comp on 2 and 4
# Bbm7 (beat 2), Cm7 (beat 4)
chords = [
    (71, 69, 67, 68, bar3_start + beat, bar3_start + beat + 0.25),
    (68, 70, 71, 72, bar3_start + beat * 3, bar3_start + beat * 3 + 0.25)
]

for note in chords:
    pitch, _, _, _, start, end = note
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# Dante: repeat motif but complete it
# F (beat 1), Ab (beat 2), Bb (beat 3), F (beat 4)
sax_notes = [
    (77, bar3_start, bar3_start + 0.25),
    (74, bar3_start + beat, bar3_start + beat + 0.25),
    (72, bar3_start + beat * 2, bar3_start + beat * 2 + 0.25),
    (77, bar3_start + beat * 3, bar3_start + beat * 3 + 0.25)
]

for note in sax_notes:
    pitch, start, end = note
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Add Little Ray to bar 3 and 4
# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar3_end = 4.5
for i in range(8):
    start = bar3_start + i * beat
    end = start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar3_start, end=bar3_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar3_start + beat * 2, end=bar3_start + beat * 2 + 0.1))

# Snares on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar3_start + beat, end=bar3_start + beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar3_start + beat * 3, end=bar3_start + beat * 3 + 0.1))

# Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_start = 4.5
for i in range(8):
    start = bar4_start + i * beat
    end = start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar4_start, end=bar4_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar4_start + beat * 2, end=bar4_start + beat * 2 + 0.1))

# Snares on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar4_start + beat, end=bar4_start + beat + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar4_start + beat * 3, end=bar4_start + beat * 3 + 0.1))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
