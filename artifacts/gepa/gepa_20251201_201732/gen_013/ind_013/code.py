
import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file with one track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (160 BPM)
tempo = mido.bpm2tempo(160)
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Key: F Major
# Time signature: 4/4
track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notations=0))

# MIDI notes: F (65), G (67), A (69), Bb (70), C (72), D (74), E (76), F (77)
# Percussion channels (Drums): 9
# Bass: Channel 0
# Piano: Channel 1
# Sax: Channel 2
# Drums: Channel 9

# Define instruments
track.append(Message('program_change', channel=0, program=40))  # Bass
track.append(Message('program_change', channel=1, program=0))    # Piano
track.append(Message('program_change', channel=2, program=64))   # Tenor Sax
track.append(Message('program_change', channel=9, program=128))  # Drums

# Constants
BPM = 160
BEAT = mido.second / BPM / 4  # 4 beats per second
BAR = BEAT * 4  # 1 bar = 4 beats
NOTE_DURATION = BEAT * 0.5  # Each note is a half beat (1/2 note)
REST_DURATION = BEAT * 0.25  # Quarter rest
F = 65
G = 67
A = 69
Bb = 70
C = 72
D = 74
E = 76
F2 = 77
F3 = 87  # For saxophone melody

# Bar 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
track.append(Message('note_on', channel=9, note=36, velocity=100, time=0))  # Kick on 1
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 2
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 3
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 4
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 5
track.append(Message('note_off', channel=9, note=36, velocity=100, time=0))  # Kick off
track.append(Message('note_off', channel=9, note=38, velocity=100, time=0))  # Snare off
track.append(Message('note_off', channel=9, note=42, velocity=90, time=0))  # Hihat off

# Bar 2: Everyone comes in — Diane on piano (F7, Ab7, Bb7, C7) — open voicings
track.append(Message('note_on', channel=1, note=87, velocity=100, time=0))  # F7 (F, A, C, Eb)
track.append(Message('note_on', channel=1, note=89, velocity=100, time=0))  # A
track.append(Message('note_on', channel=1, note=91, velocity=100, time=0))  # C
track.append(Message('note_on', channel=1, note=92, velocity=100, time=0))  # Eb

# Bar 2: Marcus on bass — walking line in F (root, 5, chromatic)
track.append(Message('note_on', channel=0, note=65, velocity=80, time=0))  # F
track.append(Message('note_on', channel=0, note=69, velocity=80, time=BEAT))  # A
track.append(Message('note_on', channel=0, note=68, velocity=80, time=BEAT))  # Ab (chromatic)
track.append(Message('note_on', channel=0, note=65, velocity=80, time=BEAT))  # F

# Bar 2: Little Ray continues with kick, snare, hihat
track.append(Message('note_on', channel=9, note=36, velocity=100, time=0))  # Kick on 1
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 2
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 3
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 4
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 5
track.append(Message('note_off', channel=9, note=36, velocity=100, time=0))  # Kick off
track.append(Message('note_off', channel=9, note=38, velocity=100, time=0))  # Snare off
track.append(Message('note_off', channel=9, note=42, velocity=90, time=0))  # Hihat off

# Bar 3: Diane on piano (Ab7, Bb7, C7, D7) — open voicings
track.append(Message('note_on', channel=1, note=88, velocity=100, time=0))  # Ab7 (Ab, C, Eb, G)
track.append(Message('note_on', channel=1, note=91, velocity=100, time=0))  # C
track.append(Message('note_on', channel=1, note=92, velocity=100, time=0))  # Eb
track.append(Message('note_on', channel=1, note=95, velocity=100, time=0))  # G

# Bar 3: Marcus on bass — walking line (5, root, chromatic, 3rd)
track.append(Message('note_on', channel=0, note=69, velocity=80, time=0))  # A
track.append(Message('note_on', channel=0, note=65, velocity=80, time=BEAT))  # F
track.append(Message('note_on', channel=0, note=66, velocity=80, time=BEAT))  # F#
track.append(Message('note_on', channel=0, note=67, velocity=80, time=BEAT))  # G

# Bar 3: Little Ray continues
track.append(Message('note_on', channel=9, note=36, velocity=100, time=0))  # Kick on 1
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 2
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 3
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 4
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 5
track.append(Message('note_off', channel=9, note=36, velocity=100, time=0))  # Kick off
track.append(Message('note_off', channel=9, note=38, velocity=100, time=0))  # Snare off
track.append(Message('note_off', channel=9, note=42, velocity=90, time=0))  # Hihat off

# Bar 4: Diane on piano (Bb7, C7, D7, E7)
track.append(Message('note_on', channel=1, note=89, velocity=100, time=0))  # Bb7 (Bb, D, F, Ab)
track.append(Message('note_on', channel=1, note=92, velocity=100, time=0))  # D
track.append(Message('note_on', channel=1, note=94, velocity=100, time=0))  # F
track.append(Message('note_on', channel=1, note=97, velocity=100, time=0))  # Ab

# Bar 4: Marcus on bass — walking line (chromatic, 3, root, 5)
track.append(Message('note_on', channel=0, note=68, velocity=80, time=0))  # Ab
track.append(Message('note_on', channel=0, note=67, velocity=80, time=BEAT))  # G
track.append(Message('note_on', channel=0, note=65, velocity=80, time=BEAT))  # F
track.append(Message('note_on', channel=0, note=69, velocity=80, time=BEAT))  # A

# Bar 4: Little Ray continues
track.append(Message('note_on', channel=9, note=36, velocity=100, time=0))  # Kick on 1
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 2
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 3
track.append(Message('note_on', channel=9, note=38, velocity=100, time=BEAT))  # Snare on 4
track.append(Message('note_on', channel=9, note=42, velocity=90, time=BEAT))  # Hihat on 5
track.append(Message('note_off', channel=9, note=36, velocity=100, time=0))  # Kick off
track.append(Message('note_off', channel=9, note=38, velocity=100, time=0))  # Snare off
track.append(Message('note_off', channel=9, note=42, velocity=90, time=0))  # Hihat off

# Bar 4: Dante on sax — melody (F, G, Bb, C)
track.append(Message('note_on', channel=2, note=F3, velocity=110, time=0))
track.append(Message('note_on', channel=2, note=G, velocity=110, time=BEAT))
track.append(Message('note_on', channel=2, note=Bb, velocity=110, time=BEAT))
track.append(Message('note_on', channel=2, note=C, velocity=110, time=BEAT))

# End of the 4 bars — leave it hanging
track.append(Message('note_off', channel=2, note=F3, velocity=110, time=0))
track.append(Message('note_off', channel=2, note=G, velocity=110, time=0))
track.append(Message('note_off', channel=2, note=Bb, velocity=110, time=0))
track.append(Message('note_off', channel=2, note=C, velocity=110, time=0))

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
