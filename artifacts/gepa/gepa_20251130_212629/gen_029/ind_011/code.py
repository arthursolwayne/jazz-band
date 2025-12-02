
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
midi = pretty_midi.PrettyMidi(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature to F major
midi.key_signature_changes = [pretty_midi.KeySignature(0, 0)]

# Define note values in F major
# F major scale: F, G, A, Bb, C, D, E
note_piano = {
    'F': 65,
    'G': 67,
    'A': 69,
    'Bb': 68,
    'C': 72,
    'D': 74,
    'E': 76
}

# Define instruments
program_saxophone = 64  # Tenor Sax
program_piano = 0       # Acoustic Piano
program_bass = 33       # Double Bass
program_drums = 0       # Acoustic Drums

# Create instrument tracks
sax_track = pretty_midi.Instrument(program=program_saxophone)
piano_track = pretty_midi.Instrument(program=program_piano)
bass_track = pretty_midi.Instrument(program=program_bass)
drums_track = pretty_midi.Instrument(program=program_drums)

# Helper function to add note with slight variation in timing and velocity
def add_note(track, pitch, start, duration, velocity=100, variation=0.02):
    note = pretty_midi.Note(
        velocity=int(velocity * (1 + np.random.uniform(-variation, variation))),
        pitch=pitch,
        start=start + np.random.uniform(-variation, variation),
        end=start + duration + np.random.uniform(-variation, variation)
    )
    track.notes.append(note)

# Time per bar in seconds (160 BPM, 4/4 time)
bar_length = 60.0 / 160 * 4  # 1.5 seconds per bar
beat_length = bar_length / 4  # 0.375 seconds per beat

# Bar 1: Drums only — build anticipation
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beat 1
add_note(drums_track, 36, 0.0, 0.1, velocity=100)
# Kick on beat 3
add_note(drums_track, 36, 2 * beat_length, 0.1, velocity=100)
# Snare on beat 2
add_note(drums_track, 38, beat_length, 0.1, velocity=80)
# Snare on beat 4
add_note(drums_track, 38, 3 * beat_length, 0.1, velocity=80)
# Hi-hat on every eighth note
for i in range(8):
    add_note(drums_track, 42, i * (beat_length / 2), 0.05, velocity=80)

# Bar 2: Bass enters with walking line
# Chromatic approaches, never the same note twice
# F -> Gb -> G -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F
bass_notes = [65, 66, 67, 69, 68, 70, 72, 71, 74, 73, 76, 65]
for i, pitch in enumerate(bass_notes):
    add_note(bass_track, pitch, i * (beat_length / 2), 0.2)

# Bar 2: Piano enters with 7th chords on 2 and 4
# F7, Bb7, D7, G7
# On beat 2 and 4
piano_notes = [
    # F7 (F, A, C, Eb)
    [65, 69, 72, 67],
    # Bb7 (Bb, D, F, Ab)
    [68, 74, 65, 66],
    # D7 (D, F#, A, C)
    [74, 77, 69, 72],
    # G7 (G, B, D, F)
    [67, 71, 74, 65]
]
for i, chord in enumerate(piano_notes):
    for note in chord:
        add_note(piano_track, note, (i + 1) * beat_length, 0.5, velocity=80)

# Bar 2-4: Sax melody — short motif, leave it hanging
# Start on F, move to Bb, then to D
# Use rests to create space and tension

# First note: F (65) on beat 1
add_note(sax_track, 65, 0.0, 0.25, velocity=110)

# Rest on beat 2 (create suspense)
# No note

# Second note: Bb (68) on beat 3
add_note(sax_track, 68, 2 * beat_length, 0.25, velocity=110)

# Rest on beat 4 (end with a question)
# No note

# End of intro — the last note is Bb, hanging, waiting for the next bar

# Add tracks to the MIDI file
midi.instruments = [sax_track, piano_track, bass_track, drums_track]

# Save the MIDI file
midi.write("waynes_moment.mid")

print("MIDI file saved as 'waynes_moment.mid'")
