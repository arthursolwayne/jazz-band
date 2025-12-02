
import pretty_midi

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the key: D major (key number = 2)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]

# Function to convert note name to MIDI pitch
def note_name_to_midi(note_name):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5,
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11
    }
    note, accidental = note_name[0], note_name[1:] if len(note_name) > 1 else ''
    pitch = note_map[note] + (1 if accidental == '#' else 0)
    return pitch + 60  # MIDI note number for middle C is 60

# Function to add a note to a track
def add_note(track, pitch, start_time, end_time, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=end_time)
    track.notes.append(note)

# Create instrument tracks
drums_track = pretty_midi.Instrument(program=10)  # Drums
bass_track = pretty_midi.Instrument(program=33)   # Bass
piano_track = pretty_midi.Instrument(program=0)  # Piano
sax_track = pretty_midi.Instrument(program=64)   # Tenor Sax

# Add tracks to MIDI
pm.instruments.append(drums_track)
pm.instruments.append(bass_track)
pm.instruments.append(piano_track)
pm.instruments.append(sax_track)

# Bar 1: Drums - sparse, open
# Kick on 1, snare on 3, hihat on every eighth
bar_length = 1.5  # 160 BPM, 4/4 time, 6 seconds for 4 bars

notes_per_bar = 8  # 160 BPM, 4/4 → 4 beats per bar, 4 eighth notes per beat
beat_duration = bar_length / 4  # 0.375s per beat
eighth_duration = beat_duration / 2  # 0.1875s per eighth note

# Kick on beat 1
add_note(drums_track, note_name_to_midi('C'), 0.0, 0.1875, velocity=100)

# Snare on beat 3
add_note(drums_track, note_name_to_midi('C'), 0.75, 0.9375, velocity=100)

# Hi-hat on every eighth note
for i in range(notes_per_bar):
    start = i * eighth_duration
    end = start + eighth_duration
    add_note(drums_track, note_name_to_midi('C'), start, end, velocity=80)

# Bar 2: Bass - walking line, chromatic, no repeating notes
# D major: D E F# G A B C# D
bass_notes = [note_name_to_midi(n) for n in ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']]

for i, pitch in enumerate(bass_notes):
    start = i * eighth_duration + bar_length
    end = start + eighth_duration
    add_note(bass_track, pitch, start, end, velocity=80)

# Bar 3: Piano - 7th chords on beat 2 and 4
# D7: D F# A C
# G7: G B D F
# A7: A C# E G
# B7: B D# F# A

chords = [
    (note_name_to_midi('D'), note_name_to_midi('F#'), note_name_to_midi('A'), note_name_to_midi('C')),  # D7
    (note_name_to_midi('G'), note_name_to_midi('B'), note_name_to_midi('D'), note_name_to_midi('F')),   # G7
    (note_name_to_midi('A'), note_name_to_midi('C#'), note_name_to_midi('E'), note_name_to_midi('G')),  # A7
    (note_name_to_midi('B'), note_name_to_midi('D#'), note_name_to_midi('F#'), note_name_to_midi('A')),  # B7
]

for i, chord in enumerate(chords):
    # Play on beat 2 and 4 (i=1 and 3)
    if i in [1, 3]:
        start = (i + 1) * beat_duration + bar_length * 2
        for pitch in chord:
            add_note(piano_track, pitch, start, start + eighth_duration, velocity=100)

# Bar 4: Saxophone - motif, sparse, emotional
# Melody: start strong, leave it hanging, return with tension

# Note: D (62), E (64), G (67), D (62)
sax_notes = [
    (note_name_to_midi('D'), 0.0, 0.375),     # D, beat 1
    (note_name_to_midi('G'), 0.75, 1.125),    # G, beat 3
    (note_name_to_midi('E'), 1.5, 1.875),     # E, beat 1 of next bar
    (note_name_to_midi('D'), 2.25, 2.625),    # D, beat 3 of next bar
    (note_name_to_midi('C#'), 3.0, 3.375),    # C#, beat 1 of third bar
    (note_name_to_midi('A'), 3.75, 4.125),    # A, beat 3
    (note_name_to_midi('B'), 4.5, 4.875),     # B, beat 1 of fourth bar
    (note_name_to_midi('D'), 5.25, 5.625)     # D, beat 3, resolves
]

for pitch, start, end in sax_notes:
    add_note(sax_track, pitch, start, end, velocity=110)

# Save the MIDI file
pm.write('dante_jazz_intro.mid')

print("MIDI file 'dante_jazz_intro.mid' created successfully.")
