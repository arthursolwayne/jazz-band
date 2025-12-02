
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: D major (key number 2)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]

# Set up instruments
# 1. Drums (channel 9)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)
pm.instruments.append(drums)

# 2. Bass (channel 0)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# 3. Piano (channel 1)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# 4. Saxophone (channel 2)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# MIDI note numbers for D major scale
D_MAJOR = [50, 52, 53, 55, 57, 59, 60]  # C4, D4, E4, F4, G4, A4, B4

# General timing parameters
beat = 0.375  # in seconds at 160 BPM
bar = 1.5     # in seconds

# Drums: Bar 1 (6.0 seconds)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat_index in range(8):  # 8 eighth notes per bar
    time = beat_index * 0.375
    if beat_index % 2 == 0:
        # Kick on 1 and 3 (0 and 2 in 0-7)
        if beat_index in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4 (1 and 3 in 0-7)
        if beat_index in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bass: Bar 1
# Walking line, chromatic approach, no repeated notes
# Starting on D (50)
bass_notes = [50, 51, 52, 53, 55, 57, 59, 60, 59, 57, 55, 53, 52, 51, 50, 50]
note_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for i, note in enumerate(bass_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=note_times[i], end=note_times[i] + 0.125)
    bass.notes.append(note_obj)

# Piano: Bar 1 (no notes)
# Bar 2: Comp on 2 and 4 with 7th chords
# Time: 6.0 to 9.0 seconds
bar_start = 6.0
bar_end = 9.0
comp_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (50, 52, 57, 60),  # D7
    # Bar 3: G7 (G, B, D, F)
    (57, 59, 62, 65),  # G7
    # Bar 4: A7 (A, C#, E, G)
    (57, 60, 64, 69),  # A7
]

for i, chord in enumerate(comp_notes):
    # Place chord on 2 and 4 (0.75 and 1.5 seconds into each bar)
    time = bar_start + i * bar + 0.75
    for note in chord:
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note_obj)
    time = bar_start + i * bar + 1.5
    for note in chord:
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note_obj)

# Sax: Bar 2-4
# Simple motif: D, F#, G, E — a question, unresolved
# Start at bar 2 (6.0 seconds)
motif = [50, 52, 53, 57]  # D, F#, G, E
note_times = [6.0, 6.375, 6.75, 7.125]
note_durations = [0.375, 0.375, 0.375, 0.375]

for i, note in enumerate(motif):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=note_times[i], end=note_times[i] + note_durations[i])
    sax.notes.append(note_obj)

# Optional: repeat the first two notes at the end of the intro (Bar 4)
note_times_end = [8.625, 8.75]
for i, note in enumerate(motif[:2]):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=note_times_end[i], end=note_times_end[i] + 0.125)
    sax.notes.append(note_obj)

# Save the MIDI file
pm.write("dante_intro.mid")
