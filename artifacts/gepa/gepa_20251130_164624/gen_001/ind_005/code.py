
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define note durations and time per beat
BPM = 160
beat = 60 / BPM
bar = 4 * beat  # 4/4 time
time_per_beat = beat
time_per_bar = bar
time_per_eighth = time_per_beat / 2

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = pretty_midi.Instrument(program=drum_program)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 - 1.5s

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.75 + 0.1))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.125 + 0.1))

# Hihat on all eighths
for i in range(8):
    hihat_time = i * time_per_eighth
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Bar 2: All instruments join
# Time: 1.5 - 3.0s

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (36, 1.5, 1.5 + 0.25),  # C
    (37, 1.75, 1.75 + 0.25),  # C#
    (38, 2.0, 2.0 + 0.25),  # D
    (40, 2.25, 2.25 + 0.25)  # E
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 1.5 + 0.25),   # C
    (64, 1.5, 1.5 + 0.25),   # E
    (67, 1.5, 1.5 + 0.25),   # G
    (71, 1.5, 1.5 + 0.25),   # Bb
    (62, 1.75, 1.75 + 0.25),  # D
    (66, 1.75, 1.75 + 0.25),  # F
    (69, 1.75, 1.75 + 0.25),  # A
    (72, 1.75, 1.75 + 0.25)   # C
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Sax: Motif - a question, unresolved, haunting
# Notes in F minor (F, Ab, Bb, D)
# Each note with unique duration
sax_notes = [
    (53, 1.5, 1.5 + 0.2),  # F
    (50, 1.7, 1.7 + 0.3),  # Ab
    (52, 1.95, 1.95 + 0.25),  # Bb
    (56, 2.2, 2.2 + 0.25)  # D
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 3: Continue the motif with the full band
# Time: 3.0 - 4.5s

# Bass: Walking
bass_notes = [
    (40, 3.0, 3.0 + 0.25),  # E
    (41, 3.25, 3.25 + 0.25),  # F
    (43, 3.5, 3.5 + 0.25),  # G
    (45, 3.75, 3.75 + 0.25)  # A
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords
piano_notes = [
    (60, 3.0, 3.0 + 0.25),   # C
    (64, 3.0, 3.0 + 0.25),   # E
    (67, 3.0, 3.0 + 0.25),   # G
    (71, 3.0, 3.0 + 0.25),   # Bb
    (62, 3.25, 3.25 + 0.25),  # D
    (66, 3.25, 3.25 + 0.25),  # F
    (69, 3.25, 3.25 + 0.25),  # A
    (72, 3.25, 3.25 + 0.25)   # C
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Same pattern
# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.75 + 0.1))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.375 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.125 + 0.1))

# Hihat on all eighths
for i in range(8):
    hihat_time = i * time_per_eighth + 3.0
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Bar 4: Continue the motif with the full band
# Time: 4.5 - 6.0s

# Bass: Walking
bass_notes = [
    (45, 4.5, 4.5 + 0.25),  # A
    (47, 4.75, 4.75 + 0.25),  # Bb
    (49, 5.0, 5.0 + 0.25),  # B
    (50, 5.25, 5.25 + 0.25)  # C
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords
piano_notes = [
    (60, 4.5, 4.5 + 0.25),   # C
    (64, 4.5, 4.5 + 0.25),   # E
    (67, 4.5, 4.5 + 0.25),   # G
    (71, 4.5, 4.5 + 0.25),   # Bb
    (62, 4.75, 4.75 + 0.25),  # D
    (66, 4.75, 4.75 + 0.25),  # F
    (69, 4.75, 4.75 + 0.25),  # A
    (72, 4.75, 4.75 + 0.25)   # C
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Same pattern
# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.5 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.25 + 0.1))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=4.875 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.625 + 0.1))

# Hihat on all eighths
for i in range(8):
    hihat_time = i * time_per_eighth + 4.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Add instruments to the PrettyMIDI object
pm.instruments = [sax, bass, piano, drums]

# Write to MIDI file
pm.write('waynes_question.mid')
