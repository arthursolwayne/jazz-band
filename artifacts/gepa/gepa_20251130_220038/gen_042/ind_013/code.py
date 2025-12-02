
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
bar_length = 1.5  # in seconds
bar_1_start = 0.0
bar_1_end = bar_1_start + bar_length

# Drums in Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    (KICK, bar_1_start + 0.0),
    (SNARE, bar_1_start + 0.375),
    (HIHAT, bar_1_start + 0.0),
    (HIHAT, bar_1_start + 0.375),
    (HIHAT, bar_1_start + 0.75),
    (HIHAT, bar_1_start + 1.125),
    (KICK, bar_1_start + 0.75),
    (SNARE, bar_1_start + 1.125),
    (HIHAT, bar_1_start + 1.5),
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

bar_2_start = bar_1_end
bar_2_end = bar_2_start + bar_length
bar_3_start = bar_2_end
bar_3_end = bar_3_start + bar_length
bar_4_start = bar_3_end
bar_4_end = bar_4_start + bar_length

# Function to create a note
def create_note(pitch, start, end, velocity=100, instrument=None):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    if instrument:
        instrument.notes.append(note)

# Marcus on bass: Walking line, chromatic approaches
# Bar 2: D -> C# -> D -> E (walking line with chromatic approach)
bass_notes = [
    (62, bar_2_start + 0.0, bar_2_start + 0.25),  # D
    (61, bar_2_start + 0.25, bar_2_start + 0.5),  # C#
    (62, bar_2_start + 0.5, bar_2_start + 0.75),  # D
    (64, bar_2_start + 0.75, bar_2_start + 1.0),  # E
]

for pitch, start, end in bass_notes:
    create_note(pitch, start, end, instrument=bass)

# Bar 3: F -> E -> F -> G
bass_notes = [
    (65, bar_3_start + 0.0, bar_3_start + 0.25),  # F
    (64, bar_3_start + 0.25, bar_3_start + 0.5),  # E
    (65, bar_3_start + 0.5, bar_3_start + 0.75),  # F
    (67, bar_3_start + 0.75, bar_3_start + 1.0),  # G
]

for pitch, start, end in bass_notes:
    create_note(pitch, start, end, instrument=bass)

# Bar 4: A -> G -> A -> B
bass_notes = [
    (69, bar_4_start + 0.0, bar_4_start + 0.25),  # A
    (67, bar_4_start + 0.25, bar_4_start + 0.5),  # G
    (69, bar_4_start + 0.5, bar_4_start + 0.75),  # A
    (71, bar_4_start + 0.75, bar_4_start + 1.0),  # B
]

for pitch, start, end in bass_notes:
    create_note(pitch, start, end, instrument=bass)

# Diane on piano: 7th chords on 2 and 4, comp on 2 and 4
# D7 chord = D, F#, A, C
# F7 chord = F, A, C, E
# A7 chord = A, C#, E, G
# B7 chord = B, D#, F#, A

# Bar 2: D7 chord on 2 and 4
piano_notes = [
    (62, bar_2_start + 0.375, bar_2_start + 0.5),  # D
    (67, bar_2_start + 0.375, bar_2_start + 0.5),  # A
    (64, bar_2_start + 0.375, bar_2_start + 0.5),  # F#
    (60, bar_2_start + 0.375, bar_2_start + 0.5),  # C
    (62, bar_2_start + 0.75, bar_2_start + 1.0),  # D
    (67, bar_2_start + 0.75, bar_2_start + 1.0),  # A
    (64, bar_2_start + 0.75, bar_2_start + 1.0),  # F#
    (60, bar_2_start + 0.75, bar_2_start + 1.0),  # C
]

for pitch, start, end in piano_notes:
    create_note(pitch, start, end, instrument=piano)

# Bar 3: F7 chord on 2 and 4
piano_notes = [
    (65, bar_3_start + 0.375, bar_3_start + 0.5),  # F
    (69, bar_3_start + 0.375, bar_3_start + 0.5),  # C
    (67, bar_3_start + 0.375, bar_3_start + 0.5),  # A
    (62, bar_3_start + 0.375, bar_3_start + 0.5),  # E
    (65, bar_3_start + 0.75, bar_3_start + 1.0),  # F
    (69, bar_3_start + 0.75, bar_3_start + 1.0),  # C
    (67, bar_3_start + 0.75, bar_3_start + 1.0),  # A
    (62, bar_3_start + 0.75, bar_3_start + 1.0),  # E
]

for pitch, start, end in piano_notes:
    create_note(pitch, start, end, instrument=piano)

# Bar 4: A7 chord on 2 and 4
piano_notes = [
    (69, bar_4_start + 0.375, bar_4_start + 0.5),  # A
    (71, bar_4_start + 0.375, bar_4_start + 0.5),  # G
    (67, bar_4_start + 0.375, bar_4_start + 0.5),  # E
    (64, bar_4_start + 0.375, bar_4_start + 0.5),  # C#
    (69, bar_4_start + 0.75, bar_4_start + 1.0),  # A
    (71, bar_4_start + 0.75, bar_4_start + 1.0),  # G
    (67, bar_4_start + 0.75, bar_4_start + 1.0),  # E
    (64, bar_4_start + 0.75, bar_4_start + 1.0),  # C#
]

for pitch, start, end in piano_notes:
    create_note(pitch, start, end, instrument=piano)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.

# Bar 2: Sax motif
sax_notes = [
    (66, bar_2_start + 0.0, bar_2_start + 0.25),  # E (Dorian 3rd)
    (68, bar_2_start + 0.25, bar_2_start + 0.5),  # G (Dorian 5th)
    (67, bar_2_start + 0.5, bar_2_start + 0.75),  # F# (Dorian 7th)
    (66, bar_2_start + 0.75, bar_2_start + 1.0),  # E
]

for pitch, start, end in sax_notes:
    create_note(pitch, start, end, instrument=sax)

# Bar 3: Leave it hanging
# No notes here — just space

# Bar 4: Return to finish the motif
sax_notes = [
    (69, bar_4_start + 0.0, bar_4_start + 0.25),  # A (Dorian 9th)
    (66, bar_4_start + 0.25, bar_4_start + 0.5),  # E
    (68, bar_4_start + 0.5, bar_4_start + 0.75),  # G
    (69, bar_4_start + 0.75, bar_4_start + 1.0),  # A
]

for pitch, start, end in sax_notes:
    create_note(pitch, start, end, instrument=sax)

# Add Drums in Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th

def add_drums(bar_start):
    # Kick on 1 and 3
    create_note(KICK, bar_start + 0.0, bar_start + 0.1, instrument=drums)
    create_note(KICK, bar_start + 0.75, bar_start + 0.85, instrument=drums)

    # Snare on 2 and 4
    create_note(SNARE, bar_start + 0.375, bar_start + 0.475, instrument=drums)
    create_note(SNARE, bar_start + 1.125, bar_start + 1.225, instrument=drums)

    # Hihat on every 8th
    create_note(HIHAT, bar_start + 0.0, bar_start + 0.1, instrument=drums)
    create_note(HIHAT, bar_start + 0.375, bar_start + 0.475, instrument=drums)
    create_note(HIHAT, bar_start + 0.75, bar_start + 0.85, instrument=drums)
    create_note(HIHAT, bar_start + 1.125, bar_start + 1.225, instrument=drums)

# Add drums to bars 2-4
add_drums(bar_2_start)
add_drums(bar_3_start)
add_drums(bar_4_start)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
