
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
drums = pretty_midi.Instrument(program=0)  # Drums
bass = pretty_midi.Instrument(program=33)   # Bass
piano = pretty_midi.Instrument(program=0)  # Piano
sax = pretty_midi.Instrument(program=64)   # Tenor Sax

pm.instruments = [drums, bass, piano, sax]

# Tempo: 160 BPM => 1 beat = 0.375 seconds, 1 bar = 1.5 seconds
# Time per bar = 1.5 seconds
# Bar = 1.5 seconds = 6 beats

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 - 1.5 seconds
# Time per beat = 0.375s

for i in range(4):
    time = i * 0.375
    # Kick on 1 and 3
    if i in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2: Bass, Piano, Sax enter

# Bass: Walking line in Dm, chromatic approaches, never repeating same note
# Dm = D, F, A, C
# Walking line with chromatic passing tones

# Bar 2 (beats 1-4: 1.5 - 3.0 seconds)
# Dm7 chord = D, F, A, C (but bass is walking)
bass_notes = [62, 61, 60, 59, 60, 61, 62, 63]  # D, C#, C, B, C, C#, D, D#
for i, pitch in enumerate(bass_notes):
    time_start = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time_start, end=time_start + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 in root position: D (62), F (65), A (69), C (60)
# Comp on 2 and 4 (each beat is 0.375s)
# Bar 2: beat 2 = 1.5 + 0.375 = 1.875
# beat 4 = 1.5 + 3 * 0.375 = 2.625

# Dm7 chord
chord_notes = [62, 65, 69, 60]
for i in [1, 3]:
    time_start = 1.5 + i * 0.375
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time_start, end=time_start + 0.125)
        piano.notes.append(note)

# Sax: Your solo idea — a short motif, make it sing, start it, leave it hanging

# Motif: D (62) -> F (65) -> C (60) -> B (59) -> A (69)
# Play the first three notes in bar 2, leave the last two hanging

# Bar 2 (1.5 - 3.0 seconds)
# Play first 3 notes (D, F, C)
for i, pitch in enumerate([62, 65, 60]):
    time_start = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_start, end=time_start + 0.125)
    sax.notes.append(note)

# Bar 3: Continue the motif
# Play next two notes (B, A) but only half the duration
for i, pitch in enumerate([59, 69]):
    time_start = 1.5 + 3 * 0.375 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_start, end=time_start + 0.0625)
    sax.notes.append(note)

# Bar 4: Let it hang — no resolution, leave the question
# Play the last note (A) again, staccato, and cut it off
note = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.625 + 0.0625)
sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file written as 'jazz_intro.mid'")
