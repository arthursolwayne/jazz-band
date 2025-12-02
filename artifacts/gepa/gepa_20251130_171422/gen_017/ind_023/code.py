
from mido import MidiFile, MidiTrack, Message
import numpy as np

# Set tempo (160 BPM)
BPM = 160
tempo = 60000000 // BPM  # microseconds per beat

# Create MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add tempo
track.append(Message('set_tempo', tempo=tempo, time=0))

# Key: F major
# Scale degrees: 1, 2, 3, 4, 5, 6, 7
# F major scale: F, G, A, Bb, C, D, E
# Notes: 65 (F), 67 (G), 69 (A), 68 (Bb), 72 (C), 74 (D), 76 (E)

# MIDI note numbers
F = 65
G = 67
A = 69
Bb = 68
C = 72
D = 74
E = 76

# Bar 1: Little Ray alone
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3

# Note: 1 beat = 60000000 / 160 / 4 = 93750 microseconds
beat = 93750

def add_snare(time):
    track.append(Message('note_on', note=38, velocity=100, time=time))
    track.append(Message('note_off', note=38, velocity=100, time=beat//2))

def add_kick(time):
    track.append(Message('note_on', note=36, velocity=100, time=time))
    track.append(Message('note_off', note=36, velocity=100, time=beat//2))

def add_hihat(time):
    track.append(Message('note_on', note=42, velocity=100, time=time))
    track.append(Message('note_off', note=42, velocity=100, time=beat//4))

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
add_kick(0)
add_hihat(0)
add_hihat(beat//4)
add_hihat(beat//2)
add_hihat(3*beat//4)
add_snare(beat//2)
add_kick(beat)
add_hihat(beat)
add_hihat(5*beat//4)
add_hihat(3*beat//2)
add_hihat(7*beat//4)
add_snare(beat*1.5)

# Bar 2: Diane on piano - 7th chords on 2 and 4
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab (but we'll use Bb, D, F, A as a substitution for phrasing)

# Bar 2: Diane plays on 2 and 4
def play_piano_notes(time, notes):
    for note in notes:
        track.append(Message('note_on', note=note, velocity=90, time=time))
        track.append(Message('note_off', note=note, velocity=90, time=beat))

# Bar 2 - Diane on 2 and 4
play_piano_notes(beat, [F, A, C, E])  # F7
play_piano_notes(beat*2, [Bb, D, F, A])  # Bb7 (subbed)

# Bar 3: Marcus on bass - walking line with chromatic approach
# F -> F# -> G -> A -> Bb -> B -> C -> D -> E -> F

bass_line = [F, 66, G, A, Bb, 70, C, D, E, F]
for i, note in enumerate(bass_line):
    time = beat * i
    track.append(Message('note_on', note=note, velocity=90, time=time))
    track.append(Message('note_off', note=note, velocity=90, time=beat//2))

# Bar 4: You on tenor sax - short motif, singable, open-ended
# F - G - Bb - rest (on beat 2)
# Then repeat with a twist: F - Bb - A - rest
# Then repeat with a slight shift: F - Bb - D - rest

def play_sax_note(time, note):
    track.append(Message('note_on', note=note, velocity=110, time=time))
    track.append(Message('note_off', note=note, velocity=110, time=beat//2))

# Motif: F - G - Bb - rest (beat 1)
play_sax_note(beat*2, F)
play_sax_note(beat*2 + beat//2, G)
play_sax_note(beat*2 + beat, Bb)
track.append(Message('note_off', note=F, velocity=110, time=0))  # just to clear
track.append(Message('note_off', note=G, velocity=110, time=0))
track.append(Message('note_off', note=Bb, velocity=110, time=0))

# Motif: F - Bb - A - rest (beat 2)
play_sax_note(beat*2 + beat*1.5, F)
play_sax_note(beat*2 + beat*2, Bb)
play_sax_note(beat*2 + beat*2.5, A)
track.append(Message('note_off', note=F, velocity=110, time=0))
track.append(Message('note_off', note=Bb, velocity=110, time=0))
track.append(Message('note_off', note=A, velocity=110, time=0))

# Motif: F - Bb - D - rest (beat 3)
play_sax_note(beat*2 + beat*3, F)
play_sax_note(beat*2 + beat*3.5, Bb)
play_sax_note(beat*2 + beat*4, D)
track.append(Message('note_off', note=F, velocity=110, time=0))
track.append(Message('note_off', note=Bb, velocity=110, time=0))
track.append(Message('note_off', note=D, velocity=110, time=0))

# End of piece
track.append(Message('end_of_track', time=0))

# Save the MIDI file
mid.save("dante_introduction.mid")
print("MIDI file generated: 'dante_introduction.mid'")
