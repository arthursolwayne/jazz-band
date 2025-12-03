
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Define the key
key = 'D'

# Define MIDI note to pitch
note_to_pitch = {
    'C': 60,
    'C#': 61,
    'Db': 61,
    'D': 62,
    'D#': 63,
    'Eb': 63,
    'E': 64,
    'F': 65,
    'F#': 66,
    'Gb': 66,
    'G': 67,
    'G#': 68,
    'Ab': 68,
    'A': 69,
    'A#': 70,
    'Bb': 70,
    'B': 71
}

# D Major scale
scale_degrees = [0, 2, 4, 5, 7, 9, 11]
scale_notes = [note_to_pitch[key] + d for d in scale_degrees]

# Instrument tracks
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the piece
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Time per bar (6 seconds / 4 bars = 1.5 seconds per bar)
bar_length = 1.5
beat_length = bar_length / 4

# BAR 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * beat_length
    if beat % 2 == 0:
        # Kick
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        # Hihat on every eighth
        for i in range(2):
            hihat_time = time + i * 0.125
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05))
    else:
        # Snare
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
        # Hihat
        for i in range(2):
            hihat_time = time + i * 0.125
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# BAR 2: Bass and Piano enter
# Bass: Walking line (D2-G2, MIDI 38-43)
bass_notes = [38, 40, 43, 42]
for i, note in enumerate(bass_notes):
    time = (1 + i) * beat_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicing, resolve on last beat of bar
piano_notes = [
    [62, 67, 72, 76],  # D - G - C - E (D major 7)
    [64, 69, 76, 72],  # E - A - D - C (E minor 7)
    [65, 70, 77, 79],  # F - Bb - E - G (F7)
    [67, 72, 76, 74]   # G - C - F - Ab (G7)
]

for i, chord in enumerate(piano_notes):
    start_time = (1 + i) * beat_length
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.25))

# BAR 3: Sax enters with motif
# Motif: D, F#, B, B (MIDI: 62, 66, 71, 71)
motif = [62, 66, 71, 71]
for i, note in enumerate(motif):
    time = (2 + i) * beat_length
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BAR 4: Sax continues, slightly altered
# Motif variation: D, F#, Bb, B (MIDI: 62, 66, 70, 71)
motif_variation = [62, 66, 70, 71]
for i, note in enumerate(motif_variation):
    time = (3 + i) * beat_length
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Save the MIDI file
pm.write("jazz_intro.mid")

print("MIDI file generated: 'jazz_intro.mid'")
