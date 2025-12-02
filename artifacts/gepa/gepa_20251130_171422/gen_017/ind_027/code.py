
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: Dm (D minor)
key = 'Dm'

# Time signature: 4/4
time_signature = (4, 4)

# Define the number of bars and the duration per bar (in seconds)
num_bars = 4
bar_duration = 6.0 / num_bars  # 6 seconds total for 4 bars
tempo = 160
beat_duration = 60.0 / tempo  # 0.375 seconds per beat
note_duration = beat_duration  # Each note is 1 beat

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Drums')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drum_inst = pretty_midi.Instrument(program=drum_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drum_inst)
pm.instruments.append(bass_inst)
pm.instruments.append(piano_inst)
pm.instruments.append(sax_inst)

# Define the Dm scale (D, F, G, A, C, D, F)
# Notes in MIDI: D (62), F (64), G (67), A (69), C (60), D (62), F (64)
# Dm7 = D, F, A, C (MIDI: 62, 64, 69, 60)

# --- DRUMS: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth ---
for bar in range(num_bars):
    for beat in range(4):
        time = bar * bar_duration + beat * beat_duration
        if beat in [0, 2]:
            drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_duration))  # Kick
        if beat in [1, 3]:
            drum_inst.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + note_duration))  # Snare
        for eighth in [0, 1]:
            drum_inst.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * (beat_duration / 2), end=time + eighth * (beat_duration / 2) + (beat_duration / 2)))  # Hi-hat

# --- BASS: Walking line in Dm, with chromatic approaches ---
# Dm scale: D (62), F (64), G (67), A (69), C (60), D (62), F (64)
# Walking line: D -> C -> D -> F -> G -> A -> Bb -> A -> G -> F -> G -> A -> Bb -> C -> D
# + chromatic approach on some notes

bass_notes = [62, 60, 62, 64, 67, 69, 70, 69, 67, 64, 67, 69, 70, 69, 67, 62]
for i, note in enumerate(bass_notes):
    time = (i % 16) * beat_duration
    bar = (i % 16) // 4
    if bar < num_bars:
        bass_inst.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_duration))

# --- PIANO: 7th chords on 2 and 4, comping (Dm7, F7, Gm7, A7) ---
# Dm7: 62 (D), 64 (F), 69 (A), 60 (C)
# F7: 64 (F), 67 (G), 71 (A), 65 (Bb)
# Gm7: 67 (G), 69 (Bb), 72 (D), 71 (F)
# A7: 69 (A), 71 (C), 76 (E), 74 (G)

piano_notes = []
for bar in range(num_bars):
    for beat in [1, 3]:
        time = bar * bar_duration + beat * beat_duration
        chord_notes = []
        if beat == 1:
            # Dm7
            chord_notes = [62, 64, 69, 60]
        else:
            # F7
            chord_notes = [64, 67, 71, 65]
        for note in chord_notes:
            piano_inst.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration))

# --- SAX: Short motif in Dm, with tension and release ---
# Melody: D (62) -> F (64) -> G (67) -> D (62) — then repeat with a slight variation
# We start it, leave it hanging, and return
sax_notes = [
    (62, 0.0),    # D
    (64, 0.375),  # F
    (67, 0.75),   # G
    (62, 1.125),  # D — then silence
    (62, 2.0),    # D again
    (64, 2.375),  # F
    (67, 2.75),   # G
    (62, 3.125)   # D
]

for i, (pitch, start_time) in enumerate(sax_notes):
    sax_inst.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start_time, end=start_time + note_duration))

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
