
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Create tracks for each instrument
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS_GUITAR)
piano = Instrument(program=Program.AC_PIANO_1)
sax = Instrument(program=Program.TENOR_SAX)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Set time per beat (in seconds)
beat = 60.0 / tempo  # 0.375 seconds per beat

# Define notes for each bar in terms of seconds
bar_length = 4 * beat  # 1.5 seconds per bar

# DRUMS: Little Ray
# Kick on beats 1 and 3, snare on 2 and 4, hi-hat on every 8th
little_ray_drums = [
    (0.0, 36),  # Kick on beat 1
    (0.375, 49),  # Hi-hat on beat 1 & 1/2
    (0.75, 36),  # Kick on beat 3
    (1.125, 49),  # Hi-hat on beat 3 & 1/2
    (1.5, 49),  # Hi-hat on beat 4
    (1.875, 49),  # Hi-hat on beat 4 & 1/2
]

for start, note in little_ray_drums:
    dr = Note(note_number=note, start=start, end=start + 0.125)
    drums.notes.append(dr)

# BASS: Marcus (Walking line in F major - root, fifth, with chromatic approaches)
# F - G - F - E - D - C - Bb - A
# Bar 1: F (G) -> E (D) -> C (Bb) -> A (F)
# Bar 2: F (G) -> E (D) -> C (Bb) -> A (F)
# Bar 3: F (G) -> E (D) -> C (Bb) -> A (F)
# Bar 4: F (G) -> E (D) -> C (Bb) -> A (F)

# Convert to MIDI notes (F = 65, G = 67, E = 64, D = 62, C = 60, Bb = 58, A = 69)
bass_notes = [
    (0.0, 65), (0.375, 67), (0.75, 64), (1.125, 62),  # Bar 1
    (1.5, 60), (1.875, 58), (2.25, 69), (2.625, 65),  # Bar 2
    (3.0, 67), (3.375, 64), (3.75, 62), (4.125, 60),  # Bar 3
    (4.5, 58), (4.875, 69), (5.25, 65), (5.625, 67)   # Bar 4
]

for start, note in bass_notes:
    note_obj = Note(note_number=note, start=start, end=start + 0.25)
    bass.notes.append(note_obj)

# PIANO: Diane (Open voicings, one chord per bar)
# Fmaj7: F, A, C, E
# Bbmaj7: Bb, D, F, Ab
# Dmin7: D, F, A, C
# Amaj7: A, C#, E, G

# Convert to MIDI notes (F=65, A=69, C=60, E=64, Bb=58, D=62, Ab=55)

piano_notes = []

# Bar 1: Fmaj7
piano_notes.extend([
    (0.0, 65), (0.0, 69), (0.0, 60), (0.0, 64)
])

# Bar 2: Bbmaj7
piano_notes.extend([
    (1.5, 58), (1.5, 62), (1.5, 65), (1.5, 55)
])

# Bar 3: Dmin7
piano_notes.extend([
    (3.0, 62), (3.0, 65), (3.0, 69), (3.0, 60)
])

# Bar 4: Amaj7
piano_notes.extend([
    (4.5, 69), (4.5, 71), (4.5, 64), (4.5, 67)
])

for start, note in piano_notes:
    note_obj = Note(note_number=note, start=start, end=start + 0.5)
    piano.notes.append(note_obj)

# SAX: Dante (One concise motif — start, leave it hanging, come back and finish)
# Motif: F - A - E - F
# Start on bar 1, repeat on bar 3
# Use note durations to create tension and release

sax_notes = [
    (0.0, 65), (0.375, 69), (0.75, 64), (1.125, 65),  # Bar 1
    (3.0, 65), (3.375, 69), (3.75, 64), (4.125, 65)   # Bar 3
]

for start, note in sax_notes:
    note_obj = Note(note_number=note, start=start, end=start + 0.25)
    sax.notes.append(note_obj)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")
