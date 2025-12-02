
import pretty_midi
import numpy as np

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (MIDI notes)
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration in seconds (160 BPM, 4/4 time)
bar_duration = 1.5  # 6 seconds for 4 bars

# -----
# Bar 1 (0.0 - 1.5s): Little Ray on drums only
# Syncopated, energetic, filled with tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define time points for the bar (in seconds)
kick_times = [0.0, 0.75]  # 1 and 3
snare_times = [0.375, 1.125]  # 2 and 4
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]

# Add drum notes
for t in kick_times:
    note = pretty_midi.Note(velocity=int(90 + np.random.uniform(-10, 10)), pitch=KICK, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=int(100 + np.random.uniform(-10, 10)), pitch=SNARE, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=int(85 + np.random.uniform(-10, 10)), pitch=HIHAT, start=t, end=t + 0.0625)
    drums.notes.append(note)

# -----
# Bar 2-4 (1.5 - 6.0s): Full quartet

# 1. Bass: Marcus – walking line in Fm, chromatic approaches, never the same note twice
# 2. Piano: Diane – 7th chords, comping on 2 and 4, emotionally charged
# 3. Sax: Dante – a haunting, simple motif, space and silence

# Time points for bars 2-4 (each bar is 1.5s)
bar_start = 1.5
bar_end = 6.0
bar_duration = 1.5

# Bass line: Walking line in Fm – F, Gb, Ab, A, Bb, B, C, Db, D, Eb, F, Gb, Ab, etc.
# Fm = F, Ab, Bb
# Use chromatic approaches on each beat

bass_notes = [
    (bar_start + 0.0, 64),  # F
    (bar_start + 0.25, 63),  # Gb
    (bar_start + 0.5, 60),  # Ab
    (bar_start + 0.75, 62),  # A
    (bar_start + 1.0, 61),  # Bb
    (bar_start + 1.25, 63),  # B
    (bar_start + 1.5, 64),  # C
    (bar_start + 1.75, 63),  # Db
    (bar_start + 2.0, 62),  # D
    (bar_start + 2.25, 61),  # Eb
    (bar_start + 2.5, 64),  # F
    (bar_start + 2.75, 63),  # Gb
    (bar_start + 3.0, 60),  # Ab
    (bar_start + 3.25, 62),  # A
    (bar_start + 3.5, 61),  # Bb
    (bar_start + 3.75, 63),  # B
    (bar_start + 4.0, 64),  # C
    (bar_start + 4.25, 63),  # Db
    (bar_start + 4.5, 62),  # D
    (bar_start + 4.75, 61),  # Eb
    (bar_start + 5.0, 64),  # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=t, end=t + 0.125)
    bass.notes.append(note)

# Piano: Diane – 7th chords, comp on 2 and 4, emotionally sharp

# Fm7: F, Ab, Bb, C
# Fm7 = 64, 60, 61, 64

# Chord voicings with tension
# Bar 2: Fm7
# Bar 3: Ab7
# Bar 4: Bb7

# Each chord is played on 2 and 4 (0.375 and 1.125 in bar)

chord_piano_notes = []

# Bar 2 (1.5 - 3.0s)
chord_piano_notes.extend([
    (1.5 + 0.375, 64),  # F
    (1.5 + 0.375, 61),  # Bb
    (1.5 + 0.375, 60),  # Ab
    (1.5 + 0.375, 64),  # C
    (1.5 + 1.125, 64),
    (1.5 + 1.125, 61),
    (1.5 + 1.125, 60),
    (1.5 + 1.125, 64),
])

# Bar 3 (3.0 - 4.5s): Ab7
chord_piano_notes.extend([
    (3.0 + 0.375, 69),  # Ab
    (3.0 + 0.375, 71),  # B
    (3.0 + 0.375, 67),  # C
    (3.0 + 0.375, 69),  # Ab
    (3.0 + 1.125, 69),
    (3.0 + 1.125, 71),
    (3.0 + 1.125, 67),
    (3.0 + 1.125, 69),
])

# Bar 4 (4.5 - 6.0s): Bb7
chord_piano_notes.extend([
    (4.5 + 0.375, 62),  # Bb
    (4.5 + 0.375, 64),  # C
    (4.5 + 0.375, 60),  # Ab
    (4.5 + 0.375, 65),  # D
    (4.5 + 1.125, 62),
    (4.5 + 1.125, 64),
    (4.5 + 1.125, 60),
    (4.5 + 1.125, 65),
])

for t, pitch in chord_piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=t, end=t + 0.125)
    piano.notes.append(note)

# Sax: Dante – simple, haunting motif, space and silence

# Motif: F, Ab, Bb, C
# Play on 1, 2, 3, 4 (0.0, 0.375, 0.75, 1.125)
# But leave the last note hanging, then return to finish it

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    (1.5, 64),  # F
    (1.5 + 0.375, 60),  # Ab
    (1.5 + 0.75, 61),  # Bb
    (1.5 + 1.125, 64),  # C (played, but held)
    (1.5 + 1.375, 64),  # C (held)
    (1.5 + 1.625, 64),  # C (held)
    (1.5 + 1.875, 64),  # C (held)
    (1.5 + 2.0, 64),  # C (held)
]

# Bar 3 (3.0 - 4.5s)
# Repeat the motif but finish it
sax_notes.extend([
    (3.0, 64),  # F
    (3.0 + 0.375, 60),  # Ab
    (3.0 + 0.75, 61),  # Bb
    (3.0 + 1.125, 64),  # C
    (3.0 + 1.375, 64),
    (3.0 + 1.625, 64),
    (3.0 + 1.875, 64),
    (3.0 + 2.0, 64),
])

# Bar 4 (4.5 - 6.0s)
# Return to the motif but with a space before it
sax_notes.extend([
    (4.5 + 0.5, 64),  # F
    (4.5 + 0.875, 60),  # Ab
    (4.5 + 1.25, 61),  # Bb
    (4.5 + 1.625, 64),  # C
    (4.5 + 1.875, 64),
    (4.5 + 2.125, 64),
    (4.5 + 2.375, 64),
    (4.5 + 2.625, 64),
])

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.125)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_russo_intro.mid")
