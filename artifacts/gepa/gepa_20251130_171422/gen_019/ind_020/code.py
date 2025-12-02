
import pretty_midi
import numpy as np

# Create a PrettyMIDI object at 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time per bar (in seconds)
time_per_bar = 6.0  # 6 seconds per 4 bars = 1.5 seconds per bar
time_per_beat = time_per_bar / 4  # 0.375 seconds per beat
note_duration = time_per_beat / 2  # 0.1875 seconds per half note

# Define Fm7 chord (F, Ab, C, Eb) in MIDI note numbers
Fm7 = [64, 68, 72, 76]  # F, Ab, C, Eb

# Set up instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Use piano for drums (no drummap)

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# --- DRUMS: Bar 1 (Little Ray) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in [0]:  # Only bar 1
    for beat in [0, 2]:  # Kick on 1 and 3
        time = bar * time_per_bar + beat * time_per_beat
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_duration)
        drums.notes.append(kick)
    for beat in [1, 3]:  # Snare on 2 and 4
        time = bar * time_per_bar + beat * time_per_beat
        snare = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + note_duration)
        drums.notes.append(snare)
    for eighth in range(0, 8):  # Hihat on every eighth
        time = bar * time_per_bar + eighth * (time_per_beat / 2)
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + note_duration / 2)
        drums.notes.append(hihat)

# --- BASS: Walking line (Marcus) ---
# Bar 1: Chromatic approach to F
# Bar 2: Fm7 walking line
# Bar 3: chromatic descending
# Bar 4: chromatic ascending

# Bar 1: Fm7 chromatic approach
bass_notes = [
    [63, 64, 68, 72, 76],  # Bar 1 (chromatic approach)
    [72, 76, 77, 71],      # Bar 2 (walking line)
    [71, 68, 67, 64],      # Bar 3 (chromatic desc)
    [64, 65, 68, 72],      # Bar 4 (chromatic asc)
]

for bar_idx, notes in enumerate(bass_notes):
    for note_idx, pitch in enumerate(notes):
        time = bar_idx * time_per_bar + note_idx * time_per_beat
        duration = time_per_beat
        bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
        bass.notes.append(bass_note)

# --- PIANO: Diane (comping on 2 and 4 with Fm7 chords) ---
# 7th chords on beats 2 and 4 (every bar)
comping_notes = [Fm7] * 4  # Fm7 on 2 and 4 of each bar

for bar_idx in range(4):
    for beat in [1, 3]:  # Beat 2 and 4
        time = bar_idx * time_per_bar + beat * time_per_beat
        for pitch in comping_notes[bar_idx]:
            note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + note_duration)
            piano.notes.append(note)

# --- TENOR SAX: Dante (melody) ---
# Start with a short motif:
# Bar 2 - 1st beat: F (64)
# Bar 2 - 2nd beat: Ab (68)
# Bar 2 - 3rd beat: G (67)
# Bar 2 - 4th beat: F (64)
# Then hold on F (64) for the rest of the bar
# Bar 3: leave a rest
# Bar 4: repeat the motif and resolve

melody_notes = [
    [64, 68, 67, 64],     # Bar 2
    [],                   # Bar 3 (rest)
    [64, 68, 67, 64],     # Bar 4
]

for bar_idx, notes in enumerate(melody_notes):
    for note_idx, pitch in enumerate(notes):
        time = (bar_idx + 1) * time_per_bar + note_idx * time_per_beat  # Start at Bar 2
        duration = time_per_beat
        sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
        piano.notes.append(sax_note)  # Using piano for melody (sax is a melody instrument)

# Add the instruments to the PrettyMIDI object
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Save the MIDI file
pm.write("dante_intro.mid")
