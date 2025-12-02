
import pretty_midi
import numpy as np

# Initialize a Pretty MIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Time per beat in seconds
time_per_beat = 60.0 / 160.0  # 0.375 seconds
time_per_bar = 4 * time_per_beat  # 1.5 seconds

# BAR 1: Little Ray on Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 to 1.5 seconds

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.75 + 0.125))

# Snare
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.375 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75 + 0.375, end=0.75 + 0.375 + 0.125))

# Hihat on every eighth
for i in range(0, 8):
    start = i * 0.125
    end = start + 0.01
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# BAR 2: Everyone enters. Sax takes the melody.

# Time: 1.5 to 3.0 seconds

# Fm = F, Ab, Bb, D, Eb
# Key: F minor

# Sax motif (simple, searching, with a suspension)
# Start on G (Bb is the 3rd of Fm, but G is a neighbor tone)
# Note values: quarter, eighth, eighth, eighth, quarter
# G (Bb7 chord), Ab, Bb, D, G

# Time per bar: 1.5
# Time for bar 2: 1.5 - 3.0
time_start = 1.5

# G (Bb7) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time_start, end=time_start + 0.375))  # G (G4)
# Ab (dominant) eighth note
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time_start + 0.375, end=time_start + 0.5))
# Bb (resolve) eighth note
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time_start + 0.5, end=time_start + 0.625))  # Bb
# D (tension) eighth note
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time_start + 0.625, end=time_start + 0.75))  # D
# Return to G on the last beat — but leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time_start + 0.75, end=time_start + 1.125))  # G (quarter)

# Bass: Walking line in Fm – F, G, Ab, Bb, Bb, C, Db, D
# Time start: 1.5 to 3.0
# Each note is 1/8th note (0.1875 sec)

bass_notes = [65, 67, 68, 70, 70, 72, 69, 71]
for i, pitch in enumerate(bass_notes):
    start = time_start + i * 0.1875
    end = start + 0.1875
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Time: 1.5 to 3.0

# Bar 2: 7th chord on beat 2 and 4
# Fm7 = F, Ab, Bb, Db
# Bbm7 = Bb, Db, F, Ab

# Beat 2: Fm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0))

# Beat 4: Bbm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=2.875))

# BAR 3: Continue the same pattern, with bass walking and piano comping
# Time: 3.0 to 4.5 seconds

# Bass: F, G, Ab, Bb, Bb, C, Db, D (same as before)
for i, pitch in enumerate(bass_notes):
    start = 3.0 + i * 0.1875
    end = start + 0.1875
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on beats 2 and 4 again
# Fm7 on beat 2 (3.875)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.875, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.875, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0))

# Bbm7 on beat 4 (4.625)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=4.625, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.625, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=4.625, end=4.875))

# BAR 4: Continue, and end with sax holding on G
# Time: 4.5 to 6.0 seconds

# Bass: F, G, Ab, Bb, Bb, C, Db, D (same as before)
for i, pitch in enumerate(bass_notes):
    start = 4.5 + i * 0.1875
    end = start + 0.1875
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on beats 2 and 4 again
# Fm7 on beat 2 (5.875)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.875, end=6.0))

# Bbm7 on beat 4 (6.625) - but we don't need it, we end at 6.0

# Sax: End on G, releasing the tension
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=6.0))

# Drums: Same pattern for bar 4
# Kick on 1 and 3 (5.0 and 5.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.0 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=5.75 + 0.125))

# Snare on 2 and 4 (5.375 and 5.75 + 0.375 = 6.125 — but we end at 6.0, so 5.375 only)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.375 + 0.125))

# Hihat on every eighth
for i in range(0, 8):
    start = 5.0 + i * 0.125
    end = start + 0.01
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Save the MIDI file
pm.write("waynes_intro.mid")
