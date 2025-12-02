
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds for each bar
bar_length_seconds = 1.5  # 160 BPM, 4/4 time
note_duration = 0.25  # quarter note
eighth_note = note_duration / 2
sixteenth_note = note_duration / 4

# Drums (Little Ray)
drums = Instrument(program=Program.DRUMS)
pm.instruments.append(drums)

# Kick on 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar_length_seconds * i, end=bar_length_seconds * i + 0.1) for i in [0, 2]]
for note in kick_notes:
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar_length_seconds * i, end=bar_length_seconds * i + 0.1) for i in [1, 3]]
for note in snare_notes:
    drums.notes.append(note)

# Hihat on every eighth note
for bar in range(4):
    for eighth in range(2):
        time = bar * bar_length_seconds + eighth * eighth_note
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(hihat)

# Piano (Diane)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
pm.instruments.append(piano)

# Chord progression: Dm7 - Gm7 - Bbm7 - Am7
chords = [
    {'time': 1.5, 'notes': [2, 5, 7, 9]},  # Dm7 (D, F, A, C)
    {'time': 3.0, 'notes': [7, 10, 12, 14]},  # Gm7 (G, Bb, D, F)
    {'time': 4.5, 'notes': [10, 13, 15, 17]},  # Bbm7 (Bb, D, F, Ab)
    {'time': 6.0, 'notes': [9, 12, 14, 16]},   # Am7 (A, C, E, G)
]

for chord in chords:
    for note in chord['notes']:
        pitch = 24 + note  # C2 is 24, so Dm7 starts at D (2, which is D2 = 24 + 2 = 26)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=chord['time'], end=chord['time'] + 0.5))

# Bass (Marcus)
bass = Instrument(program=Program.FRETLESS_BASS)
pm.instruments.append(bass)

# Walking bass line in Dm: D - F - G - A - Bb - C - D - Eb
bass_line = [
    (0.0, 2),   # D
    (0.25, 5),  # F
    (0.5, 7),   # G
    (0.75, 9),  # A
    (1.0, 10),  # Bb
    (1.25, 2),  # C (D)
    (1.5, 5),   # D
    (1.75, 6),  # Eb
]

for time, note in bass_line:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=24 + note, start=time, end=time + 0.125))

# Sax (You)
sax = Instrument(program=Program.TENOR_SAX)
pm.instruments.append(sax)

# Sax motif: D - F - G - A (Dm scale), then resolves on A
sax_notes = [
    (0.0, 2),   # D
    (0.25, 5),  # F
    (0.5, 7),   # G
    (0.75, 9),  # A

    (1.5, 9),   # A (resolve from earlier motif)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=24 + note, start=time, end=time + 0.125))

# Write the MIDI file
pm.write('dante_intro.mid')
print("MIDI file generated: 'dante_intro.mid'")
