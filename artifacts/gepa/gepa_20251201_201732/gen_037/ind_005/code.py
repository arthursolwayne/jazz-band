
from mido import MidiFile, MidiTrack, Message, MetaMessage
import numpy as np

# Constants
BPM = 160
BEAT_DURATION = 60 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # seconds per bar
SAMPLE_RATE = 44100
NOTE_DURATION = 0.375  # seconds per note (quarter note)
REST_DURATION = 0.125  # 8th note rest

# Key: D major
# Scale degrees: D (2), E (4), F# (6), G (7), A (9), B (11), C# (13)
# We'll use these as reference for improvisation and voicings

# Time signature: 4/4
# Tempo: 160 BPM

# MIDI note numbers
# D2 = 38, E2 = 40, F#2 = 42, G2 = 43, A2 = 45, B2 = 47, C#3 = 49

# Define the melody for the tenor sax (you)
# Bars 1: Little Ray on drums only
# Bars 2-4: Full ensemble, melody and harmony

# Generate the MIDI file
mid = MidiFile(ticks_per_beat=480)
track = MidiTrack()
mid.tracks.append(track)

# Set tempo
track.append(MetaMessage('set_tempo', tempo=int(60000000 / BPM), time=0))

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Convert time to ticks (480 ticks per beat)
def time_to_ticks(t):
    return int(t * 480 / BEAT_DURATION)

# Bar 1 (0.0s to 1.5s)
# Kick on 1 and 3
track.append(Message('note_on', note=36, velocity=100, time=time_to_ticks(0)))
track.append(Message('note_off', note=36, velocity=100, time=time_to_ticks(0.375)))
track.append(Message('note_on', note=36, velocity=100, time=time_to_ticks(0.75)))
track.append(Message('note_off', note=36, velocity=100, time=time_to_ticks(0.375)))

# Snare on 2 and 4
track.append(Message('note_on', note=38, velocity=100, time=time_to_ticks(0.5)))
track.append(Message('note_off', note=38, velocity=100, time=time_to_ticks(0.375)))
track.append(Message('note_on', note=38, velocity=100, time=time_to_ticks(1.0)))
track.append(Message('note_off', note=38, velocity=100, time=time_to_ticks(0.375)))

# Hi-hats on every eighth note
for t in np.arange(0, BAR_DURATION, REST_DURATION):
    if t != 0:
        track.append(Message('note_on', note=42, velocity=80, time=time_to_ticks(t)))
        track.append(Message('note_off', note=42, velocity=80, time=time_to_ticks(REST_DURATION)))

# Bar 2: Full ensemble
# Tenor sax melody: Start with a haunting motif (D to B to A to D)
# D2 (38), B2 (47), A2 (45), D2 (38) — short motif, leave it hanging

# Tenor sax (you)
track.append(Message('note_on', note=38, velocity=100, time=time_to_ticks(1.5)))
track.append(Message('note_off', note=38, velocity=100, time=time_to_ticks(0.125)))
track.append(Message('note_on', note=47, velocity=100, time=time_to_ticks(1.625)))
track.append(Message('note_off', note=47, velocity=100, time=time_to_ticks(0.125)))
track.append(Message('note_on', note=45, velocity=100, time=time_to_ticks(1.75)))
track.append(Message('note_off', note=45, velocity=100, time=time_to_ticks(0.125)))
track.append(Message('note_on', note=38, velocity=100, time=time_to_ticks(1.875)))
track.append(Message('note_off', note=38, velocity=100, time=time_to_ticks(0.125)))

# Bass (Marcus): Walking line — D2 (38), F#2 (42), G2 (43), A2 (45)
track.append(Message('note_on', note=38, velocity=80, time=time_to_ticks(1.5)))
track.append(Message('note_off', note=38, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_on', note=42, velocity=80, time=time_to_ticks(1.875)))
track.append(Message('note_off', note=42, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_on', note=43, velocity=80, time=time_to_ticks(2.25)))
track.append(Message('note_off', note=43, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_on', note=45, velocity=80, time=time_to_ticks(2.625)))
track.append(Message('note_off', note=45, velocity=80, time=time_to_ticks(0.375)))

# Piano (Diane): Open voicings, resolving on the last chord
# Bar 2: Dmaj7 (D, F#, A, C#) -> Bar 3: G7 (G, B, D, F) -> Bar 4: C#m7 (C#, E, G, B)
# Comp on 2 and 4

# Bar 2: Dmaj7 (38, 42, 45, 49)
track.append(Message('note_on', note=38, velocity=80, time=time_to_ticks(1.5)))
track.append(Message('note_on', note=42, velocity=80, time=0))
track.append(Message('note_on', note=45, velocity=80, time=0))
track.append(Message('note_on', note=49, velocity=80, time=0))
track.append(Message('note_off', note=38, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=42, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=45, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=49, velocity=80, time=time_to_ticks(0.375)))

# Bar 3: G7 (43, 47, 49, 45)
track.append(Message('note_on', note=43, velocity=80, time=time_to_ticks(2.25)))
track.append(Message('note_on', note=47, velocity=80, time=0))
track.append(Message('note_on', note=49, velocity=80, time=0))
track.append(Message('note_on', note=45, velocity=80, time=0))
track.append(Message('note_off', note=43, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=47, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=49, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=45, velocity=80, time=time_to_ticks(0.375)))

# Bar 4: C#m7 (49, 52, 45, 47)
track.append(Message('note_on', note=49, velocity=80, time=time_to_ticks(2.625)))
track.append(Message('note_on', note=52, velocity=80, time=0))
track.append(Message('note_on', note=45, velocity=80, time=0))
track.append(Message('note_on', note=47, velocity=80, time=0))
track.append(Message('note_off', note=49, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=52, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=45, velocity=80, time=time_to_ticks(0.375)))
track.append(Message('note_off', note=47, velocity=80, time=time_to_ticks(0.375)))

# Drums continue (Bar 2-4)
# Repeat same pattern
for bar in range(2, 4):
    bar_start = bar * BAR_DURATION
    for t in np.arange(bar_start, bar_start + BAR_DURATION, REST_DURATION):
        if t != bar_start:
            track.append(Message('note_on', note=42, velocity=80, time=time_to_ticks(t - bar_start)))
            track.append(Message('note_off', note=42, velocity=80, time=time_to_ticks(REST_DURATION)))

# Save the MIDI file
mid.save('dante_russo_intro.mid')

print("MIDI file saved as 'dante_russo_intro.mid'")
