
import pretty_midi

# Initialize a PrettyMIDI object with 4/4 time at 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignatureTrack()
pm.time_signature_tracks.append(time_signature)

# Set the time signature to 4/4
time_signature.time_signature = (4, 4)
time_signature.time = 0.0

# Define the key: D major
key = 'D major'

# Create instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for drums as MIDI drums are tricky
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# BPM = 160, so each beat is 0.375 seconds
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar

# Bar 1: Drums only
def add_drums(track, start_time):
    # Kick on 1 and 3
    track.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=start_time, end=start_time + 0.1))
    track.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=start_time + 2 * beat, end=start_time + 2 * beat + 0.1))

    # Snare on 2 and 4
    track.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start_time + beat, end=start_time + beat + 0.1))
    track.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start_time + 3 * beat, end=start_time + 3 * beat + 0.1))

    # Hi-hat on every eighth
    for i in range(8):
        track.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.05))

add_drums(drums, 0.0)

# Bar 2: All instruments enter

# Bass - walking line in D major in 4/4
# D - Eb - F# - G - A - B - C# - D
# Chromatic approach to A and B
bass_notes = [
    (37, 0.0, 0.375),     # D
    (38, 0.375, 0.75),    # Eb
    (40, 0.75, 1.125),    # F#
    (42, 1.125, 1.5),     # G
    (45, 1.5, 1.875),     # A
    (47, 1.875, 2.25),    # B
    (49, 2.25, 2.625),    # C#
    (37, 2.625, 3.0),     # D
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end))

# Piano - 7th chords on 2 and 4
# D7 (D, F#, A, C) on beat 2
# G7 (G, B, D, F) on beat 4

def add_piano_chord(start_time, root, seventh_interval):
    root_pitch = pretty_midi.note_number_to_pitch(root)
    seventh = root + seventh_interval
    chord = [root, root + 4, root + 7, seventh]
    for pitch in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + beat))

# D7 on beat 2
add_piano_chord(beat, 50, 10)  # D7: D (50), F# (53), A (55), C (60)
# G7 on beat 4
add_piano_chord(3 * beat, 62, 10)  # G7: G (62), B (65), D (67), F (69)

# Saxophone - Melody (4 notes, start on beat 1, short and concise)
# D - F# - A - D (with a slight rhythmic delay on the final note)

sax_notes = [
    (50, 0.0, 0.375),     # D
    (53, 0.375, 0.75),    # F#
    (55, 0.75, 1.125),    # A
    (50, 1.125, 1.5),     # D
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 3 and 4: Repeat the same pattern with slight rhythmic push or space
# We'll just repeat the same pattern for simplicity, slightly pushing the melody for tension

# Repeating the same drum pattern
add_drums(drums, bar)

# Repeating bass line
for pitch, start, end in bass_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + bar, end=end + bar))

# Repeating piano chords
# D7 on beat 2
add_piano_chord(beat + bar, 50, 10)  # D7: D (50), F# (53), A (55), C (60)
# G7 on beat 4
add_piano_chord(3 * beat + bar, 62, 10)  # G7: G (62), B (65), D (67), F (69)

# Repeating saxophone melody, with slight rhythmic delay on final note
sax_notes = [
    (50, 0.0 + bar, 0.375 + bar),     # D
    (53, 0.375 + bar, 0.75 + bar),    # F#
    (55, 0.75 + bar, 1.125 + bar),    # A
    (50, 1.125 + bar, 1.5 + bar),     # D
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Write the MIDI file
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
