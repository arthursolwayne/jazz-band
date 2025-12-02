
import pretty_midi

# Create a MIDI file with 160 BPM, F major key, 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes: kick (36), snare (38), hihat (42)
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray plays alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Bar 1: 0.0 - 1.5s
    # Kick on 1 (0.0), 3 (1.125s)
    for kick_time in [0.0, 1.125]:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time + start, end=kick_time + start + 0.125)
        drums.notes.append(note)
    # Snare on 2 (0.75), 4 (1.5)
    for snare_time in [0.75, 1.5]:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time + start, end=snare_time + start + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5, 1.875, etc.)
    for hihat_time in [0.0, 0.375, 0.75, 1.125, 1.5]:
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=hihat_time + start, end=hihat_time + start + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time from 1.5 to 6.0s (3 bars)
start = 1.5

# Bass line: walking line with chromatic approaches
# F major scale: F, G, A, Bb, B, C, D, E
# Chromatic approaches = half steps above or below target notes
# F -> E (chromatic), F -> G (scale), etc.
# Bass line (in 16th notes):
# F, E, F, G (bar 2)
# A, Bb, A, Bb (bar 3)
# B, C, D, E (bar 4)

# Time divisions: each bar is 1.5s, so 16th note is 0.09375s
# Bar 2: 1.5s to 3.0s
# Bar 3: 3.0s to 4.5s
# Bar 4: 4.5s to 6.0s

# Bar 2: F, E, F, G
bass_notes = [77, 76, 77, 78]  # F (77), E (76), F (77), G (78)
for i, note in enumerate(bass_notes):
    start_time = 1.5 + i * 0.09375
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.09375)
    bass.notes.append(note_obj)

# Bar 3: A, Bb, A, Bb
bass_notes = [69, 70, 69, 70]  # A (69), Bb (70), A (69), Bb (70)
for i, note in enumerate(bass_notes):
    start_time = 3.0 + i * 0.09375
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.09375)
    bass.notes.append(note_obj)

# Bar 4: B, C, D, E
bass_notes = [71, 72, 74, 76]  # B (71), C (72), D (74), E (76)
for i, note in enumerate(bass_notes):
    start_time = 4.5 + i * 0.09375
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.09375)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, E (notes 77, 82, 72, 76)
# Bb7: Bb, D, F, Ab (notes 70, 75, 77, 78)
# Bar 2: F7 on beat 2
# Bar 3: Bb7 on beat 2
# Bar 4: F7 on beat 2

# Bar 2: F7 on beat 2 (time 2.25s)
for note in [77, 82, 72, 76]:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=2.25, end=2.25 + 0.25)
    piano.notes.append(note_obj)

# Bar 3: Bb7 on beat 2 (time 3.75s)
for note in [70, 75, 77, 78]:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=3.75, end=3.75 + 0.25)
    piano.notes.append(note_obj)

# Bar 4: F7 on beat 2 (time 5.25s)
for note in [77, 82, 72, 76]:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=5.25, end=5.25 + 0.25)
    piano.notes.append(note_obj)

# Tenor Sax: Motif in F major
# Start with a short motif: F (77), G (78), A (69), Bb (70), rest on beat 4
# Start at 1.5s, hold each note for 0.375s (quarter note)
sax_notes = [77, 78, 69, 70]
for i, note in enumerate(sax_notes):
    start_time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
