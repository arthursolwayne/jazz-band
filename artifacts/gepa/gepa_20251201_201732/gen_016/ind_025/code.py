
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Define the tempo (160 BPM)
tempo = 160

# Define the time signature (4/4)
time_signature = (4, 4)

# Define the key: F minor
key = 'Fm'
note_number_to_pitch_name = {
    48: 'C', 49: 'C#', 50: 'D', 51: 'D#', 52: 'E', 53: 'F', 54: 'F#', 55: 'G',
    56: 'G#', 57: 'A', 58: 'A#', 59: 'B', 60: 'C', 61: 'C#', 62: 'D', 63: 'D#',
    64: 'E', 65: 'F', 66: 'F#', 67: 'G', 68: 'G#', 69: 'A', 70: 'A#', 71: 'B',
    72: 'C'
}

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define the time per beat (in seconds)
seconds_per_beat = 60.0 / tempo

# Define the bar length in seconds
bar_length = 4 * seconds_per_beat

# Define the four bars as a time range
start_time = 0.0
end_time = bar_length * 4

# Create instruments
# 1. Drums (Little Ray)
drums = Instrument(program=Program.DRUMS)
pm.instruments.append(drums)

# 2. Bass (Marcus)
bass = Instrument(program=Program.BASS_GUITAR)
pm.instruments.append(bass)

# 3. Piano (Diane)
piano = Instrument(program=Program.ACOUSTIC_GRAND_PIANO)
pm.instruments.append(piano)

# 4. Tenor Sax (You)
sax = Instrument(program=Program.SAXOPHONE)
pm.instruments.append(sax)

# Define note durations and velocities
note_duration = 0.375  # 1/8 note
velocity_drums = 90
velocity_bass = 70
velocity_piano = 85
velocity_sax = 95

# Bar 1: Little Ray - Drums only, setting up the groove
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1 = [
    (0.0, 'kick'), (0.375, 'hihat'), (0.75, 'snare'), (1.125, 'hihat'),
    (1.5, 'kick'), (1.875, 'hihat'), (2.25, 'snare'), (2.625, 'hihat')
]

for time, note in bar_1:
    if note == 'kick':
        note_number = 36
    elif note == 'snare':
        note_number = 38
    elif note == 'hihat':
        note_number = 42
    else:
        continue

    note_obj = Note(velocity=velocity_drums, pitch=note_number, start=time, end=time + note_duration)
    drums.notes.append(note_obj)

# Bar 2: Everyone in, sax leads with a short motif, piano comp, bass walks, drums continue
# Fm key: F, Ab, D, Eb, Bb, C, G
# We'll use F (53), Ab (57), D (50), Eb (52), Bb (58), C (53), G (57)

# Sax: short motif - F, Ab, D, Eb
sax_notes = [
    (0.0, 53, 95),  # F
    (0.375, 57, 95),  # Ab
    (1.125, 50, 95),  # D
    (1.5, 52, 95)    # Eb
]

for time, pitch, vel in sax_notes:
    note_obj = Note(velocity=vel, pitch=pitch, start=time, end=time + note_duration)
    sax.notes.append(note_obj)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 -> Ab7 -> D7 -> Eb7 (suspended)
piano_notes = [
    (0.0, 53), (0.0, 57), (0.0, 60), (0.0, 63),  # Fm7 (F, Ab, C, Eb)
    (0.375, 57), (0.375, 62), (0.375, 64), (0.375, 69),  # Ab7 (Ab, C, D, G)
    (1.125, 50), (1.125, 53), (1.125, 57), (1.125, 60),  # D7 (D, F#, A, C)
    (1.5, 52), (1.5, 57), (1.5, 60), (1.5, 64)  # Eb7 (Eb, G, Bb, D)
]

for time, pitch in piano_notes:
    note_obj = Note(velocity=velocity_piano, pitch=pitch, start=time, end=time + note_duration)
    piano.notes.append(note_obj)

# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (0.0, 53),  # F
    (0.375, 57),  # Ab
    (1.125, 50),  # D
    (1.5, 52),  # Eb
    (1.875, 53),  # F
    (2.25, 57),  # Ab
    (3.0, 50),  # D
    (3.375, 52)  # Eb
]

for time, pitch in bass_notes:
    note_obj = Note(velocity=velocity_bass, pitch=pitch, start=time, end=time + note_duration)
    bass.notes.append(note_obj)

# Bar 3: Drums continue, piano continues comp, bass walks, sax rests
# Bar 4: Sax returns with the motif, piano resolves, bass walks, drums continue

