
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key (F major)
key = 'F'

# Bar length in seconds (160 BPM, 4/4)
bar_length = 6.0  # 4 bars = 6 seconds
beat_length = 0.375  # 1 beat = 0.375 seconds
note_length = 0.375  # quarter note length

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI program 0
bass_program = pretty_midi.instrument_name_to_program('Double Bass')  # MIDI program 33
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')  # MIDI program 8
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')  # MIDI program 67

# Add instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# --- DRUMS ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Just hihat, build tension
# Bars 2-4: Add kick and snare, syncopation

# Bar 1
# Hihat on every eighth
for i in range(8):
    time = i * 0.1875  # eighth note at 160 BPM
    note = pretty_midi.Note(velocity=int(100 + 20 * np.sin(i * np.pi / 4)), pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(note)

# Bars 2-4
for bar in range(2, 5):  # bars 2, 3, 4
    bar_start = bar * bar_length
    # Kick on 1 and 3
    for kick_beat in [0, 2]:
        time = bar_start + kick_beat * beat_length
        velocity = int(100 + 20 * np.random.rand())
        note = pretty_midi.Note(velocity=velocity, pitch=36, start=time, end=time + 0.2)
        drums.notes.append(note)
    # Snare on 2 and 4
    for snare_beat in [1, 3]:
        time = bar_start + snare_beat * beat_length
        velocity = int(100 + 20 * np.random.rand())
        note = pretty_midi.Note(velocity=velocity, pitch=38, start=time, end=time + 0.15)
        drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        time = bar_start + i * 0.1875
        velocity = int(100 + 20 * np.sin(i * np.pi / 4))
        note = pretty_midi.Note(velocity=velocity, pitch=42, start=time, end=time + 0.1875)
        drums.notes.append(note)

# --- BASS ---
# Walking line, chromatic approaches, no repeated notes
# F major scale: F, G, A, Bb, B, C, D
# F7 chord: F, A, C, E
# Walking bass line with chromatic passing tones

note_list = [
    77,  # F (C4)
    79,  # G
    81,  # A
    78,  # Bb (Ab4)
    82,  # B
    84,  # C
    87,  # D
    89,  # E (D5)
]

# Build the walking line with chromatic passing tones
bass_line = [
    77, 78, 79, 81,
    82, 84, 87, 89,
    89, 87, 84, 82,
    78, 77, 79, 81,
    84, 82, 78, 77
]

# Map to time and add to bass instrument
for i, pitch in enumerate(bass_line):
    time = i * beat_length
    velocity = 100
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# --- PIANO ---
# 7th chords on 2 and 4
# F7 chord: F, A, C, E
# Comp on 2 and 4, sharp and emotional, with tension and release

# Define chords for each bar
bar_chords = [
    None,  # No chord on bar 1
    [77, 82, 84, 89],  # F7 on bar 2
    [77, 82, 84, 89],  # F7 on bar 3
    [77, 82, 84, 89],  # F7 on bar 4
]

# Define velocities with dynamic variation
velocities = [100, 110, 120, 115, 100, 105, 120, 110]

for bar in range(2, 5):  # bars 2, 3, 4
    bar_start = bar * bar_length
    # Comp on 2 and 4
    for beat in [1, 3]:
        time = bar_start + beat * beat_length
        for i, pitch in enumerate(bar_chords[bar - 2]):
            velocity = velocities[i]
            note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
            piano.notes.append(note)

# --- SAX ---
# One short motif, haunting, with space and silence
# F (77), Bb (78), C (84), E (89)
# Start on F, end on E, with space

motif = [
    (0.0, 77),  # F
    (0.5, 78),  # Bb
    (1.0, 84),  # C
    (1.5, 89),  # E
]

for start, pitch in motif:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro_wayne.mid')
print("MIDI file written as 'jazz_intro_wayne.mid'")
