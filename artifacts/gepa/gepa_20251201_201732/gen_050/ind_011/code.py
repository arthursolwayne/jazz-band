
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Time per bar in seconds (160 BPM => 0.375 seconds per beat, 1.5 seconds per bar)
time_per_beat = 0.375
time_per_bar = 1.5

# BAR 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        
        # Kick on 1 and 3
        if beat in [0, 2]:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        
        # Snare on 2 and 4
        if beat in [1, 3]:
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1))
        
        # Hihat on every eighth note
        for eighth in range(2):
            hihat_time = time + eighth * time_per_beat / 2
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# BAR 2: Everyone in, melody starts on saxophone
# Time for bar 2
bar = 1
time = bar * time_per_bar

# Bass line: walking in F minor, roots and fifths with chromatic approaches
# F minor scale: F, G, Ab, A, Bb, B, C
# Walking line: F, Bb, Ab, B, F, Bb, Ab, B
# Use MIDI notes for F2 (F3 is 77, F2 is 70)
bass_notes = [
    (70, time + 0.0, time + 0.1),  # F2
    (71, time + 0.375, time + 0.475),  # G2
    (68, time + 0.75, time + 0.85),  # Ab2
    (72, time + 1.125, time + 1.225),  # B2
    (70, time + 1.5, time + 1.6),  # F2
    (71, time + 1.875, time + 1.975),  # G2
    (68, time + 2.25, time + 2.35),  # Ab2
    (72, time + 2.625, time + 2.725)  # B2
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Open voicings, resolving on bar 4
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Bb7 (Bb, D, F, Ab)
# Each chord is played with open voicings, and comp on 2 and 4

# Bar 2: Fm7 (F, Ab, C, Eb)
chord_notes = [76, 71, 72, 74]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Bar 3: G7 (G, B, D, F)
chord_notes = [77, 79, 80, 76]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + time_per_beat * 2, end=time + time_per_beat * 2 + 0.1))

# Bar 4: Bb7 (Bb, D, F, Ab)
chord_notes = [71, 74, 76, 71]
for note in chord_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + time_per_beat * 3, end=time + time_per_beat * 3 + 0.1))

# Drums: same pattern as bar 1
# Kick and snare on 1, 2, 3, 4
for beat in range(4):
    time = bar * time_per_bar + beat * time_per_beat
    
    if beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    
    if beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1))
    
    for eighth in range(2):
        hihat_time = time + eighth * time_per_beat / 2
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Saxophone: haunting, incomplete motif
# F - Ab - Bb - rest
# Then repeat with variation
# Start at time + 0.25 to give space
start_time = time + 0.25

# First motif
sax_notes = [
    (76, start_time, start_time + 0.1),  # F
    (71, start_time + 0.375, start_time + 0.475),  # Ab
    (74, start_time + 0.75, start_time + 0.85),  # Bb
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Second motif with variation
# F - B - rest
start_time = time + 1.5

sax_notes = [
    (76, start_time, start_time + 0.1),  # F
    (79, start_time + 0.375, start_time + 0.475),  # B
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Save the MIDI file
# midi.write disabled
