
from mido import MidiFile, MidiTrack, Message, MetaMessage
from mido import tempo2bpm

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (160 BPM)
track.append(MetaMessage('set_tempo', tempo=tempo2bpm(160)*1000, time=0))

# Define the time division (480 ticks per quarter note)
ticks_per_beat = 480
ticks_per_bar = 4 * ticks_per_beat  # 4/4 time

# Define the key: F major
# Scale degrees: F (1), G (2), A (3), Bb (4), C (5), D (6), E (7)
# Note values in F major: F (65), G (67), A (69), Bb (70), C (72), D (74), E (76)

# Define the note values for each instrument
# Little Ray (drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Diane (piano): 7th chords on 2 and 4
# Marcus (bass): Walking line with chromatic approaches
# Dante (tenor sax): Motif with a question, leave it hanging, then resolve

# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 4/4 time, 16th note divisions

# Time in ticks:
# 1 bar = 480 * 4 = 1920 ticks

# Bar 1: 0-1920 ticks
bar1_start = 0
bar1_end = 1920

# Kick on beat 1 and 3 (beat 0 and 2 in bar)
track.append(Message('note_on', note=35, velocity=100, time=bar1_start + 0 * ticks_per_beat))
track.append(Message('note_off', note=35, velocity=100, time=bar1_start + 0 * ticks_per_beat + 100))
track.append(Message('note_on', note=35, velocity=100, time=bar1_start + 2 * ticks_per_beat))
track.append(Message('note_off', note=35, velocity=100, time=bar1_start + 2 * ticks_per_beat + 100))

# Snare on beat 2 and 4 (beat 1 and 3 in bar)
track.append(Message('note_on', note=38, velocity=100, time=bar1_start + 1 * ticks_per_beat))
track.append(Message('note_off', note=38, velocity=100, time=bar1_start + 1 * ticks_per_beat + 100))
track.append(Message('note_on', note=38, velocity=100, time=bar1_start + 3 * ticks_per_beat))
track.append(Message('note_off', note=38, velocity=100, time=bar1_start + 3 * ticks_per_beat + 100))

# Hihat on every eighth (4 per bar)
for i in range(8):
    track.append(Message('note_on', note=42, velocity=100, time=bar1_start + i * (ticks_per_beat // 2)))
    track.append(Message('note_off', note=42, velocity=100, time=bar1_start + i * (ticks_per_beat // 2) + 50))

# Bar 2: Everyone in

# Diane (piano): 7th chords on 2 and 4
# Bar 2: Beat 1: F7 (F, A, C, E)
# Beat 2: G7 (G, B, D, F)
# Beat 3: A7 (A, C, E, G)
# Beat 4: Bb7 (Bb, D, F, Ab)

# Diane plays chords on 2 and 4
diane_notes = [
    (2 * ticks_per_beat, 65, 72, 69, 76),
    (4 * ticks_per_beat, 67, 76, 74, 65)
]

for time, *notes in diane_notes:
    for note in notes:
        track.append(Message('note_on', note=note, velocity=90, time=time))
    for note in reversed(notes):
        track.append(Message('note_off', note=note, velocity=90, time=time + 100))

# Marcus (bass): Walking line with chromatic approaches
# Bar 2: F -> G -> A -> Bb -> C -> D -> E -> F

bass_notes = [
    (0 * ticks_per_beat, 65),  # F
    (1 * ticks_per_beat, 67),  # G
    (2 * ticks_per_beat, 69),  # A
    (3 * ticks_per_beat, 70),  # Bb
    (4 * ticks_per_beat, 72),  # C
    (5 * ticks_per_beat, 74),  # D
    (6 * ticks_per_beat, 76),  # E
    (7 * ticks_per_beat, 65)   # F
]

for time, note in bass_notes:
    track.append(Message('note_on', note=note, velocity=80, time=time))
    track.append(Message('note_off', note=note, velocity=80, time=time + 100))

# Little Ray (drums): Same pattern as bar 1
# Kick, snare, hihat
track.append(Message('note_on', note=35, velocity=100, time=bar1_end + 0 * ticks_per_beat))
track.append(Message('note_off', note=35, velocity=100, time=bar1_end + 0 * ticks_per_beat + 100))
track.append(Message('note_on', note=35, velocity=100, time=bar1_end + 2 * ticks_per_beat))
track.append(Message('note_off', note=35, velocity=100, time=bar1_end + 2 * ticks_per_beat + 100))

track.append(Message('note_on', note=38, velocity=100, time=bar1_end + 1 * ticks_per_beat))
track.append(Message('note_off', note=38, velocity=100, time=bar1_end + 1 * ticks_per_beat + 100))
track.append(Message('note_on', note=38, velocity=100, time=bar1_end + 3 * ticks_per_beat))
track.append(Message('note_off', note=38, velocity=100, time=bar1_end + 3 * ticks_per_beat + 100))

for i in range(8):
    track.append(Message('note_on', note=42, velocity=100, time=bar1_end + i * (ticks_per_beat // 2)))
    track.append(Message('note_off', note=42, velocity=100, time=bar1_end + i * (ticks_per_beat // 2) + 50))

# Bar 3: Dante (tenor sax): Motif, leave it hanging
# F (65), G (67), E (76), rest (65) — question, tension, release

dante_notes = [
    (0 * ticks_per_beat, 65),
    (1 * ticks_per_beat, 67),
    (2 * ticks_per_beat, 76),
    (4 * ticks_per_beat, 65)  # Let the rest do the work
]

for time, note in dante_notes:
    track.append(Message('note_on', note=note, velocity=100, time=time))
    track.append(Message('note_off', note=note, velocity=100, time=time + 100))

# Bar 4: Dante resolves the motif
# F (65), A (69), C (72), E (76) — resolution, closure

dante_notes = [
    (0 * ticks_per_beat, 65),
    (1 * ticks_per_beat, 69),
    (2 * ticks_per_beat, 72),
    (3 * ticks_per_beat, 76)
]

for time, note in dante_notes:
    track.append(Message('note_on', note=note, velocity=100, time=bar1_end + time))
    track.append(Message('note_off', note=note, velocity=100, time=bar1_end + time + 100))

# Add final meta message to end the track
track.append(MetaMessage('end_of_track', time=0))

# Save the MIDI file
mid.save('dante_intro.mid')
