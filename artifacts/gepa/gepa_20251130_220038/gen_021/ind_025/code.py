
from mido import MidiFile, MidiTrack, Message, tempo2bpm
import numpy as np

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo to 160 BPM
tempo = mido.bpm2tempo(160)
track.append(Message('set_tempo', tempo=tempo, time=0))

# Define the time resolution (ticks per beat)
ticks_per_beat = 480  # standard MIDI resolution
bar_length = 4 * ticks_per_beat  # 4/4 time
total_length = bar_length * 4  # 4 bars

# Define the key: D major
# Scale degrees: D (0), E (2), F# (4), G (5), A (7), B (9), C# (11)
# Root note is D (62 MIDI note number)

# Little Ray: Bar 1 - Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 - 4/4
for beat in range(4):
    time = beat * ticks_per_beat
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        track.append(Message('note_on', note=36, velocity=100, time=time))
        track.append(Message('note_off', note=36, velocity=100, time=1))
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        track.append(Message('note_on', note=38, velocity=110, time=time))
        track.append(Message('note_off', note=38, velocity=110, time=1))
    # Hi-hat on every eighth
    for eighth in range(2):
        track.append(Message('note_on', note=42, velocity=60, time=time + eighth * ticks_per_beat//2))
        track.append(Message('note_off', note=42, velocity=60, time=1))

# Bars 2-4: All instruments in. You (tenor) take the melody.
# Diane (piano): 7th chords, comp on 2 and 4
# Marcus (bass): Walking line, chromatic approaches, never the same note twice
# You (tenor): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Define the motif (in D major): D - F# - A - C# (Dm7)
motif = [62, 66, 69, 71]  # D, F#, A, C#
note_durations = [0.5, 0.5, 0.5, 0.5]  # quarter notes

# Diane: 7th chords on 2 and 4 (bar 2: D7, bar 3: G7, bar 4: C7)
diane_notes = {
    2: [62, 66, 69, 71],  # D7
    3: [67, 71, 74, 76],  # G7
    4: [60, 64, 67, 69]   # C7
}

# Marcus: walking bass line in D major
# Root-fifth-root-bass walk (chromatic approach to G on bar 2, etc.)
bass_line = [
    62, 67, 62, 64,  # D, G, D, Eb (chromatic approach to E)
    67, 72, 67, 70,  # G, B, G, A
    69, 71, 69, 71,  # A, C#, A, C#
    71, 74, 71, 74   # C#, E, C#, E
]

# You: Tenor sax
# Play the motif in bar 2 (first two notes), leave it hanging, return in bar 4 to finish

# Bar 2: Play first two notes (D, F#)
bar_2_start = 1 * bar_length
for i, note in enumerate(motif[:2]):
    time = bar_2_start + i * ticks_per_beat
    track.append(Message('note_on', note=note, velocity=100, time=time))
    track.append(Message('note_off', note=note, velocity=100, time=ticks_per_beat))

# Bar 3: Diane plays chord on beat 2
bar_3_start = 2 * bar_length
diane_notes_bar3 = diane_notes[3]
for i, note in enumerate(diane_notes_bar3):
    time = bar_3_start + (i % 2) * ticks_per_beat * 2  # on 2 and 4
    track.append(Message('note_on', note=note, velocity=90, time=time))
    track.append(Message('note_off', note=note, velocity=90, time=ticks_per_beat))

# Bar 4: Marcus walks, Diane plays chord on beat 2, you finish the motif
bar_4_start = 3 * bar_length
for i, note in enumerate(bass_line[8:]):
    time = bar_4_start + i * ticks_per_beat
    track.append(Message('note_on', note=note, velocity=90, time=time))
    track.append(Message('note_off', note=note, velocity=90, time=ticks_per_beat))

# Diane: 7th chord on beat 2
diane_notes_bar4 = diane_notes[4]
for i, note in enumerate(diane_notes_bar4):
    time = bar_4_start + (i % 2) * ticks_per_beat * 2  # on 2 and 4
    track.append(Message('note_on', note=note, velocity=90, time=time))
    track.append(Message('note_off', note=note, velocity=90, time=ticks_per_beat))

# You: Finish the motif in bar 4
for i, note in enumerate(motif[2:]):
    time = bar_4_start + i * ticks_per_beat
    track.append(Message('note_on', note=note, velocity=100, time=time))
    track.append(Message('note_off', note=note, velocity=100, time=ticks_per_beat))

# Save the MIDI file
mid.save('dante_russo_intro.mid')
