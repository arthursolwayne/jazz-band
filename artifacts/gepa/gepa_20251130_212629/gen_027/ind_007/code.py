
import pretty_midi
import numpy as np

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set key signature to D minor
pm.key_signatures = [pretty_midi.KeySignature(1, 0.0)]  # D minor (1 = D)

# Define the time per bar in seconds
BPM = 160
time_per_beat = 60.0 / BPM
time_per_bar = time_per_beat * 4  # 4 bars = 6 seconds

# Define instruments
program_drums = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
program_piano = pretty_midi.instrument_name_to_program('Electric Piano')
program_bass = pretty_midi.instrument_name_to_program('Double Bass')
program_sax = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
drums = pretty_midi.Instrument(program=program_drums)
piano = pretty_midi.Instrument(program=program_piano)
bass = pretty_midi.Instrument(program=program_bass)
sax = pretty_midi.Instrument(program=program_sax)

# Add instruments to the MIDI file
pm.instruments = [drums, piano, bass, sax]

# Define bar start times
bar_start_times = [0.0, time_per_bar, time_per_bar * 2, time_per_bar * 3]

# -----------------------------
# BAR 1: Little Ray on Drums
# -----------------------------
# Snare on 2 and 4
snare_hits = [time_per_bar * (1/4) * 2, time_per_bar * (1/4) * 4]
for hit in snare_hits:
    note = pretty_midi.Note(velocity=90, pitch=68, start=hit, end=hit + 0.1)
    drums.notes.append(note)

# Kick on 1 and 3
kick_hits = [0.0, time_per_bar * 2]
for hit in kick_hits:
    note = pretty_midi.Note(velocity=100, pitch=36, start=hit, end=hit + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_notes = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for hit in hihat_notes:
    note = pretty_midi.Note(velocity=85, pitch=42, start=hit, end=hit + 0.05)
    drums.notes.append(note)

# -----------------------------
# BAR 2-4: Everyone in. Tenor sax takes the melody.
# -----------------------------

# Define the sax motif (4 bars, 4 measures)
# Start at time 1.5 seconds (bar 2)
# Dm7: Dm7 is D, F, A, C (root, b3, 5, b7)

# Motif: D, F, A, C — but with space and variation
# Start with D, rest, F, A, rest, C — leave it hanging

# Define the note times and durations
sax_notes = [
    (1.5, 0.25, 62),   # D (note 62)
    (1.75, 0.25, 65),  # F (note 65)
    (2.0, 0.25, 67),   # A (note 67)
    (2.25, 0.25, 69)   # C (note 69)
]

# Add the sax notes
for start, duration, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# -----------------------------
# Bass line: Walking line with chromatic approaches
# -----------------------------
# Start at bar 2 (time 1.5 seconds)
bass_notes = [
    (1.5, 0.25, 62),   # D
    (1.75, 0.25, 63),  # Eb (chromatic approach)
    (2.0, 0.25, 60),   # C
    (2.25, 0.25, 62)   # D
]

for start, duration, pitch in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# -----------------------------
# Piano: 7th chords on beat 2 and 4
# -----------------------------
# Dm7: D, F, A, C
# Start at bar 2, play on beat 2 and 4
piano_notes = [
    (1.75, 0.25, 62),   # D
    (1.75, 0.25, 65),   # F
    (1.75, 0.25, 67),   # A
    (1.75, 0.25, 69),   # C

    (2.25, 0.25, 62),   # D
    (2.25, 0.25, 65),   # F
    (2.25, 0.25, 67),   # A
    (2.25, 0.25, 69)    # C
]

for start, duration, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# -----------------------------
# Save the MIDI file
# -----------------------------
pm.write("dante_intro.mid")
print("MIDI file created: dante_intro.mid")
