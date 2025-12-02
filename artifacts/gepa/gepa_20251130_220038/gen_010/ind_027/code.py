
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds (160 BPM = 6 beats per second)
beat = 0.375  # 60 / 160 = 0.375s per beat
bar = beat * 4  # 1.5 seconds per bar

# Define instrument programs
sax_program = Program(64, 0)  # Tenor sax
piano_program = Program(0, 0)  # Acoustic piano
bass_program = Program(33, 0)  # Double bass
drums_program = Program(0, 1)  # Acoustic drum set

# Create instruments
sax = Instrument(program=sax_program)
piano = Instrument(program=piano_program)
bass = Instrument(program=bass_program)
drums = Instrument(program=drums_program)

# Add instruments to the MIDI
pm.instruments.append(sax)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(drums)

# --- Bar 1: Little Ray - Drums Only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1, time = 0.0
drum_notes = [
    (0.0, 35, 100),  # Kick on 1
    (0.375, 48, 100),  # Snare on 2
    (0.75, 35, 100),  # Kick on 3
    (1.125, 48, 100),  # Snare on 4
    (0.0, 42, 80),  # Hihat on 1
    (0.1875, 42, 80),  # Hihat on 1 &
    (0.375, 42, 80),  # Hihat on 2
    (0.5625, 42, 80),  # Hihat on 2 &
    (0.75, 42, 80),  # Hihat on 3
    (0.9375, 42, 80),  # Hihat on 3 &
    (1.125, 42, 80),  # Hihat on 4
    (1.3125, 42, 80),  # Hihat on 4 &
]

for start, note, velocity in drum_notes:
    note_obj = Note(velocity, note, start, start + 0.125)
    drums.notes.append(note_obj)

# --- Bar 2: Diane on Piano - Dm7 comp on 2 and 4 ---
# Dm7 = D, F, A, C
# Comp on 2 and 4

# 2nd beat of bar
note_d = Note(100, 62, 1.5, 1.625)  # D4
note_f = Note(100, 64, 1.5, 1.625)  # F4
note_a = Note(100, 67, 1.5, 1.625)  # A4
note_c = Note(100, 60, 1.5, 1.625)  # C4

# 4th beat of bar
note_d2 = Note(100, 62, 2.25, 2.375)
note_f2 = Note(100, 64, 2.25, 2.375)
note_a2 = Note(100, 67, 2.25, 2.375)
note_c2 = Note(100, 60, 2.25, 2.375)

piano.notes.extend([note_d, note_f, note_a, note_c, note_d2, note_f2, note_a2, note_c2])

# --- Bar 3: Marcus on Bass – walking line, chromatic approaches ---
# Dm7 bass line: D, C, B, A, G, F, E, D

# Time for each note
bass_notes = [
    (3.0, 62, 100),  # D4
    (3.375, 60, 100),  # C4
    (3.75, 61, 100),  # B4
    (4.125, 67, 100),  # A4
    (4.5, 65, 100),  # G4
    (4.875, 64, 100),  # F4
    (5.25, 63, 100),  # E4
    (5.625, 62, 100),  # D4
]

for start, note, velocity in bass_notes:
    note_obj = Note(velocity, note, start, start + 0.125)
    bass.notes.append(note_obj)

# --- Bar 4: You – Tenor Sax – Motif that starts, hangs, and resolves ---
# Motif: C#4, D4, F4, A4 (Dm7 scale) – resolved to G4 (i.e., Dm7 to G7?)

sax_notes = [
    (6.0, 61, 100),  # C#4
    (6.1875, 62, 100),  # D4
    (6.375, 64, 100),  # F4
    (6.5625, 67, 100),  # A4
    (6.75, 62, 100),  # D4 (rest)
    (7.0, 66, 100),  # G4 (Resolution)
]

for start, note, velocity in sax_notes:
    note_obj = Note(velocity, note, start, start + 0.125)
    sax.notes.append(note_obj)

# Save the MIDI file
pm.write("Dante_Russo_4_Bar_Intro.mid")
