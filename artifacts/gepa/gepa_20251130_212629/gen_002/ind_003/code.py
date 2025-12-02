
import pretty_midi
import numpy as np

# Create a MIDI file object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature and key (Dm7 = D minor with 7th)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)   # Bass
piano = pretty_midi.Instrument(program=0)  # Piano
sax = pretty_midi.Instrument(program=64)   # Tenor Sax

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Time per bar in seconds (160 BPM = 60 / 160 = 0.375 sec per beat, 4/4 time)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar

# Bar 1: Drums only (Little Ray)
bar_start = 0
bar_end = bar

# Kick on 1 and 3
for beat_idx in [0, 2]:
    kick_time = bar_start + beat_idx * beat
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4
for beat_idx in [1, 3]:
    snare_time = bar_start + beat_idx * beat
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

# Hi-hat on every 8th note
for i in range(0, 4):
    hihat_time = bar_start + i * beat / 2
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bar 2–4: Full ensemble

# Define the key (Dm7)
base_key = 2  # C = 0, D = 2

# Bass line (Marcus) - chromatic walking line
bass_notes = [
    2, 1, 3, 4, 5, 4, 3, 2,  # Dm7 chromatic walking
    2, 1, 3, 4, 5, 4, 3, 2,
    2, 1, 3, 4, 5, 4, 3, 2,
    2, 1, 3, 4, 5, 4, 3, 2,
]

bass_times = [bar_start + beat * i for i in range(len(bass_notes))]
for t, n in zip(bass_times, bass_notes):
    note = pretty_midi.Note(velocity=100, pitch=n + base_key, start=t, end=t + beat)
    bass.notes.append(note)

# Diane's piano comping (7th chords on 2 and 4)
# Dm7 = D, F, A, C
# Chord durations: 2 beats
chord_notes = {
    0: [2, 5, 7, 10],  # Dm7
    1: [2, 5, 7, 10],
    2: [2, 5, 7, 10],
    3: [2, 5, 7, 10],
}

note_velocity = 100
for beat_idx in [1, 3]:
    for root in chord_notes.get(beat_idx, []):
        time = bar_start + beat_idx * beat
        note = pretty_midi.Note(velocity=note_velocity, pitch=root + base_key, start=time, end=time + 0.5)
        piano.notes.append(note)

# Tenor sax motif (You) - unique, melodic, tension and release
# Motif: D, F#, A, D (melodic minor), rest on beat 3
sax_notes = [2, 5, 7, 2]  # D, F#, A, D (D melodic minor)
sax_times = [bar_start + beat * i for i in [0, 0.5, 1, 1.5]]
sax_durations = [0.3, 0.3, 0.3, 0.5]  # End of last note on beat 2 (beat 1.5)

for t, n, d in zip(sax_times, sax_notes, sax_durations):
    note = pretty_midi.Note(velocity=110, pitch=n + base_key, start=t, end=t + d)
    sax.notes.append(note)

# Write the MIDI file
pm.write("dante_intro.mid")
print("Generated 'dante_intro.mid'")
