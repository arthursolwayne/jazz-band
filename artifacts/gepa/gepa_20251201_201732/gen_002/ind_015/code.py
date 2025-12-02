
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to F minor (key number 21)
pm.key_signature_changes = [pretty_midi.KeySignature(21, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# Time per beat in seconds
tempo = 160  # BPM
beat = 60.0 / tempo  # seconds per beat
bar_length = 4 * beat  # 4 bars = 6 seconds

# Define the start time for each bar in seconds
bar_times = [0, beat, 2 * beat, 3 * beat]

# === DRUMS: Little Ray (Bar 1) ===
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start_time = bar_times[bar]
    for i in range(8):
        # Kick on 1 and 3 (beats 0 and 2 of the bar)
        if i == 0 or i == 2:
            note = pretty_midi.Note(velocity=80, pitch=36, start=start_time + i * beat / 8, end=start_time + i * beat / 8 + 0.1)
            drums.notes.append(note)
        # Snare on 2 and 4 (beats 1 and 3 of the bar)
        if i == 1 or i == 3:
            note = pretty_midi.Note(velocity=80, pitch=38, start=start_time + i * beat / 8, end=start_time + i * beat / 8 + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * beat / 8, end=start_time + i * beat / 8 + 0.1)
        drums.notes.append(note)

# === BASS: Marcus (Bars 1-4) ===
# Walking bass line in Fm (F, Ab, D, C, F, Ab, D, C)
# Root and fifth with chromatic approaches
bass_notes = [
    # Bar 1
    (45, 0),  # F2
    (40, 0.25),  # Eb2 (chromatic approach)
    (50, 0.5),  # C3 (fifth)
    (48, 0.75),  # Bb2 (chromatic approach)

    # Bar 2
    (48, 1),  # Bb2
    (45, 1.25),  # F2
    (55, 1.5),  # D3 (fifth)
    (53, 1.75),  # C#3 (chromatic approach)

    # Bar 3
    (53, 2),  # C#3
    (50, 2.25),  # C3
    (57, 2.5),  # E3 (fifth)
    (55, 2.75),  # D3

    # Bar 4
    (55, 3),  # D3
    (50, 3.25),  # C3
    (60, 3.5),  # F4 (octave)
    (58, 3.75),  # Eb4 (chromatic approach)
]

for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# === PIANO: Diane (Bars 2-4) ===
# Open voicings, resolving on the last chord of each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: C7 (C, E, G, Bb)

# Bar 2
piano_notes = [
    (65, 1, 0.5),  # F4
    (60, 1, 0.5),  # Ab4
    (67, 1, 0.5),  # C5
    (65, 1, 0.5),  # Eb5
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3
piano_notes = [
    (62, 2, 0.5),  # D4
    (65, 2, 0.5),  # F4
    (67, 2, 0.5),  # A4
    (67, 2, 0.5),  # C5
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 4
piano_notes = [
    (60, 3, 0.5),  # C4
    (64, 3, 0.5),  # E4
    (67, 3, 0.5),  # G4
    (62, 3, 0.5),  # Bb4
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# === SAX: Dante (Bars 2-4) ===
# Motif: F, Ab, C, G (Fm7 -> G7)
# Start it, leave it hanging, come back and finish it

# Bar 2: F, Ab, C
note = pretty_midi.Note(velocity=100, pitch=65, start=1, end=1 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.25, end=1.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75)
sax.notes.append(note)

# Bar 3: Rest
# Bar 4: G, Bb, D (G7)
note = pretty_midi.Note(velocity=100, pitch=67, start=3, end=3 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
sax.notes.append(note)

# Write the MIDI file to disk
pm.write("fm_intro.mid")
