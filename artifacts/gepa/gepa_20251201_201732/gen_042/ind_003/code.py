
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.instruments = []

# Set tempo to 160 BPM
pm.time_signature_changes[0].tempo = 160 * (60 / 120)  # convert to MIDI tempo units

# BPM: 160, 4/4 time
# One beat = 0.375 seconds, one bar = 1.5 seconds
# Total length of 4 bars: 6.0 seconds
pm.resolution = 480  # Standard MIDI resolution

# Function to add note to instrument
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instrument.notes.append(note)

# Create instruments
# 1. Bass (Marcus)
bass = pretty_midi.Instrument(program=33)  # Double Bass
pm.instruments.append(bass)

# 2. Piano (Diane)
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano)

# 3. Drums (Little Ray)
drums = pretty_midi.Instrument(program=10)  # Drums
pm.instruments.append(drums)

# 4. Tenor Sax (You)
sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone
pm.instruments.append(sax)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # 4/4 at 160 BPM
beat = bar_length / 4  # 0.375s
time = 0.0

# Drums: Bar 1
add_note(drums, 35, time + 0.0, time + 0.05, 100)  # Kick on 1
add_note(drums, 38, time + 0.375, time + 0.425, 100)  # Snare on 2
add_note(drums, 42, time + 0.75, time + 0.8, 100)  # Kick on 3
add_note(drums, 38, time + 1.125, time + 1.175, 100)  # Snare on 4

# Hihat on every eighth
for i in range(8):
    add_note(drums, 46, time + i * beat / 2, time + i * beat / 2 + 0.05, 100)

time += bar_length

# Bar 2: Bass, Piano, Sax
# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
# Fm7 chord: F, Ab, C, D (but we're in Fm, so maybe F, Ab, C, Eb)
# Let's use Fm (F, Ab, C, Eb) as the underlying harmony

# Bass line: F, Eb, Ab, C (chromatic approach to F)
# Start at time = 1.5

# Bass
add_note(bass, 53, time, time + 0.375, 100)  # F2
add_note(bass, 51, time + 0.375, time + 0.75, 100)  # Eb2
add_note(bass, 56, time + 0.75, time + 1.125, 100)  # Ab2
add_note(bass, 58, time + 1.125, time + 1.5, 100)  # C2

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb) as an open voicing, but resolved on the last
# Use F, Ab, C, Eb in a spread voicing
f = 53  # F2
ab = 60  # Ab3
c = 67  # C4
eb = 64  # Eb4

# Add piano chord on beat 2 and 4
add_note(piano, f, time + 0.375, time + 0.45, 100)
add_note(piano, ab, time + 0.375, time + 0.45, 100)
add_note(piano, c, time + 0.375, time + 0.45, 100)
add_note(piano, eb, time + 0.375, time + 0.45, 100)

add_note(piano, f, time + 1.125, time + 1.2, 100)
add_note(piano, ab, time + 1.125, time + 1.2, 100)
add_note(piano, c, time + 1.125, time + 1.2, 100)
add_note(piano, eb, time + 1.125, time + 1.2, 100)

# Sax: Your voice — short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Let's do F, Bb, F (a simple motif that hangs)

# First note: F (53) on the "and" of 1
add_note(sax, 53, time + 0.1875, time + 0.375, 110)
# Second note: Bb (58) on the "and" of 2
add_note(sax, 58, time + 0.5625, time + 0.75, 110)
# Third note: F (53) on the "and" of 3
add_note(sax, 53, time + 0.9375, time + 1.125, 110)

time += bar_length

# Bar 3: Bass, Piano, Sax
# Bass: Continue walking, this time F, Ab, Bb, C
# Fm7 again

add_note(bass, 53, time, time + 0.375, 100)  # F2
add_note(bass, 56, time + 0.375, time + 0.75, 100)  # Ab2
add_note(bass, 57, time + 0.75, time + 1.125, 100)  # Bb2
add_note(bass, 58, time + 1.125, time + 1.5, 100)  # C2

# Piano: Fm7 again
add_note(piano, f, time + 0.375, time + 0.45, 100)
add_note(piano, ab, time + 0.375, time + 0.45, 100)
add_note(piano, c, time + 0.375, time + 0.45, 100)
add_note(piano, eb, time + 0.375, time + 0.45, 100)

add_note(piano, f, time + 1.125, time + 1.2, 100)
add_note(piano, ab, time + 1.125, time + 1.2, 100)
add_note(piano, c, time + 1.125, time + 1.2, 100)
add_note(piano, eb, time + 1.125, time + 1.2, 100)

# Sax: Let the motif finish — complete it
# The motif is F, Bb, F
# So we repeat the first note on the "and" of 3
add_note(sax, 53, time + 0.9375, time + 1.125, 110)

time += bar_length

# Bar 4: Bass, Piano, Sax
# Fm7 again, but resolved
# Bass: F, Eb, Ab, C
# Piano: F, Ab, C, Eb — but now resolved

add_note(bass, 53, time, time + 0.375, 100)  # F2
add_note(bass, 51, time + 0.375, time + 0.75, 100)  # Eb2
add_note(bass, 56, time + 0.75, time + 1.125, 100)  # Ab2
add_note(bass, 58, time + 1.125, time + 1.5, 100)  # C2

# Piano: Fm7 chord again, but now resolved on the last note
add_note(piano, f, time + 0.375, time + 0.45, 100)
add_note(piano, ab, time + 0.375, time + 0.45, 100)
add_note(piano, c, time + 0.375, time + 0.45, 100)
add_note(piano, eb, time + 0.375, time + 0.45, 100)

add_note(piano, f, time + 1.125, time + 1.2, 100)
add_note(piano, ab, time + 1.125, time + 1.2, 100)
add_note(piano, c, time + 1.125, time + 1.2, 100)
add_note(piano, eb, time + 1.125, time + 1.2, 100)

# Sax: Complete the motif — repeat the first note at the end
add_note(sax, 53, time + 1.125, time + 1.3125, 110)

# Add drums for bar 3 and 4
# Bar 3: Drums
for i in range(8):
    add_note(drums, 46, time + i * beat / 2, time + i * beat / 2 + 0.05, 100)
add_note(drums, 35, time + 0.0, time + 0.05, 100)  # Kick on 1
add_note(drums, 38, time + 0.375, time + 0.425, 100)  # Snare on 2
add_note(drums, 35, time + 0.75, time + 0.8, 100)  # Kick on 3
add_note(drums, 38, time + 1.125, time + 1.175, 100)  # Snare on 4

# Bar 4: Drums
for i in range(8):
    add_note(drums, 46, time + bar_length + i * beat / 2, time + bar_length + i * beat / 2 + 0.05, 100)
add_note(drums, 35, time + bar_length + 0.0, time + bar_length + 0.05, 100)  # Kick on 1
add_note(drums, 38, time + bar_length + 0.375, time + bar_length + 0.425, 100)  # Snare on 2
add_note(drums, 35, time + bar_length + 0.75, time + bar_length + 0.8, 100)  # Kick on 3
add_note(drums, 38, time + bar_length + 1.125, time + bar_length + 1.175, 100)  # Snare on 4

# Write MIDI to file
pm.write("intro_in_Fm.mid")
