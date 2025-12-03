
import pretty_midi

# Create a new MIDI file with tempo set to 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: Kick=36, Snare=38, Hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Define time in seconds for each bar (160 BPM, 4/4 time, 4 bars = 6 seconds)
bar_duration = 1.5
total_duration = 6.0

# Bar 1: Drums alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(1):
    start_time = bar * bar_duration
    end_time = start_time + bar_duration

    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=start_time + beat * 0.375, end=start_time + beat * 0.375 + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=start_time + beat * 0.375, end=start_time + beat * 0.375 + 0.1)
        drums.notes.append(note)

    # Hihat on every eighth
    for beat in range(8):
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start_time + beat * 0.125, end=start_time + beat * 0.125 + 0.05)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Start at 1.5s
start_time = 1.5
end_time = 6.0

# Bass line: Marcus on walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root) and F# (fifth) with chromatic approach
    ('D2', 0.0),       # D2
    ('D#2', 0.25),     # chromatic up
    ('F#2', 0.5),      # F#2
    ('F2', 0.75),      # chromatic down
    ('D2', 1.0),       # D2

    # Bar 3: G (root) and B (fifth) with chromatic approach
    ('G2', 1.5),
    ('G#2', 1.75),
    ('B2', 2.0),
    ('A#2', 2.25),
    ('G2', 2.5),

    # Bar 4: A (root) and C# (fifth) with chromatic approach
    ('A2', 3.0),
    ('A#2', 3.25),
    ('C#3', 3.5),
    ('C3', 3.75),
    ('A2', 4.0)
]

for i, (pitch, time_offset) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_from_name(pitch), start=start_time + time_offset, end=start_time + time_offset + 0.25)
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#) - open voicing
piano_notes_bar2 = ['D3', 'F#3', 'A3', 'C#4']
for note_name in piano_notes_bar2:
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_from_name(note_name), start=start_time, end=end_time)
    piano.notes.append(note)

# Bar 3: G7 (G B D F) - open voicing
piano_notes_bar3 = ['G3', 'B3', 'D4', 'F4']
for note_name in piano_notes_bar3:
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_from_name(note_name), start=start_time + bar_duration, end=end_time)
    piano.notes.append(note)

# Bar 4: A7 (A C# E G) - open voicing
piano_notes_bar4 = ['A3', 'C#4', 'E4', 'G4']
for note_name in piano_notes_bar4:
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_from_name(note_name), start=start_time + 2 * bar_duration, end=end_time)
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - E4 - F#4 (call), then lower to D4 (response)
sax_notes = [
    # Start of motif at 1.5s
    ('D4', start_time, 0.3),
    ('E4', start_time, 0.3),
    ('F#4', start_time, 0.3),
    # Leave it hanging until 3.0s
    ('D4', start_time + 1.5, 0.3),
]

for note_name, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pretty_midi.note_number_from_name(note_name), start=start, end=start + duration)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
# midi.write disabled
