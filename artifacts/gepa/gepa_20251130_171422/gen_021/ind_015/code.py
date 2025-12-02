
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures for 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key as D minor (Dm)
# Dm = D, F, A (scale degrees 1, b3, 5)

# Instrument: Tenor Sax (program 64)
sax = pretty_midi.Instrument(program=64)
pm.instruments.append(sax)

# Instrument: Bass (program 33)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Instrument: Piano (program 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Instrument: Drums (program 10)
drums = pretty_midi.Instrument(program=10)
pm.instruments.append(drums)

# Define tempo and beats per bar
bpm = 160
beat_time = 60.0 / bpm  # seconds per beat
bar_time = beat_time * 4  # 4/4 time, 4 beats per bar

# Map drum notes to MIDI numbers
kick = 36  # Kick drum
snare = 38  # Snare drum
hihat = 42  # Closed hihat
cymbal = 49  # Crash cymbal

# Bar 1: Little Ray (drums) alone. Build tension.
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0
bar1_end = bar_time
for beat in [0, 2]:  # kick on 1 and 3
    time = bar1_start + beat * beat_time
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
    drums.notes.append(note)
for beat in [1, 3]:  # snare on 2 and 4
    time = bar1_start + beat * beat_time
    note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.1)
    drums.notes.append(note)
for beat in range(4):  # hihat on every eighth
    time = bar1_start + beat * beat_time / 2
    note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2: Everyone in. Tenor sax takes the melody.
bar2_start = bar1_end
bar2_end = bar1_end + bar_time

# Tenor sax: short, emotive motif starting on Dm (D, F, A), ascending with tension
# Motif: D (D4) -> F (F4) -> A (A4) -> C (C5) -> Bb (Bb4)
notes = [
    (4, 100, bar2_start, bar2_start + 0.3),   # D4
    (5, 100, bar2_start + 0.3, bar2_start + 0.6),  # F4
    (9, 95, bar2_start + 0.6, bar2_start + 0.9),   # A4
    (12, 100, bar2_start + 0.9, bar2_start + 1.2),  # C5
    (10, 90, bar2_start + 1.2, bar2_start + 1.5),   # Bb4
]
for pitch, velocity, start, end in notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 60, start=start, end=end)
    sax.notes.append(note)

# Bass: Walking line, chromatic approach to Dm
# Dm7: D, F, A, C
bass_notes = [
    (2, 90, bar2_start, bar2_start + 0.25),  # D (D2)
    (3, 90, bar2_start + 0.25, bar2_start + 0.5),  # Eb (chromatic approach)
    (5, 95, bar2_start + 0.5, bar2_start + 0.75),  # F (F2)
    (7, 90, bar2_start + 0.75, bar2_start + 1.0),  # G (chromatic approach)
    (9, 90, bar2_start + 1.0, bar2_start + 1.25),  # A (A2)
    (10, 90, bar2_start + 1.25, bar2_start + 1.5),  # Bb (chromatic approach)
]
for pitch, velocity, start, end in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (comping)
# Dm7 = D, F, A, C (chord on beat 2 and 4)
piano_notes = [
    (2, 100, bar2_start + 0.5, bar2_start + 0.75),  # D (D4)
    (5, 100, bar2_start + 0.5, bar2_start + 0.75),  # F (F4)
    (9, 100, bar2_start + 0.5, bar2_start + 0.75),  # A (A4)
    (12, 100, bar2_start + 0.5, bar2_start + 0.75),  # C (C5)
    (2, 100, bar2_start + 1.5, bar2_start + 1.75),  # D (D4)
    (5, 100, bar2_start + 1.5, bar2_start + 1.75),  # F (F4)
    (9, 100, bar2_start + 1.5, bar2_start + 1.75),  # A (A4)
    (12, 100, bar2_start + 1.5, bar2_start + 1.75),  # C (C5)
]
for pitch, velocity, start, end in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    piano.notes.append(note)

# Bar 3 & 4: Variation of the motif, resolution and space
bar3_start = bar2_end
bar4_start = bar3_start + bar_time
bar4_end = bar4_start + bar_time

# Tenor sax: variation, slightly resolving
notes = [
    (4, 105, bar4_start, bar4_start + 0.3),   # D4
    (5, 105, bar4_start + 0.3, bar4_start + 0.6),   # F4
    (9, 90, bar4_start + 0.6, bar4_start + 0.9),    # A4
    (12, 105, bar4_start + 0.9, bar4_start + 1.2),  # C5
    (9, 95, bar4_start + 1.2, bar4_start + 1.5),    # A4 (resolution)
]
for pitch, velocity, start, end in notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 60, start=start, end=end)
    sax.notes.append(note)

# Bass: Walking line to Dm again, resolving
bass_notes = [
    (2, 90, bar4_start, bar4_start + 0.25),  # D (D2)
    (3, 90, bar4_start + 0.25, bar4_start + 0.5),  # Eb (chromatic)
    (5, 95, bar4_start + 0.5, bar4_start + 0.75),  # F (F2)
    (7, 90, bar4_start + 0.75, bar4_start + 1.0),  # G (chromatic)
    (9, 90, bar4_start + 1.0, bar4_start + 1.25),  # A (A2)
    (10, 90, bar4_start + 1.25, bar4_start + 1.5),  # Bb (chromatic)
]
for pitch, velocity, start, end in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    bass.notes.append(note)

# Piano: resolve on Dm7 again
piano_notes = [
    (2, 100, bar4_start + 0.5, bar4_start + 0.75),  # D (D4)
    (5, 100, bar4_start + 0.5, bar4_start + 0.75),  # F (F4)
    (9, 100, bar4_start + 0.5, bar4_start + 0.75),  # A (A4)
    (12, 100, bar4_start + 0.5, bar4_start + 0.75),  # C (C5)
    (2, 100, bar4_start + 1.5, bar4_start + 1.75),  # D (D4)
    (5, 100, bar4_start + 1.5, bar4_start + 1.75),  # F (F4)
    (9, 100, bar4_start + 1.5, bar4_start + 1.75),  # A (A4)
    (12, 100, bar4_start + 1.5, bar4_start + 1.75),  # C (C5)
]
for pitch, velocity, start, end in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    piano.notes.append(note)

# Drums: Bar 3 and 4 continue with same pattern
for bar in [3, 4]:
    bar_start = bar2_end + (bar - 2) * bar_time
    for beat in [0, 2]:
        time = bar_start + beat * beat_time
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        time = bar_start + beat * beat_time
        note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        time = bar_start + beat * beat_time / 2
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.05)
        drums.notes.append(note)

# Save the MIDI file
pm.write("Dante_Whisper_Intro.mid")
print("MIDI file generated: Dante_Whisper_Intro.mid")
