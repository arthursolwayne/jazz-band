
import pretty_midi
import numpy as np

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds
KICK = 36
SNARE = 38
HIHAT = 42

# Bar durations in seconds (160 BPM, 4/4 time)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375
HALF_BEAT = 0.1875

# --- DRUMS: LITTLE RAY (Bar 1: 0.0 - 1.5s) ---
# Set up the groove with syncopation and energy
drum_notes = []

# Kick on 1 and 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.0 + HALF_BEAT))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.5 + HALF_BEAT))

# Snare on 2 and 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.75, end=0.75 + HALF_BEAT))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.5 + 0.75, end=1.5 + 0.75 + HALF_BEAT))

# Hi-hat on every eighth note
for i in range(0, 3):
    for j in range(0, 8):  # 8 eighth notes per bar
        start = i * BAR_DURATION + j * HALF_BEAT
        end = start + HALF_BEAT
        drum_notes.append(pretty_midi.Note(velocity=70 + np.random.randint(0, 20), pitch=HIHAT, start=start, end=end))

# Add some syncopated fills
# A little offbeat snare
drum_notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=0.5, end=0.5 + HALF_BEAT))
drum_notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=1.0, end=1.0 + HALF_BEAT))

drums.notes.extend(drum_notes)

# --- BASS: MARCUS (Bar 2-4: 1.5 - 6.0s) ---
# Walking bass with chromatic approaches, no repetition
bass_notes = []

# Start at Dm7 (D, F, A, C)
start_note = pretty_midi.note_number_to_name(62)  # D4
start_piano_key = 62

# Define a walking line in D minor
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Walking pattern: root, b9, 3, 5, b7, root, etc.
walk_intervals = [0, -1, 3, 5, -2, 0, 3, 5]

# Start from D
current_note = start_piano_key
for bar in range(2, 5):
    for beat in range(4):  # four beats per bar
        beat_start = bar * BAR_DURATION - 1.5 + beat * BEAT_DURATION
        note_number = current_note + walk_intervals[beat % len(walk_intervals)]
        duration = BEAT_DURATION
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=note_number, start=beat_start, end=beat_start + duration))
        current_note = note_number

bass.notes.extend(bass_notes)

# --- PIANO: DIANE (Bar 2-4: 1.5 - 6.0s) ---
# Comping with 7th chords on 2 and 4
piano_notes = []

# Dm7 chord: D, F, A, C
root = 62
third = 64
fifth = 67
seventh = 60

# On beats 2 and 4, play full voicings
for bar in range(2, 5):
    for beat in range(4):
        beat_start = bar * BAR_DURATION - 1.5 + beat * BEAT_DURATION
        if beat == 1 or beat == 3:
            # Play full Dm7 chord
            for note in [root, third, fifth, seventh]:
                piano_notes.append(pretty_midi.Note(velocity=100 + np.random.randint(-10, 10), pitch=note, start=beat_start, end=beat_start + BEAT_DURATION))

# Add some chromatic passing tones and tension
for bar in range(2, 5):
    for beat in range(4):
        beat_start = bar * BAR_DURATION - 1.5 + beat * BEAT_DURATION
        # Add some chromatic passing tones between beats
        if beat < 3:
            pass_tone = root + 1
            piano_notes.append(pretty_midi.Note(velocity=80, pitch=pass_tone, start=beat_start + BEAT_DURATION * 0.75, end=beat_start + BEAT_DURATION * 0.75 + 0.1))

piano.notes.extend(piano_notes)

# --- SAX: DANTÉ (Bar 2-4: 1.5 - 6.0s) ---
# A simple, haunting motif — start it, leave it hanging, come back
# Let's go with: D - Eb - F - D (quarter notes), then repeat but end on F
# D is 62, Eb is 63, F is 64

sax_notes = []

# First iteration
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.5 + BEAT_DURATION, end=1.5 + 2*BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2*BEAT_DURATION, end=1.5 + 3*BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3*BEAT_DURATION, end=1.5 + 4*BEAT_DURATION))

# Second iteration, same motif but end on F (64)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.0 + BEAT_DURATION, end=3.0 + 2*BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0 + 2*BEAT_DURATION, end=3.0 + 3*BEAT_DURATION))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0 + 3*BEAT_DURATION, end=3.0 + 4*BEAT_DURATION))

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_shot.mid")
print("MIDI file created: 'waynes_shot.mid'")
