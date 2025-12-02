
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_drums = pretty_midi.Instrument(program=10)
track_bass = pretty_midi.Instrument(program=33)
track_piano = pretty_midi.Instrument(program=0)
track_sax = pretty_midi.Instrument(program=64)

# Time per bar in seconds
bar_length = 6.0 / 4  # 1.5 seconds per bar
tempo = 160  # BPM
note_length = 0.375  # 1/16th note in seconds (since 60 / 160 = 0.375)

# Time division for 16th notes
time = 0.0

# Define a scale in F major (F, G, A, Bb, C, D, E)
F_major = [72, 74, 76, 77, 79, 81, 83]  # MIDI notes for F (C4 = 60, F4 = 72)

# --- DRUMS (Little Ray) ---
# Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
for bar in range(4):
    time = bar * bar_length
    # Kick on 1 and 3
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_length))
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 2 * note_length, end=time + 3 * note_length))
    # Snare on 2 and 4
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + note_length, end=time + 2 * note_length))
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 3 * note_length, end=time + 4 * note_length))
    # Hihat on every 8th
    for i in range(4):
        track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * note_length, end=time + i * note_length + 0.125))

# --- BASS (Marcus) --- Walking line
# A chromatic walking line in F major with tension
bass_notes = [
    72, 73, 74, 77,  # F, F#, G, Bb
    79, 80, 81, 77,  # C, C#, D, Bb
    72, 73, 74, 77,  # F, F#, G, Bb
    79, 80, 81, 77   # C, C#, D, Bb
]
for i, note in enumerate(bass_notes):
    track_bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=i * note_length, end=i * note_length + note_length))

# --- PIANO (Diane) --- 7th chords on 2 & 4
# F7 (F, A, C, Eb) on 2 & 4
def play_chord(chord, time):
    for note in chord:
        track_piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_length))

# F7
F7 = [72, 76, 79, 77]
for bar in range(4):
    time = bar * bar_length + 2 * note_length
    play_chord(F7, time)
    time = bar * bar_length + 4 * note_length
    play_chord(F7, time)

# --- SAX (You) --- A short motif: F -> A -> Bb -> C -> F (no scale runs, expressive)
sax_notes = [72, 76, 77, 79, 72]  # F, A, Bb, C, F
for i, note in enumerate(sax_notes):
    start = i * note_length
    end = start + note_length
    track_sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments = [track_drums, track_bass, track_piano, track_sax]

# Save the MIDI file
midi.write("jazz_intro.mid")
