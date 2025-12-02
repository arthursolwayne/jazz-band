
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize a PrettyMIDI object at 160 BPM, 4/4 time
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per beat
beats_per_bar = 4
bpm = 160
seconds_per_beat = 60 / bpm
seconds_per_bar = seconds_per_beat * beats_per_bar
total_duration = 6.0  # 4 bars

# Create instruments
drums = Instrument(program=Program.DRUMS)
piano = Instrument(program=Program.PIANO)
bass = Instrument(program=Program.BASS)
sax = Instrument(program=Program.TENOR_SAX)

pm.instruments.append(drums)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(sax)

# --- DRUMS: Bar 1 (0–1.5s) -------------------------------
# Kick on 1 and 3
kick_notes = [(0.0, 36, 100), (0.75, 36, 100)]
# Snare on 2 and 4
snare_notes = [(0.375, 38, 100), (1.125, 38, 100)]
# Hihat on every 8th note
hihat_notes = [(i * 0.375, 42, 100) for i in range(0, int(4 * 2) + 1)]

# Add to drum instrument
for time, note, velocity in kick_notes + snare_notes + hihat_notes:
    drums.notes.append(Note(note_number=note, start=time, end=time + 0.1, velocity=velocity))

# --- PIANO: Bars 2–4 (1.5–6.0s) -------------------------------
# Comping on 2 and 4: Dm7 (F, A, C, D)
# Dm7: D, F, A, C
# Use 7th chords
# Comp on beats 2 and 4 of each bar

def add_piano_notes(start_time):
    # Dm7: D, F, A, C
    chord_notes = [50, 53, 57, 59]  # D, F, A, C
    for note in chord_notes:
        piano.notes.append(Note(note_number=note, start=start_time, end=start_time + 0.3, velocity=100))
        piano.notes.append(Note(note_number=note, start=start_time + 0.6, end=start_time + 0.9, velocity=100))

# Comp on beat 2 and 4 of bars 2, 3, 4
bar2_beat2 = 1.5 + (0.75 * 1)  # 1.5 + 0.75 = 2.25
bar2_beat4 = 1.5 + (0.75 * 3)  # 1.5 + 2.25 = 3.75
bar3_beat2 = 1.5 + (0.75 * 5)  # 1.5 + 3.75 = 5.25
bar3_beat4 = 1.5 + (0.75 * 7)  # 1.5 + 5.25 = 6.75 (this is beyond the 6s limit, so skip)
bar4_beat2 = 1.5 + (0.75 * 9)  # 1.5 + 6.75 = 8.25 (beyond, skip)
bar4_beat4 = 1.5 + (0.75 * 11) # 1.5 + 8.25 = 9.75 (beyond)

# Only add the ones within the 4.5–6.0s window
add_piano_notes(2.25)
add_piano_notes(3.75)
add_piano_notes(5.25)

# --- BASS: Bars 2–4 (1.5–6.0s) -------------------------------
# Walking line in Dm, chromatic, no repetition
# Start at Dm root (D) on beat 1 of bar 2 (1.5s)

bass_notes = {
    # Bar 2
    1.5: 50,   # D
    1.875: 51, # Eb
    2.25: 52,  # E
    2.625: 53, # F
    3.0: 55,   # G
    3.375: 57, # A
    3.75: 59,  # Bb
    4.125: 60, # B
    4.5: 62,   # C
    4.875: 63, # C#
    5.25: 64,  # D
    5.625: 65, # D#
    6.0: 67,   # E
}

for time, note in bass_notes.items():
    bass.notes.append(Note(note_number=note, start=time, end=time + 0.125, velocity=100))

# --- SAX: Bars 2–4 (1.5–6.0s) -------------------------------

# Melody: Start with a short motif — D, F, A, D (Dm7), then pause
# Time: 1.5 to 2.0s
sax_notes = [
    (1.5, 50, 100),  # D
    (1.75, 53, 100), # F
    (2.0, 57, 100),  # A
    (2.25, 50, 100), # D (repeat)
]

# Then leave a space (no notes from 2.25 to 2.75)
# Then return with a slightly higher note (maybe Bb, 59)
sax_notes.append((2.75, 59, 100))  # Bb
sax_notes.append((3.0, 57, 100))  # A

# Add to sax instrument
for time, note, velocity in sax_notes:
    sax.notes.append(Note(note_number=note, start=time, end=time + 0.25, velocity=velocity))

# Save the MIDI file
pm.write("jazz_intro_dmin_dante_russo.mid")
print("MIDI file created: jazz_intro_dmin_dante_russo.mid")
