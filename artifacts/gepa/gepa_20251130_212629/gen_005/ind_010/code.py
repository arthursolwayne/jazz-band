
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
time_per_beat = 60.0 / tempo  # seconds per beat
bar_duration = time_per_beat * 4  # 4 beats per bar
total_duration = bar_duration * 4  # 4 bars

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define instruments (MIDI program numbers)
drums_program = 128  # Drums
bass_program = 33    # Double Bass
piano_program = 0    # Acoustic Piano
saxophone_program = 62  # Tenor Saxophone

# Create instruments
drums = Instrument(program=drums_program)
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
sax = Instrument(program=saxophone_program)

# Add instruments to the PrettyMIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Function to create a note
def create_note(note_number, start, duration):
    return Note(velocity=100, pitch=note_number, start=start, end=start + duration)

# Duration per beat in seconds
beat_duration = time_per_beat

# Bar 1: Drums alone (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_beat = bar1_start

# Kick on beats 1 and 3
drums.notes.append(create_note(36, bar1_beat, 0.15))  # Kick on beat 1
drums.notes.append(create_note(36, bar1_beat + 2*beat_duration, 0.15))  # Kick on beat 3

# Snare on beats 2 and 4
drums.notes.append(create_note(38, bar1_beat + beat_duration, 0.15))  # Snare on beat 2
drums.notes.append(create_note(38, bar1_beat + 3*beat_duration, 0.15))  # Snare on beat 4

# Hi-hats on every eighth note
for i in range(8):
    hihat_time = bar1_beat + i * beat_duration / 2
    drums.notes.append(create_note(42, hihat_time, 0.1))

# Bar 2: All in — sax starts the melody
bar2_start = bar1_start + bar_duration
bar2_beat = bar2_start

# Melody: Tenor sax (D minor key)
# Start with a short motif that sings — D, F, Bb, C
sax_notes = [
    create_note(62, bar2_beat, 0.5),  # D4
    create_note(64, bar2_beat + 0.5, 0.5),  # F4
    create_note(60, bar2_beat + 1.0, 0.5),  # Bb4
    create_note(61, bar2_beat + 1.5, 0.5),  # C5
]

sax.notes.extend(sax_notes)

# Bass line: Marcus — chromatic approach, walking line
# Dm7 chord: D, F, A, C
# Bass line: D, C, B, Bb, A, Ab, G, G
bass_notes = [
    create_note(62, bar2_beat, 0.5),  # D
    create_note(60, bar2_beat + 0.5, 0.5),  # C
    create_note(59, bar2_beat + 1.0, 0.5),  # B
    create_note(58, bar2_beat + 1.5, 0.5),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: Diane — 7th chords, comp on 2 and 4
piano_notes = [
    create_note(62, bar2_beat + 1.0, 0.5),  # D7
    create_note(64, bar2_beat + 1.0, 0.5),
    create_note(67, bar2_beat + 1.0, 0.5),
    create_note(71, bar2_beat + 1.0, 0.5),
    create_note(62, bar2_beat + 2.0, 0.5),  # D7 on beat 4
    create_note(64, bar2_beat + 2.0, 0.5),
    create_note(67, bar2_beat + 2.0, 0.5),
    create_note(71, bar2_beat + 2.0, 0.5),
]

piano.notes.extend(piano_notes)

# Bar 3: Continue the melody, leave it hanging
bar3_start = bar2_start + bar_duration
bar3_beat = bar3_start

# Continue the sax melody, but break it on the third note
# D, F, Bb, leave it hanging on Bb
sax_notes = [
    create_note(62, bar3_beat, 0.5),  # D4
    create_note(64, bar3_beat + 0.5, 0.5),  # F4
    create_note(60, bar3_beat + 1.0, 0.5),  # Bb4
]

sax.notes.extend(sax_notes)

# Bass line: Marcus continues the walking line
bass_notes = [
    create_note(62, bar3_beat, 0.5),  # D
    create_note(60, bar3_beat + 0.5, 0.5),  # C
    create_note(59, bar3_beat + 1.0, 0.5),  # B
    create_note(58, bar3_beat + 1.5, 0.5),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: Diane continues comping
piano_notes = [
    create_note(62, bar3_beat + 1.0, 0.5),  # D7
    create_note(64, bar3_beat + 1.0, 0.5),
    create_note(67, bar3_beat + 1.0, 0.5),
    create_note(71, bar3_beat + 1.0, 0.5),
    create_note(62, bar3_beat + 2.0, 0.5),  # D7 on beat 4
    create_note(64, bar3_beat + 2.0, 0.5),
    create_note(67, bar3_beat + 2.0, 0.5),
    create_note(71, bar3_beat + 2.0, 0.5),
]

piano.notes.extend(piano_notes)

# Bar 4: Resolve with something unexpected
bar4_start = bar3_start + bar_duration
bar4_beat = bar4_start

# Sax resolves the motif — D, F, Bb, C — but ends on a B
sax_notes = [
    create_note(62, bar4_beat, 0.5),  # D4
    create_note(64, bar4_beat + 0.5, 0.5),  # F4
    create_note(60, bar4_beat + 1.0, 0.5),  # Bb4
    create_note(59, bar4_beat + 1.5, 0.5),  # B4 (unexpected)
]

sax.notes.extend(sax_notes)

# Bass line: This time, a chromatic descent into B
bass_notes = [
    create_note(62, bar4_beat, 0.5),  # D
    create_note(60, bar4_beat + 0.5, 0.5),  # C
    create_note(59, bar4_beat + 1.0, 0.5),  # B
    create_note(58, bar4_beat + 1.5, 0.5),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: Diane resolves with a D7 chord
piano_notes = [
    create_note(62, bar4_beat + 1.0, 0.5),  # D7
    create_note(64, bar4_beat + 1.0, 0.5),
    create_note(67, bar4_beat + 1.0, 0.5),
    create_note(71, bar4_beat + 1.0, 0.5),
    create_note(62, bar4_beat + 2.0, 0.5),  # D7 on beat 4
    create_note(64, bar4_beat + 2.0, 0.5),
    create_note(67, bar4_beat + 2.0, 0.5),
    create_note(71, bar4_beat + 2.0, 0.5),
]

piano.notes.extend(piano_notes)

# Drums: Bar 4 — same pattern
bar4_beat = bar4_start

# Kick on beats 1 and 3
drums.notes.append(create_note(36, bar4_beat, 0.15))  # Kick on beat 1
drums.notes.append(create_note(36, bar4_beat + 2*beat_duration, 0.15))  # Kick on beat 3

# Snare on beats 2 and 4
drums.notes.append(create_note(38, bar4_beat + beat_duration, 0.15))  # Snare on beat 2
drums.notes.append(create_note(38, bar4_beat + 3*beat_duration, 0.15))  # Snare on beat 4

# Hi-hats on every eighth note
for i in range(8):
    hihat_time = bar4_beat + i * beat_duration / 2
    drums.notes.append(create_note(42, hihat_time, 0.1))

# Write MIDI file
pm.write('dante_intro.mid')

print("MIDI file 'dante_intro.mid' has been created.")
