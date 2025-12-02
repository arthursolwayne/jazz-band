
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F major
key = 'F'

# Time signature: 4/4
time_signature = (4, 4)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')

# Add instruments
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)

pm.instruments.extend([drums, sax, piano, bass])

# Define the tempo in BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(*time_signature, time=0)]

# Define the duration per bar (6 seconds for 4 bars)
bar_duration = 6.0 / 4
note_duration = 0.375  # 1/8 note in seconds at 160 BPM

# --------------------------
# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# --------------------------
bar1_start = 0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 2 * note_duration, end=bar1_start + 2 * note_duration + note_duration))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + note_duration, end=bar1_start + note_duration + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 3 * note_duration, end=bar1_start + 3 * note_duration + note_duration))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i * note_duration, end=bar1_start + i * note_duration + note_duration))

# --------------------------
# Bars 2-4: Full quartet
# --------------------------
bar2_start = bar_duration
bar3_start = bar2_start + bar_duration
bar4_start = bar3_start + bar_duration

# Define saxophone melody (F major scale: F, G, A, Bb, B, C, D, E)
# Melody: F, rest, G, rest, A, Bb, rest, C — a whispering question
sax_notes = [
    (bar2_start, 72, 0.5),     # F4
    (bar2_start + note_duration, 72, 0),  # rest
    (bar2_start + 2 * note_duration, 74, 0.5),  # G4
    (bar2_start + 3 * note_duration, 74, 0),  # rest
    (bar2_start + 4 * note_duration, 76, 0.5),  # A4
    (bar2_start + 5 * note_duration, 77, 0.5),  # Bb4
    (bar2_start + 6 * note_duration, 76, 0),  # rest
    (bar2_start + 7 * note_duration, 72, 0.5),  # F4
]

for start, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Bass line: Walking line, chromatic approaches, never the same note twice
# F, G, Ab, A, Bb, B, C, D
bass_notes = [
    (bar2_start, 45, 0.5),  # F3
    (bar2_start + note_duration, 47, 0.5),  # G3
    (bar2_start + 2 * note_duration, 46, 0.5),  # Ab3
    (bar2_start + 3 * note_duration, 47, 0.5),  # A3
    (bar2_start + 4 * note_duration, 46, 0.5),  # Bb3
    (bar2_start + 5 * note_duration, 48, 0.5),  # B3
    (bar2_start + 6 * note_duration, 48, 0.5),  # C3
    (bar2_start + 7 * note_duration, 50, 0.5),  # D3
]

for start, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat (Bar2 + 1 * note_duration)
    (bar2_start + note_duration, 64, 0.5),  # F7: F, A, C, Eb
    (bar2_start + note_duration, 67, 0.5),
    (bar2_start + note_duration, 69, 0.5),
    (bar2_start + note_duration, 69, 0.5),  # Eb (from F7)

    # Bar 2 - 4th beat (Bar2 + 3 * note_duration)
    (bar2_start + 3 * note_duration, 64, 0.5),
    (bar2_start + 3 * note_duration, 67, 0.5),
    (bar2_start + 3 * note_duration, 69, 0.5),
    (bar2_start + 3 * note_duration, 69, 0.5),

    # Bar 3 - 2nd beat
    (bar3_start + note_duration, 64, 0.5),
    (bar3_start + note_duration, 67, 0.5),
    (bar3_start + note_duration, 69, 0.5),
    (bar3_start + note_duration, 69, 0.5),

    # Bar 3 - 4th beat
    (bar3_start + 3 * note_duration, 64, 0.5),
    (bar3_start + 3 * note_duration, 67, 0.5),
    (bar3_start + 3 * note_duration, 69, 0.5),
    (bar3_start + 3 * note_duration, 69, 0.5),

    # Bar 4 - 2nd beat
    (bar4_start + note_duration, 64, 0.5),
    (bar4_start + note_duration, 67, 0.5),
    (bar4_start + note_duration, 69, 0.5),
    (bar4_start + note_duration, 69, 0.5),

    # Bar 4 - 4th beat
    (bar4_start + 3 * note_duration, 64, 0.5),
    (bar4_start + 3 * note_duration, 67, 0.5),
    (bar4_start + 3 * note_duration, 69, 0.5),
    (bar4_start + 3 * note_duration, 69, 0.5),
]

for start, pitch, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Add the drum pattern (same as Bar 1)
for i in range(4):
    bar_start = bar2_start + i * bar_duration
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + note_duration))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 2 * note_duration, end=bar_start + 2 * note_duration + note_duration))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + note_duration, end=bar_start + note_duration + note_duration))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 3 * note_duration, end=bar_start + 3 * note_duration + note_duration))

    # Hi-hat on every eighth
    for j in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + j * note_duration, end=bar_start + j * note_duration + note_duration))

# Save the MIDI
pm.write('jazz_intro.mid')
print("MIDI file created: jazz_intro.mid")
