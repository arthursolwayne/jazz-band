
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: F Major
key = 'F'

# Define note pitches based on F Major scale: F, G, A, Bb, B, C, D
# For the melody, we’ll use F, Bb, B, and D as the core motif.

# Instrument: Tenor Saxophone (Program 64)
sax = pretty_midi.Instrument(program=64)

# Instrument: Bass (Program 33)
bass = pretty_midi.Instrument(program=33)

# Instrument: Piano (Program 0)
piano = pretty_midi.Instrument(program=0)

# Instrument: Drums (Program 1)
drums = pretty_midi.Instrument(program=1)

# Time in seconds per beat: 60 / 160 = 0.375
beat_time = 0.375

# Time per bar: 4 beats * 0.375 = 1.5 seconds
bar_time = 1.5

# Define note durations and velocities
note_duration = 0.375  # One beat
velocity = 100

# Bar 1: Drums only (buildup, tension)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0

# Kick on 1
drums.notes.append(pretty_midi.Note(velocity, 36, bar1_start, bar1_start + 0.1))  # Kick

# Snare on 2
drums.notes.append(pretty_midi.Note(velocity, 38, bar1_start + beat_time, bar1_start + beat_time + 0.1))  # Snare

# Hats on every eighth
for i in range(0, 8):
    time = bar1_start + (i * beat_time / 2)
    drums.notes.append(pretty_midi.Note(velocity, 42, time, time + 0.05))  # Hihat

# Bar 2: Bass, Piano, Sax enter

bar2_start = bar_time

# Bass: Walking line in F Major
# F, G, A, Bb, B, C, D, E (chromatic approach to F)
bass_notes = [71, 72, 74, 75, 76, 77, 79, 78]  # F, G, A, Bb, B, C, D, Eb
for i, pitch in enumerate(bass_notes):
    start = bar2_start + (i * beat_time)
    end = start + note_duration
    bass.notes.append(pretty_midi.Note(velocity, pitch, start, end))

# Piano: 7th chords, comp on 2 and 4
# Chord sequence: F7, Bb7, B7, C7
chords = [
    (71, 74, 76, 78),  # F7
    (74, 76, 78, 81),  # Bb7
    (76, 79, 81, 83),  # B7
    (77, 79, 82, 84),  # C7
]

for i, chord in enumerate(chords):
    start = bar2_start + (i * beat_time)
    if i == 1 or i == 3:  # comp on 2 and 4
        for pitch in chord:
            piano.notes.append(pretty_midi.Note(velocity, pitch, start, start + 0.25))

# Sax: Melody motif — F, Bb, B, D — starts on beat 1, ends on beat 3, leaves it hanging
sax_notes = [
    (71, bar2_start, bar2_start + note_duration),  # F
    (74, bar2_start + beat_time, bar2_start + beat_time + note_duration),  # Bb
    (76, bar2_start + 2 * beat_time, bar2_start + 2 * beat_time + note_duration),  # B
    (79, bar2_start + 2 * beat_time, bar2_start + 2 * beat_time + note_duration / 2),  # D (half note)
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, pitch, start, end))

# Bar 3: Drums continue
bar3_start = 2 * bar_time

# Kick on 1
drums.notes.append(pretty_midi.Note(velocity, 36, bar3_start, bar3_start + 0.1))  # Kick

# Snare on 2
drums.notes.append(pretty_midi.Note(velocity, 38, bar3_start + beat_time, bar3_start + beat_time + 0.1))  # Snare

# Hats on every eighth
for i in range(0, 8):
    time = bar3_start + (i * beat_time / 2)
    drums.notes.append(pretty_midi.Note(velocity, 42, time, time + 0.05))  # Hihat

# Bar 4: Sax continues, Bass continues, Piano continues

bar4_start = 3 * bar_time

# Bass: Walking line (continuation of the sequence)
bass_notes = [71, 72, 74, 75]  # F, G, A, Bb
for i, pitch in enumerate(bass_notes):
    start = bar4_start + (i * beat_time)
    end = start + note_duration
    bass.notes.append(pretty_midi.Note(velocity, pitch, start, end))

# Piano: 7th chords, comp on 2 and 4
# Chord sequence: F7, Bb7, B7, C7 (repeat of Bar 2)
for i, chord in enumerate(chords):
    start = bar4_start + (i * beat_time)
    if i == 1 or i == 3:
        for pitch in chord:
            piano.notes.append(pretty_midi.Note(velocity, pitch, start, start + 0.25))

# Sax: Continue the motif, resolve on beat 4
sax_notes = [
    (79, bar4_start + 2 * beat_time, bar4_start + 3 * beat_time),  # D to end of bar
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, pitch, start, end))

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file created: 'dante_intro.mid'")
