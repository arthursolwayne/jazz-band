
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
bass_instrument = Instrument(program=33, is_drum=False)
piano_instrument = Instrument(program=0, is_drum=False)
drums_instrument = Instrument(program=0, is_drum=True)
sax_instrument = Instrument(program=69, is_drum=False)

# Helper function to add notes
def add_notes(instrument, notes, start_time, velocity=100):
    for pitch, duration in notes:
        note = Note(velocity, pitch, start_time, start_time + duration)
        instrument.notes.append(note)

# Timeline in seconds
BAR_DURATION = 0.75  # 160 BPM, 4/4 time, 1 bar = 0.75 seconds
TIME = 0.0

# DRUMS - Bar 1: Only kick and snare on 1 and 3
TIME = 0.0
add_notes(drums_instrument, [(36, 0.375), (38, 0.375)], TIME)  # Kick on 1, Snare on 3
TIME += BAR_DURATION

# DRUMS - Bar 2-4: Full rhythm (kick on 1 and 3, snare on 2 and 4, hihat on eighths)
for bar in range(3):
    TIME = bar * BAR_DURATION
    # Kick on 1 and 3
    add_notes(drums_instrument, [(36, 0.375), (36, 0.375)], TIME, velocity=100)
    # Snare on 2 and 4
    add_notes(drums_instrument, [(38, 0.375), (38, 0.375)], TIME + 0.375, velocity=100)
    # Hi-hat on every eighth
    for i in range(4):
        add_notes(drums_instrument, [(42, 0.1875)], TIME + i * 0.1875, velocity=80)

# BASS - Bar 1: Root with chromatic approach
TIME = 0.0
add_notes(bass_instrument, [(70, 0.75)], TIME)  # F (70) with a chromatic approach
TIME += BAR_DURATION

# BASS - Bar 2: F (70) with approach
add_notes(bass_instrument, [(69, 0.1875), (70, 0.5625)], TIME)

# BASS - Bar 3: B♭ (71) with approach
add_notes(bass_instrument, [(70, 0.1875), (71, 0.5625)], TIME + BAR_DURATION)

# BASS - Bar 4: C (72) with approach
add_notes(bass_instrument, [(71, 0.1875), (72, 0.5625)], TIME + 2 * BAR_DURATION)

# PIANO - Bar 1: Open voicing (F7)
TIME = 0.0
add_notes(piano_instrument, [(70, 0.75), (72, 0.75), (74, 0.75), (77, 0.75)], TIME)

# PIANO - Bar 2: Gm7 (G, B♭, D, F)
TIME = BAR_DURATION
add_notes(piano_instrument, [(71, 0.75), (73, 0.75), (75, 0.75), (70, 0.75)], TIME)

# PIANO - Bar 3: C7 (C, E, G, B)
TIME = 2 * BAR_DURATION
add_notes(piano_instrument, [(72, 0.75), (74, 0.75), (76, 0.75), (79, 0.75)], TIME)

# PIANO - Bar 4: D7 (D, F#, A, C)
TIME = 3 * BAR_DURATION
add_notes(piano_instrument, [(73, 0.75), (76, 0.75), (78, 0.75), (72, 0.75)], TIME)

# SAX - Bar 1: No notes (rest)
# Bar 2: Motif starts — descending line with space
TIME = BAR_DURATION
add_notes(sax_instrument, [(70, 0.1875), (67, 0.1875), (65, 0.1875)], TIME)  # F - D - B♭
TIME += 0.5625  # Leave it hanging

# Bar 3: Rest — let the rhythm and harmony build
# Bar 4: Return with the motif in a new key (C) but keep the shape
TIME = 3 * BAR_DURATION
add_notes(sax_instrument, [(72, 0.1875), (69, 0.1875), (67, 0.1875)], TIME)  # C - A - G

# Add instruments to MIDI
midi.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Save the MIDI file
# midi.write disabled
