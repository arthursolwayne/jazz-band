
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Electric Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define time in seconds per beat
bpm = 160
beats_per_bar = 4
time_per_beat = 60 / bpm
time_per_bar = time_per_beat * beats_per_bar

# Define note durations in seconds
eighth = time_per_beat / 2
quarter = time_per_beat
half = time_per_beat * 2
whole = time_per_beat * 4

# Define the key: Fm (F, Ab, Bb)
# Root = F (65), Ab = 69, Bb = 70, C = 72, Eb = 74, Gb = 76, G = 78

# Time reference
time = 0.0

# -----------------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add dynamic velocity and syncopation
# -----------------------------

# Bar 1 (time 0.0 to 1.5s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=0.75 + 0.1))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + 0.08))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.125 + 0.08))

# Hihat on every eighth
hihat_notes = [42, 42, 42, 42, 42, 42, 42, 42]
for i, note in enumerate(hihat_notes):
    start = i * eighth
    end = start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=end))

# Bar 2 (time 1.5 to 3.0s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=95, pitch=36, start=1.5, end=1.5 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=36, start=2.25, end=2.25 + 0.1))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=105, pitch=38, start=1.875, end=1.875 + 0.08))
drums.notes.append(pretty_midi.Note(velocity=105, pitch=38, start=2.625, end=2.625 + 0.08))

# Hihat on every eighth
for i, note in enumerate(hihat_notes):
    start = 1.5 + i * eighth
    end = start + 0.05
    drums.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=end))

# -----------------------------
# BASS: Marcus
# Walking line, chromatic approaches, never the same note twice
# -----------------------------

# Bar 1 (time 0.0 to 1.5s)
# Fm7 -> Ab -> Bb -> C -> Fm7
bass_notes = [65, 69, 70, 72, 65]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + quarter / 4))
    time += quarter / 4

# Bar 2 (time 1.5 to 3.0s)
# Fm7 -> Ab -> Bb -> Eb -> Fm7
bass_notes = [65, 69, 70, 74, 65]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + quarter / 4))
    time += quarter / 4

# -----------------------------
# PIANO: Diane
# 7th chords, comp on 2 and 4
# Emotional, sharp, tension and release
# -----------------------------

# Bar 1 (time 0.0 to 1.5s)
# Fm7 on 1, Ab7 on 2, Bb7 on 3, Fm7 on 4 (but comp on 2 and 4)

# Fm7 on 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.0, end=0.0 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=0.0, end=0.0 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=0.0, end=0.0 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=0.0, end=0.0 + 0.2))

# Ab7 on 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=0.375, end=0.375 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=0.375, end=0.375 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=0.375, end=0.375 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=0.375, end=0.375 + 0.2))

# Bar 2 (time 1.5 to 3.0s)
# Bb7 on 3 (notate here), but comp on 2 and 4

# Fm7 on 1
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.5 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.5 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.5 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.5 + 0.2))

# Bb7 on 2
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=1.875 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=1.875 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=1.875 + 0.2))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=1.875 + 0.2))

# -----------------------------
# SAX: Dante
# One short motif, haunting, make it sing, leave it hanging
# -----------------------------

# Bar 1 (time 0.0 to 1.5s): motif
# Motif: F (65), Ab (69), Bb (70), rest
# Then repeat with a slight variation

# First part (0.0 to 0.6s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=0.0, end=0.0 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=0.2, end=0.2 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=0.4, end=0.4 + 0.2))

# Bar 2 (time 1.5 to 3.0s): repeat with slight variation (add a trill or slight delay)
# F, Ab, Bb, rest (but slightly delayed or with a trill on F)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.7, end=1.7 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=1.9, end=1.9 + 0.2))

# Save the MIDI file
midi.writeFile("dante_intro.mid")
