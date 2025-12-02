
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instrument assignments
# 1. Drums (Little Ray)
drums = pretty_midi.Instrument(program=128)
pm.instruments.append(drums)

# 2. Bass (Marcus)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# 3. Piano (Diane)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# 4. Tenor Sax (You)
sax = pretty_midi.Instrument(program=64)
pm.instruments.append(sax)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# BPM: 160
pm.instruments[0].tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Bar 1: Drums only — sparse, rhythmic tension
# Kick on 1 and 3, snare on 2 and 4, hihat open on every 8th
# Time per bar: 1.5 seconds (since 160 BPM, 60/160 = 0.375s per beat, 4 beats = 1.5s)
# So 1 bar = 1.5s

# Bar 1: 0.0 to 1.5s
# Kick on 0.0 and 0.75s (beats 1 and 3)
# Snare on 0.375 and 1.125s (beats 2 and 4)
# Hihat on every 8th: 0.0, 0.375, 0.75, 1.125, 1.5s (but stop before 1.5s)
for t in [0.0, 0.375, 0.75, 1.125]:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)  # Hihat
    drums.notes.append(note)
for t in [0.0, 0.75]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)  # Kick
    drums.notes.append(note)
for t in [0.375, 1.125]:
    note = pretty_midi.Note(velocity=100, pitch=48, start=t, end=t + 0.1)  # Snare
    drums.notes.append(note)

# Bar 2: Full ensemble enters
# Start at 1.5s (Bar 2)

# Marcus: Walking bass line - D2-G2, roots and fifths with chromatic approaches
# D2 = 38, G2 = 43 — D (38), D# (39), G (43), G# (44), D (38), D# (39), G (43), G# (44)
# Bar 2: D2, D#, G2, G#, D2, D#, G2, G#
# Bar 3: D2, D#, G2, G#, D2, D#, G2, G#
# Bar 4: D2, D#, G2, G#, D2, D#, G2, G#

for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        step = i % 4
        if step == 0:
            pitch = 38  # D2
        elif step == 1:
            pitch = 39  # D#
        elif step == 2:
            pitch = 43  # G2
        elif step == 3:
            pitch = 44  # G#
        note = pretty_midi.Note(velocity=85, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1)
        bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Bb7 (Bb, D, F, Ab)
# Comp on 2 and 4

# Bar 2
chord = [62, 67, 69, 72]  # Dmaj7
for beat in [1, 3]:
    start = 1.5 + beat * 0.375
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
        piano.notes.append(note)

# Bar 3
chord = [67, 71, 69, 64]  # Gm7
for beat in [1, 3]:
    start = 3.0 + beat * 0.375
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
        piano.notes.append(note)

# Bar 4
chord = [62, 67, 69, 70]  # Bb7 (from Cmaj7, but D is the key)
for beat in [1, 3]:
    start = 4.5 + beat * 0.375
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
        piano.notes.append(note)

# You: Tenor Sax — a short, haunting motif that starts, lingers, and returns

# Bar 2: Start the motif at 1.5s
# Motif: E4 (64), C#5 (70), B4 (71), rest — then repeat
# Bar 3: repeat the motif
# Bar 4: repeat the motif, then end with a lingering note

# Bar 2
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.7, end=1.8)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.9, end=2.0)
sax.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=3.1, end=3.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.3, end=3.4)
sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=70, start=4.6, end=4.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.8, end=5.0)
sax.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro.mid')
print("Generated 'jazz_intro.mid' — your shot at Wayne.")
