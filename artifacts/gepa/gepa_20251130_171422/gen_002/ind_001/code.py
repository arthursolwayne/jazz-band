
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor
key_signature = pretty_midi.KeySignature(key_number=1)  # D minor
pm.key_signature = key_signature

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature = time_signature

# Define the time per bar in seconds (BPM = 160)
time_per_bar = 60 / 160 * 4  # 6 seconds per 4 bars
time_per_beat = 60 / 160  # 0.375 seconds per beat

# Define the time for each bar
bar_times = [0, time_per_beat * 4, time_per_beat * 8, time_per_beat * 12, time_per_beat * 16]

# --- Drums (Little Ray) ---
drums = pretty_midi.Instrument(program=0)  # Drums

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1, 5):
    bar_start = bar_times[bar]
    beat_start = bar_start
    for beat in range(4):
        # Kick on 1 and 3
        if beat in [0, 2]:
            note = pretty_midi.Note(
                velocity=85,
                pitch=36,  # Kick drum
                start=beat_start,
                end=beat_start + time_per_beat
            )
            drums.notes.append(note)
        # Snare on 2 and 4
        if beat in [1, 3]:
            note = pretty_midi.Note(
                velocity=90,
                pitch=38,  # Snare drum
                start=beat_start,
                end=beat_start + time_per_beat
            )
            drums.notes.append(note)
        # Hihat on every eighth note
        for eighth in [0, 0.5]:
            note = pretty_midi.Note(
                velocity=70,
                pitch=42,  # Hihat
                start=beat_start + eighth,
                end=beat_start + eighth + 0.1875
            )
            drums.notes.append(note)
        beat_start += time_per_beat

pm.instruments.append(drums)

# --- Bass (Marcus) ---
bass = pretty_midi.Instrument(program=33)  # Double Bass

# Bar 1: No bass
# Bars 2-4: Walking line with chromatic approaches

# Bar 2 (starting at 4 beats)
bar_2_start = bar_times[1]
bar_2_notes = [
    (bar_2_start, 48),  # D (root)
    (bar_2_start + time_per_beat * 0.25, 49),  # Eb (chromatic)
    (bar_2_start + time_per_beat * 0.5, 47),  # C (4th)
    (bar_2_start + time_per_beat * 0.75, 50),  # F (chromatic)
    (bar_2_start + time_per_beat, 50),  # F
    (bar_2_start + time_per_beat + time_per_beat * 0.25, 51),  # G (5th)
    (bar_2_start + time_per_beat + time_per_beat * 0.5, 50),  # F
    (bar_2_start + time_per_beat + time_per_beat * 0.75, 49),  # Eb
    (bar_2_start + time_per_beat * 2, 48),  # D
]

for time, pitch in bar_2_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Bar 3: Moving chromatically again
bar_3_start = bar_times[2]
bar_3_notes = [
    (bar_3_start, 48),  # D
    (bar_3_start + time_per_beat * 0.25, 49),  # Eb
    (bar_3_start + time_per_beat * 0.5, 50),  # F
    (bar_3_start + time_per_beat * 0.75, 51),  # G
    (bar_3_start + time_per_beat, 50),  # F
    (bar_3_start + time_per_beat + time_per_beat * 0.25, 49),  # Eb
    (bar_3_start + time_per_beat + time_per_beat * 0.5, 48),  # D
    (bar_3_start + time_per_beat + time_per_beat * 0.75, 47),  # C
    (bar_3_start + time_per_beat * 2, 48),  # D
]

for time, pitch in bar_3_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

# Bar 4: Resolution
bar_4_start = bar_times[3]
bar_4_notes = [
    (bar_4_start, 48),  # D
    (bar_4_start + time_per_beat * 0.25, 47),  # C
    (bar_4_start + time_per_beat * 0.5, 48),  # D
    (bar_4_start + time_per_beat * 0.75, 47),  # C
    (bar_4_start + time_per_beat, 48),  # D
    (bar_4_start + time_per_beat + time_per_beat * 0.25, 47),  # C
    (bar_4_start + time_per_beat + time_per_beat * 0.5, 48),  # D
    (bar_4_start + time_per_beat + time_per_beat * 0.75, 47),  # C
    (bar_4_start + time_per_beat * 2, 48),  # D
]

for time, pitch in bar_4_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.1)
    bass.notes.append(note)

pm.instruments.append(bass)

# --- Piano (Diane) ---
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano

