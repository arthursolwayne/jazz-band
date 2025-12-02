
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # standard MIDI resolution

# Tempo: 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0)]

# Setup instruments
drums_program = pretty_midi.programs.Program(0)  # percussion
bass_program = pretty_midi.programs.Program(33)  # electric bass
piano_program = pretty_midi.programs.Program(0)  # grand piano
sax_program = pretty_midi.programs.Program(64)   # tenor sax

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Function to convert beats to seconds
def beat_to_sec(beats):
    return beats * 60.0 / 160.0

# ----------------------
# 1. Little Ray: Drums
# ----------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# We only need this for the first bar

# Kick on 1 and 3
kick_notes = [36, 36]  # C1
kick_times = [beat_to_sec(0), beat_to_sec(2)]
kick_velocity = [64, 64]
for note, time, vel in zip(kick_notes, kick_times, kick_velocity):
    drums.notes.append(pretty_midi.Note(vel, note, time, time + 0.1))

# Snare on 2 and 4
snare_notes = [38, 38]  # D1
snare_times = [beat_to_sec(1), beat_to_sec(3)]
snare_velocity = [80, 80]
for note, time, vel in zip(snare_notes, snare_times, snare_velocity):
    drums.notes.append(pretty_midi.Note(vel, note, time, time + 0.1))

# Hi-hat on every 8th
hihat_notes = [42] * 4  # G2
hihat_times = [beat_to_sec(0), beat_to_sec(0.5), beat_to_sec(1), beat_to_sec(1.5),
               beat_to_sec(2), beat_to_sec(2.5), beat_to_sec(3), beat_to_sec(3.5)]
hihat_velocity = [40] * 8
for note, time, vel in zip(hihat_notes, hihat_times, hihat_velocity):
    drums.notes.append(pretty_midi.Note(vel, note, time, time + 0.05))

# ----------------------
# 2. Marcus: Bass (Walking line with chromatic approaches)
# ----------------------
# Bar 1 to Bar 4 (4 bars = 6 seconds)
# Walking bass line in D major
# D - E - F# - G - A - B - C# - D (chromatic approach to A)
# Starting at D (note 62)
bass_notes = [
    62, 64, 65, 67, 69, 71, 73, 74,  # D - E - F# - G - A - B - C# - D
    62, 64, 65, 67, 69, 71, 73, 74
]
bass_times = [beat_to_sec(i) for i in range(0, 8)] + [beat_to_sec(i) for i in range(8, 16)]
bass_velocity = [60] * len(bass_notes)

for note, time, vel in zip(bass_notes, bass_times, bass_velocity):
    bass.notes.append(pretty_midi.Note(vel, note, time, time + 0.25))

# ----------------------
# 3. Diane: Piano - 7th chords, comp on 2 and 4
# ----------------------
# Bars 2 and 4: Comping on beats 2 and 4
# Chords in D major: Dmaj7, Gmaj7, A7, Dmaj7

# Bar 2: Dmaj7 = D, F#, A, C#
bar2_chord_notes = [62, 67, 71, 74]
bar2_times = [beat_to_sec(1), beat_to_sec(1), beat_to_sec(1), beat_to_sec(1)]
bar2_velocity = [80, 80, 80, 80]

for note, time, vel in zip(bar2_chord_notes, bar2_times, bar2_velocity):
    piano.notes.append(pretty_midi.Note(vel, note, time, time + 0.25))

# Bar 4: Dmaj7 again
bar4_chord_notes = [62, 67, 71, 74]
bar4_times = [beat_to_sec(3), beat_to_sec(3), beat_to_sec(3), beat_to_sec(3)]
bar4_velocity = [80, 80, 80, 80]

for note, time, vel in zip(bar4_chord_notes, bar4_times, bar4_velocity):
    piano.notes.append(pretty_midi.Note(vel, note, time, time + 0.25))

# ----------------------
# 4. Dante: Tenor Sax - Emotive motif
# ----------------------
# Start at Bar 2, 3rd beat (beat 2.5)
# Phrase: D (62) - F# (67) - A (71) - rest - D (62) - B (71) - rest - and end on A (71) with a cry

# Time for the sax melody
sax_notes = [62, 67, 71, 0, 62, 71, 0, 71]
sax_times = [
    beat_to_sec(2.5),  # D
    beat_to_sec(2.75), # F#
    beat_to_sec(3),    # A
    beat_to_sec(3),    # rest
    beat_to_sec(3.25), # D
    beat_to_sec(3.5),  # B
    beat_to_sec(3.5),  # rest
    beat_to_sec(3.75)  # A
]
sax_velocity = [40, 60, 80, 0, 60, 80, 0, 100]  # build dynamics

for note, time, vel in zip(sax_notes, sax_times, sax_velocity):
    if note != 0:
        sax.notes.append(pretty_midi.Note(vel, note, time, time + 0.125))

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
