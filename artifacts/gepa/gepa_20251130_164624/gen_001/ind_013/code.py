
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define instruments
saxophone = pretty_midi.Instrument(program=64)  # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Electric bass
piano = pretty_midi.Instrument(program=0)     # Acoustic piano
drums = pretty_midi.Instrument(program=128)   # Drums

pm.instruments = [saxophone, bass, piano, drums]

# Constants for timing
note_duration = 0.375  # 1/16th note at 160 BPM
bar_length = 1.5       # 4/4 bar at 160 BPM

# --- BAR 1: Drums only (0.0 - 1.5s) ---
# Kick on beats 1 and 3
kick_beats = [0.0, 1.0]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# Snare on beats 2 and 4
snare_beats = [0.5, 1.5]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# Hi-hat on every eighth note
hihat_beats = [0.0, 0.5, 1.0, 1.5]
for beat in hihat_beats:
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# --- BAR 2-4: All instruments (1.5 - 6.0s) ---

# Define key: Dm7 (Dm7 = D, F, A, C)
# Root note: D (62)
root = 62

# --- SAXOPHONE: Short, singable motif that starts in Bar 2, leaves a gap, resolves in Bar 4 ---
# Melody: D (62) -> F (65) -> G (67) -> D (62) -> leave a gap -> C (60) -> A (65) -> D (62)
# Time positions in seconds (Bar 1.5s = 1.5, Bar 2 = 1.5 + 0.375 = 1.875)
sax_notes = [
    (1.875, 62, 100, 0.375),  # D
    (2.25, 65, 100, 0.375),   # F
    (2.625, 67, 100, 0.375),  # G
    (3.0, 62, 100, 0.375),    # D
    (3.75, 60, 100, 0.375),   # C
    (4.125, 65, 100, 0.375),  # A
    (4.5, 62, 100, 0.375)     # D
]

for start, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    saxophone.notes.append(note)

# --- BASS: Walking line with chromatic approaches, no repeated notes ---
# Dm7: D F A C
# Walking line in D Dorian: D, Eb, F, G, A, Bb, B, C
# Start with D (62), walk down chromatically: C (60), B (59), Bb (58), A (65), G (67), F (65), Eb (62), D (62)

bass_notes = [
    (1.5, 62, 100, 0.375),  # D
    (1.875, 60, 100, 0.375), # C
    (2.25, 59, 100, 0.375),  # B
    (2.625, 58, 100, 0.375), # Bb
    (3.0, 65, 100, 0.375),   # A
    (3.375, 67, 100, 0.375), # G
    (3.75, 65, 100, 0.375),  # F
    (4.125, 62, 100, 0.375), # Eb
    (4.5, 62, 100, 0.375)    # D
]

for start, pitch, velocity, duration in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# --- PIANO: 7th chords on beats 2 and 4 (1.5 - 6.0s) ---
# Chords: Dm7, F7, A7, Cm7
# Dm7: D (62), F (65), A (69), C (60)
# F7: F (65), A (69), C (60), Eb (62)
# A7: A (69), C (60), E (64), G (67)
# Cm7: C (60), Eb (62), G (67), Bb (58)

# Bars 2-4 (each bar = 1.5s)
# Bar 2: Dm7 on beat 2 (1.5 + 0.5 = 2.0s)
# Bar 3: F7 on beat 2 (3.0s)
# Bar 4: A7 on beat 2 (4.5s)
# Then Cm7 on beat 4 (6.0s)

# Dm7 on beat 2 (2.0s)
for pitch in [62, 65, 69, 60]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=2.0, end=2.0 + 0.25)
    piano.notes.append(note)

# F7 on beat 2 (3.0s)
for pitch in [65, 69, 60, 62]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=3.0, end=3.0 + 0.25)
    piano.notes.append(note)

# A7 on beat 2 (4.5s)
for pitch in [69, 60, 64, 67]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=4.5, end=4.5 + 0.25)
    piano.notes.append(note)

# Cm7 on beat 4 (6.0s)
for pitch in [60, 62, 67, 58]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=6.0, end=6.0 + 0.25)
    piano.notes.append(note)

# --- DRUMS: Bar 2-4 (1.5 - 6.0s) ---
# Kick on beats 1 and 3 of each bar
kick_beats = [1.5, 2.5, 3.5, 4.5]
for beat in kick_beats:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# Snare on beats 2 and 4 of each bar
snare_beats = [2.0, 3.0, 4.0, 5.0]
for beat in snare_beats:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# Hi-hat on every eighth note (from 1.5s to 6.0s)
for beat in np.arange(1.5, 6.0, 0.25):
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat, end=beat + note_duration)
    drums.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
