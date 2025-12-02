
from midiutil import MIDIFile
import numpy as np

# Initialize MIDI file
midi = MIDIFile(1)
track = 0
time = 0
midi.addTempo(track, time, 160)

# Key: F minor
# Notes in F minor: F, Gb, Ab, Bb, B, Db, Eb

# Define instruments (MIDI channel 0 is default for all)
# Tenor Sax (MIDI 64), Bass (MIDI 33), Piano (MIDI 0), Drums (MIDI 9)

# TIME: 160 BPM, 4/4 time. 4 bars = 6.0 seconds. Beat = 0.375s, Bar = 1.5s.

# BAR 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time in beats: 0 - 1.5s

# Kick (MIDI 36)
midi.addNote(track, 9, 0, 0, 0.375, 36)
midi.addNote(track, 9, 0, 1.125, 0.375, 36)

# Snare (MIDI 38)
midi.addNote(track, 9, 0, 0.75, 0.375, 38)
midi.addNote(track, 9, 0, 1.5, 0.375, 38)

# Hihat (MIDI 42)
for i in range(0, 2):
    for j in range(0, 4):
        midi.addNote(track, 9, 0, i*1.5 + j*0.375, 0.1875, 42)

# BAR 2: Diane on piano (open voicing, different chord each bar)
# Chord: Ab7 (Ab, C, Eb, Gb)
# Play on beat 2 and 4
# Time: 1.5 - 3.0s

# Ab7 (MIDI 57, 60, 64, 62)
# Beat 2 (time = 1.5)
midi.addNote(track, 0, 1.5, 1.5, 0.1875, 57)
midi.addNote(track, 0, 1.5, 1.5, 0.1875, 60)
midi.addNote(track, 0, 1.5, 1.5, 0.1875, 64)
midi.addNote(track, 0, 1.5, 1.5, 0.1875, 62)

# Beat 4 (time = 3.0)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 57)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 60)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 64)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 62)

# BAR 2: Marcus on bass (walking line, roots and fifths with chromatic approaches)
# Fm root (MIDI 53), Bb (MIDI 58), Ab (MIDI 60), Eb (MIDI 62), Db (MIDI 61), Gb (MIDI 62)
# Roots and fifths: F, C, Ab, Eb, Bb, F, etc.
# Time: 1.5 - 3.0s

# Walking line: F (53), C (58), Ab (60), Eb (62), Bb (58), F (53)
# Each note held for 0.375 seconds

# F (beat 2)
midi.addNote(track, 33, 1.5, 1.5, 0.375, 53)

# C (beat 3)
midi.addNote(track, 33, 2.25, 0.375, 58)

# Ab (beat 4)
midi.addNote(track, 33, 3.0, 0.375, 60)

# Bb (beat 4, chromatic approach)
midi.addNote(track, 33, 3.0, 0.375, 58)

# BAR 3: Diane on piano (next chord: Bb7)
# Bb7 (Bb, D, F, Ab)
# Play on beat 2 and 4
# Time: 3.0 - 4.5s

# Bb7 on beat 2 (time = 3.0)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 58)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 62)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 53)
midi.addNote(track, 0, 3.0, 3.0, 0.1875, 60)

# Bb7 on beat 4 (time = 4.5)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 58)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 62)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 53)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 60)

# BAR 3: Marcus on bass (walking line)
# B (MIDI 62), F (MIDI 53), Eb (MIDI 62), Ab (MIDI 60), Db (MIDI 61), Bb (MIDI 58)
# Roots and fifths: B, F, Eb, Ab, Db, Bb

# B (beat 2)
midi.addNote(track, 33, 3.0, 3.0, 0.375, 62)

# F (beat 3)
midi.addNote(track, 33, 3.75, 0.375, 53)

# Eb (beat 4)
midi.addNote(track, 33, 4.5, 0.375, 62)

# Ab (beat 4, chromatic approach)
midi.addNote(track, 33, 4.5, 0.375, 60)

# BAR 4: Diane on piano (next chord: Eb7)
# Eb7 (Eb, G, Bb, Db)
# Play on beat 2 and 4
# Time: 4.5 - 6.0s

# Eb7 on beat 2 (time = 4.5)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 62)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 67)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 58)
midi.addNote(track, 0, 4.5, 4.5, 0.1875, 61)

# Eb7 on beat 4 (time = 6.0)
midi.addNote(track, 0, 6.0, 6.0, 0.1875, 62)
midi.addNote(track, 0, 6.0, 6.0, 0.1875, 67)
midi.addNote(track, 0, 6.0, 6.0, 0.1875, 58)
midi.addNote(track, 0, 6.0, 6.0, 0.1875, 61)

# BAR 4: Marcus on bass (walking line)
# Eb (MIDI 62), Ab (MIDI 60), Gb (MIDI 62), Bb (MIDI 58), Db (MIDI 61), F (MIDI 53)
# Roots and fifths: Eb, Ab, Gb, Bb, Db, F

# Eb (beat 2)
midi.addNote(track, 33, 4.5, 4.5, 0.375, 62)

# Ab (beat 3)
midi.addNote(track, 33, 5.25, 0.375, 60)

# Gb (beat 4)
midi.addNote(track, 33, 6.0, 0.375, 62)

# Bb (beat 4, chromatic approach)
midi.addNote(track, 33, 6.0, 0.375, 58)

# BAR 4: You on tenor sax (motif)
# Start on beat 2, leave it hanging, come back on beat 4
# Motif: F (MIDI 53), Gb (MIDI 62), Bb (MIDI 58), leave out the last note — make it a question

# F (beat 2)
midi.addNote(track, 64, 3.0, 3.0, 0.375, 53)

# Gb (beat 3)
midi.addNote(track, 64, 3.75, 0.375, 62)

# Bb (beat 4)
midi.addNote(track, 64, 4.5, 0.375, 58)

# Leave the last note out — it's the question.

# Save the MIDI file
with open("dante_intro.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file generated: 'dante_intro.mid'")
