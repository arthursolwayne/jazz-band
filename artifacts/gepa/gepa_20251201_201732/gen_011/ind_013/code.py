
import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo to 160 BPM
# 60,000,000 microseconds per minute / 160 beats per minute = 375,000 microseconds per beat
track.append(mido.MetaMessage('set_tempo', tempo=375000))

# Define note values
F3 = 71
G3 = 72
A3 = 74
Bb3 = 73
C4 = 72
D4 = 74
E4 = 76
F4 = 77
G4 = 79
A4 = 81
Bb4 = 80
C5 = 81

# Define time in ticks (approx. 480 ticks per beat)
ticks_per_beat = 480
tick_per_bar = ticks_per_beat * 4  # 4 beats per bar

# Bar 1: Little Ray (Drums) - Setup, build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th note
# Time: 0 to 1.5s (Bar 1)
for i in range(0, tick_per_bar, ticks_per_beat // 2):  # every 8th note
    if i % ticks_per_beat == 0:  # Kick on beat 1, 3
        track.append(Message('note_on', note=36, velocity=100, time=i))
        track.append(Message('note_off', note=36, velocity=100, time=ticks_per_beat // 2))
    elif i % ticks_per_beat == ticks_per_beat // 2:  # Snare on beat 2, 4
        track.append(Message('note_on', note=38, velocity=100, time=i))
        track.append(Message('note_off', note=38, velocity=100, time=ticks_per_beat // 2))
    track.append(Message('note_on', note=42, velocity=60, time=i))  # hi-hat
    track.append(Message('note_off', note=42, velocity=60, time=ticks_per_beat // 4))

# Bar 2: Diane (Piano) - Open voicings, first chord
# Fmaj7 (F, A, C, E) -> F, A, C, E (71, 74, 77, 76)
# Time: 1.5 to 3.0s (Bar 2)
track.append(Message('note_on', note=F3, velocity=100, time=0))
track.append(Message('note_on', note=A3, velocity=100, time=0))
track.append(Message('note_on', note=C4, velocity=100, time=0))
track.append(Message('note_on', note=E4, velocity=100, time=0))

# Bar 3: Marcus (Bass) - Walking line: F2 (38) -> G2 (39) -> A2 (41) -> Bb2 (40)
# Time: 3.0 to 4.5s (Bar 3)
track.append(Message('note_on', note=38, velocity=80, time=0))
track.append(Message('note_off', note=38, velocity=80, time=ticks_per_beat // 2))
track.append(Message('note_on', note=39, velocity=80, time=ticks_per_beat // 2))
track.append(Message('note_off', note=39, velocity=80, time=ticks_per_beat // 2))
track.append(Message('note_on', note=41, velocity=80, time=ticks_per_beat))
track.append(Message('note_off', note=41, velocity=80, time=ticks_per_beat // 2))
track.append(Message('note_on', note=40, velocity=80, time=ticks_per_beat * 1.5))
track.append(Message('note_off', note=40, velocity=80, time=ticks_per_beat // 2))

# Bar 4: You (Tenor Sax) - Melody, short motif, searching, open-ended
# F4 (77) -> D4 (74) -> rest -> F4 (77) -> D4 (74)
# Time: 4.5 to 6.0s (Bar 4)
track.append(Message('note_on', note=F4, velocity=110, time=0))
track.append(Message('note_off', note=F4, velocity=110, time=ticks_per_beat // 2))
track.append(Message('note_on', note=D4, velocity=110, time=ticks_per_beat // 2))
track.append(Message('note_off', note=D4, velocity=110, time=ticks_per_beat // 2))
track.append(Message('note_on', note=F4, velocity=110, time=ticks_per_beat * 1.5))
track.append(Message('note_off', note=F4, velocity=110, time=ticks_per_beat // 2))
track.append(Message('note_on', note=D4, velocity=110, time=ticks_per_beat * 2))
track.append(Message('note_off', note=D4, velocity=110, time=ticks_per_beat // 2))

# End of track
track.append(mido.MetaMessage('end_of_track', time=0))

# Save the MIDI file
mid.save('dante_intro.mid')
