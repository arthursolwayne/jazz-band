
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures and key
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: D major (D = 62 MIDI note)
key = 'D'

# Create instruments
bass_program = Program(33)  # Electric Bass
piano_program = Program(0)  # Acoustic Grand Piano
drums_program = Program(0)  # Drums (Use percussion)
sax_program = Program(69)   # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
drums_instrument = Instrument(program=drums_program)
sax_instrument = Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Define timing: 4 bars at 160 BPM
# 4 bars = 6 seconds
# Each bar = 1.5 seconds
# Each beat = 0.375 seconds
bar_length = 1.5
beat_length = 0.375

# Helper function to place notes at a specific time
def add_note(instrument, pitch, start_time, duration=0.375, velocity=100):
    note = Note(pitch=pitch, start=start_time, end=start_time + duration, velocity=velocity)
    instrument.notes.append(note)

# ==============================
# Drums: Bar 1 (Little Ray alone)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 starts at time 0.0
# Bar 1 = 0.0 - 1.5

# Kick on 1 (0.0) and 3 (0.75)
add_note(drums_instrument, 36, 0.0, 0.125, 100)  # Kick
add_note(drums_instrument, 36, 0.75, 0.125, 100)  # Kick

# Snare on 2 (0.375) and 4 (1.125)
add_note(drums_instrument, 38, 0.375, 0.125, 100)  # Snare
add_note(drums_instrument, 38, 1.125, 0.125, 100)  # Snare

# Hi-hat on every eighth
hi_hat_notes = [42, 42, 42, 42, 42, 42, 42, 42]
for i, pitch in enumerate(hi_hat_notes):
    add_note(drums_instrument, pitch, i * beat_length, 0.125, 80)

# ==============================
# Bass: Bar 1 (Walking line, D2 to G2)
# D2 = MIDI 38, G2 = MIDI 43
# Walking line: D2, F#2, G2, A2, D2, F#2, G2, A2
# Roots and fifths with chromatic approaches
# Bar 1 = 0.0 - 1.5

bass_notes = [38, 40, 43, 45, 38, 40, 43, 45]
for i, pitch in enumerate(bass_notes):
    add_note(bass_instrument, pitch, i * beat_length, 0.125, 80)

# ==============================
# Piano: Bar 1 - Open voicings, comp on 2 and 4
# D major chord (D F# A) - open voicing: D (62), A (69), F# (66), C# (63)
# Bar 1 = 0.0 - 1.5
# Comp on 2 and 4 (beat 2 and beat 4)

piano_notes = [[62, 66, 69, 63], [62, 66, 69, 63]]  # Two chords, on beat 2 and 4
for i, chord in enumerate(piano_notes):
    time = (i + 1) * beat_length  # Beat 2 and beat 4
    for pitch in chord:
        add_note(piano_instrument, pitch, time, 0.25, 90)

# ==============================
# Bar 2-4: Everyone in, sax takes melody
# You: Tenor sax, one short motif, make it sing. Start it, leave it hanging, finish it.

# Time for bar 2 = 1.5
# Bar 2-4 = 1.5 to 4.5

# Tenor sax melody (D major scale: D, E, F#, G, A, B, C#, D)
# Your motif: D, E, F#, G (start), leave it hanging, return with A, B, C#, D

# D = 62, E = 64, F# = 66, G = 67, A = 69, B = 71, C# = 72

# Bar 2 (1.5-3.0)
add_note(sax_instrument, 62, 1.5, 0.375)  # D
add_note(sax_instrument, 64, 1.875, 0.375)  # E
add_note(sax_instrument, 66, 2.25, 0.375)   # F#
add_note(sax_instrument, 67, 2.625, 0.375)  # G

# Bar 3 (3.0-4.5)
add_note(sax_instrument, 69, 3.0, 0.375)   # A
add_note(sax_instrument, 71, 3.375, 0.375)  # B
add_note(sax_instrument, 72, 3.75, 0.375)   # C#
add_note(sax_instrument, 62, 4.125, 0.375)  # D (return to D, completing the motif)

# Piano: Bar 2-4, open voicings. Each bar different chord: D, G, A, D
# Bar 2: Dmaj7 (D F# A C#) - open voicing
# Bar 3: G7 (G B D F) - open voicing
# Bar 4: Amaj7 (A C# E G) - open voicing
# Bar 2 (1.5-3.0)
piano_notes = [[62, 66, 69, 72], [67, 71, 69, 65], [69, 72, 74, 67]]
for i, chord in enumerate(piano_notes):
    time = 1.5 + i * bar_length
    for pitch in chord:
        add_note(piano_instrument, pitch, time, 0.5, 90)

# Bass: Bar 2-4, walking line, roots and fifths
# D2 to G2 to A2 to D2
# Bar 2: D2, F#2, G2, A2
# Bar 3: A2, C#2, D2, E2
# Bar 4: D2, F#2, G2, A2

bass_notes = [
    [38, 40, 43, 45],
    [45, 47, 49, 51],
    [38, 40, 43, 45]
]
for i, bar in enumerate(bass_notes):
    for j, pitch in enumerate(bar):
        time = 1.5 + i * bar_length + j * beat_length
        add_note(bass_instrument, pitch, time, 0.125, 80)

# Drums: Bar 2-4 (same pattern as bar 1, but extended)
for i in range(2, 4):
    time_start = i * bar_length
    # Kick on 1 and 3
    add_note(drums_instrument, 36, time_start + 0.0, 0.125, 100)
    add_note(drums_instrument, 36, time_start + 0.75, 0.125, 100)

    # Snare on 2 and 4
    add_note(drums_instrument, 38, time_start + 0.375, 0.125, 100)
    add_note(drums_instrument, 38, time_start + 1.125, 0.125, 100)

    # Hi-hat on every eighth
    for j in range(8):
        add_note(drums_instrument, 42, time_start + j * beat_length, 0.125, 80)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
