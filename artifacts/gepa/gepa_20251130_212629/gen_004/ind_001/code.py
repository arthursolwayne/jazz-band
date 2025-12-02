
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use F minor scale: F, Gb, Ab, Bb, B, Db, Eb
# MIDI Note numbers:
# F = 65
# Gb = 66
# Ab = 67
# Bb = 68
# B = 69
# Db = 70
# Eb = 71

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=65)

pm.instruments = [drums, bass, piano, sax]

# Timing constants
BPM = 160
note_duration = 0.375  # 60 / BPM
bar_duration = 1.5  # 4/4 at 160 BPM
time_step = note_duration

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time = 0 to 1.5 seconds

# Kick on beats 1 and 3 (0.0, 1.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + note_duration / 2))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.5 + note_duration / 2))

# Snare on beats 2 and 4 (0.75, 1.5 + 0.75 = 2.25)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.75 + note_duration / 2))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.25 + note_duration / 2))

# Hi-hat on every eighth note (0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
for t in np.arange(0, 2.625, note_duration):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + note_duration / 2))

# Bar 2: All instruments come in

# Bass line - chromatic, walking line, no repeated notes
# Start at F (65), walk down chromatically: F, Eb, Db, B, Bb, Ab, Gb, F
# Keep it within the bar (0.0 - 1.5 seconds)
bass_notes = [65, 71, 70, 69, 68, 67, 66, 65]
bass_durations = [note_duration] * len(bass_notes)
times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=times[i], end=times[i] + bass_durations[i]))

# Piano chords - 7th chords, comp on 2 and 4, driving and emotional
# Bar 2: F7 (F, Ab, Bb, Db)
# Bar 3: Bb7 (Bb, Db, Eb, F)
# Bar 4: Eb7 (Eb, Gb, Ab, Bb)

# Time of each chord: 0.0 to 0.75, 0.75 to 1.5, 1.5 to 2.25
chords = [
    # Bar 2: F7 - F, Ab, Bb, Db
    (65, 67, 68, 70),
    # Bar 3: Bb7 - Bb, Db, Eb, F
    (68, 70, 71, 65),
    # Bar 4: Eb7 - Eb, Gb, Ab, Bb
    (71, 66, 67, 68),
]

for i, chord in enumerate(chords):
    start = 0.75 * i
    end = start + 0.75
    for pitch in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Saxophone motif - simple, melodic, leaves space
# F, Ab, Bb, F (ending on F)
# Start at bar 2, lasting 1.5 seconds

sax_notes = [65, 67, 68, 65]
sax_durations = [note_duration] * len(sax_notes)
sax_times = [0.75, 1.125, 1.5, 1.875]

for i, note in enumerate(sax_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=sax_times[i], end=sax_times[i] + sax_durations[i]))

# Write to a MIDI file
pm.write("dante_intro.mid")
