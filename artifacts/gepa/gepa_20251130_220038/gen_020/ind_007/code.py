
from midiutil import MIDIFile

# Initialize MIDI file
mid = MIDIFile(1)
track = 0
time = 0
tempo = 160  # BPM
mid.addTempo(track, time, tempo)

# Define instruments
# 0: Drums
# 1: Bass
# 2: Piano
# 3: Saxophone

# BAR 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
# We'll use MIDI note numbers for drums
# 35: Kick, 38: Snare, 42: Hi-hat

# Bar 1: 0.0 to 1.5 seconds
# Eighth note = 0.375 seconds
# Time = 0.0

# Kick on 1 and 3
mid.addNote(track, 0, 35, 0.0, 0.375, 100)
mid.addNote(track, 0, 35, 1.125, 0.375, 100)

# Snare on 2 and 4
mid.addNote(track, 0, 38, 0.75, 0.375, 100)
mid.addNote(track, 0, 38, 1.5, 0.375, 100)

# Hi-hat on every eighth
for i in range(0, 8):
    mid.addNote(track, 0, 42, i * 0.375, 0.125, 100)

# BAR 2: Everyone in. Diane on piano, Marcus on bass, you on sax

# Diane (Piano) - 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# We'll play a Dm7 chord on beat 2 and 4

# Bar 2: Time = 1.5 to 3.0
# Beat 2 = 1.5 + 0.75 = 2.25
# Beat 4 = 1.5 + 1.5 = 3.0

# Dm7 chord at beat 2
d7_notes = [D, F, A, C]  # MIDI note numbers for D, F, A, C
d = 62  # D4
f = 64  # F4
a = 67  # A4
c = 60  # C4

# Diane plays the chord for 1 beat (0.75s)
mid.addNote(track, 2, d, 2.25, 0.75, 100)
mid.addNote(track, 2, f, 2.25, 0.75, 100)
mid.addNote(track, 2, a, 2.25, 0.75, 100)
mid.addNote(track, 2, c, 2.25, 0.75, 100)

# Diane plays Dm7 again on beat 4
mid.addNote(track, 2, d, 3.0, 0.75, 100)
mid.addNote(track, 2, f, 3.0, 0.75, 100)
mid.addNote(track, 2, a, 3.0, 0.75, 100)
mid.addNote(track, 2, c, 3.0, 0.75, 100)

# Marcus on bass - walking line, chromatic, forward motion

# Dm7 walking line in D minor: D, C, Bb, B, A, G, F, E, D, C, B, Bb, A, G, F, E

# Bar 2: Dm7 root motion
# Time = 1.5
# 8th note = 0.375s

bass_notes = [
    d,  # D (1.5)
    c,  # C (1.875)
    61,  # Bb (2.25)
    62,  # B (2.625)
    a,  # A (3.0)
]

for i, note in enumerate(bass_notes):
    mid.addNote(track, 1, note, 1.5 + i * 0.375, 0.375, 100)

# BAR 3: You on saxophone - haunted melody, simple, with rests

# Start at 3.0 (Bar 3 start)
# First note: D (62) at 3.0 for 0.375s
mid.addNote(track, 3, d, 3.0, 0.375, 100)

# Rest for 0.375s (3.375 to 3.75)
# Then F (64) at 3.75 for 0.375s
mid.addNote(track, 3, 64, 3.75, 0.375, 100)

# Rest for 0.375s (4.125 to 4.5)
# Then A (67) at 4.5 for 0.375s
mid.addNote(track, 3, 67, 4.5, 0.375, 100)

# BAR 4: Continue the sax melody with resolution

# Rest for 0.375s (4.875 to 5.25)
# Then C (60) at 5.25 for 0.375s
mid.addNote(track, 3, 60, 5.25, 0.375, 100)

# BAR 4: Drums again
# Same pattern as bar 1
# Time = 3.0 to 4.5

# Kick on 1 and 3 (3.0 and 4.125)
mid.addNote(track, 0, 35, 3.0, 0.375, 100)
mid.addNote(track, 0, 35, 4.125, 0.375, 100)

# Snare on 2 and 4 (3.75 and 4.5)
mid.addNote(track, 0, 38, 3.75, 0.375, 100)
mid.addNote(track, 0, 38, 4.5, 0.375, 100)

# Hi-hat on every eighth
for i in range(0, 8):
    mid.addNote(track, 0, 42, 3.0 + i * 0.375, 0.125, 100)

# End the file
with open("dante_intro.mid", "wb") as output_file:
    mid.writeFile(output_file)
