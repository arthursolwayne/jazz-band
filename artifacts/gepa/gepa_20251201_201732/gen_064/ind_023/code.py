
import pretty_midi

# Create a new MIDI file with the given tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
time = 0.0

# Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.375))
# Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time + 0.75, end=time + 0.75 + 0.375))
# Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time + 1.125, end=time + 1.125 + 0.375))
# Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time + 1.5, end=time + 1.5 + 0.375))

# Hihat on every eighth note
for i in range(8):
    hihat_start = time + i * 0.375
    hihat_end = hihat_start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_start, end=hihat_end))

# Bar 2: Full quartet (1.5 - 3.0s)
time = 1.5

# Bass: Walking line in F minor (start with F2, then G2, Ab2, A2, etc.)
# F2 (38), G2 (40), Ab2 (41), A2 (43)
bass_notes = [38, 40, 41, 43]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))
    time += 0.375

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> F, Ab, C, Eb
piano_notes = [71, 68, 72, 64]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.5, end=1.5 + 0.375))

# Sax: Motif — start with open, call-and-response
# F (71), Ab (68), C (72), then leave it hanging
sax_notes = [71, 68, 72]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.5 + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
time = 3.0

# Bass: Walking line continues (Bb2 (42), B2 (43), C2 (44), D2 (45))
bass_notes = [42, 43, 44, 45]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))
    time += 0.375

# Piano: Bb7 (Bb, D, F, Ab) -> Bb, D, F, Ab
piano_notes = [67, 74, 71, 68]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.0, end=3.0 + 0.375))

# Sax: Continue motif — answer the question
# Bb (67), D (74), F (71), leave it hanging again
sax_notes = [67, 74, 71]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.0 + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
time = 4.5

# Bass: Walking line continues (Eb2 (53), F2 (55), G2 (57), Ab2 (58))
bass_notes = [53, 55, 57, 58]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))
    time += 0.375

# Piano: Gm7 (G, Bb, D, F) -> G, Bb, D, F
piano_notes = [76, 71, 74, 71]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5, end=4.5 + 0.375))

# Sax: Complete the motif — return to F and resolve
# G (76), Bb (71), F (71), then resolve with a slight delay
sax_notes = [76, 71, 71]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.5 + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
