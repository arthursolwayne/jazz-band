
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds
BAR_DURATION = 1.5
TIME_RESOLUTION = 1 / 16  # 16th notes per second

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        time = bar * BAR_DURATION + beat * 0.75
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.25)
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        time = bar * BAR_DURATION + beat * 0.75
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)
    for beat in range(4):  # Hi-hat on every 8th
        time = bar * BAR_DURATION + beat * 0.375
        note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2-4: Full Quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7 (key of D)
bass_notes = [
    # Bar 2
    (1.5, 62), (1.75, 64), (2.0, 64), (2.25, 65),  # Dm7
    (2.5, 69), (2.75, 71), (3.0, 71), (3.25, 72),  # G7
    # Bar 3
    (3.5, 67), (3.75, 69), (4.0, 69), (4.25, 71),  # Cmaj7
    (4.5, 76), (4.75, 78), (5.0, 78), (5.25, 79),  # F7
    # Bar 4
    (5.5, 62), (5.75, 64), (6.0, 64), (6.25, 65)   # Dm7
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comping behind
# Dm7 (bar 2) -> G7 (bar 2) -> Cmaj7 (bar 3) -> F7 (bar 3) -> Dm7 (bar 4)
piano_notes = {
    1.5: [62, 67, 72, 74],  # Dm7
    2.0: [69, 74, 79, 81],  # G7
    2.5: [67, 72, 77, 80],  # Cmaj7
    3.0: [76, 81, 86, 88],  # F7
    3.5: [62, 67, 72, 74],  # Dm7
    4.0: [69, 74, 79, 81],  # G7
    4.5: [67, 72, 77, 80],  # Cmaj7
    5.0: [76, 81, 86, 88],  # F7
    5.5: [62, 67, 72, 74],  # Dm7
}

for time, pitches in piano_notes.items():
    for pitch in pitches:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Tenor Sax (You): Melody
# Short motif with space, haunting, not scale-based
sax_notes = [
    (1.5, 62, 0.5),  # D (start of motif)
    (2.0, 64, 0.25), # E (chromatic approach)
    (2.25, 62, 0.25),# D (return)
    (2.5, 69, 0.5),  # G (extension)
    (3.0, 62, 0.5),  # D (restatement)
    (3.5, 67, 0.5),  # C (suspense)
    (4.0, 69, 0.5),  # G (return)
    (4.5, 67, 0.5),  # C (resolve)
    (5.0, 62, 1.0)   # D (end on a question)
]

for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