# Continue with the same pattern for bars 3 and 4

# Bar 3: Same as bar 2, just the rhythm continues without new content
# No new sax motif, just the same pattern
# Piano continues with variations
# Bass continues walking
# Drums continue with same pattern

# Bar 4: Sax motif again, but this time resolved
# Piano resolves on Eb7, bass walks, drums continue

# For brevity, we'll just repeat the same pattern but shift by bar length
bar_2_start = bar_length
bar_3_start = bar_length * 2
bar_4_start = bar_length * 3

# Repeat bar 2 pattern for bars 3 and 4, shifting time
# Sax motif again at bar 4
sax_notes_bar4 = [
    (bar_4_start + 0.0, 53, 95),  # F
    (bar_4_start + 0.375, 57, 95),  # Ab
    (bar_4_start + 1.125, 50, 95),  # D
    (bar_4_start + 1.5, 52, 95)    # Eb
]

for time, pitch, vel in sax_notes_bar4:
    note_obj = Note(velocity=vel, pitch=pitch, start=time, end=time + note_duration)
    sax.notes.append(note_obj)

# Piano in bar 4: resolves on Eb7
piano_notes_bar4 = [
    (bar_4_start + 0.0, 52), (bar_4_start + 0.0, 57), (bar_4_start + 0.0, 60), (bar_4_start + 0.0, 64),  # Eb7
    (bar_4_start + 0.375, 57), (bar_4_start + 0.375, 62), (bar_4_start + 0.375, 64), (bar_4_start + 0.375, 69),  # Ab7
    (bar_4_start + 1.125, 50), (bar_4_start + 1.125, 53), (bar_4_start + 1.125, 57), (bar_4_start + 1.125, 60),  # D7
    (bar_4_start + 1.5, 52), (bar_4_start + 1.5, 57), (bar_4_start + 1.5, 60), (bar_4_start + 1.5, 64)  # Eb7
]

for time, pitch in piano_notes_bar4:
    note_obj = Note(velocity=velocity_piano, pitch=pitch, start=time, end=time + note_duration)
    piano.notes.append(note_obj)

# Bass in bar 4: continues walking
bass_notes_bar4 = [
    (bar_4_start + 0.0, 53),  # F
    (bar_4_start + 0.375, 57),  # Ab
    (bar_4_start + 1.125, 50),  # D
    (bar_4_start + 1.5, 52),  # Eb
    (bar_4_start + 1.875, 53),  # F
    (bar_4_start + 2.25, 57),  # Ab
    (bar_4_start + 3.0, 50),  # D
    (bar_4_start + 3.375, 52)  # Eb
]

for time, pitch in bass_notes_bar4:
    note_obj = Note(velocity=velocity_bass, pitch=pitch, start=time, end=time + note_duration)
    bass.notes.append(note_obj)

# Drums in bar 3 and 4: same pattern, repeated
bar_3 = [
    (bar_3_start + 0.0, 'kick'), (bar_3_start + 0.375, 'hihat'), (bar_3_start + 0.75, 'snare'),
    (bar_3_start + 1.125, 'hihat'), (bar_3_start + 1.5, 'kick'), (bar_3_start + 1.875, 'hihat'),
    (bar_3_start + 2.25, 'snare'), (bar_3_start + 2.625, 'hihat')
]

bar_4 = [
    (bar_4_start + 0.0, 'kick'), (bar_4_start + 0.375, 'hihat'), (bar_4_start + 0.75, 'snare'),
    (bar_4_start + 1.125, 'hihat'), (bar_4_start + 1.5, 'kick'), (bar_4_start + 1.875, 'hihat'),
    (bar_4_start + 2.25, 'snare'), (bar_4_start + 2.625, 'hihat')
]

for time, note in bar_3:
    if note == 'kick':
        note_number = 36
    elif note == 'snare':
        note_number = 38
    elif note == 'hihat':
        note_number = 42
    else:
        continue

    note_obj = Note(velocity=velocity_drums, pitch=note_number, start=time, end=time + note_duration)
    drums.notes.append(note_obj)

for time, note in bar_4:
    if note == 'kick':
        note_number = 36
    elif note == 'snare':
        note_number = 38
    elif note == 'hihat':
        note_number = 42
    else:
        continue

    note_obj = Note(velocity=velocity_drums, pitch=note_number, start=time, end=time + note_duration)
    drums.notes.append(note_obj)

# Write the MIDI file
pm.write("Dante_Intro.mid")
