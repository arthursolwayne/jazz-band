
import pretty_midi

# Initialize MIDI with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# 1 bar = 1.5 seconds, 4 bars = 6 seconds
BAR_DURATION = 1.5

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(0, 4):
    time = beat * 0.375  # each beat is 0.375s
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Time shift
start_time = 1.5

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (24, start_time + 0.0),  # F
    (23, start_time + 0.25), # Eb chromatic
    (25, start_time + 0.5),  # G
    (24, start_time + 0.75), # F
    (26, start_time + 1.0),  # A
    (25, start_time + 1.25), # G
    (24, start_time + 1.5),  # F
    (23, start_time + 1.75), # Eb
    (22, start_time + 2.0),  # D
    (23, start_time + 2.25), # D#
    (24, start_time + 2.5),  # F
    (25, start_time + 2.75), # G
    (26, start_time + 3.0),  # A
    (27, start_time + 3.25), # Bb
    (26, start_time + 3.5),  # A
    (25, start_time + 3.75), # G
    (24, start_time + 4.0),  # F
    (23, start_time + 4.25), # Eb
    (22, start_time + 4.5),  # D
    (23, start_time + 4.75), # D#
    (24, start_time + 5.0),  # F
    (25, start_time + 5.25), # G
    (26, start_time + 5.5),  # A
    (27, start_time + 5.75)  # Bb
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
# F7 on beat 2 and 4 of bar 2, Bb7 on beat 2 and 4 of bar 3, D7 on beat 2 and 4 of bar 4
# Each chord is played as a comp (arpeggiated quickly)
def add_piano_chord(chord, time):
    chord_notes = {
        'F7': [60, 64, 67, 69],
        'Bb7': [62, 65, 69, 71],
        'D7': [62, 65, 67, 71]
    }
    for note in chord_notes[chord]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

# Bar 2: F7 on beat 2 and 4
add_piano_chord('F7', start_time + 0.5)
add_piano_chord('F7', start_time + 1.5)

# Bar 3: Bb7 on beat 2 and 4
add_piano_chord('Bb7', start_time + 2.5)
add_piano_chord('Bb7', start_time + 3.5)

# Bar 4: D7 on beat 2 and 4
add_piano_chord('D7', start_time + 4.5)
add_piano_chord('D7', start_time + 5.5)

# Drums continue: same pattern as bar 1, starting at 1.5s
for beat in range(0, 4):
    time = beat * 0.375 + start_time
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.125))

# Saxophone: Your motif (start at 1.5s)
# Motif: F - G - Ab - F (scaleless, singing, open-ended)
sax_notes = [
    (60, start_time + 0.0),  # F
    (62, start_time + 0.25), # G
    (61, start_time + 0.5),  # Ab
    (60, start_time + 0.75)  # F
]
for pitch, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
