
import pretty_midi

# Create a new MIDI file with the given tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Constants for timing
bar_length = 1.5  # seconds per bar at 160 BPM
note_length = 0.375  # quarter note in seconds at 160 BPM

# ------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood with space and energy

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=note_length))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=note_length * 2, end=note_length * 3))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=note_length, end=note_length * 2))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=note_length * 3, end=note_length * 4))

# Hihat on every eighth note
for i in range(0, 4):
    hihat_start = i * note_length
    hihat_end = hihat_start + note_length / 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=hihat_start, end=hihat_end))

# ------------------
# Bar 2: Full quartet enters (1.5 - 3.0s)

# Bass line: chromatic walk, Dm7 -> Cm7 -> Bm7 -> Am7
bass_notes = [[62, 61, 60, 59], [60, 59, 58, 57], [58, 57, 56, 55], [55, 54, 53, 52]]
for i, notes in enumerate(bass_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 1 + i * note_length
        end = start + note_length / 4
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on offbeats, supporting the rhythm
# Dm7 on beat 1 (offbeat 1.5), Cm7 on beat 2 (offbeat 2.5), Bm7 on beat 3 (offbeat 3.5), Am7 on beat 4 (offbeat 4.5)
piano_notes = [
    [62, 67, 65, 60],  # Dm7
    [60, 65, 63, 57],  # Cm7
    [58, 63, 61, 55],  # Bm7
    [55, 60, 58, 52]   # Am7
]

for i, notes in enumerate(piano_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 1 + (i + 0.5) * note_length
        end = start + note_length / 2
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Saxophone: One phrase — a question, a memory, a challenge
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, G — then return to D
sax_note_values = [62, 64, 65, 67, 62]
for i, pitch in enumerate(sax_note_values):
    start = bar_length * 1 + i * note_length
    end = start + note_length
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# ------------------
# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: chromatic again, but slightly altered for tension
bass_notes = [[62, 61, 60, 59], [60, 59, 58, 57], [58, 57, 56, 55], [55, 54, 53, 52]]
for i, notes in enumerate(bass_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 2 + i * note_length
        end = start + note_length / 4
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: same chords, but with a dissonant twist on beat 3
piano_notes = [
    [62, 67, 65, 60],  # Dm7
    [60, 65, 63, 57],  # Cm7
    [58, 63, 61, 55],  # Bm7
    [55, 60, 58, 52]   # Am7
]

for i, notes in enumerate(piano_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 2 + (i + 0.5) * note_length
        end = start + note_length / 2
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Saxophone: Develop the motif — repeat the motif but with a slight variation
sax_note_values = [62, 64, 65, 67, 62, 64, 65, 67]
for i, pitch in enumerate(sax_note_values):
    start = bar_length * 2 + i * note_length
    end = start + note_length
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# ------------------
# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: chromatic again, resolving slightly
bass_notes = [[62, 61, 60, 59], [60, 59, 58, 57], [58, 57, 56, 55], [55, 54, 53, 52]]
for i, notes in enumerate(bass_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 3 + i * note_length
        end = start + note_length / 4
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: same chords, but with a stronger resolution on beat 4
piano_notes = [
    [62, 67, 65, 60],  # Dm7
    [60, 65, 63, 57],  # Cm7
    [58, 63, 61, 55],  # Bm7
    [55, 60, 58, 52]   # Am7
]

for i, notes in enumerate(piano_notes):
    for j, pitch in enumerate(notes):
        start = bar_length * 3 + (i + 0.5) * note_length
        end = start + note_length / 2
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Saxophone: End with a strong resolution — the motif returns, but finishes
sax_note_values = [62, 64, 65, 67, 62]
for i, pitch in enumerate(sax_note_values):
    start = bar_length * 3 + i * note_length
    end = start + note_length
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# ------------------
# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI to a file
midi.write("dante_jazz_intro.mid")
