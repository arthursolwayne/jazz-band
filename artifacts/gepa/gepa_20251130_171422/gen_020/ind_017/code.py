
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]
midi.instruments = []

# Define time in seconds per bar
bar_length = 6.0 / 4  # 1.5 seconds per bar
beat_length = bar_length / 4  # 0.375 seconds per beat

def add_note(instrument, pitch, start_time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# --- BAR 1: Little Ray (Drums) sets the groove ---
# Kick on 1 and 3
add_note(drums, 36, 0.0, 0.25)  # Kick on 1
add_note(drums, 36, 1.5, 0.25)  # Kick on 3

# Snare on 2 and 4
add_note(drums, 38, 0.75, 0.25)  # Snare on 2
add_note(drums, 38, 2.25, 0.25)  # Snare on 4

# Hihat on every 8th note
for i in range(0, 4):
    add_note(drums, 42, i * 0.375, 0.125)  # 8th notes

# Add drum instrument
midi.instruments.append(drums)

# --- BAR 2: Full Ensemble Enters ---
# --- Marcus on Bass: Walking line in F major with chromatic approaches ---
bass_notes = [
    (53, 0.0),  # F (Bass) - root
    (55, 0.75), # G (chromatic approach)
    (53, 1.5),  # F again
    (51, 2.25)  # D (chromatic approach)
]
for pitch, time in bass_notes:
    add_note(bass, pitch, time, 0.25)

# --- Diane on Piano: 7th chords on 2 and 4 ---
# F7 (F, A, C, E♭)
add_note(piano, 71, 0.75, 0.25)  # F
add_note(piano, 74, 0.75, 0.25)  # A
add_note(piano, 76, 0.75, 0.25)  # C
add_note(piano, 70, 0.75, 0.25)  # E♭

# C7 on 2.25
add_note(piano, 67, 2.25, 0.25)  # C
add_note(piano, 70, 2.25, 0.25)  # E
add_note(piano, 72, 2.25, 0.25)  # G
add_note(piano, 69, 2.25, 0.25)  # B♭

# --- Dante on Tenor Sax: Melody in F major, concise, searching, emotional ---
# Use F major scale: F, G, A, B♭, C, D, E
# Melody: F - G - A - B♭ - C - D - E - F (but cut off at E)
# Start at 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625

sax_notes = [
    (71, 0.0, 0.25),  # F
    (72, 0.375, 0.25),  # G
    (74, 0.75, 0.25),  # A
    (73, 1.125, 0.25),  # B♭
    (76, 1.5, 0.25),  # C
    (77, 1.875, 0.25),  # D
    (79, 2.25, 0.25),  # E
    (71, 2.625, 0.25)  # F
]

for pitch, time, duration in sax_notes:
    add_note(sax, pitch, time, duration)

# Add instruments to MIDI
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Save MIDI file
midi.write('dantes_intro.mid')
print("MIDI file created: 'dantes_intro.mid'")
