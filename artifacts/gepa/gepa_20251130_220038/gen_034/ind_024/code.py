
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time per bar = 1.5 seconds
bar_length = 1.5
bar_count = 4

# BAR 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):  # two beats per bar
    # Kick on beat 1 and 3
    if i == 0:
        kick_time = 0.0
    elif i == 1:
        kick_time = bar_length / 2
    kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)
    
    # Snare on beat 2 and 4
    if i == 0:
        snare_time = bar_length / 2
    elif i == 1:
        snare_time = bar_length
    snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)
    
    # Hihat on every eighth note
    for j in range(2):
        hihat_time = i * bar_length / 2 + j * bar_length / 4
        hihat_note = pretty_midi.Note(velocity=100, pitch=hihat, start=hihat_time, end=hihat_time + 0.1)
        drums.notes.append(hihat_note)

# BAR 2: Full ensemble (1.5 - 3.0s)

# Bass line (walking line in Dm, chromatic approaches)
bass_notes = [
    (31, 1.5),     # D (root)
    (32, 1.75),    # Eb (chromatic)
    (33, 2.0),     # E (3rd)
    (30, 2.25),    # C (7th)
    (29, 2.5),     # Bb (flattened 5th)
    (31, 2.75),    # D again
    (32, 3.0),     # Eb
]

for pitch, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chords (7th chords, comp on 2 and 4)
# Dm7 in root position: D, F, A, C
def play_chord(chord, start_time, duration=0.25):
    for pitch in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + duration)
        piano.notes.append(piano_note)

# Bar 2 - 2nd beat (1.75s)
dmin7 = [50, 52, 55, 57]  # D, F, A, C (Dm7)
play_chord(dmin7, 1.75)

# Bar 3 - 2nd beat (3.25s)
play_chord(dmin7, 3.25)

# Sax melody (Dante's motif)
# Motif: D - Eb - E - C (Dm scale, but with that chromatic twist)
# Start on beat 1 (1.5s), leave it hanging on E (beat 2.25s), come back on beat 3.75s with C to resolve
sax_notes = [
    (50, 1.5, 0.5),   # D
    (52, 2.25, 0.25), # Eb
    (53, 3.75, 0.5),  # E
    (57, 4.25, 0.5)   # C
]

for pitch, time, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(sax_note)

# BAR 3: Full ensemble (3.0 - 4.5s)
# Bass continues walking
bass_notes = [
    (31, 3.0),     # D
    (32, 3.25),    # Eb
    (33, 3.5),     # E
    (30, 3.75),    # C
    (29, 4.0),     # Bb
    (31, 4.25),    # D
    (32, 4.5),     # Eb
]

for pitch, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chord again on beat 2 and 4
play_chord(dmin7, 3.25)
play_chord(dmin7, 4.25)

# BAR 4: Full ensemble (4.5 - 6.0s)
# Bass continues walking
bass_notes = [
    (31, 4.5),     # D
    (32, 4.75),    # Eb
    (33, 5.0),     # E
    (30, 5.25),    # C
    (29, 5.5),     # Bb
    (31, 5.75),    # D
    (32, 6.0),     # Eb
]

for pitch, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chord on beat 2 and 4
play_chord(dmin7, 4.75)
play_chord(dmin7, 5.75)

# Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    # Kick on beat 1 and 3
    if i == 0:
        kick_time = 4.5
    elif i == 1:
        kick_time = 4.5 + bar_length / 2
    kick_note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)
    
    # Snare on beat 2 and 4
    if i == 0:
        snare_time = 4.5 + bar_length / 2
    elif i == 1:
        snare_time = 4.5 + bar_length
    snare_note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)
    
    # Hihat on every eighth note
    for j in range(2):
        hihat_time = 4.5 + i * bar_length / 2 + j * bar_length / 4
        hihat_note = pretty_midi.Note(velocity=100, pitch=hihat, start=hihat_time, end=hihat_time + 0.1)
        drums.notes.append(hihat_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
