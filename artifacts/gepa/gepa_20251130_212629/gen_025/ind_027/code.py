
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.beat_time = 0.375  # 160 BPM, 60 / 160 = 0.375 seconds per beat
pm.resolution = 480  # MIDI resolution (default)

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define key and scale
key = 'F'
scale = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']  # F major scale

# Time per bar (4/4, 160 BPM)
time_per_bar = 6.0  # 6 seconds per 4 bars
time_per_beat = 0.375  # 6 / 16 = 0.375

# ---------------------------
# 1. Create instruments
# ---------------------------

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# ---------------------------
# 2. Bar 1: Little Ray (drums) only – build tension
# ---------------------------

# Kick on 1 and 3
# Snare on 2 and 4
# Hi-hat on every eighth
# Bar 1: 0.0 - 1.5 seconds

# Kick on 1 and 3
for beat in [0, 2]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * time_per_beat, end=beat * time_per_beat + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4
for beat in [1, 3]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=beat * time_per_beat, end=beat * time_per_beat + 0.1)
    drums.notes.append(snare)

# Hi-hat on every eighth
for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=i * (time_per_beat / 2), end=i * (time_per_beat / 2) + 0.05)
    drums.notes.append(hihat)

# ---------------------------
# 3. Bars 2-4: Full ensemble
# ---------------------------

# Bar 2: 1.5 - 3.0 seconds
# Bar 3: 3.0 - 4.5 seconds
# Bar 4: 4.5 - 6.0 seconds

# Define your motif – a short, open phrase on the tenor sax
# Example: F - Bb - C - E (F7 chord) as a descending line with space
# Using F, Bb, C, E, with rests in between

# Time positions: 0.0, 0.5, 1.0, 1.5 (relative to bar start)
# Let's place notes on 0.0, 0.75 (rest in between), 1.33 (rest), 1.5 (end)

# Bar 2: Start of melody
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.2)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.75 + 0.2)
note3 = pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.0 + 0.2)
note4 = pretty_midi.Note(velocity=100, pitch=76, start=2.3, end=2.3 + 0.2)

sax.notes.extend([note1, note2, note3, note4])

# Bars 2-4: Bass line – walk with chromatic approaches
# Bass notes: F -> G -> Ab -> A -> Bb -> C -> D -> Eb -> F
# Time 1.5 to 6.0
bass_notes = [65, 67, 68, 69, 71, 72, 74, 75, 65]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * time_per_beat
    end = start + 0.2
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4 beats, comp on 2 and 4
# Bar 2: F7 on beat 2 (1.5 + 1.0 = 2.5)
# Bar 3: G7 on beat 2 (3.5)
# Bar 4: C7 on beat 2 (4.5)

# F7 chord: F, A, Bb, C
# G7 chord: G, B, D, F
# C7 chord: C, E, G, Bb

# Function to add chord from root
def add_chord(root, time, duration, instrument):
    notes = []
    if root == 'F':
        notes = [65, 68, 71, 72]  # F, A, Bb, C
    elif root == 'G':
        notes = [67, 71, 74, 65]  # G, B, D, F
    elif root == 'C':
        notes = [60, 64, 67, 71]  # C, E, G, B
    for pitch in notes:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
        instrument.notes.append(note)

# Add chords on 2 and 4 (beat 2 and 4 of each bar)
for bar in [2, 3, 4]:
    time = 1.5 + (bar - 2) * 1.5
    add_chord('F', time + 1.0, 0.2, piano)  # Beat 2
    add_chord('G', time + 2.0, 0.2, piano)  # Beat 4

# ---------------------------
# 4. Save the MIDI
# ---------------------------

pm.write("the_edge_intro.mid")

print("MIDI file 'the_edge_intro.mid' has been saved.")
