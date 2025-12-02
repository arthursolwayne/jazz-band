
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: F Major
# F Major scale: F, G, A, Bb, B, C, D
# We'll use F Major key (no sharps/flats in scale, but chromatic tension in bass)

# Create instruments
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")
bass_program = pretty_midi.instrument_name_to_program("Double Bass")
piano_program = pretty_midi.instrument_name_to_program("Acoustic Piano")
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")  # Using piano for drums (will map later)

# Create instruments
sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [sax, bass, piano, drums]

# Time per bar: 1.5 seconds
# Beats per bar: 4
# Tempo: 160 BPM => 1 beat = 0.375 seconds

# Function to convert beats to time
def beat_to_time(beats):
    return beats * 0.375

# --- DRUMS: Little Ray -------
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
# Bar 1: Kick on 1, snare on 2, hi-hat on 1-2-3-4
# Bar 1: 16th note hi-hat pattern
# Kick 1, 3
# Snare 2, 4
# Hi-hat every 1/8 note

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=beat_to_time(0), end=beat_to_time(0) + 0.1875))  # Kick
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=beat_to_time(1), end=beat_to_time(1) + 0.1875))  # Snare

# Hi-hat every eighth note
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=beat_to_time(i * 0.5), end=beat_to_time(i * 0.5) + 0.125))

# Bar 2-4: Full ensemble enters, but drums continue the same pattern
# Just need to extend the hi-hat and kick/snare as needed
for bar in range(2, 5):
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=beat_to_time(bar * 4 + i * 0.5), end=beat_to_time(bar * 4 + i * 0.5) + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=beat_to_time(bar * 4), end=beat_to_time(bar * 4) + 0.1875))  # Kick
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=beat_to_time(bar * 4 + 2), end=beat_to_time(bar * 4 + 2) + 0.1875))  # Snare

# --- BASS: Marcus ------
# Walking bass line with chromatic tension
# F Major key: F, G, A, Bb, B, C, D
# Chromatic approaches: e.g., E -> F, Bb -> A, etc.

# Bar 1: F -> G -> A -> Bb (walk up)
# Bar 2: B -> C -> D -> Eb (chromatic approach to Eb)
# Bar 3: Eb -> F -> G -> A (chromatic approach to F)
# Bar 4: A -> Bb -> B -> C (chromatic approach to B)

# Convert pitches to MIDI numbers (F = 65)
def note_to_midi(note):
    return pretty_midi.note_name_to_number(note)

notes = [
    ('F', 0.0), ('G', 0.25), ('A', 0.5), ('Bb', 0.75),
    ('B', 1.0), ('C', 1.25), ('D', 1.5), ('Eb', 1.75),
    ('Eb', 2.0), ('F', 2.25), ('G', 2.5), ('A', 2.75),
    ('A', 3.0), ('Bb', 3.25), ('B', 3.5), ('C', 3.75)
]

for note, start in notes:
    pitch = note_to_midi(note)
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# --- PIANO: Diane ------
# 7th chords on 2 and 4, punchy and emotionally charged
# F7 = F, A, C, Eb
# G7 = G, B, D, F
# A7 = A, C, E, G
# Bb7 = Bb, D, F, Ab

# Bar 1: 2 and 4
# Bar 2: 2 and 4
# Bar 3: 2 and 4
# Bar 4: 2 and 4

# 7th chords at beat 2 and 4 (0.5 and 1.0 in bar)
# Each chord stays for 0.25 seconds

def add_seventh_chord(instrument, root, start_time):
    root_midi = note_to_midi(root)
    third_midi = root_midi + 4
    fifth_midi = root_midi + 7
    seventh_midi = root_midi + 10  # minor 7th
    duration = 0.25

    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=root_midi, start=start_time, end=start_time + duration))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=third_midi, start=start_time, end=start_time + duration))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=fifth_midi, start=start_time, end=start_time + duration))
    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=seventh_midi, start=start_time, end=start_time + duration))

# Bar 1
add_seventh_chord(piano, 'G', beat_to_time(1.0))  # 2nd beat
add_seventh_chord(piano, 'Bb', beat_to_time(2.0))  # 4th beat

# Bar 2
add_seventh_chord(piano, 'A', beat_to_time(5.0))
add_seventh_chord(piano, 'C', beat_to_time(6.0))

# Bar 3
add_seventh_chord(piano, 'B', beat_to_time(8.0))
add_seventh_chord(piano, 'D', beat_to_time(9.0))

# Bar 4
add_seventh_chord(piano, 'Eb', beat_to_time(11.0))
add_seventh_chord(piano, 'F', beat_to_time(12.0))

# --- SAX: Dante ------
# Unique motif: F -> Ab -> Bb -> C -> Ab -> Bb -> C -> D
# Rhythmic: 16th notes with syncopation
# Avoid rests, make it sing

# Convert notes to MIDI
note_values = ['F', 'Ab', 'Bb', 'C', 'Ab', 'Bb', 'C', 'D']
note_durations = [0.125] * 8  # 16th notes

# Start time for sax: bar 1, beat 0
start_time = 0.0

for note in note_values:
    pitch = note_to_midi(note)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start_time, end=start_time + note_durations[0]))
    start_time += note_durations[0]

# Save the MIDI file
pm.write("wayne_intro.mid")
print("MIDI file written as 'wayne_intro.mid'")
