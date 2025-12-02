
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F minor
pm.key_signature = pretty_midi.KeySignature(key='f', mode='minor')

# Define instruments
# Tenor Sax (program 64)
tenor_sax = pretty_midi.Instrument(program=64)
pm.instruments.append(tenor_sax)

# Bass (program 33)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (program 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (program 9)
drums = pretty_midi.Instrument(program=9)
pm.instruments.append(drums)

# Time parameters
BPM = 160
note_duration = 0.375  # 1 beat in 160 BPM = 0.375s
bar_length = 1.5  # 4/4 at 160 BPM is 1.5 seconds

# DYNAMICS
velocities = [90, 85, 95, 80, 88, 92, 83, 87]  # dynamic variation

# TIMING OFFSETS (for subtle human feel)
timing_offsets = [0.0, -0.01, 0.02, -0.02, 0.01, -0.03, 0.0, -0.01]

# BAR 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use MIDI note numbers for drums:
# Kick: 36, Snare: 38, Hihat: 42

# Bar 1: 4 beats
for beat in range(4):
    time = beat * note_duration + timing_offsets[beat]
    if beat % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1))
    # Hihat on every eighth
    if beat % 2 == 0:
        hi_hat_time = time + 0.1875
    else:
        hi_hat_time = time
    drums.notes.append(pretty_midi.Note(velocity=85, pitch=42, start=hi_hat_time, end=hi_hat_time + 0.1))

# BAR 2: Everyone enters
# Tenor Sax melody: short motif, start, leave hanging
# Use Fm scale: F, Gb, Ab, Bb, B, Db, Eb

# Tenor motif: F, Ab, Bb, rest
tenor_notes = [
    (65, 0.0, 90),  # F (65)
    (69, 0.375, 95), # Ab (69)
    (67, 0.75, 92),  # Bb (67)
    (None, 1.125, 0) # Rest
]

for i, (pitch, time_offset, velocity) in enumerate(tenor_notes):
    if pitch is not None:
        start = (1 + i) * note_duration + timing_offsets[i]
        tenor_sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Bass: Walking line, chromatic approaches
# Fm walking line: F, Gb, Ab, Bb, B, Db, Eb, F
# Start on F (bar 2), walk down chromatically

bass_notes = [
    (65, 0.0, 70),   # F
    (64, 0.375, 75), # Gb
    (69, 0.75, 70),  # Ab
    (67, 1.125, 75), # Bb
]

for i, (pitch, time_offset, velocity) in enumerate(bass_notes):
    start = (1 + i) * note_duration + timing_offsets[i]
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Piano: 7th chords on 2 and 4
# Fm7: F, Ab, Bb, Db
# Bbm7: Bb, Db, F, Ab

# Bar 2: 2nd beat (time = 0.375)
piano_notes_bar2_2 = [
    (65, 0.375, 80),  # F
    (69, 0.375, 80),  # Ab
    (67, 0.375, 80),  # Bb
    (64, 0.375, 80)   # Db
]
for pitch, time, velocity in piano_notes_bar2_2:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# Bar 2: 4th beat (time = 1.125)
piano_notes_bar2_4 = [
    (67, 1.125, 80),  # Bb
    (64, 1.125, 80),  # Db
    (65, 1.125, 80),  # F
    (69, 1.125, 80)   # Ab
]
for pitch, time, velocity in piano_notes_bar2_4:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# BAR 3: Tenor continues motif, but doesn't resolve
# Echo the first motif, but shift the last note
tenor_notes_bar3 = [
    (65, 0.0, 90),   # F
    (69, 0.375, 95), # Ab
    (67, 0.75, 92),  # Bb
    (64, 1.125, 90)  # Gb (instead of rest)
]

for i, (pitch, time_offset, velocity) in enumerate(tenor_notes_bar3):
    if pitch is not None:
        start = (2 + i) * note_duration + timing_offsets[i]
        tenor_sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Bass continues walking
bass_notes_bar3 = [
    (62, 0.0, 70),   # Eb
    (65, 0.375, 75), # F
    (64, 0.75, 70),  # Gb
    (69, 1.125, 75)  # Ab
]

for i, (pitch, time_offset, velocity) in enumerate(bass_notes_bar3):
    start = (2 + i) * note_duration + timing_offsets[i]
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Piano: 7th chords on 2 and 4
# Abm7: Ab, Bb, Db, F
# Dbm7: Db, F, Ab, Bb

# Bar 3: 2nd beat (time = 0.375)
piano_notes_bar3_2 = [
    (69, 0.375, 80),  # Ab
    (67, 0.375, 80),  # Bb
    (64, 0.375, 80),  # Db
    (65, 0.375, 80)   # F
]
for pitch, time, velocity in piano_notes_bar3_2:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# Bar 3: 4th beat (time = 1.125)
piano_notes_bar3_4 = [
    (64, 1.125, 80),  # Db
    (65, 1.125, 80),  # F
    (69, 1.125, 80),  # Ab
    (67, 1.125, 80)   # Bb
]
for pitch, time, velocity in piano_notes_bar3_4:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# BAR 4: Tenor ends with a question, not a resolution
# Motif: F, Ab, rest, Bb
tenor_notes_bar4 = [
    (65, 0.0, 95),   # F
    (69, 0.375, 95), # Ab
    (None, 0.75, 0), # Rest
    (67, 1.125, 90)  # Bb
]

for i, (pitch, time_offset, velocity) in enumerate(tenor_notes_bar4):
    if pitch is not None:
        start = (3 + i) * note_duration + timing_offsets[i]
        tenor_sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Bass continues walking
bass_notes_bar4 = [
    (67, 0.0, 70),   # Bb
    (62, 0.375, 75), # Eb
    (65, 0.75, 70),  # F
    (64, 1.125, 75)  # Gb
]

for i, (pitch, time_offset, velocity) in enumerate(bass_notes_bar4):
    start = (3 + i) * note_duration + timing_offsets[i]
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Piano: 7th chords on 2 and 4
# Bbm7: Bb, Db, F, Ab
# Fm7: F, Ab, Bb, Db

# Bar 4: 2nd beat (time = 0.375)
piano_notes_bar4_2 = [
    (67, 0.375, 80),  # Bb
    (64, 0.375, 80),  # Db
    (65, 0.375, 80),  # F
    (69, 0.375, 80)   # Ab
]
for pitch, time, velocity in piano_notes_bar4_2:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# Bar 4: 4th beat (time = 1.125)
piano_notes_bar4_4 = [
    (65, 1.125, 80),  # F
    (69, 1.125, 80),  # Ab
    (67, 1.125, 80),  # Bb
    (64, 1.125, 80)   # Db
]
for pitch, time, velocity in piano_notes_bar4_4:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1))

# Bar 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = (3 + beat) * note_duration + timing_offsets[beat]
    if beat % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1))
    # Hihat on every eighth
    if beat % 2 == 0:
        hi_hat_time = time + 0.1875
    else:
        hi_hat_time = time
    drums.notes.append(pretty_midi.Note(velocity=85, pitch=42, start=hi_hat_time, end=hi_hat_time + 0.1))

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written to 'dante_intro.mid'")
