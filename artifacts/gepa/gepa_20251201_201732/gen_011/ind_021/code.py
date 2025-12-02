
import pretty_midi

# Initialize the MIDI file and set tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track = pretty_midi.Instrument(program=64)  # Tenor sax (program 64)

# Time constants
beat = 0.375  # seconds per beat at 160 BPM
bar = 1.5     # seconds per bar (4 beats)
time = 0.0

# ---------------------------
# Bar 1: Little Ray (Drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# ---------------------------

# Kick on 1 and 3
kick_notes = [36, 36]  # C2
kick_times = [time, time + 2 * beat]

# Snare on 2 and 4
snare_notes = [38, 38]  # D2
snare_times = [time + beat, time + 3 * beat]

# Hihat on every eighth note (8 notes per bar)
hihat_notes = [42] * 8  # F#2
hihat_times = [time + i * beat / 2 for i in range(8)]

# Add drum notes to the track
for note, time in zip(kick_notes, kick_times):
    track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(snare_notes, snare_times):
    track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    track.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05))

# ---------------------------
# Bar 2: Diane (Piano) – Open voicings, different chords each bar
# ---------------------------

# Bar 2: F7 (F, A, C, E)
chord_notes = [72, 76, 79, 82]  # F4, A4, C5, E5
chord_time = time + beat * 2
track.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=chord_time, end=chord_time + 0.5))
track.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=chord_time, end=chord_time + 0.5))
track.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=chord_time, end=chord_time + 0.5))
track.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=chord_time, end=chord_time + 0.5))

# ---------------------------
# Bar 3: Marcus (Bass) – Walking line with chromatic approaches
# ---------------------------

# F2-G2 (root to fifth) with chromatic approaches
# F2 (53), F#2 (54), G2 (55), G#2 (56), A2 (57), etc.
# Use a walking line with chromatic approaches
bass_notes = [53, 54, 55, 56]
bass_times = [time + beat * 3, time + beat * 3 + beat / 2, time + beat * 3 + beat, time + beat * 3 + 1.5 * beat]

for note, t in zip(bass_notes, bass_times):
    track.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=t, end=t + 0.3))

# ---------------------------
# Bar 4: You (Tenor Sax) – One short motif, make it sing
# ---------------------------

# You start with a motif: F (72), G (74), F (72), E (71)
# Let it hang on the last note (E)

motif_notes = [72, 74, 72, 71]
motif_times = [time + beat * 3, time + beat * 3 + beat / 2, time + beat * 3 + beat, time + beat * 3 + 1.5 * beat]

for note, t in zip(motif_notes, motif_times):
    track.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=t, end=t + 0.3))

# ---------------------------
# Add the track to the MIDI file and save
# ---------------------------

midi.instruments.append(track)
midi.write("dante_intro.mid")
print("Generated: dante_intro.mid")
