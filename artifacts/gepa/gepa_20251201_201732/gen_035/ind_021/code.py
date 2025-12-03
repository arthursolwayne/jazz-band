
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time per bar in seconds (160 BPM, 4/4 time)
bar_length = 1.5  # 60 / (160 * 4 / 4) = 1.5s per bar

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_1_start = 0.0
bar_1_end = bar_length

# Drum pattern for bar 1
notes = [
    # Kick on 1 and 3
    (bar_1_start + 0.0, drum_notes['kick'], 1.0),
    (bar_1_start + 0.75, drum_notes['kick'], 1.0),
    # Snare on 2 and 4
    (bar_1_start + 0.375, drum_notes['snare'], 1.0),
    (bar_1_start + 0.75 * 3, drum_notes['snare'], 1.0),
    # Hihat on every eighth note
    (bar_1_start + 0.0, drum_notes['hihat'], 0.375),
    (bar_1_start + 0.375, drum_notes['hihat'], 0.375),
    (bar_1_start + 0.75, drum_notes['hihat'], 0.375),
    (bar_1_start + 1.125, drum_notes['hihat'], 0.375),
    (bar_1_start + 1.5, drum_notes['hihat'], 0.375)
]

for start, note, duration in notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 2-4: Full quartet (1.5 - 6.0s)
start_time = bar_1_end

# Bass line: Marcus, walking line with chromatic approaches
# D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (start_time, 38, 0.375),  # D2
    (start_time + 0.375, 40, 0.375),  # Eb2 (chromatic approach)
    (start_time + 0.75, 43, 0.375),  # G2
    (start_time + 1.125, 42, 0.375),  # F#2 (chromatic approach)
    (start_time + 1.5, 45, 0.375),  # A2
    (start_time + 1.875, 44, 0.375),  # Ab2 (chromatic approach)
    (start_time + 2.25, 47, 0.375),  # C3
    (start_time + 2.625, 46, 0.375),  # Bb2 (chromatic approach)
    (start_time + 3.0, 50, 0.375),  # D3
    (start_time + 3.375, 52, 0.375),  # Eb3 (chromatic approach)
    (start_time + 3.75, 55, 0.375),  # G3
    (start_time + 4.125, 54, 0.375),  # F#3 (chromatic approach)
    (start_time + 4.5, 57, 0.375),  # A3
    (start_time + 4.875, 56, 0.375),  # Ab3 (chromatic approach)
    (start_time + 5.25, 59, 0.375),  # C4
    (start_time + 5.625, 58, 0.375),  # Bb3 (chromatic approach)
]

for start, pitch, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
# Bar 3: G7 (G-B-D-F)
# Bar 4: A7 (A-C#-E-G)
piano_notes = [
    # Bar 2 (Dmaj7)
    (start_time, 62, 0.5),  # D4
    (start_time, 67, 0.5),  # F#4
    (start_time, 69, 0.5),  # A4
    (start_time, 72, 0.5),  # C#5

    # Bar 3 (G7)
    (start_time + 1.5, 67, 0.5),  # G4
    (start_time + 1.5, 71, 0.5),  # B4
    (start_time + 1.5, 69, 0.5),  # D5
    (start_time + 1.5, 70, 0.5),  # F5

    # Bar 4 (A7)
    (start_time + 3.0, 71, 0.5),  # A4
    (start_time + 3.0, 76, 0.5),  # C#5
    (start_time + 3.0, 77, 0.5),  # E5
    (start_time + 3.0, 81, 0.5),  # G5
]

for start, pitch, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Dante, short motif, sing it, leave it hanging, come back
# Motif: D4 - E4 - F#4 - G4 (Dorian feel)
# Starts at the second bar, "sings" the motif, then leaves it hanging at F#4
# Comes back on the last bar to finish it

# Bar 2
sax_notes = [
    (start_time, 62, 0.375),   # D4
    (start_time + 0.375, 64, 0.375),  # E4
    (start_time + 0.75, 67, 0.375),   # F#4
    (start_time + 1.125, 69, 0.375),  # G4
]

# Bar 4 (comes back to finish the motif)
sax_notes += [
    (start_time + 3.0, 67, 0.375),   # F#4
    (start_time + 3.375, 69, 0.375),  # G4
    (start_time + 3.75, 71, 0.375),   # A4
]

for start, pitch, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Drums continue with the same pattern in bars 2-4
for bar in range(2, 5):
    bar_start = start_time + (bar - 1) * bar_length
    for start, note, duration in notes:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + start, end=bar_start + start + duration)
        drums.notes.append(note_obj)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
