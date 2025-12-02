
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')

# Create instrument tracks
drum_inst = pretty_midi.Instrument(program=drums_program)
sax_inst = pretty_midi.Instrument(program=sax_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
bass_inst = pretty_midi.Instrument(program=bass_program)

pm.instruments = [drum_inst, sax_inst, piano_inst, bass_inst]

# Define time in seconds per bar at 160 BPM
bpm = 160
time_per_beat = 60.0 / bpm  # 0.375 seconds per beat
time_per_bar = 4 * time_per_beat  # 1.5 seconds per bar

# --- BAR 1: Drums only ---
# Kick on 1 & 3, Snare on 2 & 4, Hihat on every 8th

for beat in [0, 2]:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=beat * time_per_beat, end=beat * time_per_beat + 0.1)
    drum_inst.notes.append(kick_note)

for beat in [1, 3]:
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=beat * time_per_beat, end=beat * time_per_beat + 0.1)
    drum_inst.notes.append(snare_note)

for i in range(8):
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=i * time_per_beat / 2, end=i * time_per_beat / 2 + 0.05)
    drum_inst.notes.append(hihat_note)

# --- BAR 2–4: Full Quartet ---

# Time starts at 1.5 seconds (end of Bar 1)
start_time = 1.5

# Bass: Walking line in D minor
bass_notes = [
    # Bar 2: Dm7 (D, F, Ab, C)
    (50, start_time + 0.0, start_time + 0.375),  # D (50)
    (53, start_time + 0.375, start_time + 0.75), # F (53)
    (55, start_time + 0.75, start_time + 1.125), # Ab (55)
    (57, start_time + 1.125, start_time + 1.5),  # C (57)
    
    # Bar 3: Dm7 (chromatic walk down)
    (57, start_time + 1.5, start_time + 1.875),
    (55, start_time + 1.875, start_time + 2.25),
    (53, start_time + 2.25, start_time + 2.625),
    (50, start_time + 2.625, start_time + 3.0),
    
    # Bar 4: Dm7 (chromatic walk up)
    (48, start_time + 3.0, start_time + 3.375),
    (50, start_time + 3.375, start_time + 3.75),
    (52, start_time + 3.75, start_time + 4.125),
    (53, start_time + 4.125, start_time + 4.5),
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    bass_inst.notes.append(note)

# Piano: 7th chords, comping on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, Ab, C) on 2 and 4
    (50, start_time + 0.375, start_time + 0.45),
    (53, start_time + 0.375, start_time + 0.45),
    (55, start_time + 0.375, start_time + 0.45),
    (57, start_time + 0.375, start_time + 0.45),
    
    (50, start_time + 1.125, start_time + 1.2),
    (53, start_time + 1.125, start_time + 1.2),
    (55, start_time + 1.125, start_time + 1.2),
    (57, start_time + 1.125, start_time + 1.2),
    
    # Bar 3: Dm7
    (50, start_time + 2.25, start_time + 2.325),
    (53, start_time + 2.25, start_time + 2.325),
    (55, start_time + 2.25, start_time + 2.325),
    (57, start_time + 2.25, start_time + 2.325),
    
    # Bar 4: Dm7
    (50, start_time + 3.75, start_time + 3.825),
    (53, start_time + 3.75, start_time + 3.825),
    (55, start_time + 3.75, start_time + 3.825),
    (57, start_time + 3.75, start_time + 3.825),
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano_inst.notes.append(note)

# Drums: Continue the energy (kick, snare, hihat)
for bar in range(2, 4):
    for beat in [0, 2]:
        kick_note = pretty_midi.Note(velocity=100, pitch=36, start=(bar * time_per_bar) + beat * time_per_beat, end=(bar * time_per_bar) + beat * time_per_beat + 0.1)
        drum_inst.notes.append(kick_note)

    for beat in [1, 3]:
        snare_note = pretty_midi.Note(velocity=110, pitch=38, start=(bar * time_per_bar) + beat * time_per_beat, end=(bar * time_per_bar) + beat * time_per_beat + 0.1)
        drum_inst.notes.append(snare_note)

    for i in range(8):
        hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=(bar * time_per_bar) + (i * time_per_beat) / 2, end=(bar * time_per_bar) + (i * time_per_beat) / 2 + 0.05)
        drum_inst.notes.append(hihat_note)

# Saxophone: Simple, open-ended motif — D, F, Ab, Bb — playing on beats 1, 2, 3, and 4 of bar 2
sax_notes = [
    (50, start_time + 0.0, start_time + 0.375),  # D
    (53, start_time + 0.375, start_time + 0.75),  # F
    (55, start_time + 0.75, start_time + 1.125),  # Ab
    (57, start_time + 1.125, start_time + 1.5),   # Bb
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax_inst.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro_dmin.mid')

print("MIDI file 'jazz_intro_dmin.mid' generated successfully.")
