
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the time per bar (160 BPM, 4/4 time => 6 seconds per 4 bars)
time_per_bar = 60 / 160 * 4  # 6 seconds for 4 bars
time_per_beat = 60 / 160  # 0.375 seconds per beat
time_per_eighth = time_per_beat / 2  # 0.1875 seconds per eighth

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # using piano for drum mapping
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Time for each bar
bar_start_time = 0

# ------------------ Drums (Little Ray) ------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = bar_start_time + beat * time_per_beat
    if beat in [0, 2]:
        # Kick
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + time_per_beat / 4))
    if beat in [1, 3]:
        # Snare
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + time_per_beat / 4))
    # Hi-Hat on every eighth
    for eighth in range(2):
        hihat_time = time + eighth * time_per_eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + time_per_eighth / 2))

# Bar 2: Same pattern
bar_start_time += time_per_bar
for beat in range(4):
    time = bar_start_time + beat * time_per_beat
    if beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + time_per_beat / 4))
    if beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + time_per_beat / 4))
    for eighth in range(2):
        hihat_time = time + eighth * time_per_eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + time_per_eighth / 2))

# Bar 3: Same pattern
bar_start_time += time_per_bar
for beat in range(4):
    time = bar_start_time + beat * time_per_beat
    if beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + time_per_beat / 4))
    if beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + time_per_beat / 4))
    for eighth in range(2):
        hihat_time = time + eighth * time_per_eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + time_per_eighth / 2))

# Bar 4: Same pattern, with a slight roll on beat 4
bar_start_time += time_per_bar
for beat in range(4):
    time = bar_start_time + beat * time_per_beat
    if beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + time_per_beat / 4))
    if beat in [1, 3]:
        if beat == 3:
            # Roll on beat 4
            for i in range(4):
                roll_time = time + i * time_per_beat / 4
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=roll_time, end=roll_time + time_per_beat / 8))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + time_per_beat / 4))
    for eighth in range(2):
        hihat_time = time + eighth * time_per_eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + time_per_eighth / 2))

# ------------------ Bass (Marcus) ------------------
# Bar 2: Walking line: D Eb F G, Ab Bb B C
bar_start_time = time_per_bar  # start at bar 2
bass_notes = [
    (0, 2, 62),  # D
    (0, 2, 63),  # Eb
    (0, 2, 64),  # F
    (0, 2, 65),  # G
    (0, 2, 66),  # Ab
    (0, 2, 67),  # Bb
    (0, 2, 68),  # B
    (0, 2, 69),  # C
]

for i, note_info in enumerate(bass_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + (i % 4) * time_per_beat + (i // 4) * time_per_bar
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# ------------------ Piano (Diane) ------------------
# Bar 2: Dm7 (D F A C) on beat 2
bar_start_time = time_per_bar
piano_notes = [
    (1, 2, 62),  # D
    (1, 2, 64),  # F
    (1, 2, 69),  # A
    (1, 2, 72),  # C
]

for i, note_info in enumerate(piano_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + i * time_per_beat
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# Bar 3: G7 (G B D F) on beat 2
bar_start_time += time_per_bar
piano_notes = [
    (1, 2, 67),  # G
    (1, 2, 71),  # B
    (1, 2, 69),  # D
    (1, 2, 65),  # F
]

for i, note_info in enumerate(piano_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + i * time_per_beat
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# Bar 4: Cm7 (C Eb G Bb) on beat 2
bar_start_time += time_per_bar
piano_notes = [
    (1, 2, 60),  # C
    (1, 2, 63),  # Eb
    (1, 2, 69),  # G
    (1, 2, 67),  # Bb
]

for i, note_info in enumerate(piano_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + i * time_per_beat
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# ------------------ Sax (Dante) ------------------
# Bar 3: D (beat 1), Bb (beat 3), rest on beat 4
bar_start_time = 2 * time_per_bar  # bar 3
sax_notes = [
    (0, 0.5, 62),  # D
    (2, 0.5, 66),  # Bb
]

for i, note_info in enumerate(sax_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + i * time_per_beat
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# Bar 4: C (beat 1), D (beat 2), Bb (beat 3), rest on beat 4
bar_start_time += time_per_bar
sax_notes = [
    (0, 0.5, 60),  # C
    (1, 0.5, 62),  # D
    (2, 0.5, 66),  # Bb
]

for i, note_info in enumerate(sax_notes):
    velocity, duration, pitch = note_info
    start_time = bar_start_time + i * time_per_beat
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration))

# Write the MIDI file
pm.write("dante_intro.mid")
