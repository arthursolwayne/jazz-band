
import pretty_midi
import numpy as np

# Set tempo and time signature
TEMPO = 160  # BPM
TIME_SIGNATURE = (4, 4)

# Time per beat in seconds
BEAT_DURATION = 60.0 / TEMPO
BAR_DURATION = BEAT_DURATION * 4  # 4/4 time

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=TEMPO, time_signature_numerator=4, time_signature_denominator=4)

# Define instruments
instrument_tenor = pretty_midi.Instrument(program=64)  # Tenor sax
instrument_piano = pretty_midi.Instrument(program=0)    # Acoustic piano
instrument_bass = pretty_midi.Instrument(program=33)    # Double bass
instrument_drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drum set

pm.instruments = [instrument_tenor, instrument_piano, instrument_bass, instrument_drums]

# Key: D major
KEY = 'D'

# MIDI note numbers
D4 = 62     # D4
F4 = 65     # F4
G4 = 67     # G4
A4 = 69     # A4
B4 = 71     # B4
C5 = 72     # C5
D5 = 74     # D5
F5 = 77     # F5
G5 = 79     # G5
A5 = 81     # A5
B5 = 83     # B5
C6 = 84     # C6
D6 = 86     # D6

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(bar_start):
    kick_notes = [D4]  # Kick is just a click
    snare_notes = [D5]  # Snare is slightly higher
    hihat_notes = [D6]  # Hihat tapped at the same point
    time = bar_start

    # Kick on beats 1 and 3
    for beat in [0, 2]:
        time = bar_start + beat * BEAT_DURATION
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time, end=time + 0.05)
        instrument_drums.notes.append(note)

    # Snare on beats 2 and 4
    for beat in [1, 3]:
        time = bar_start + beat * BEAT_DURATION
        note = pretty_midi.Note(velocity=110, pitch=snare_notes[0], start=time, end=time + 0.05)
        instrument_drums.notes.append(note)

    # Hihat on every eighth note
    for i in range(8):
        time = bar_start + i * BEAT_DURATION / 2
        note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=time, end=time + 0.025)
        instrument_drums.notes.append(note)

# Bar 1
add_drums(0.0)

# Bar 2-4: Full ensemble

# Bass line: Walking line, chromatic approaches, no repeating notes
bass_line = [
    (D4, 0.25, 100),  # D4
    (F4, 0.25, 90),   # F4
    (G4, 0.25, 85),   # G4
    (A4, 0.25, 90),   # A4
    (B4, 0.25, 100),  # B4
    (C5, 0.25, 95),   # C5
    (D5, 0.25, 110),  # D5
    (F5, 0.25, 105),  # F5
    (G5, 0.25, 115),  # G5
    (A5, 0.25, 100),  # A5
    (B5, 0.25, 110),  # B5
    (C6, 0.25, 95),   # C6
    (D6, 0.25, 100),  # D6
    (F5, 0.25, 110),  # F5 (chromatic approach)
    (G5, 0.25, 115),  # G5
    (D5, 0.25, 100)   # D5
]

# Time for bass line (start at 1.5s)
bass_time = 1.5
for note, duration, velocity in bass_line:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=bass_time, end=bass_time + duration)
    instrument_bass.notes.append(note_obj)
    bass_time += duration

# Piano chords: 7th chords, comp on 2 and 4
# Time: 1.5s to 4.5s (3 bars)
def add_piano_chords():
    bar_time = 1.5
    chords = [
        (D4, F4, A4, C5),  # D7 (D F A C)
        (G4, B4, D5, F5),  # G7 (G B D F)
        (A4, C5, E5, G5),  # A7 (A C E G)
        (B4, D5, F5, A5),  # B7 (B D F A)
        (C5, E5, G5, B5),  # C7 (C E G B)
        (D5, F5, A5, C6),  # D7 (D F A C)
        (G4, B4, D5, F5),  # G7
        (A4, C5, E5, G5),  # A7
    ]

    for i, (root, third, fifth, seventh) in enumerate(chords):
        time = bar_time + i * BEAT_DURATION
        velocity = 100 if (i % 2 == 0) else 80  # Vary dynamics
        note1 = pretty_midi.Note(velocity=velocity, pitch=root, start=time, end=time + 0.25)
        note2 = pretty_midi.Note(velocity=velocity, pitch=third, start=time, end=time + 0.25)
        note3 = pretty_midi.Note(velocity=velocity, pitch=fifth, start=time, end=time + 0.25)
        note4 = pretty_midi.Note(velocity=velocity, pitch=seventh, start=time, end=time + 0.25)
        instrument_piano.notes.extend([note1, note2, note3, note4])

add_piano_chords()

# Tenor sax: Short motif, space, dynamics
# Motif: D5 (G4) -> F5 -> G5 -> rest -> back to D5, end with a B4
tenor_notes = [
    (D5, 0.25, 100),   # Start with a strong D
    (F5, 0.25, 110),   # Move up to F
    (G5, 0.25, 115),   # G on beat 3
    (0, 0.25, 0),      # Rest on beat 4
    (D5, 0.25, 100),   # Re-enter on bar 2 beat 1
    (B4, 0.25, 90),    # End with a B4 on beat 2
    (0, 0.25, 0),      # Rest on beat 3
    (D5, 0.25, 110),   # End with a strong D on beat 4
]

tenor_time = 1.5
for note, duration, velocity in tenor_notes:
    if note != 0:
        note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=tenor_time, end=tenor_time + duration)
        instrument_tenor.notes.append(note_obj)
    tenor_time += duration

# Save the MIDI file
pm.write("jazz_intro_wayne_shorter.mid")

print("MIDI file generated: jazz_intro_wayne_shorter.mid")
