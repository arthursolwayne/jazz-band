
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Set the key to F minor
key = 'Fm'

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define the total duration (4 bars at 160 BPM in 4/4 time)
total_time = 4 * 60 / 160  # 6 seconds

# Get a new instrument for each player
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=128)    # Drums

pm.instruments = [tenor_sax, bass, piano, drums]

# Define note durations and velocities
NOTE_DURATION = 0.375  # 1 beat at 160 BPM is 0.375 seconds
VEL_TENOR = 100
VEL_BASS = 80
VEL_PIANO = 100
VEL_DRUMS = 100

# Bars are 1.5 seconds each (6 seconds total)
BAR_DURATION = 1.5

# Define the time points for each bar
bar_times = [0.0, BAR_DURATION, 2 * BAR_DURATION, 3 * BAR_DURATION]

# DRUMS: Bar 1 - Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# This is bar 0 to BAR_DURATION

# Kick on 0.0 and 1.5 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=0.0, end=0.0 + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=1.5, end=1.5 + NOTE_DURATION/2))

# Snare on 0.75 and 2.25 (beat 2 and 4)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=0.75, end=0.75 + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=2.25, end=2.25 + NOTE_DURATION/2))

# Hi-hats on every eighth note
for i in range(0, 4):
    start = i * NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=42, start=start, end=start + NOTE_DURATION/2))

# BASS: Bar 1 - Marcus plays a chromatic walking line, starting on F (Fm key)
# Notes in Fm: F, Gb, Ab, Bb, B, C, Db, D

# First bar: F -> Gb -> Ab -> Bb (chromatic walking)
bass_notes = [71, 69, 67, 65]  # F, Gb, Ab, Bb (MIDI pitches)
for i, note in enumerate(bass_notes):
    start = i * NOTE_DURATION
    end = start + NOTE_DURATION
    bass.notes.append(pretty_midi.Note(velocity=VEL_BASS, pitch=note, start=start, end=end))

# PIANO: Bar 1 - Diane plays 7th chords on 2 and 4
# Comp on 2 and 4, F7 on 2 and Bb7 on 4 (but in Fm, Bb is natural)
# F7 = F, A, C, E (but chord is F7 in F minor = F, Ab, C, Eb)

# Comp on 2 (beat 2 at 0.75) and 4 (beat 4 at 2.25)
# F7 = F, Ab, C, Eb
chords = {0.75: [71, 67, 69, 64], 2.25: [71, 67, 69, 64]}  # F7 chord (F, Ab, C, Eb)
for time, notes in chords.items():
    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=VEL_PIANO, pitch=note, start=time, end=time + NOTE_DURATION))

# TENOR SAX: Bar 1 - rests
# No notes in bar 1

# BASS: Bar 2 - Marcus continues walking line
# Ab -> Bb -> B -> C (chromatic)
bass_notes = [67, 65, 66, 67]  # Ab, Bb, B, C
for i, note in enumerate(bass_notes):
    start = BAR_DURATION + i * NOTE_DURATION
    end = start + NOTE_DURATION
    bass.notes.append(pretty_midi.Note(velocity=VEL_BASS, pitch=note, start=start, end=end))

# PIANO: Bar 2 - Diane continues comping on 2 and 4
# Bb7 on beat 2 (BAR_DURATION + 0.75), F7 on beat 4 (BAR_DURATION + 2.25)
chords = {BAR_DURATION + 0.75: [65, 62, 64, 67], BAR_DURATION + 2.25: [71, 67, 69, 64]}  # Bb7, F7
for time, notes in chords.items():
    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=VEL_PIANO, pitch=note, start=time, end=time + NOTE_DURATION))

# DRUMS: Bar 2 - same pattern
# Kick on 1 and 3 of the bar (BAR_DURATION + 0.0 and BAR_DURATION + 1.5)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=BAR_DURATION, end=BAR_DURATION + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=BAR_DURATION + 1.5, end=BAR_DURATION + 1.5 + NOTE_DURATION/2))

# Snare on 2 and 4 (BAR_DURATION + 0.75 and BAR_DURATION + 2.25)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=BAR_DURATION + 0.75, end=BAR_DURATION + 0.75 + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=BAR_DURATION + 2.25, end=BAR_DURATION + 2.25 + NOTE_DURATION/2))

# Hi-hats on every eighth
for i in range(0, 4):
    start = BAR_DURATION + i * NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=42, start=start, end=start + NOTE_DURATION/2))

# TENOR SAX: Bar 2 - Start the motif
# You take the melody: F, Ab, Bb, C (Fm scale) but with space and tension
# F (71), Ab (67), Bb (65), C (67)
# Play F on beat 1, Ab on 2, Bb on 3, and leave C hanging on beat 4.

start_times = [BAR_DURATION, BAR_DURATION + 0.75, BAR_DURATION + 1.5, BAR_DURATION + 2.25]
notes = [71, 67, 65, 67]

for i, (start, note) in enumerate(zip(start_times, notes)):
    if i == 3:
        # End on C, leave it hanging
        tenor_sax.notes.append(pretty_midi.Note(velocity=VEL_TENOR, pitch=note, start=start, end=start + NOTE_DURATION/2))
    else:
        tenor_sax.notes.append(pretty_midi.Note(velocity=VEL_TENOR, pitch=note, start=start, end=start + NOTE_DURATION))

