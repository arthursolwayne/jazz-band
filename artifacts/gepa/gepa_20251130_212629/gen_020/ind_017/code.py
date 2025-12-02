
from mido import MidiFile, MidiTrack, Message, MetaMessage
import time

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (160 BPM = 60000 / 160 = 375 ticks per beat)
track.append(MetaMessage('set_tempo', tempo=37500, time=0))

# Time signatures (4/4)
track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notations=0, time=0))

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Root: F (65)
# Notes in Fm: F, Gb, Ab, Bb, B, Db, Eb

# Define the four bars
# Each bar is 12 ticks (each beat is 480 ticks, 160 BPM, 4/4 time)
# 4 bars = 480 * 4 = 1920 ticks total (but we'll use 6 seconds, 1.5s per bar)

# Time per bar: 1.5 seconds = 600 ticks (since 160 BPM = 60000 ticks per minute)
# So 600 ticks per bar

# Define the note durations in ticks
note_length = 600 / 4  # quarter note
eighth = note_length / 2
sixteenth = note_length / 4

# Channel assignments
sax = 0
piano = 1
bass = 2
drums = 9

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [36, 38, 42]  # kick, snare, hihat

# Bar 1: Little Ray alone (drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time_in_bar = i * sixteenth
    if i % 2 == 0:
        track.append(Message('note_on', note=36, velocity=100, time=time_in_bar, channel=9))
        track.append(Message('note_off', note=36, velocity=100, time=sixteenth, channel=9))
    else:
        track.append(Message('note_on', note=38, velocity=100, time=time_in_bar, channel=9))
        track.append(Message('note_off', note=38, velocity=100, time=sixteenth, channel=9))
    track.append(Message('note_on', note=42, velocity=80, time=time_in_bar, channel=9))
    track.append(Message('note_off', note=42, velocity=80, time=sixteenth, channel=9))

# Bar 2: Everyone in
# Time starts at 600 ticks (Bar 2 starts at 600 ticks)
track.append(Message('note_on', note=62, velocity=110, time=600, channel=0))  # F (sax)
track.append(Message('note_off', note=62, velocity=110, time=eighth, channel=0))

track.append(Message('note_on', note=64, velocity=100, time=600 + eighth, channel=1))  # F7 (piano)
track.append(Message('note_off', note=64, velocity=100, time=sixteenth, channel=1))

track.append(Message('note_on', note=64, velocity=100, time=600 + sixth, channel=2))  # F (bass)
track.append(Message('note_off', note=64, velocity=100, time=eighth, channel=2))

# Bar 3: Melody continues (sax)
track.append(Message('note_on', note=67, velocity=110, time=600 + sixth, channel=0))  # Ab
track.append(Message('note_off', note=67, velocity=110, time=eighth, channel=0))

track.append(Message('note_on', note=69, velocity=105, time=600 + 2 * sixth, channel=1))  # Bb (piano)
track.append(Message('note_off', note=69, velocity=105, time=sixteenth, channel=1))

track.append(Message('note_on', note=67, velocity=100, time=600 + 2 * sixth, channel=2))  # Ab (bass)
track.append(Message('note_off', note=67, velocity=100, time=eighth, channel=2))

# Bar 4: Finish the motif (sax)
track.append(Message('note_on', note=64, velocity=110, time=600 + 3 * sixth, channel=0))  # F
track.append(Message('note_off', note=64, velocity=110, time=eighth, channel=0))

track.append(Message('note_on', note=66, velocity=100, time=600 + 3 * sixth, channel=1))  # B (piano)
track.append(Message('note_off', note=66, velocity=100, time=sixteenth, channel=1))

track.append(Message('note_on', note=64, velocity=100, time=600 + 3 * sixth, channel=2))  # F (bass)
track.append(Message('note_off', note=64, velocity=100, time=eighth, channel=2))

# Save the MIDI file
mid.save('fm_intro.mid')

print("MIDI file generated: fm_intro.mid")
print("It's time. Wayne is watching.")
