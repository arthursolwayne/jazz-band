
import pretty_midi
import numpy as np

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time per bar = 6.0 seconds / 4 bars = 1.5 seconds per bar
# Time per beat = 0.375 seconds

# --- Drums: Bar 1 (0.0 - 1.5 seconds) ---
# Kick on 1 and 3 (0.0, 0.75)
# Snare on 2 and 4 (0.375, 1.125)
# Hihat on every eighth (0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125)
for t in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Kick on 1 and 3
for t in [0.0, 0.75]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.05)
    drums.notes.append(note)

# Snare on 2 and 4
for t in [0.375, 1.125]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.05)
    drums.notes.append(note)

# --- Bass: Bar 1 (0.0 - 1.5 seconds) ---
# Roots and fifths with chromatic approaches
# Dm: D, F, A -> D (root), F (b3), A (5)

# Dm bass line: D -> F -> D -> F (with chromatic approaches)
# Time: 0.0, 0.375, 0.75, 1.125

notes = [
    (0.0, 50, 100),  # D2
    (0.375, 53, 90), # F2 (chromatic approach to F)
    (0.75, 50, 100), # D2
    (1.125, 53, 90)  # F2
]

for start, pitch, vel in notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# --- Piano: Bar 1 (0.0 - 1.5 seconds) ---
# Open voicings on beat 2 and 4 (0.375 and 1.125)
# Comp on 2 and 4, resolve on the last bar

# Bar 1: Dm7 (D, F, A, C)
notes = [
    (0.375, 52, 90), # D (D2)
    (0.375, 55, 90), # F (F2)
    (0.375, 57, 80), # A (A2)
    (0.375, 59, 80), # C (C3)
]

for start, pitch, vel in notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# --- Sax: Bar 1 (0.0 - 1.5 seconds) ---
# No sax in bar 1. Silence is the setup.

# --- Drums: Bars 2-4 (1.5 - 6.0 seconds) ---
# Same pattern, repeated 3 times (bars 2, 3, 4)
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    for t in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
        note = pretty_midi.Note(velocity=80, pitch=42, start=start_time + t, end=start_time + t + 0.05)
        drums.notes.append(note)

    for t in [0.0, 0.75]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start_time + t, end=start_time + t + 0.05)
        drums.notes.append(note)

    for t in [0.375, 1.125]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start_time + t, end=start_time + t + 0.05)
        drums.notes.append(note)

# --- Bass: Bars 2-4 (1.5 - 6.0 seconds) ---
# Dm bass line: D -> F -> D -> F (with chromatic approaches)
# Repeating the pattern for bars 2-4
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    notes = [
        (start_time + 0.0, 50, 100),  # D2
        (start_time + 0.375, 53, 90), # F2
        (start_time + 0.75, 50, 100), # D2
        (start_time + 1.125, 53, 90)  # F2
    ]
    for start, pitch, vel in notes:
        note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
        bass.notes.append(note)

# --- Piano: Bars 2-4 (1.5 - 6.0 seconds) ---
# Open voicings on beat 2 and 4 (0.375 and 1.125)
# Resolve on the last bar (bar 4) with a Dm7 chord

for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Comp on beat 2 (0.375)
    if bar != 4:
        notes = [
            (start_time + 0.375, 52, 90), # D2
            (start_time + 0.375, 55, 90), # F2
            (start_time + 0.375, 57, 80), # A2
            (start_time + 0.375, 59, 80), # C3
        ]
        for start, pitch, vel in notes:
            note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
            piano.notes.append(note)

    # Comp on beat 4 (1.125) with a slight resolution
    if bar == 4:
        notes = [
            (start_time + 1.125, 52, 90), # D2
            (start_time + 1.125, 55, 90), # F2
            (start_time + 1.125, 57, 80), # A2
            (start_time + 1.125, 59, 80), # C3
            (start_time + 1.125, 62, 70)  # F3 (chromatic resolution)
        ]
        for start, pitch, vel in notes:
            note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
            piano.notes.append(note)

# --- Sax: Bars 2-4 (1.5 - 6.0 seconds) ---
# Your moment: A short, haunting motif that doesn't resolve
# Start on beat 1 (1.5) with a single note, leave it hanging

# Dm scale: D, E♭, F, G, A, B♭, C
# Motif: D (50), B♭ (60) — a hint of the minor sixth, unresolved

# Bar 2 (1.5 - 3.0)
note = pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.6, end=1.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=55, start=1.7, end=1.8)
sax.notes.append(note)

# Bar 3 (3.0 - 4.5)
note = pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.1)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.1, end=3.2)
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=55, start=3.2, end=3.3)
sax.notes.append(note)

# Bar 4 (4.5 - 6.0)
note = pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.6)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=4.6, end=4.7)
sax.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=55, start=4.7, end=4.8)
sax.notes.append(note)

# Write the MIDI file
pm.write('dante_russo_4bar_intro.mid')
print("MIDI file 'dante_russo_4bar_intro.mid' has been created.")
