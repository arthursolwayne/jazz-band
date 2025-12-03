
import pretty_midi
from pretty_midi import PrettyMIDI, Instrument, Note

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = PrettyMIDI(initial_tempo=tempo, time_signature=(time_signature[0], time_signature[1]))

# Define bar duration (in seconds)
bar_duration = 6.0 / 4  # 6 seconds / 4 bars = 1.5 seconds per bar
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# Define MIDI note numbers
# Dm7: Dm (D - F - Ab - C)
# We'll use Dm7 as the key center, but with unexpected harmonies
Dm7 = [62, 65, 67, 71]  # D - F - Ab - C (MIDI notes)
Dm = [62, 65, 67]       # Dm triad

# Define the chords for each bar
bar_1 = [62, 65, 67, 69]  # Dm7 with a chromatic passing tone
bar_2 = [62, 65, 68, 72]  # Dm7 with flat 9 (Ab -> Bb)
bar_3 = [62, 64, 67, 71]  # Dm7 with a tritone substitution (G7)
bar_4 = [62, 65, 67, 71]  # Resolving to Dm7

# Define the time in seconds for each bar
bar_times = [0.0, 1.5, 3.0, 4.5]

# Create instruments

# Bass (Marcus)
bass = Instrument(program=33)  # Double Bass
pm.instruments.append(bass)

# Piano (Diane)
piano = Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano)

# Drums (Little Ray)
drums = Instrument(program=11)  # Drums
pm.instruments.append(drums)

# Tenor Sax (You)
sax = Instrument(program=64)  # Tenor Saxophone
pm.instruments.append(sax)

#----------------------
# DRUMS (Little Ray)
#----------------------

# Kick on 1 and 3 (beats 1 and 3)
kick_notes = [36, 36]  # MIDI note for kick
kick_times = [0.0, 1.5]  # beat 1 and 3 of bar 1

# Snare on 2 and 4 (beats 2 and 4)
snare_notes = [38, 38]
snare_times = [0.75, 2.25]  # beat 2 and 4 of bar 1

# Hihat on every eighth
hihat_notes = [42] * 8
hihat_times = [i * 0.375 for i in range(8)]

# Add to drum instrument
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(Note(note, time, time + 0.1))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(Note(note, time, time + 0.1))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(Note(note, time, time + 0.05))

#----------------------
# BASS (Marcus)
#----------------------

# Walking bass line in Dm7 (D - F - Ab - C)
# Bar 1: D -> F -> Ab -> C (chromatic approach)
# Bar 2: F -> Ab -> Bb -> D (chromatic passing to D)
# Bar 3: Ab -> Bb -> C -> Eb (tritone substitution)
# Bar 4: Bb -> C -> Eb -> F (resolving back)

bass_notes = [
    62, 65, 67, 71,  # Bar 1
    65, 67, 69, 62,  # Bar 2
    67, 69, 71, 64,  # Bar 3
    69, 71, 64, 65   # Bar 4
]

bass_times = [0.0, 0.375, 0.75, 1.125,  # Bar 1
              1.5, 1.875, 2.25, 2.625,  # Bar 2
              3.0, 3.375, 3.75, 4.125,  # Bar 3
              4.5, 4.875, 5.25, 5.625]  # Bar 4

for note, time in zip(bass_notes, bass_times):
    bass.notes.append(Note(note, time, time + 0.1))

#----------------------
# PIANO (Diane)
#----------------------

# Comp on 2 and 4, open voicings
# Bar 1: Dm7 (D - F - Ab - C)
# Bar 2: Dm7 with Bb (flat 9)
# Bar 3: G7 (tritone substitution)
# Bar 4: Dm7 (resolve)

# Bar 1
piano_notes = [62, 65, 67, 71]
piano_times = [0.75, 0.75, 0.75, 0.75]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(Note(note, time, time + 0.25))

# Bar 2
piano_notes = [62, 65, 68, 72]
piano_times = [2.25, 2.25, 2.25, 2.25]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(Note(note, time, time + 0.25))

# Bar 3
piano_notes = [67, 71, 72, 76]
piano_times = [3.75, 3.75, 3.75, 3.75]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(Note(note, time, time + 0.25))

# Bar 4
piano_notes = [62, 65, 67, 71]
piano_times = [5.25, 5.25, 5.25, 5.25]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(Note(note, time, time + 0.25))

#----------------------
# SAX (You)
#----------------------

# Tenor sax motif: D - Eb - F - F# (then rests)
# Notes: [62, 64, 65, 66]
# Time: 0.0, 0.375, 0.75, 1.125

# Play the first three notes, then rest
sax_notes = [62, 64, 65]
sax_times = [0.0, 0.375, 0.75]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(Note(note, time, time + 0.25))

# Rest for the last note (F#), then return to D on bar 4

# Return on beat 4 of bar 4 (time 5.625)
sax_notes = [62]
sax_times = [5.625]

for note, time in zip(sax_notes, sax_times):
    sax.notes.append(Note(note, time, time + 0.25))

#----------------------
# Write to MIDI file
#----------------------
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been generated.")
