
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a MIDI file
midi = pretty_midi.PrettyMIDI()
tempo = 160  # BPM
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(tempo, 0)]

# Time per beat in seconds
beat_time = 60.0 / tempo  # 0.375 seconds per beat
bar_time = beat_time * 4  # 1.5 seconds per bar

# Define the start time for each bar
bar_starts = [i * bar_time for i in range(4)]

# -----------------------------
# 1. Little Ray - Drums (Bar 1 only)
# -----------------------------
drums = Instrument(program=Program(0, 0), is_drum=True)
drums.name = "Drums"

# Kick on beat 1 and 3
for bar in range(1):
    start = bar_starts[bar]
    for beat in [0, 2]:
        note = Note(36, start + beat * beat_time, start + beat * beat_time + 0.1)
        drums.notes.append(note)

# Snare on beat 2 and 4
for bar in range(1):
    start = bar_starts[bar]
    for beat in [1, 3]:
        note = Note(38, start + beat * beat_time, start + beat * beat_time + 0.1)
        drums.notes.append(note)

# Hihat on every 8th note
for bar in range(1):
    start = bar_starts[bar]
    for i in range(8):
        note = Note(42, start + i * (beat_time / 2), start + i * (beat_time / 2) + 0.05)
        drums.notes.append(note)

midi.instruments.append(drums)

# -----------------------------
# 2. Marcus - Bass (Bars 2-4)
# -----------------------------
bass = Instrument(program=Program(33, 0))
bass.name = "Bass"

# Chromatic walking line in D major: D, C#, D, E, F, G, A, B
chromatic_walk = [62, 63, 62, 64, 65, 67, 69, 71]  # D, C#, D, E, F, G, A, B
note_lengths = [beat_time / 2 for _ in range(len(chromatic_walk))]

# Start at bar 2
start_time = bar_starts[1]

for i, pitch in enumerate(chromatic_walk):
    note = Note(pitch, start_time + i * (beat_time / 2), start_time + i * (beat_time / 2) + note_lengths[i])
    bass.notes.append(note)

midi.instruments.append(bass)

# -----------------------------
# 3. Diane - Piano (Bars 2-4)
# -----------------------------
piano = Instrument(program=Program(0, 0))
piano.name = "Piano"

# 7th chords on beats 2 and 4 in D major
chords = {
    0: [62, 67, 69, 71],  # D7 (D, F#, A, C#)
    1: [62, 67, 69, 71],
    2: [62, 67, 69, 71],
    3: [62, 67, 69, 71]
}

for bar in range(2, 4):
    start = bar_starts[bar]
    chord = chords[bar - 2]
    for note in chord:
        note_obj = Note(note, start + 1 * beat_time, start + 1 * beat_time + 0.2)
        piano.notes.append(note_obj)
        note_obj = Note(note, start + 3 * beat_time, start + 3 * beat_time + 0.2)
        piano.notes.append(note_obj)

midi.instruments.append(piano)

# -----------------------------
# 4. You - Tenor Sax (Bars 2-4)
# -----------------------------
tenor = Instrument(program=Program(64, 0))
tenor.name = "Tenor Sax"

# Your motif in D major: D, E, F#, G, D
motif = [62, 64, 66, 67, 62]
note_lengths = [0.2, 0.2, 0.2, 0.2, 0.2]

# Start at bar 2
start_time = bar_starts[1]

for i, pitch in enumerate(motif):
    note = Note(pitch, start_time + i * 0.2, start_time + i * 0.2 + note_lengths[i])
    tenor.notes.append(note)

midi.instruments.append(tenor)

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written to 'dante_intro.mid'")
