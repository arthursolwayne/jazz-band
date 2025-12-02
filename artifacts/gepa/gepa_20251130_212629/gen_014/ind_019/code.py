
from mido import MidiFile, MidiTrack, Message, MetaMessage
import numpy as np

# Constants
BPM = 160
BEATS_PER_BAR = 4
NOTE_DURATION = 0.5  # 1/2 note per beat (at 160 BPM, 1 beat = 0.375s, so this is 0.75s)

# MIDI note numbers for D major scale
D_MAJOR_SCALE = [50, 52, 53, 55, 57, 59, 60]  # D, E, F#, G, A, B, C#

# Time per bar in seconds
SECONDS_PER_BAR = 60.0 / BPM * BEATS_PER_BAR  # 6.0 seconds

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo
track.append(MetaMessage('set_tempo', tempo=600000 // BPM, time=0))  # 600000 microseconds per beat

# Function to add a note
def add_note(note, time, duration, velocity=100):
    track.append(Message('note_on', note=note, velocity=velocity, time=time))
    track.append(Message('note_off', note=note, velocity=0, time=duration))

# Bar 1: Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat every eighth)
bar_1 = SECONDS_PER_BAR / BEATS_PER_BAR  # duration of each beat
for beat in range(BEATS_PER_BAR):
    time = beat * bar_1
    if beat == 0 or beat == 2:
        add_note(36, time, bar_1)  # Kick on 1 and 3
    if beat == 1 or beat == 3:
        add_note(38, time, bar_1)  # Snare on 2 and 4
    add_note(42, time, bar_1 / 2)  # Hi-hat on every eighth note

# Bar 2: Bass enters with walking line in D major (chromatic approach)
bass_notes = [50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 57, 55, 53, 50]
for i, note in enumerate(bass_notes):
    time = (1 + i * 0.25) * bar_1  # 1/4 note per beat
    add_note(note, time, bar_1 / 4, velocity=60)

# Bar 2: Piano enters with 7th chords on 2 and 4
# D7 = D, F#, A, C
# G7 = G, Bb, D, F
# A7 = A, C#, E, G
chords = [
    (50, 53, 57, 60),  # D7
    (55, 58, 62, 57),  # G7 (with chromatic passing)
    (57, 60, 64, 67),  # A7
]
for i, chord in enumerate(chords):
    time = (1 + i * 0.5) * bar_1  # on 2nd and 4th beats
    for note in chord:
        add_note(note, time, bar_1 / 2, velocity=80)

# Bar 2: Tenor sax enters with the motif (your moment)
sax_motif = [55, 57, 55, 53]  # G, A, G, F#
for i, note in enumerate(sax_motif):
    time = (1 + i * 0.5) * bar_1
    add_note(note, time, bar_1 / 2, velocity=100)

# Bar 3: Continue with walking bass, comping piano, and sax melody (motif repeated slightly altered)
# Bass continues the same pattern
for i, note in enumerate(bass_notes):
    time = (2 + i * 0.25) * bar_1
    add_note(note, time, bar_1 / 4, velocity=60)

# Piano continues with comping on 2 and 4
for i, chord in enumerate(chords):
    time = (2 + i * 0.5) * bar_1
    for note in chord:
        add_note(note, time, bar_1 / 2, velocity=80)

# Sax repeats motif, slightly altered
sax_motif = [55, 57, 55, 53, 55, 57, 55, 53, 55]  # G, A, G, F#, G, A, G, F#, G
for i, note in enumerate(sax_motif):
    time = (2 + i * 0.25) * bar_1
    add_note(note, time, bar_1 / 4, velocity=100)

# Bar 4: Full ensemble, motif resolved
# Bass continues
for i, note in enumerate(bass_notes):
    time = (3 + i * 0.25) * bar_1
    add_note(note, time, bar_1 / 4, velocity=60)

# Piano continues
for i, chord in enumerate(chords):
    time = (3 + i * 0.5) * bar_1
    for note in chord:
        add_note(note, time, bar_1 / 2, velocity=80)

# Sax resolves the motif
sax_motif = [55, 57, 55, 53, 55, 57, 55, 53, 55, 57, 55, 53, 50]  # Resolving to D
for i, note in enumerate(sax_motif):
    time = (3 + i * 0.25) * bar_1
    add_note(note, time, bar_1 / 4, velocity=100)

# Add drum fills on bar 4
for beat in range(BEATS_PER_BAR):
    time = (3 + beat) * bar_1 / BEATS_PER_BAR
    if beat == 0 or beat == 2:
        add_note(36, time, bar_1 / 4)  # Kick on 1 and 3
    if beat == 1 or beat == 3:
        add_note(38, time, bar_1 / 4)  # Snare on 2 and 4
    add_note(42, time, bar_1 / 8)  # Hi-hat on every eighth note

# Save the MIDI file
mid.save('dante_russo_intro.mid')
print("MIDI file 'dante_russo_intro.mid' has been created.")
