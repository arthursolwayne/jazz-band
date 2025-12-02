
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64, is_drum=False)  # Tenor sax (program 64)
pm.instruments.append(instrument)

# Time settings
BPM = 160
quarter_note = 60 / BPM  # seconds per quarter note
bar_length = 4 * quarter_note  # 4/4 time
total_length = 4 * bar_length  # 4 bars

# Function to convert time to seconds
def time_to_sec(t):
    return t * quarter_note

# --- DRUMS (Little Ray on drums) ---
drums = pretty_midi.Instrument(program=0, is_drum=True)
pm.instruments.append(drums)

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    beat = i * quarter_note
    # Kick on 1 and 3
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=beat, end=beat + 0.1))
    # Snare on 2 and 4
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=beat, end=beat + 0.1))
    # Hihat on every 8th
    for j in range(2):
        hihat_time = beat + j * (quarter_note / 2)
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# --- BASS (Marcus) ---
bass = pretty_midi.Instrument(program=33, is_drum=False)
pm.instruments.append(bass)

# Walking bass line in Dm, chromatic approaches
# Dm7 chord: D, F, A, C
# Walking line: D, Eb, F, G, A, Bb, B, C, D
bass_notes = [62, 63, 65, 67, 69, 70, 71, 72, 62]  # D, Eb, F, G, A, Bb, B, C, D

for i, note in enumerate(bass_notes):
    start = time_to_sec(i)
    end = start + 0.5
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# --- PIANO (Diane) ---
piano = pretty_midi.Instrument(program=0, is_drum=False)
pm.instruments.append(piano)

# 7th chord comping on 2 and 4
# Dm7 = D, F, A, C
chord_notes = [62, 65, 72, 67]  # D, A, C, F

for i in range(2):  # bars 2 and 4
    bar_start = time_to_sec(i + 1)  # bar 2 and bar 4
    for note in chord_notes:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start, end=bar_start + 0.5))

# --- TENOR SAX (You) ---
# Motif: D, Eb, F, G (ascending), then D, F, G, D (descending with a rest at the end)
sax_notes = [
    (62, 0.0),  # D
    (63, 0.25),  # Eb
    (65, 0.5),  # F
    (67, 0.75),  # G
    (62, 1.0),  # D
    (65, 1.25),  # F
    (67, 1.5),  # G
    (62, 1.75),  # D
    (62, 2.0),  # silence at the end
]

for note_info in sax_notes:
    note, time = note_info
    start = time_to_sec(1 + time)
    end = start + 0.25
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Save the MIDI file
pm.write("dm_intro.mid")
print("MIDI file saved as 'dm_intro.mid'")
