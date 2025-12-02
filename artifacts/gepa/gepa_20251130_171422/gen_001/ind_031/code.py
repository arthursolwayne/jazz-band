
import pretty_midi
import numpy as np

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key: F Major (pitch class 6)
key = 'F'
key_number = pretty_midi.note_number_to_name(69).split('/')[0]  # F4

# Define duration in seconds for 4 bars (160 BPM = 1.5 seconds per bar)
bar_duration = 1.5
total_duration = 4 * bar_duration

# Tracks
track_sax = pretty_midi.Instrument(program=64)  # Tenor Sax
track_piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
track_bass = pretty_midi.Instrument(program=33)  # Electric Bass
track_drums = pretty_midi.Instrument(program=10)  # Acoustic Drums

pm.instruments = [track_sax, track_piano, track_bass, track_drums]

# --- BAR 1: DRUMS ONLY (TENSION) ---
# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
bar1_start = 0.0
bar1_end = bar_duration

# Kick on 1 and 3
kick_notes = [36, 36]  # C2
kick_times = [bar1_start + 0.0, bar1_start + 0.75]  # 1 and 3
for note, time in zip(kick_notes, kick_times):
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Snare on 2 and 4
snare_notes = [38, 38]  # D2
snare_times = [bar1_start + 0.375, bar1_start + 1.125]  # 2 and 4
for note, time in zip(snare_notes, snare_times):
    track_drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1))

# Hi-hat on every 8th
hihat_notes = [42] * 8  # G2 (hi-hat)
hihat_times = [bar1_start + 0.0, bar1_start + 0.375, bar1_start + 0.75, bar1_start + 1.125, bar1_start + 1.5,
               bar1_start + 1.875, bar1_start + 2.25, bar1_start + 2.625]
for note, time in zip(hihat_notes, hihat_times):
    track_drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05))

# --- BAR 2: SAX MELODY (DANTE) ---
bar2_start = bar1_end
bar2_end = bar1_end + bar_duration

# Sax melody: F7 -> D7 -> Bb7 -> F7 (motif in F)
# F (66), D (62), Bb (60), F (66)
sax_notes = [66, 62, 60, 66]
sax_durations = [0.25, 0.25, 0.25, 0.25]
sax_times = [bar2_start + 0.0, bar2_start + 0.25, bar2_start + 0.5, bar2_start + 0.75]

for note, time, duration in zip(sax_notes, sax_times, sax_durations):
    track_sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration))

# --- BAR 3: CHROMATIC WALKING BASS (MARCUS) ---
bar3_start = bar2_end
bar3_end = bar3_start + bar_duration

# Chromatic walk in F: F (66), G (67), Ab (68), A (69), Bb (60), B (61), C (60), D (62), etc.
# Simulate a chromatic walk over 4 bars
chromatic_walk = [66, 67, 68, 69, 60, 61, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 71, 70, 69, 68, 67, 66]

# Walking pace: 1/8 note
for i, pitch in enumerate(chromatic_walk):
    start = bar3_start + i * 0.375
    duration = 0.375
    track_bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration))

# --- BAR 4: PIANO COMPING (DIANE) ---
bar4_start = bar3_end
bar4_end = bar4_start + bar_duration

# Diane's piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb) = 66, 69, 67, 64
# Comp on 2 and 4 only
for i in [0, 2]:  # 2nd and 4th beats
    time = bar4_start + i * 0.75 + 0.125  # 0.125 offset for comp feel
    duration = 0.125
    # Play F7 chord
    for note in [66, 69, 67, 64]:
        track_piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# --- FINAL TOUCH: SENSE OF FORWARD MOTION ---
# End on a sustained F note (66), resolving the motif and leaving room for continuation
track_sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=bar2_end - 0.1, end=bar4_end))

# Save the MIDI file
pm.write("jazz_intro_dante.mid")

print("MIDI file created: jazz_intro_dante.mid")
