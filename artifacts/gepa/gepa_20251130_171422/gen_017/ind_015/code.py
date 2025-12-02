
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDICreator()
pm.time_signature_changes = [pretty_midi.TimeSignature(time_signature[0], time_signature[1], 0)]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo, 0)]

# Define note durations (in seconds)
note_duration = 0.375  # 1/16th note at 160 BPM
bar_length = 6.0  # 4 bars = 6 seconds at 160 BPM

# Define the key: D minor (D, Eb, F, G, Ab, Bb, C)
# MIDI note numbers for D minor scale
Dm_notes = [62, 63, 65, 67, 68, 70, 72]  # D, Eb, F, G, Ab, Bb, C

# --- Bar 1: Drums only ---
# Little Ray
drums = pretty_midi.Instrument(program=10)  # Drums

# Kick on 1 and 3 (beats 0 and 2 in bar 1)
kick_notes = [36, 36]  # Kick drum is note 36
kick_times = [0.0, note_duration * 2.0]  # Beat 1 and 3
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Snare on 2 and 4 (beats 1 and 3 in bar 1)
snare_notes = [38, 38]  # Snare drum is note 38
snare_times = [note_duration, note_duration * 3.0]
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Hi-hat on every eighth (8 notes per bar)
hihat_note = 42  # Hi-hat is note 42
hihat_times = [note_duration * i for i in range(8)]
for time in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat_note, start=time, end=time + 0.05))

pm.instruments.append(drums)

# --- Bar 2: Full Band Enters ---
# Bass (Marcus)
bass = pretty_midi.Instrument(program=33)  # Upright Bass
# Walking bass line: D, Eb, F, G, Ab, Bb, C, D
bass_notes = [62, 63, 65, 67, 68, 70, 72, 62]
bass_times = [note_duration * i for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_duration))

pm.instruments.append(bass)

# Piano (Diane)
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano

# 7th chords, comp on 2 and 4
# Bar 2: Dm7
Dm7 = [62, 67, 71, 70]  # D, F, A, Bb
piano_notes = Dm7
piano_times = [note_duration * 1.0, note_duration * 3.0]  # Beats 2 and 4
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1))

# Bar 3: Gm7
Gm7 = [67, 72, 76, 75]  # G, Bb, D, Eb
piano_notes = Gm7
piano_times = [note_duration * 1.0, note_duration * 3.0]  # Beats 2 and 4
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time + bar_length / 2, end=time + 0.1 + bar_length / 2))

# Bar 4: Cm7
Cm7 = [60, 65, 69, 68]  # C, Eb, G, Ab
piano_notes = Cm7
piano_times = [note_duration * 1.0, note_duration * 3.0]  # Beats 2 and 4
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time + bar_length * 1.5, end=time + 0.1 + bar_length * 1.5))

pm.instruments.append(piano)

# --- Tenor Sax (You) ---
# Start with a short, expressive motif in D minor
# Bar 2: Start of motif
# D (62), Eb (63), F (65), Eb (63), D (62)
sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone

sax_notes = [62, 63, 65, 63, 62]
sax_times = [note_duration * 1.0, note_duration * 1.5, note_duration * 2.0, note_duration * 2.5, note_duration * 3.0]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration))

# Bar 4: Resolve the motif
# Play the same motif again but resolve with a Bb (70)
# D, Eb, F, Eb, Bb
sax_notes = [62, 63, 65, 63, 70]
sax_times = [note_duration * 5.0, note_duration * 5.5, note_duration * 6.0, note_duration * 6.5, note_duration * 7.0]
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration))

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