# Bar 1: No piano
# Bar 2: 7th chords on 2 and 4
bar_2_piano_start = bar_times[1]
bar_2_piano_notes = [
    (bar_2_piano_start + time_per_beat * 0.5, 50),  # F (Dm7: D, F, A, C)
    (bar_2_piano_start + time_per_beat * 0.5, 57),  # A
    (bar_2_piano_start + time_per_beat * 0.5, 60),  # C
    (bar_2_piano_start + time_per_beat * 0.5, 62),  # D
    (bar_2_piano_start + time_per_beat * 0.5, 67),  # G (chromatic)

    (bar_2_piano_start + time_per_beat * 1.5, 50),  # F
    (bar_2_piano_start + time_per_beat * 1.5, 57),  # A
    (bar_2_piano_start + time_per_beat * 1.5, 60),  # C
    (bar_2_piano_start + time_per_beat * 1.5, 62),  # D
    (bar_2_piano_start + time_per_beat * 1.5, 67),  # G
]

for time, pitch in bar_2_piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Bar 3: Similar comping
bar_3_piano_start = bar_times[2]
bar_3_piano_notes = [
    (bar_3_piano_start + time_per_beat * 0.5, 50),
    (bar_3_piano_start + time_per_beat * 0.5, 57),
    (bar_3_piano_start + time_per_beat * 0.5, 60),
    (bar_3_piano_start + time_per_beat * 0.5, 62),
    (bar_3_piano_start + time_per_beat * 0.5, 67),

    (bar_3_piano_start + time_per_beat * 1.5, 50),
    (bar_3_piano_start + time_per_beat * 1.5, 57),
    (bar_3_piano_start + time_per_beat * 1.5, 60),
    (bar_3_piano_start + time_per_beat * 1.5, 62),
    (bar_3_piano_start + time_per_beat * 1.5, 67),
]

for time, pitch in bar_3_piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

# Bar 4: Continue comping
bar_4_piano_start = bar_times[3]
bar_4_piano_notes = [
    (bar_4_piano_start + time_per_beat * 0.5, 50),
    (bar_4_piano_start + time_per_beat * 0.5, 57),
    (bar_4_piano_start + time_per_beat * 0.5, 60),
    (bar_4_piano_start + time_per_beat * 0.5, 62),
    (bar_4_piano_start + time_per_beat * 0.5, 67),

    (bar_4_piano_start + time_per_beat * 1.5, 50),
    (bar_4_piano_start + time_per_beat * 1.5, 57),
    (bar_4_piano_start + time_per_beat * 1.5, 60),
    (bar_4_piano_start + time_per_beat * 1.5, 62),
    (bar_4_piano_start + time_per_beat * 1.5, 67),
]

for time, pitch in bar_4_piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.1)
    piano.notes.append(note)

pm.instruments.append(piano)

# --- Tenor Sax (Dante) ---
sax = pretty_midi.Instrument(program=64)  # Tenor Sax

# Bar 1: No sax
# Bar 2: Start the motif
bar_2_sax_start = bar_times[1]
bar_2_sax_notes = [
    (bar_2_sax_start + time_per_beat * 0.25, 62),  # D (tenor sax)
    (bar_2_sax_start + time_per_beat * 0.75, 64),  # E
    (bar_2_sax_start + time_per_beat * 1.25, 62),  # D
    (bar_2_sax_start + time_per_beat * 1.75, 64),  # E
    (bar_2_sax_start + time_per_beat * 2.25, 62),  # D
]

for time, pitch in bar_2_sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Bar 3: Repeat the motif
bar_3_sax_start = bar_times[2]
bar_3_sax_notes = [
    (bar_3_sax_start + time_per_beat * 0.25, 62),
    (bar_3_sax_start + time_per_beat * 0.75, 64),
    (bar_3_sax_start + time_per_beat * 1.25, 62),
    (bar_3_sax_start + time_per_beat * 1.75, 64),
    (bar_3_sax_start + time_per_beat * 2.25, 62),
]

for time, pitch in bar_3_sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Bar 4: End the motif, leave it hanging
bar_4_sax_start = bar_times[3]
bar_4_sax_notes = [
    (bar_4_sax_start + time_per_beat * 0.25, 62),
    (bar_4_sax_start + time_per_beat * 0.75, 64),
    (bar_4_sax_start + time_per_beat * 1.25, 62),
    (bar_4_sax_start + time_per_beat * 1.75, 64),
    (bar_4_sax_start + time_per_beat * 2.25, 62),
]

for time, pitch in bar_4_sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file written to 'dante_intro.mid'")
