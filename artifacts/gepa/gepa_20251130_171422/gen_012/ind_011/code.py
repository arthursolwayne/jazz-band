
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, piano, bass, sax]

# Set BPM and note duration
BPM = 160
note_duration = 60.0 / BPM  # seconds per beat
bar_duration = 4 * note_duration  # 4 beats per bar
total_time = bar_duration * 4  # 4 bars

# Function to create a note
def create_note(note_number, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    return note

# DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    for beat in range(4):
        time = bar * bar_duration + beat * note_duration
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            drums.notes.append(create_note(36, time, time + note_duration, velocity=80))
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            drums.notes.append(create_note(38, time, time + note_duration, velocity=80))
        # Hi-Hat on every eighth note
        for eighth in range(2):
            hihat_time = time + (eighth * note_duration / 2)
            drums.notes.append(create_note(42, hihat_time, hihat_time + note_duration / 2, velocity=60))

# PIANO: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Root position for bar 2 and 4
for bar in [1, 3]:
    time = bar * bar_duration
    # Fm7 chord (F, Ab, C, Eb) — root position, played on beat 2 and 4
    root = 65  # F
    third = 68  # Ab
    fifth = 72  # C
    seventh = 69  # Eb

    for beat in [1, 3]:
        chord_start = bar * bar_duration + beat * note_duration
        # Play chord for 0.5 beats
        piano.notes.append(create_note(root, chord_start, chord_start + note_duration / 2, velocity=80))
        piano.notes.append(create_note(third, chord_start, chord_start + note_duration / 2, velocity=80))
        piano.notes.append(create_note(fifth, chord_start, chord_start + note_duration / 2, velocity=80))
        piano.notes.append(create_note(seventh, chord_start, chord_start + note_duration / 2, velocity=80))

# BASS: Walking line, chromatic approaches, never the same note twice
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [65, 66, 68, 69, 71, 72, 73, 74]  # F, Gb, Ab, A, Bb, B, C, Db
bass_pattern = [65, 67, 68, 69, 71, 72, 73, 74, 69, 71, 72, 68, 69, 71, 72, 73]

for i, note in enumerate(bass_pattern):
    start = note_duration * i
    end = start + note_duration
    bass.notes.append(create_note(note, start, end, velocity=70))

# SAX: Your moment — a short motif, start it, leave it hanging, come back and finish it
# Fm key - F minor
# Motif: F, Bb, Gb, rest (then repeat)
motif = [65, 71, 66, -1]  # F, Bb, Gb, rest

# First presentation (Bar 1: only sax)
for i, note in enumerate(motif):
    if note != -1:
        start = i * note_duration
        end = start + note_duration
        sax.notes.append(create_note(note, start, end, velocity=100))

# Second presentation (Bar 2: repeat the motif, but shift it)
# Shift by 1 beat
for i, note in enumerate(motif):
    if note != -1:
        start = bar_duration + i * note_duration
        end = start + note_duration
        sax.notes.append(create_note(note, start, end, velocity=100))

# Write the MIDI file
pm.write("dante_russo_intro.mid")

print("MIDI file 'dante_russo_intro.mid' created successfully.")