# BASS: Bar 3 - Marcus continues walking line
# C -> Db -> D -> Eb (chromatic)
bass_notes = [67, 66, 68, 64]  # C, Db, D, Eb
for i, note in enumerate(bass_notes):
    start = 2 * BAR_DURATION + i * NOTE_DURATION
    end = start + NOTE_DURATION
    bass.notes.append(pretty_midi.Note(velocity=VEL_BASS, pitch=note, start=start, end=end))

# PIANO: Bar 3 - Diane continues comping on 2 and 4
# F7 on beat 2 (2*BAR_DURATION + 0.75), Bb7 on beat 4
chords = {2 * BAR_DURATION + 0.75: [71, 67, 69, 64], 2 * BAR_DURATION + 2.25: [65, 62, 64, 67]}  # F7, Bb7
for time, notes in chords.items():
    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=VEL_PIANO, pitch=note, start=time, end=time + NOTE_DURATION))

# DRUMS: Bar 3 - same pattern
# Kick on 1 and 3 of the bar (2*BAR_DURATION + 0.0 and 2*BAR_DURATION + 1.5)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=2 * BAR_DURATION, end=2 * BAR_DURATION + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=2 * BAR_DURATION + 1.5, end=2 * BAR_DURATION + 1.5 + NOTE_DURATION/2))

# Snare on 2 and 4 (2*BAR_DURATION + 0.75 and 2*BAR_DURATION + 2.25)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=2 * BAR_DURATION + 0.75, end=2 * BAR_DURATION + 0.75 + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=2 * BAR_DURATION + 2.25, end=2 * BAR_DURATION + 2.25 + NOTE_DURATION/2))

# Hi-hats on every eighth
for i in range(0, 4):
    start = 2 * BAR_DURATION + i * NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=42, start=start, end=start + NOTE_DURATION/2))

# TENOR SAX: Bar 3 - Continue the motif
# C (67) is already played, now we resolve it. Build tension with a rest, then resolve to F (71) on beat 4.

# Rest on beat 1 and 2, play C on beat 3, resolve to F on beat 4

# Rest on beat 1 and 2:
# No notes

# C on beat 3 (2*BAR_DURATION + 1.5)
tenor_sax.notes.append(pretty_midi.Note(velocity=VEL_TENOR, pitch=67, start=2*BAR_DURATION + 1.5, end=2*BAR_DURATION + 1.5 + NOTE_DURATION))

# F on beat 4 (2*BAR_DURATION + 2.25)
tenor_sax.notes.append(pretty_midi.Note(velocity=VEL_TENOR, pitch=71, start=2*BAR_DURATION + 2.25, end=2*BAR_DURATION + 2.25 + NOTE_DURATION/2))

# BASS: Bar 4 - Marcus continues walking line
# Eb -> F -> Gb -> Ab (chromatic)
bass_notes = [64, 71, 69, 67]  # Eb, F, Gb, Ab
for i, note in enumerate(bass_notes):
    start = 3 * BAR_DURATION + i * NOTE_DURATION
    end = start + NOTE_DURATION
    bass.notes.append(pretty_midi.Note(velocity=VEL_BASS, pitch=note, start=start, end=end))

# PIANO: Bar 4 - Diane continues comping on 2 and 4
# Bb7 on beat 2 (3*BAR_DURATION + 0.75), F7 on beat 4
chords = {3 * BAR_DURATION + 0.75: [65, 62, 64, 67], 3 * BAR_DURATION + 2.25: [71, 67, 69, 64]}  # Bb7, F7
for time, notes in chords.items():
    for note in notes:
        piano.notes.append(pretty_midi.Note(velocity=VEL_PIANO, pitch=note, start=time, end=time + NOTE_DURATION))

# DRUMS: Bar 4 - same pattern
# Kick on 1 and 3 of the bar (3*BAR_DURATION + 0.0 and 3*BAR_DURATION + 1.5)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=3 * BAR_DURATION, end=3 * BAR_DURATION + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=36, start=3 * BAR_DURATION + 1.5, end=3 * BAR_DURATION + 1.5 + NOTE_DURATION/2))

# Snare on 2 and 4 (3*BAR_DURATION + 0.75 and 3*BAR_DURATION + 2.25)
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=3 * BAR_DURATION + 0.75, end=3 * BAR_DURATION + 0.75 + NOTE_DURATION/2))
drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=38, start=3 * BAR_DURATION + 2.25, end=3 * BAR_DURATION + 2.25 + NOTE_DURATION/2))

# Hi-hats on every eighth
for i in range(0, 4):
    start = 3 * BAR_DURATION + i * NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=VEL_DRUMS, pitch=42, start=start, end=start + NOTE_DURATION/2))

# TENOR SAX: Bar 4 - Resolution
# F (71) on beat 1, Ab (67) on beat 2, Bb (65) on beat 3, C (67) on beat 4
# End the motif, leaving it open — a question still in the air

start_times = [3 * BAR_DURATION, 3 * BAR_DURATION + 0.75, 3 * BAR_DURATION + 1.5, 3 * BAR_DURATION + 2.25]
notes = [71, 67, 65, 67]

for start, note in zip(start_times, notes):
    tenor_sax.notes.append(pretty_midi.Note(velocity=VEL_TENOR, pitch=note, start=start, end=start + NOTE_DURATION))

# Save the MIDI file
pm.write("four_bar_intro_Fm.mid")
