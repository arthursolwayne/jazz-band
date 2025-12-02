
import pretty_midi

# Set up the tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
key = 'Dm'

# Create the PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define times for each bar (160 BPM => 60/160 = 0.375 sec per beat, 1.5 seconds per bar)
bar_length = 1.5  # seconds per bar

# Define instrument programs
sax_program = 64  # Tenor Sax
piano_program = 0  # Acoustic Piano
bass_program = 33  # Double Bass
drums_program = 0  # Acoustic Drums

# Add instruments
sax = pretty_midi.Instrument(program=sax_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments.append(sax)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(drums)

#--------------------------#
# Bar 1: Drums only - build tension
#--------------------------#

# Kick on 1 and 3
drum_notes = [
    (36, 1.0, 0.0),  # Kick on beat 1
    (36, 1.0, 2.0),  # Kick on beat 3
]

# Snare on 2 and 4
drum_notes += [
    (38, 1.0, 0.5),  # Snare on beat 2
    (38, 1.0, 2.5),  # Snare on beat 4
]

# Hi-hat on every eighth note
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=i * 0.375, end=i * 0.375 + 0.15))

# Add drum notes
for pitch, velocity, start in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.1))

#--------------------------#
# Bar 2: Piano enters with a dissonant 7th chord, bass enters with a chromatic walk
#--------------------------#

# Piano: Dm7 (D F A C) with some tension
piano_notes = [
    (62, 100, 0.0),  # D
    (64, 100, 0.0),  # F
    (67, 100, 0.0),  # A
    (69, 100, 0.0),  # C
    # Add a #11 (F#) for dissonance
    (66, 100, 0.0),  # F#
]

# Add piano notes
for pitch, velocity, start in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.5))

# Bass: Chromatic walk starting from D
bass_notes = [
    (62, 100, 1.5),  # D
    (63, 100, 1.75),  # Eb
    (64, 100, 2.0),  # F
    (65, 100, 2.25),  # F#
]

# Add bass notes
for pitch, velocity, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

#--------------------------#
# Bar 3: Saxophone enters with the motif (D, F, A, rest, then D again)
#--------------------------#

# Motif: D (62), F (64), A (67), rest, D (62)
sax_notes = [
    (62, 100, 3.0),  # D
    (64, 100, 3.5),  # F
    (67, 100, 4.0),  # A
    (62, 100, 5.0),  # D (reprise)
]

# Add sax notes
for pitch, velocity, start in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.5))

#--------------------------#
# Bar 4: Sax repeats, slightly altered (D, F, A, G, rest)
#--------------------------#

# Motif variation: D (62), F (64), A (67), G (65), rest
sax_notes = [
    (62, 100, 5.5),  # D
    (64, 100, 6.0),  # F
    (67, 100, 6.5),  # A
    (65, 100, 7.0),  # G
]

# Add sax notes
for pitch, velocity, start in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.5))

#--------------------------#
# Save the melody to a MIDI file
#--------------------------#

pm.write('dante_intro.mid')

print("MIDI file saved as 'dante_intro.mid'")
