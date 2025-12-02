
import pretty_midi
import numpy as np

# Constants
BPM = 160
BAR_DURATION = 6.0  # 4 bars = 6 seconds
BEAT_DURATION = BAR_DURATION / 4  # 1.5 seconds per bar
NOTE_DURATION = BEAT_DURATION / 4  # 0.375 seconds per quarter note

# Key: F Major
KEY = 'F'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Instrument assignments
# Tenor Sax (You)
tenor_sax = pretty_midi.Instrument(program=64)
pm.instruments.append(tenor_sax)

# Bass (Marcus)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (Diane)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (Little Ray)
drums = pretty_midi.Instrument(program=128)
pm.instruments.append(drums)

# Define note values (F Major scale: F, G, A, Bb, B, C, D)
F_MAJOR_SCALE = [72, 74, 76, 77, 79, 81, 83]  # F4, G4, A4, Bb4, B4, C5, D5

# Map drum notes
# Kick on 1 and 3
KICK = 36
# Snare on 2 and 4
SNARE = 38
# Hihat on every eighth
HIHAT = 42

# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * BEAT_DURATION + beat * NOTE_DURATION
        if beat in [0, 2]:
            # Kick
            note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        if beat in [1, 3]:
            # Snare
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        # Hihat on every eighth
        for eighth in [0, 1]:
            note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + eighth * NOTE_DURATION / 2,
                                    end=time + eighth * NOTE_DURATION / 2 + NOTE_DURATION / 4)
            drums.notes.append(note)

# Bars 2-4: Everyone in

# Tenor sax melody (your motif)
# Start with a descending line: F, Bb, B, A, G
# Then repeat with a slight variation
sax_notes = [
    (72, 0.0),  # F4 at start of bar
    (77, 0.5),  # Bb4 at second beat
    (79, 1.0),  # B4 at third beat
    (76, 1.5),  # A4 at fourth beat
    (74, 2.0),  # G4 at start of next bar
    (77, 2.5),  # Bb4
    (79, 3.0),  # B4
    (76, 3.5)   # A4
]

# Add sax notes to the tenor_sax instrument
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    tenor_sax.notes.append(sax_note)

# Bass line (Marcus): Walking line, chromatic approach
# F -> Gb -> G -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F
bass_notes = [
    (72, 0.0),  # F4
    (73, 0.5),  # Gb4
    (74, 1.0),  # G4
    (76, 1.5),  # A4
    (77, 2.0),  # Bb4
    (79, 2.5),  # B4
    (81, 3.0),  # C5
    (82, 3.5)   # Db5
]

for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=60, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano (Diane): Comp on 2 and 4, 7th chords
# F7 on beat 2
# A7 on beat 4
# F7 = F, A, C, Eb
# A7 = A, C#, E, G
piano_notes = [
    # Bar 2
    (72, 0.5, 85),  # F4
    (82, 0.5, 85),  # Eb4
    (76, 0.5, 85),  # A4
    (81, 0.5, 85),  # C5
    # Bar 3
    (81, 1.5, 85),  # A4
    (84, 1.5, 85),  # C#5
    (86, 1.5, 85),  # E5
    (88, 1.5, 85),  # G5
    # Bar 4
    (72, 2.5, 85),  # F4
    (82, 2.5, 85),  # Eb4
    (76, 2.5, 85),  # A4
    (81, 2.5, 85),  # C5
]

for note, time, vel in piano_notes:
    piano_note = pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Add drum fills for bar 3 (to add energy)
# Snare on beat 3
snare_fill = pretty_midi.Note(velocity=100, pitch=SNARE, start=2.0, end=2.0 + NOTE_DURATION)
drums.notes.append(snare_fill)

# Add a roll on the hihat for the last beat
for i in range(0, int(NOTE_DURATION * 2), 2):
    note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=3.5 + i * 0.125, end=3.5 + i * 0.125 + 0.0625)
    drums.notes.append(note)

# Save the MIDI file
pm.write("wayne_sax_intro.mid")
print("MIDI file saved as 'wayne_sax_intro.mid'")
