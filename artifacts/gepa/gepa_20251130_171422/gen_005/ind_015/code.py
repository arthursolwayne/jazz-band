
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define the key (F minor)
key = 'Fm'

# Create instruments
drums = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Time constants
bar_length = 1.5  # seconds per bar (160 BPM)
beat_length = bar_length / 4  # 0.375 seconds per beat

# Function to add a note to an instrument
def add_note(instrument, note_number, start_time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# -----------------------------
# BAR 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# -----------------------------
# Kick on beats 1 and 3
add_note(drums, pretty_midi.note_name_to_number('C3'), 0.0, 0.1)
add_note(drums, pretty_midi.note_name_to_number('C3'), 0.75, 0.1)

# Snare on beats 2 and 4
add_note(drums, pretty_midi.note_name_to_number('G3'), 0.375, 0.1)
add_note(drums, pretty_midi.note_name_to_number('G3'), 1.125, 0.1)

# Hi-hats on every eighth note
for i in range(0, 4):
    add_note(drums, pretty_midi.note_name_to_number('C5'), i * 0.375, 0.1, velocity=80)

# -----------------------------
# BAR 2-4: Full ensemble
# -----------------------------

# Define time for bars 2-4 (start at 1.5s)
bar_start = 1.5

# -----------------------------
# BASS LINE - Marcus (chromatic, walking line, no repeated notes)
# F minor scale: F, Gb, G, Ab, A, Bb, B (but he plays chromatically)
# We use a chromatic line from F down to D
# Notes in F minor scale: F, Gb, G, Ab, A, Bb, B, C (chromatic tone)
bass_notes = [78, 77, 76, 75, 74, 73, 72, 71]  # F, Eb, D, C, Bb, A, G, F# (chromatic steps)
for i, note in enumerate(bass_notes):
    add_note(bass, note, bar_start + i * beat_length, 0.25)

# -----------------------------
# PIANO - Diane (comping on 2 and 4 with 7th chords)
# Fm7: F, Ab, Bb, C
# Gm7: G, Bb, C, D
# Am7: A, C, D, E
# Bb7: Bb, D, F, G
chords = [
    [78, 75, 72, 70],  # Fm7
    [77, 72, 70, 69],  # Gm7
    [74, 70, 69, 67],  # Am7
    [72, 69, 78, 77]   # Bb7 (no 7th, just F and G to imply dominant)
]
for i, chord in enumerate(chords):
    for note in chord:
        add_note(piano, note, bar_start + i * beat_length + 0.25, 0.25, velocity=85)

# -----------------------------
# SAX - Dante (your motif)
# Fm: F, Ab, Bb, C, D, Eb, G
# Motif: F - Ab - Bb - (rest) -> then F - Ab - Bb - Ab
# Make it sing, leave it hanging, then resolve
sax_notes = [
    78,  # F
    75,  # Ab
    72,  # Bb
    75,  # Ab
    78,  # F
    75,  # Ab
    72,  # Bb
    75   # Ab
]
sax_durations = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]
for i, note in enumerate(sax_notes):
    add_note(sax, note, bar_start + i * 0.15, sax_durations[i], velocity=110)

# -----------------------------
# Add instruments to the PrettyMIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Save to MIDI file
pm.write("f_minor_intro.mid")
print("MIDI file saved as 'f_minor_intro.mid'")
