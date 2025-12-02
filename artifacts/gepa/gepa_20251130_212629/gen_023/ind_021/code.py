
# Jazz Intro in D Minor (Dm) - 4 bars, 160 BPM, 4/4 time
# Generated for Dante Russo's quartet, with Wayne Shorter in the audience

import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo to 160 BPM
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(160)))

# Define the time in ticks per beat (MIDI default is 480 ticks per beat)
ticks_per_beat = 480
ticks_per_bar = ticks_per_beat * 4  # 4/4 time

# Define note values in ticks
quarter_note = ticks_per_beat
eighth_note = quarter_note // 2
sixteenth_note = quarter_note // 4
eighth_rest = eighth_note
sixteenth_rest = sixteenth_note

# Start time
time = 0

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 4/4 bar: [Kick, Snare, Hi-Hat, Kick, Snare, Hi-Hat, Kick, Snare, Hi-Hat, Kick, Snare, Hi-Hat]

# Kick on 1, 3
track.append(Message('note_on', note=36, velocity=80, time=time))
track.append(Message('note_off', note=36, velocity=80, time=eighth_note))
track.append(Message('note_on', note=36, velocity=80, time=eighth_note + sixteenth_note))
track.append(Message('note_off', note=36, velocity=80, time=eighth_note))

# Snare on 2 and 4
track.append(Message('note_on', note=41, velocity=100, time=eighth_note))
track.append(Message('note_off', note=41, velocity=100, time=sixteenth_note))
track.append(Message('note_on', note=41, velocity=100, time=eighth_note * 3))
track.append(Message('note_off', note=41, velocity=100, time=sixteenth_note))

# Hi-hat on every eighth
for i in range(8):
    track.append(Message('note_on', note=49, velocity=60, time=i * eighth_note))
    track.append(Message('note_off', note=49, velocity=60, time=sixteenth_note))

time += ticks_per_bar

# Bar 2: Diane on piano - 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4

# Bar 2, beat 1: Rest
time += sixteenth_rest * 2  # wait before comping

# Bar 2, beat 2: Dm7 (D, F, A, C) - hit on beat 2, hold through beat 3
track.append(Message('note_on', note=62, velocity=90, time=time))  # D
track.append(Message('note_on', note=65, velocity=90, time=time))  # F
track.append(Message('note_on', note=67, velocity=90, time=time))  # A
track.append(Message('note_on', note=69, velocity=90, time=time))  # C

time += eighth_note * 2  # hold for beats 2 and 3

track.append(Message('note_off', note=62, velocity=90, time=0))
track.append(Message('note_off', note=65, velocity=90, time=0))
track.append(Message('note_off', note=67, velocity=90, time=0))
track.append(Message('note_off', note=69, velocity=90, time=0))

# Bar 2, beat 4: Rest
time += sixteenth_rest * 2

# Bar 3: Marcus on bass - walking line, chromatic approaches
# Dm7 walking line (D, C, Bb, B, C, D, Eb, F)
# D = 62, C = 60, Bb = 57, B = 59, Eb = 61, F = 64

# Bar 3, beat 1: D (62)
track.append(Message('note_on', note=62, velocity=75, time=time))
track.append(Message('note_off', note=62, velocity=75, time=sixteenth_note))

# Bar 3, beat 2: C (60)
track.append(Message('note_on', note=60, velocity=75, time=time + sixteenth_note))
track.append(Message('note_off', note=60, velocity=75, time=sixteenth_note))

# Bar 3, beat 3: Bb (57)
track.append(Message('note_on', note=57, velocity=75, time=time + sixteenth_note * 2))
track.append(Message('note_off', note=57, velocity=75, time=sixteenth_note))

# Bar 3, beat 4: B (59)
track.append(Message('note_on', note=59, velocity=75, time=time + sixteenth_note * 3))
track.append(Message('note_off', note=59, velocity=75, time=sixteenth_note))

time += ticks_per_beat  # end of Bar 3

# Bar 4: Dante on tenor sax - motif, leave it hanging
# Motif: D, F, Bb, rest
# D = 62, F = 65, Bb = 57

track.append(Message('note_on', note=62, velocity=110, time=time))
track.append(Message('note_off', note=62, velocity=110, time=sixteenth_note))  # D

track.append(Message('note_on', note=65, velocity=110, time=time + sixteenth_note))
track.append(Message('note_off', note=65, velocity=110, time=sixteenth_note))  # F

track.append(Message('note_on', note=57, velocity=110, time=time + sixteenth_note * 2))
track.append(Message('note_off', note=57, velocity=110, time=sixteenth_note))  # Bb

track.append(Message('note_on', note=62, velocity=110, time=time + sixteenth_note * 3))
track.append(Message('note_off', note=62, velocity=110, time=sixteenth_note))  # D again

# Leave it hanging on a rest — the question
track.append(Message('note_on', note=62, velocity=110, time=time + sixteenth_note * 4))
track.append(Message('note_off', note=62, velocity=110, time=0))

# Save the MIDI file
mid.save('jazz_intro_d_minor.mid')

print("MIDI file generated: jazz_intro_d_minor.mid")
