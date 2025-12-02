
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick(36), snare(38), hihat(42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Define the time in seconds for each bar (160 BPM = 0.375s per beat, 1.5s per bar)
bar_length = 1.5
beat_length = 0.375

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = bar_length

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=bar_1_start + 0.0, end=bar_1_start + beat_length))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=bar_1_start + 2 * beat_length, end=bar_1_start + 3 * beat_length))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['snare'], start=bar_1_start + beat_length, end=bar_1_start + 2 * beat_length))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['snare'], start=bar_1_start + 3 * beat_length, end=bar_1_start + 4 * beat_length))

# Hihat on every eighth note
for i in range(8):
    hihat_start = bar_1_start + i * beat_length / 2
    hihat_end = hihat_start + beat_length / 2
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=drum_notes['hihat'], start=hihat_start, end=hihat_end))

# Bar 2: Full quartet (1.5 - 3.0s)
bar_2_start = 1.5
bar_2_end = bar_2_start + bar_length

# Bass line: walking line in Dm, chromatic approach to F
# Dm7 chord: D F A C
# Bass line: D - Eb - F - G - A - Bb - B - C - D
# (walking line, chromatic approach to F)
bass_notes = [62, 63, 65, 67, 69, 70, 71, 72]
bass_durations = [beat_length] * 8

for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=bar_2_start + i * beat_length, end=bar_2_start + (i + 1) * beat_length))

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4 (beat 2 and 4 of bar 2)
piano_notes = [62, 65, 69, 72]  # Dm7
piano_durations = [beat_length] * 2

# Bar 2 beat 2
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[0], start=bar_2_start + beat_length, end=bar_2_start + 2 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[1], start=bar_2_start + beat_length, end=bar_2_start + 2 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[2], start=bar_2_start + beat_length, end=bar_2_start + 2 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[3], start=bar_2_start + beat_length, end=bar_2_start + 2 * beat_length))

# Bar 2 beat 4
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[0], start=bar_2_start + 3 * beat_length, end=bar_2_start + 4 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[1], start=bar_2_start + 3 * beat_length, end=bar_2_start + 4 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[2], start=bar_2_start + 3 * beat_length, end=bar_2_start + 4 * beat_length))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=piano_notes[3], start=bar_2_start + 3 * beat_length, end=bar_2_start + 4 * beat_length))

# Sax: Your motif — short, singable, leaves it hanging
# Dm scale: D E F G A Bb C
# Motif: D - F - G - A (4 notes, 0.375s each)
# Starts on bar 2 beat 1, then rests for 1.5s, comes back on bar 4 beat 1

sax_notes = [62, 65, 67, 69]
sax_durations = [beat_length] * 4

# First part of the motif (bar 2, beat 1)
for i, note in enumerate(sax_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_2_start + i * beat_length, end=bar_2_start + (i + 1) * beat_length))

# Bar 3: No sax — leave it hanging
# Bar 4: Come back with the motif (full phrase)

bar_4_start = 3.0
bar_4_end = bar_4_start + bar_length

# Repeat the motif (bar 4, beat 1)
for i, note in enumerate(sax_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_4_start + i * beat_length, end=bar_4_start + (i + 1) * beat_length))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
