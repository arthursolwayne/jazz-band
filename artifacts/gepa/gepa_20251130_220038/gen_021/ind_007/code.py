
import mido
from mido import Message, MidiFile, MidiTrack

# Constants
BPM = 160
BEATS_PER_BAR = 4
TICKS_PER_BEAT = 960
TICKS_PER_BAR = TICKS_PER_BEAT * BEATS_PER_BAR
NOTE_DURATION_MULTIPLIER = 1  # No tempo change, just ticks

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Scale degrees: 1=F, 2=G, 3=Ab, 4=Bb, 5=B, 6=Db, 7=Eb

# Time in ticks per beat and per bar
TICKS_PER_BAR = TICKS_PER_BEAT * BEATS_PER_BAR
TICKS_PER_EIGHTH = TICKS_PER_BEAT // 2
TICKS_PER_QUARTER = TICKS_PER_BEAT

# Create a new MIDI file and track
mid = MidiFile(ticks_per_beat=TICKS_PER_BEAT)
track_sax = MidiTrack()
track_piano = MidiTrack()
track_bass = MidiTrack()
track_drums = MidiTrack()

mid.tracks.append(track_sax)
mid.tracks.append(track_piano)
mid.tracks.append(track_bass)
mid.tracks.append(track_drums)

# Program changes
track_sax.append(Message('program_change', program=64, channel=0))  # Tenor sax
track_piano.append(Message('program_change', program=0, channel=1))  # Acoustic piano
track_bass.append(Message('program_change', program=33, channel=2))  # Double bass
track_drums.append(Message('program_change', program=0, channel=9))  # Acoustic drums

# Bar 1: Drums only
# Kick on 1 and 3
track_drums.append(Message('note_on', note=36, velocity=100, time=0))
track_drums.append(Message('note_off', note=36, velocity=100, time=TICKS_PER_QUARTER))
track_drums.append(Message('note_on', note=36, velocity=100, time=TICKS_PER_QUARTER))
track_drums.append(Message('note_off', note=36, velocity=100, time=TICKS_PER_QUARTER))

# Snare on 2 and 4
track_drums.append(Message('note_on', note=38, velocity=110, time=TICKS_PER_EIGHTH))
track_drums.append(Message('note_off', note=38, velocity=110, time=TICKS_PER_EIGHTH))
track_drums.append(Message('note_on', note=38, velocity=110, time=TICKS_PER_QUARTER * 2))
track_drums.append(Message('note_off', note=38, velocity=110, time=TICKS_PER_EIGHTH))

# Hi-hat on every eighth
for i in range(8):
    track_drums.append(Message('note_on', note=42, velocity=90, time=0))
    track_drums.append(Message('note_off', note=42, velocity=90, time=TICKS_PER_EIGHTH))

# Bar 2: All instruments come in

# Bass line: Chromatic walking line in F minor
bass_notes = [65, 66, 67, 68, 69, 70, 71, 64]  # F, Gb, G, Ab, A, Bb, B, Eb
for note in bass_notes:
    track_bass.append(Message('note_on', note=note, velocity=80, time=0))
    track_bass.append(Message('note_off', note=note, velocity=80, time=TICKS_PER_EIGHTH))

# Piano: Comp on 2 and 4, 7th chords
piano_notes = [
    (64, 67, 69, 70, 66),  # F7 (F, A, C#, Eb, Gb) - on beat 1
    (65, 68, 70, 71, 67),  # Gb7 (Gb, Bb, D, F, Ab) - on beat 2
    (66, 69, 71, 72, 68),  # G7 (G, B, D, F#, A) - on beat 3 (but not played here)
    (64, 67, 69, 70, 66),  # F7 - on beat 4
]

for i, chord in enumerate(piano_notes):
    for note in chord:
        track_piano.append(Message('note_on', note=note, velocity=90, time=0))
    for note in chord:
        track_piano.append(Message('note_off', note=note, velocity=90, time=TICKS_PER_EIGHTH * (i + 1)))

# Saxophone melody: Start it, leave it hanging, finish it
sax_notes = [
    (64, 1.0),       # F, quarter note
    (67, 0.75),      # A, dotted eighth
    (65, 0.25),      # G, sixteenth
    (64, 0.25),      # F, sixteenth
    (67, 0.75),      # A, dotted eighth
    (64, 0.75),      # F, dotted eighth
    (67, 0.75),      # A, dotted eighth
    (64, 1.0)        # F, quarter note (resolution)
]

start_time = TICKS_PER_QUARTER * 1  # Start on beat 1 of bar 2

for note, duration in sax_notes:
    ticks = int(duration * TICKS_PER_QUARTER)
    track_sax.append(Message('note_on', note=note, velocity=100, time=start_time))
    track_sax.append(Message('note_off', note=note, velocity=100, time=ticks))
    start_time += ticks

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
