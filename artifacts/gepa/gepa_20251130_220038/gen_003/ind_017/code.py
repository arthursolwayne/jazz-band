
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key: F minor (F, Gb, Ab, Bb, B, C, D)
# We'll use F minor (F, Gb, Ab, Bb, B, C, D)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Time per bar = 1.5 seconds (at 160 BPM)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375  # 60 / 160 = 0.375 seconds per beat

# Helper functions
def note_to_midi(note, octave=4):
    note_map = {
        'F': 0, 'Gb': 1, 'Ab': 2, 'Bb': 3, 'B': 4, 'C': 5, 'D': 6
    }
    return note_map[note] + 12 * (octave + 1)

def play_note(instrument, note, time, duration=0.375, velocity=100):
    pitch = note_to_midi(note)
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    instrument.notes.append(note)

# ---------------------------- BAR 1: Drums only ----------------------------

# Little Ray's intro: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: time from 0.0 to 1.5 seconds

# Kick on 1 and 3
play_note(drums, 'C', 0.0, velocity=100, duration=0.1)
play_note(drums, 'C', 0.75, velocity=100, duration=0.1)

# Snare on 2 and 4
play_note(drums, 'Snare', 0.375, velocity=80, duration=0.1)
play_note(drums, 'Snare', 1.125, velocity=80, duration=0.1)

# HiHat on every eighth (16 notes in bar)
for i in range(8):
    play_note(drums, 'HiHat', i * 0.375, velocity=60, duration=0.1)

# ---------------------------- BAR 2: Everyone enters ----------------------------

# Time: 1.5 to 3.0 seconds

# Marcus: Walking bass line in F minor - F, Gb, Ab, Bb, C, D, B, Ab
# (F, Gb, Ab, Bb, B, C, D, Ab) – chromatic approach

bass_notes = ['F', 'Gb', 'Ab', 'Bb', 'B', 'C', 'D', 'Ab']
for i, note in enumerate(bass_notes):
    play_note(bass, note, 1.5 + i * 0.375, duration=0.375)

# Diane: 7th chords on 2 and 4, comping F7, Bb7, D7, Ab7
# Bar 2: time = 1.5 - 3.0

# F7 (F, A, C, Eb) on beat 2 (1.875)
# Bb7 (Bb, D, F, Ab) on beat 4 (2.625)
# Use piano for comping

# F7 on beat 2
play_note(piano, 'F', 1.875, duration=0.1)
play_note(piano, 'A', 1.875, duration=0.1)
play_note(piano, 'C', 1.875, duration=0.1)
play_note(piano, 'Eb', 1.875, duration=0.1)

# Bb7 on beat 4
play_note(piano, 'Bb', 2.625, duration=0.1)
play_note(piano, 'D', 2.625, duration=0.1)
play_note(piano, 'F', 2.625, duration=0.1)
play_note(piano, 'Ab', 2.625, duration=0.1)

# Little Ray continues with same pattern
# Kick on 1 and 3 (2.25 and 3.0)
play_note(drums, 'C', 2.25, velocity=100, duration=0.1)
play_note(drums, 'C', 3.0, velocity=100, duration=0.1)

# Snare on 2 and 4 (2.625 and 3.375)
play_note(drums, 'Snare', 2.625, velocity=80, duration=0.1)
play_note(drums, 'Snare', 3.375, velocity=80, duration=0.1)

# HiHat on every eighth (8 notes at 2.25 - 3.0)
for i in range(8):
    play_note(drums, 'HiHat', 2.25 + i * 0.375, velocity=60, duration=0.1)

# ---------------------------- BAR 3: You take the melody ----------------------------

# Time: 3.0 to 4.5 seconds

# Your motif: F, Ab, Bb, B — a question, a memory, a moment
# One short phrase, resolved in the last bar

# F, Ab, Bb, B — start it, leave it hanging, come back and finish it
# Play on beats 1, 2, 3, 4 of bar 3

# F (beat 1: 3.0)
play_note(sax, 'F', 3.0, duration=0.375, velocity=100)

# Ab (beat 2: 3.375)
play_note(sax, 'Ab', 3.375, duration=0.375, velocity=100)

# Bb (beat 3: 3.75)
play_note(sax, 'Bb', 3.75, duration=0.375, velocity=100)

# B (beat 4: 4.125)
play_note(sax, 'B', 4.125, duration=0.375, velocity=100)

# ---------------------------- BAR 4: Resolution ----------------------------
# Time: 4.5 to 6.0 seconds

# Let the melody return in the next bar (not in this 4-bar intro)

#----------------------------- Write to file -----------------------------
midi.write("dante_introduction.mid")

print("MIDI file 'dante_introduction.mid' has been created.")
