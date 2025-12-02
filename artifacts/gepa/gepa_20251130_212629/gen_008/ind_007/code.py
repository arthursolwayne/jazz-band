
import pretty_midi
from pretty_midi import Note, Instrument, NoteArray

# Set tempo and key
tempo = 160  # BPM
key = 'Fm'  # F minor
time_signature = (4, 4)

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo=tempo, time=0)]

# Define time per beat and bar
beats_per_bar = 4
ticks_per_beat = pm.resolution  # 480 ticks per beat by default
bar_duration = beats_per_bar * ticks_per_beat / pm.resolution * 60 / tempo

# Define the 4 bars
total_time = 4 * bar_duration

# Helper function to convert time to ticks
def time_to_ticks(t):
    return int(t * pm.resolution * tempo / 60)

# ------------------------------
# 1. Drums (Little Ray)
# ------------------------------

drums = Instrument(program=10, is_drum=True)
pm.instruments.append(drums)

# Kick on 1 and 3
kick_notes = [
    (0, time_to_ticks(0)),  # Bar 1, beat 1
    (0, time_to_ticks(1.5)),  # Bar 1, beat 3
]

# Snare on 2 and 4
snare_notes = [
    (8, time_to_ticks(0.75)),  # Bar 1, beat 2
    (8, time_to_ticks(2.25)),  # Bar 1, beat 4
]

# Hihat on every 8th note
hihat_notes = []
for t in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75]:
    hihat_notes.append((42, time_to_ticks(t)))

# Add all drum notes
for note, time in kick_notes + snare_notes + hihat_notes:
    drums.notes.append(Note(pitch=note, start=time, end=time + 0.15))

# ------------------------------
# 2. Bass (Marcus)
# ------------------------------

bass = Instrument(program=33)
pm.instruments.append(bass)

# Walking line in F minor: F - Gb - G - Ab - A - Bb - B - C
# We’ll use chromatic approach above and below the scale
# Start at bar 2 (time = 1.5 seconds)
pattern = [36, 37, 38, 39, 41, 42, 43, 44]  # F, Gb, G, Ab, A, Bb, B, C

# Repeat the walking line across the 3 bars
for i in range(1, 4):  # bars 2, 3, 4
    for j, note in enumerate(pattern):
        start_time = i * bar_duration + j * 0.375
        end_time = start_time + 0.25
        bass.notes.append(Note(pitch=note, start=start_time, end=end_time))

# ------------------------------
# 3. Piano (Diane)
# ------------------------------

piano = Instrument(program=0)
pm.instruments.append(piano)

# 7th chords: F7, Bb7, Eb7, Ab7 (ii-V-I in Fm)
# Played on 2 and 4 of each bar (bars 2-4)
# We'll spread them across beats 2 and 4 of bars 2, 3, and 4

chords = {
    1: [60, 62, 64, 67],  # F7 (F, A, C, E)
    2: [62, 64, 66, 69],  # Bb7 (Bb, D, F, Ab)
    3: [64, 66, 68, 71],  # Eb7 (Eb, G, Bb, Db)
    4: [66, 68, 70, 73],  # Ab7 (Ab, C, Eb, Gb)
}

# Play chords on beat 2 and 4 of bars 2–4
for bar in [2, 3, 4]:
    for beat in [2, 4]:
        start_time = (bar - 1) * bar_duration + (beat - 1) * 0.375
        for note in chords[bar]:
            piano.notes.append(Note(pitch=note, start=start_time, end=start_time + 0.25))

# ------------------------------
# 4. Tenor Sax (You)
# ------------------------------

sax = Instrument(program=64)
pm.instruments.append(sax)

# Simple, short motif: F - Eb - D - C
# Start on beat 1 of bar 2
motif = [65, 63, 62, 60]  # F, Eb, D, C
motif_durations = [0.25, 0.25, 0.25, 0.25]

# Play the motif on bar 2, beat 1
for i, note in enumerate(motif):
    start_time = 1.5 + i * 0.25
    sax.notes.append(Note(pitch=note, start=start_time, end=start_time + 0.25))

# Leave it hanging — repeat the first note on beat 3 of bar 2 (but not full note)
sax.notes.append(Note(pitch=65, start=1.5 + 0.5, end=1.5 + 0.5 + 0.125))

# Then come back with the full motif on beat 1 of bar 3
for i, note in enumerate(motif):
    start_time = 3.0 + i * 0.25
    sax.notes.append(Note(pitch=note, start=start_time, end=start_time + 0.25))

# Save the MIDI file
pm.write('jazz_intro_Fm.mid')
