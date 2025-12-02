
import pretty_midi

# Create a MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar duration in seconds (160 BPM, 4/4)
bar_length = 1.5  # seconds per bar

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for beat in range(4):
    time = beat * 0.375  # 0.375s per beat
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every 8th
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
# Start at F (65), walk down chromatically to E (64), then up to G (67)
bass_notes = [
    (1.5, 65, 100),
    (1.875, 64, 100),
    (2.25, 67, 100),
    (2.625, 69, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 on beat 2 (2.25s), Bb7 on beat 4 (2.625s)
piano_notes = [
    # F7: F, A, C, E (65, 68, 72, 69)
    (2.25, 65, 100),
    (2.25, 68, 100),
    (2.25, 72, 100),
    (2.25, 69, 100),
    # Bb7: Bb, D, F, Ab (62, 65, 69, 67)
    (2.625, 62, 100),
    (2.625, 65, 100),
    (2.625, 69, 100),
    (2.625, 67, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Melody - short motif, singable, start and leave it hanging
# F (65), G (67), A (69), then resolve on F (65) at the end of bar 4
# Motif: F -> G -> A -> F
sax_notes = [
    # Bar 2: F (65) on beat 1 (1.5s)
    (1.5, 65, 110),
    # Bar 2: G (67) on beat 2 (1.875s), leave it hanging
    (1.875, 67, 110),
    # Bar 3: A (69) on beat 1 (2.25s)
    (2.25, 69, 110),
    # Bar 4: F (65) on beat 3 (3.375s), resolve it
    (3.375, 65, 110)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bar 3 and 4: Drums continue
for bar in range(2, 4):
    start_time = bar * bar_length
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every 8th
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 3: Bass continues (3.0 - 4.5s)
# Chromatic walk: F (65), E (64), G (67), A (69)
bass_notes = [
    (3.0, 65, 100),
    (3.375, 64, 100),
    (3.75, 67, 100),
    (4.125, 69, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Bar 3: Piano continues (3.0 - 4.5s)
# F7 on beat 2 (3.375s), Bb7 on beat 4 (3.75s)
piano_notes = [
    (3.375, 65, 100),
    (3.375, 68, 100),
    (3.375, 72, 100),
    (3.375, 69, 100),
    (3.75, 62, 100),
    (3.75, 65, 100),
    (3.75, 69, 100),
    (3.75, 67, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Bar 4: Sax continues (4.5s)
# End on F (65), resolve
sax_notes = [
    (4.5, 65, 110)
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
