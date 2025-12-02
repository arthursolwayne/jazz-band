
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]  # 160 BPM

# Define time in seconds per bar
bar_length = 1.5  # 6 seconds for 4 bars

# Time per beat in seconds
beat_length = bar_length / 4  # 0.375 seconds per beat

# Define key: F minor
key = 'Fm'

# Create instruments
drums = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# -----------------------------
# BAR 1: Drums only
# -----------------------------
# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=beat_length))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2*beat_length, end=3*beat_length))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1*beat_length, end=1.5*beat_length))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3*beat_length, end=3.5*beat_length))

# Hi-hat on every eighth note
for t in np.arange(0, 4*beat_length, beat_length / 2):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + beat_length / 2))

# -----------------------------
# BAR 2-4: Full ensemble
# -----------------------------

# -----------------------------
# BASS: Walking line in Fm, chromatic approaches
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Chromatic approach to each chord
# Using Fm7 (F, Ab, Bb, Db)
# Walking bass line:
bass_notes = [53, 51, 55, 52, 54, 50, 57, 55, 53, 51, 55, 52, 54, 50, 57, 55]  # F, Eb, G, F#, F, D, A, G, F, Eb, G, F#, F, D, A, G
bass_durations = [beat_length] * len(bass_notes)
for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=i * beat_length, end=(i + 1) * beat_length))

# -----------------------------
# PIANO: 7th chords, comp on beats 2 and 4
# Fm7 (F, Ab, Bb, Db)
# Gm7 (G, Bb, Db, F)
# Am7 (A, C, Eb, G)
# Bb7 (Bb, D, F, Ab)
# Comp on beats 2 and 4 (beat 1 and 3)
piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=80, pitch=53, start=bar_length, end=bar_length + beat_length))  # F (beat 2)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=bar_length, end=bar_length + beat_length))  # Ab
piano_notes.append(pretty_midi.Note(velocity=80, pitch=58, start=bar_length, end=bar_length + beat_length))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=50, start=bar_length, end=bar_length + beat_length))  # Db

# Gm7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar_length * 2, end=bar_length * 2 + beat_length))  # G
piano_notes.append(pretty_midi.Note(velocity=80, pitch=58, start=bar_length * 2, end=bar_length * 2 + beat_length))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=50, start=bar_length * 2, end=bar_length * 2 + beat_length))  # Db
piano_notes.append(pretty_midi.Note(velocity=80, pitch=53, start=bar_length * 2, end=bar_length * 2 + beat_length))  # F

piano.notes.extend(piano_notes)

# -----------------------------
# SAX: Main motif, one short phrase, make it sing
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Start on F, play a short motif that ends on a suspended note
# F - Ab - Bb - B (then leave it hanging)
# Start at bar 2
sax_notes = [
    (53, 0.25),  # F
    (51, 0.25),  # Gb
    (55, 0.25),  # Ab
    (58, 0.25),  # Bb
    (60, 0.25),  # B
]

sax_start = bar_length  # Start at bar 2
for i, (note, dur) in enumerate(sax_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=sax_start + i * dur, end=sax_start + (i + 1) * dur))

# -----------------------------
# Write to MIDI file
# -----------------------------
pm.write("fmin_intro.mid")
print("MIDI file 'fmin_intro.mid' created successfully.")
