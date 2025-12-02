
import pretty_midi
from pretty_midi import Note, NoteSequence

# Initialize the MIDI file with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time per beat in seconds
tempo = 60.0 / 160  # seconds per beat

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Double Bass
piano = pretty_midi.Instrument(program=0)    # Acoustic Piano
sax = pretty_midi.Instrument(program=64)     # Tenor Sax

pm.instruments = [drums, bass, piano, sax]

# Bar duration in seconds (160 BPM, 4/4 time)
bar_duration = 4 * tempo
total_duration = 4 * bar_duration

# ==================
# DRUMS: Little Ray
# ==================
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
for bar in range(4):
    for beat in [0, 2]:  # 1st and 3rd beat
        kick_time = bar * bar_duration + beat * tempo
        drums.notes.append(Note(36, 100, kick_time, kick_time + 0.1))
    for beat in [1, 3]:  # 2nd and 4th beat
        snare_time = bar * bar_duration + beat * tempo
        drums.notes.append(Note(38, 100, snare_time, snare_time + 0.1))
    for eighth in range(8):  # Every eighth note
        hihat_time = bar * bar_duration + (eighth * tempo / 2)
        hihat_velocity = 80 if eighth % 2 == 0 else 60  # Alternate velocity for rhythm
        drums.notes.append(Note(42, hihat_velocity, hihat_time, hihat_time + 0.05))

# ==================
# BASS: Marcus (Walking Line)
# ==================
# D major scale: D, E, F#, G, A, B, C#, D
# Walking line with chromatic approach
# We are in 4 bars, so 16 beats
# Let's build a walking line with chromatic approaches
bass_notes = [
    # Bar 1
    [45, 46, 47, 49, 50, 52, 53, 54],  # D, E, F#, G, A, B, C#, D
    # Bar 2
    [54, 52, 50, 49, 47, 46, 45, 43],  # D, C#, B, A, G, F#, E, D-
    # Bar 3
    [43, 45, 46, 47, 49, 50, 52, 53],  # D-, D, E, F#, G, A, B, C#
    # Bar 4
    [53, 52, 50, 49, 47, 46, 45, 43],  # C#, B, A, G, F#, E, D, D-
]

for bar in range(4):
    for beat in range(8):
        note = bass_notes[bar][beat]
        start = bar * bar_duration + (beat * tempo / 2)
        end = start + (tempo / 2)
        bass.notes.append(Note(note, 80, start, end))

# ==================
# PIANO: Diane (Comp on 2 & 4 with 7th chords)
# ==================
# D7: D, F#, A, C
# G7: G, B, D, F
# A7: A, C#, E, G
# B7: B, D#, F#, A

# Bar 1: D7 on 2 & 4
for beat in [1, 3]:
    time = beat * tempo
    piano.notes.append(Note(62, 100, time, time + 0.1))
    piano.notes.append(Note(67, 100, time, time + 0.1))
    piano.notes.append(Note(71, 100, time, time + 0.1))
    piano.notes.append(Note(69, 100, time, time + 0.1))

# Bar 2: G7 on 2 & 4
for beat in [1, 3]:
    time = (1 * bar_duration) + (beat * tempo)
    piano.notes.append(Note(67, 100, time, time + 0.1))
    piano.notes.append(Note(71, 100, time, time + 0.1))
    piano.notes.append(Note(72, 100, time, time + 0.1))
    piano.notes.append(Note(69, 100, time, time + 0.1))

# Bar 3: A7 on 2 & 4
for beat in [1, 3]:
    time = (2 * bar_duration) + (beat * tempo)
    piano.notes.append(Note(71, 100, time, time + 0.1))
    piano.notes.append(Note(76, 100, time, time + 0.1))
    piano.notes.append(Note(79, 100, time, time + 0.1))
    piano.notes.append(Note(77, 100, time, time + 0.1))

# Bar 4: B7 on 2 & 4
for beat in [1, 3]:
    time = (3 * bar_duration) + (beat * tempo)
    piano.notes.append(Note(73, 100, time, time + 0.1))
    piano.notes.append(Note(77, 100, time, time + 0.1))
    piano.notes.append(Note(80, 100, time, time + 0.1))
    piano.notes.append(Note(79, 100, time, time + 0.1))

# ==================
# SAX: You (Short motif, emotional, mysterious)
# ==================
# D (D4) -> F# (F#4) -> A (A4) -> D (D4) -> F# (F#4) -> G# (G#4) -> A (A4) -> D (D4)
# This phrase starts on the last beat of bar 1, then continues into bars 2-4
# D4 = 62, F#4 = 67, A4 = 71, G#4 = 70

sax_notes = [
    (62, 0.3), (67, 0.3), (71, 0.3),
    (62, 0.3), (67, 0.3), (70, 0.3), (71, 0.3), (62, 0.3)
]

# Start at the last beat of bar 1
start_time = bar_duration * 3 + (tempo / 2)
for i in range(len(sax_notes)):
    note, duration = sax_notes[i]
    sax.notes.append(Note(note, 110, start_time + i * tempo / 2, start_time + i * tempo / 2 + duration))

# Save the MIDI file
pm.write("jazz_intro_d_major.mid")

print("MIDI file created: jazz_intro_d_major.mid")
