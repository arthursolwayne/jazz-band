
import pretty_midi

# Create the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Assign drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray (drums) alone (0.0 - 1.5s)
# Simple groove: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_length = 1.5  # seconds

# Bar 1: 0.0 to 1.5s
drum_notes = [
    (kick, 0.0),     # Kick on 1
    (hihat, 0.1875), # Hihat on 1+
    (hihat, 0.375),  # Hihat on 2
    (snare, 0.5625), # Snare on 2+
    (hihat, 0.75),   # Hihat on 3
    (kick, 0.9375),  # Kick on 3
    (hihat, 1.125),  # Hihat on 3+
    (hihat, 1.3125), # Hihat on 4
    (snare, 1.5),    # Snare on 4
]

# Add to drums instrument
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Start time for Bar 2
start_time = 1.5

# Marcus on Bass: Walking line in Fm (F, Gb, Ab, Bb, C, Db, Eb, F)
# Chromatic approach to F
bass_notes = [
    (64, start_time),     # F (1st beat)
    (63, start_time + 0.375), # Gb (2nd beat)
    (62, start_time + 0.75),  # Ab (3rd beat)
    (60, start_time + 1.125), # Bb (4th beat)
]

# Diane on Piano: 7th chords comping on beat 2 and 4
# Fm7 chord: F, Ab, Bb, Db
# Rootless voicing: Ab, Bb, Db, F (inverted)
piano_notes = [
    (82, start_time + 0.375), # Ab (2nd beat)
    (80, start_time + 0.375), # Bb
    (70, start_time + 0.375), # Db
    (77, start_time + 0.375), # F
    (82, start_time + 1.125), # Ab (4th beat)
    (80, start_time + 1.125), # Bb
    (70, start_time + 1.125), # Db
    (77, start_time + 1.125), # F
]

# Little Ray on Drums: continues groove
drum_notes_bar_2 = [
    (kick, start_time),     # Kick on 1
    (hihat, start_time + 0.1875), # Hihat on 1+
    (hihat, start_time + 0.375),  # Hihat on 2
    (snare, start_time + 0.5625), # Snare on 2+
    (hihat, start_time + 0.75),   # Hihat on 3
    (kick, start_time + 0.9375),  # Kick on 3
    (hihat, start_time + 1.125),  # Hihat on 3+
    (hihat, start_time + 1.3125), # Hihat on 4
    (snare, start_time + 1.5),    # Snare on 4
]

for note, time in drum_notes_bar_2:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante on Sax: Motif in Fm — short, singable, with tension and release
# One motif: F, Ab, C, F (sings Fm7)
# Then leave it hanging, return to finish it with a resolution

sax_notes = [
    (64, start_time),     # F (1st beat)
    (62, start_time + 0.375), # Ab (2nd beat)
    (67, start_time + 0.75),  # C (3rd beat)
    (64, start_time + 1.125), # F (4th beat)
    (64, start_time + 1.5),   # F again to finish the phrase (5th beat)
]

for note, time in sax_notes:
    no = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(no)

# Add notes to bass and piano
for note, time in bass_notes:
    no = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    bass.notes.append(no)

for note, time in piano_notes:
    no = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(no)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
