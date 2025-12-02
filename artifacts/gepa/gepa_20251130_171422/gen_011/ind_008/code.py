
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum definitions
kick = 36
snare = 38
hihat = 42

# Time per bar (at 160 BPM, 4/4 time)
bar_length = 6.0  # seconds

# Time per beat
beat_length = bar_length / 4  # 1.5 seconds per beat

# BAR 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1
drum_notes = [
    (0, kick, 1.0),           # Kick on beat 1
    (beat_length, snare, 1.0),     # Snare on beat 2
    (2 * beat_length, kick, 1.0),  # Kick on beat 3
    (3 * beat_length, snare, 1.0),     # Snare on beat 4
]

# Add hihat on every eighth note
for i in range(8):
    time = i * beat_length / 2
    if time not in [0, beat_length, 2 * beat_length, 3 * beat_length]:
        drum_notes.append((time, hihat, 0.5))

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# BAR 2: Bass enters, walking line with chromatic approaches
# Dm7 chord: D, F, A, C
# Walking bass line: D -> C -> Eb -> F -> G -> A -> Bb -> B -> C -> D (with chromatic passing)

# Time for bar 2 starts at 6.0 seconds
bar_start = 6.0

# Bass notes in bar 2
bass_notes = [
    (bar_start, 62, 100),  # D (root)
    (bar_start + beat_length, 60, 100),  # C (chromatic approach)
    (bar_start + 2 * beat_length, 61, 100),  # Eb (chromatic)
    (bar_start + 3 * beat_length, 65, 100),  # F (3rd)
    (bar_start + 4 * beat_length, 67, 100),  # G (5th)
    (bar_start + 5 * beat_length, 69, 100),  # A (7th)
    (bar_start + 6 * beat_length, 68, 100),  # Bb (chromatic)
    (bar_start + 7 * beat_length, 71, 100),  # B (chromatic)
    (bar_start + 8 * beat_length, 69, 100),  # A
    (bar_start + 9 * beat_length, 67, 100),  # G
    (bar_start + 10 * beat_length, 65, 100),  # F
    (bar_start + 11 * beat_length, 62, 100),  # D
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# BAR 2: Piano enters, comping on 2 and 4 with 7th chords
# Dm7: D, F, A, C

# Time for piano comping
piano_notes = [
    (bar_start + beat_length, 62, 100),  # D
    (bar_start + beat_length, 65, 100),  # F (with D)
    (bar_start + beat_length, 69, 100),  # A
    (bar_start + beat_length, 67, 100),  # C

    (bar_start + 3 * beat_length, 62, 100),  # D
    (bar_start + 3 * beat_length, 65, 100),  # F
    (bar_start + 3 * beat_length, 69, 100),  # A
    (bar_start + 3 * beat_length, 67, 100),  # C
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# BAR 2: Saxophone enters with a simple, striking motif
# Melody: D (62) -> E (64) -> F# (66) -> D (62)
# Leave it hanging on the last note (D)

sax_notes = [
    (bar_start, 62, 100),  # D (start on beat 1)
    (bar_start + 0.5 * beat_length, 64, 100),  # E
    (bar_start + 1.0 * beat_length, 66, 100),  # F#
    (bar_start + 1.5 * beat_length, 62, 100),  # D (leave it hanging)
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# BAR 3: Everyone continues
# Bass continues walking, piano continues comping, drums same pattern
# Saxophone continues the motif and resolves it

# BAR 3 starts at 12.0 seconds

# Bass continues from previous pattern
bass_notes_bar3 = [
    (12.0, 62, 100),  # D
    (12.0 + beat_length, 60, 100),  # C
    (12.0 + 2 * beat_length, 61, 100),  # Eb
    (12.0 + 3 * beat_length, 65, 100),  # F
    (12.0 + 4 * beat_length, 67, 100),  # G
    (12.0 + 5 * beat_length, 69, 100),  # A
    (12.0 + 6 * beat_length, 68, 100),  # Bb
    (12.0 + 7 * beat_length, 71, 100),  # B
    (12.0 + 8 * beat_length, 69, 100),  # A
    (12.0 + 9 * beat_length, 67, 100),  # G
    (12.0 + 10 * beat_length, 65, 100),  # F
    (12.0 + 11 * beat_length, 62, 100),  # D
]

for time, note, velocity in bass_notes_bar3:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano continues comping on 2 and 4
piano_notes_bar3 = [
    (12.0 + beat_length, 62, 100),  # D
    (12.0 + beat_length, 65, 100),  # F
    (12.0 + beat_length, 69, 100),  # A
    (12.0 + beat_length, 67, 100),  # C

    (12.0 + 3 * beat_length, 62, 100),  # D
    (12.0 + 3 * beat_length, 65, 100),  # F
    (12.0 + 3 * beat_length, 69, 100),  # A
    (12.0 + 3 * beat_length, 67, 100),  # C
]

for time, note, velocity in piano_notes_bar3:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Saxophone continues motif and resolves
# Resolves the D to D again but with a slight variation
# D -> E -> F# -> D (same as before, but now repeat on next bar)

sax_notes_bar3 = [
    (12.0, 62, 100),  # D
    (12.0 + 0.5 * beat_length, 64, 100),  # E
    (12.0 + 1.0 * beat_length, 66, 100),  # F#
    (12.0 + 1.5 * beat_length, 62, 100),  # D
]

for time, note, velocity in sax_notes_bar3:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# BAR 4: Drums continue, saxophone resolves on last note
# Saxophone resolves the motif with a slight variation to D again

# Bar 4 starts at 18.0 seconds

# Drums continue same pattern as bar 1
bar4_drum_notes = [
    (18.0, kick, 1.0),
    (18.0 + beat_length, snare, 1.0),
    (18.0 + 2 * beat_length, kick, 1.0),
    (18.0 + 3 * beat_length, snare, 1.0),
]

# Hihat on every eighth note
for i in range(8):
    time = 18.0 + i * beat_length / 2
    if time not in [18.0, 18.0 + beat_length, 18.0 + 2 * beat_length, 18.0 + 3 * beat_length]:
        bar4_drum_notes.append((time, hihat, 0.5))

for time, note, velocity in bar4_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass continues walking pattern
bass_notes_bar4 = [
    (18.0, 62, 100),  # D
    (18.0 + beat_length, 60, 100),  # C
    (18.0 + 2 * beat_length, 61, 100),  # Eb
    (18.0 + 3 * beat_length, 65, 100),  # F
    (18.0 + 4 * beat_length, 67, 100),  # G
    (18.0 + 5 * beat_length, 69, 100),  # A
    (18.0 + 6 * beat_length, 68, 100),  # Bb
    (18.0 + 7 * beat_length, 71, 100),  # B
    (18.0 + 8 * beat_length, 69, 100),  # A
    (18.0 + 9 * beat_length, 67, 100),  # G
    (18.0 + 10 * beat_length, 65, 100),  # F
    (18.0 + 11 * beat_length, 62, 100),  # D
]

for time, note, velocity in bass_notes_bar4:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano continues comping
piano_notes_bar4 = [
    (18.0 + beat_length, 62, 100),  # D
    (18.0 + beat_length, 65, 100),  # F
    (18.0 + beat_length, 69, 100),  # A
    (18.0 + beat_length, 67, 100),  # C

    (18.0 + 3 * beat_length, 62, 100),  # D
    (18.0 + 3 * beat_length, 65, 100),  # F
    (18.0 + 3 * beat_length, 69, 100),  # A
    (18.0 + 3 * beat_length, 67, 100),  # C
]

for time, note, velocity in piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Saxophone resolves the motif
# D -> E -> F# -> D (same again, but now with a slight pause at the end)
sax_notes_bar4 = [
    (18.0, 62, 100),  # D
    (18.0 + 0.5 * beat_length, 64, 100),  # E
    (18.0 + 1.0 * beat_length, 66, 100),  # F#
    (18.0 + 1.5 * beat_length, 62, 100),  # D (end on D)
]

for time, note, velocity in sax_notes_bar4:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_intro.mid")
