
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time signature and bar length
bar_length = 1.5  # 60 / 160 * 4 = 1.5 seconds per bar
total_time = 6.0  # 4 bars

# BAR 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375  # 0.375s per beat
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.375))
    if i in [0, 2]:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.375))
    if i in [1, 3]:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.375))

# BAR 2: Full band (1.5 - 3.0s)
# BASS LINE: Walking line in D minor with chromatic approaches
# Notes: D - Eb - E - F - G - A - Bb - B - C - D (chromatic up to C, then back)
bass_notes = [
    (1.5, 2, 100), (1.75, 3, 100), (2.0, 4, 100),
    (2.25, 5, 100), (2.5, 7, 100), (2.75, 9, 100),
    (3.0, 10, 100), (3.25, 11, 100), (3.5, 12, 100),
    (3.75, 2, 100)
]

for start, pitch, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# PIANO: 7th chords on 2 and 4, comping
# D7 = D F# A C
# G7 = G B D F
# Bm7b5 = B D F# A
# F#7 = F# A C E
piano_notes = [
    (1.5, 2, 100), (1.5, 4, 100), (1.5, 7, 100), (1.5, 9, 100),  # D7 on 1
    (1.75, 2, 100), (1.75, 4, 100), (1.75, 7, 100), (1.75, 9, 100),  # D7 on 2
    (2.0, 5, 100), (2.0, 7, 100), (2.0, 9, 100), (2.0, 11, 100),  # G7 on 3
    (2.25, 5, 100), (2.25, 7, 100), (2.25, 9, 100), (2.25, 11, 100),  # G7 on 4
    (2.5, 2, 100), (2.5, 4, 100), (2.5, 7, 100), (2.5, 9, 100),  # D7 on 5
    (2.75, 2, 100), (2.75, 4, 100), (2.75, 7, 100), (2.75, 9, 100),  # D7 on 6
    (3.0, 5, 100), (3.0, 7, 100), (3.0, 9, 100), (3.0, 11, 100),  # G7 on 7
    (3.25, 5, 100), (3.25, 7, 100), (3.25, 9, 100), (3.25, 11, 100),  # G7 on 8
]

for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# SAX: Motif - D F# B D (1.5 - 1.75s) then leave it hanging (1.75 - 2.0s)
# Then repeat and resolve (2.0 - 3.0s)
sax_notes = [
    (1.5, 2, 100), (1.5, 4, 100), (1.5, 7, 100), (1.5, 2, 100),
    (2.0, 2, 100), (2.0, 4, 100), (2.0, 7, 100), (2.0, 2, 100),
    (2.5, 2, 100), (2.5, 4, 100), (2.5, 7, 100), (2.5, 2, 100)
]

for start, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_russo_intro.mid")
