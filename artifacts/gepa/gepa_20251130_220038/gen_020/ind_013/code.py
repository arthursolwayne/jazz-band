
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time in seconds
bar_length = 1.5  # 160 BPM, 4/4 time

#---------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth
for i in range(0, 6):
    hihat_time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.125))

#---------------------
# Bars 2-4: Full quartet (1.5 - 6.0s)

# Initial time for bars 2-4
start_time = 1.5

#---------------------
# Bass Line: Marcus (Walking line, chromatic approaches, never the same note twice)
# Notes: F, G, Ab, A, Bb, B, C, Db, D, Eb, E, F# (chromatic line)
bass_notes = [77, 79, 78, 80, 77, 79, 81, 79, 81, 83, 81, 83]  # F, G, Ab, A, Bb, B, C, Db, D, Eb, E, F#

for i, note in enumerate(bass_notes):
    start = start_time + i * 0.375
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=end))

#---------------------
# Piano: Diane (7th chords, comp on 2 and 4)
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab

# Bar 2: F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=1.875, end=2.125))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=1.875, end=2.125))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=1.875, end=2.125))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=1.875, end=2.125))  # Eb

# Bar 3: Bb7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.625))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.625))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=3.375, end=3.625))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=3.375, end=3.625))  # Ab

# Bar 4: F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.125))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.125))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=4.875, end=5.125))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.125))  # Eb

#---------------------
# Saxophone: Dante (Your motif — short, melodic, haunting)
# Motif: F, G#, Bb, B, F
# Start at bar 2, beat 1, then leave it hanging

motif_notes = [77, 81, 81, 82, 77]  # F, G#, Bb, B, F
motif_durations = [0.375, 0.375, 0.375, 0.375, 0.375]  # Each note on an eighth note

for i, note in enumerate(motif_notes):
    start = 1.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + motif_durations[i]))

#---------------------
# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
