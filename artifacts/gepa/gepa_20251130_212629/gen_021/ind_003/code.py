
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Function to convert beats to seconds
def beat_to_seconds(beats, tempo):
    return beats * 60.0 / tempo

# Define the time of each bar (4/4 time)
BAR_TIME = beat_to_seconds(4, tempo)

# Each bar is 6 seconds
# So each beat is 6 / 4 = 1.5 seconds
BEAT_TIME = 1.5

# Define instrument channels
# 0: Drums (Little Ray)
# 1: Bass (Marcus)
# 2: Piano (Diane)
# 3: Tenor Sax (You)

# Create instrument tracks
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drum_instrument = pretty_midi.Instrument(program=drum_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drum_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(sax_instrument)

# ---------------------------
# BAR 1 - Little Ray on drums (just hihat and kick)
# Kick on 1 and 3
# Hihat on every eighth note

bar1_time = 0.0

# Kick on 1 and 3
for beat in [0, 2]:
    time = bar1_time + beat * BEAT_TIME
    drum_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1))

# Hihat on every eighth
for eighth in range(0, 8):
    time = bar1_time + (eighth * BEAT_TIME) / 2.0
    if eighth % 2 == 0:  # on the downbeats
        drum_instrument.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.05))

# ---------------------------
# BAR 2 - Everyone in. Melody on sax.
# Bar 2 - 4-note motif, start of the melody

bar2_time = bar1_time + BEAT_TIME

# Tenor sax melody - 4-note motif, spaced with rests
sax_notes = [
    (bar2_time + 0.0, 62, 0.5, 90),  # C (F7, Fmaj7)
    (bar2_time + 1.2, 67, 0.3, 80),  # G (F7, Fmaj7)
    (bar2_time + 2.0, 60, 0.2, 95),  # E (F7, Fmaj7)
    (bar2_time + 2.8, 62, 0.2, 90)   # C (F7, Fmaj7)
]

for start, pitch, duration, velocity in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Bass line - walking line, chromatic, no repetition
bass_notes = [
    (bar2_time, 53, 0.25, 70),  # Bb
    (bar2_time + 0.25, 54, 0.25, 75),  # B
    (bar2_time + 0.5, 55, 0.25, 70),  # C
    (bar2_time + 0.75, 53, 0.25, 75),  # Bb
    (bar2_time + 1.0, 52, 0.25, 70),  # A
    (bar2_time + 1.25, 53, 0.25, 75),  # Bb
    (bar2_time + 1.5, 54, 0.25, 70),  # B
    (bar2_time + 1.75, 53, 0.25, 75),  # Bb
    (bar2_time + 2.0, 52, 0.25, 70),  # A
    (bar2_time + 2.25, 53, 0.25, 75),  # Bb
    (bar2_time + 2.5, 54, 0.25, 70),  # B
    (bar2_time + 2.75, 53, 0.25, 75)   # Bb
]

for start, pitch, duration, velocity in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Piano comping on 2 and 4
piano_notes = []

# Bar 2, beat 2 (halfway through the bar)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar2_time + 0.75, end=bar2_time + 1.0))  # F (F7)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=bar2_time + 0.75, end=bar2_time + 1.0))  # C (F7)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar2_time + 0.75, end=bar2_time + 1.0))  # A (F7)

# Bar 2, beat 4
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar2_time + 2.25, end=bar2_time + 2.5))  # F (F7)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=69, start=bar2_time + 2.25, end=bar2_time + 2.5))  # C (F7)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar2_time + 2.25, end=bar2_time + 2.5))  # A (F7)

for note in piano_notes:
    piano_instrument.notes.append(note)

# ---------------------------
# BAR 3 - Continue melody with subtle variation
bar3_time = bar2_time + BEAT_TIME

# Tenor sax: repeat motif with slight variation in timing and note
sax_notes_bar3 = [
    (bar3_time + 0.0, 62, 0.4, 90),  # C (F7)
    (bar3_time + 1.2, 67, 0.3, 80),  # G (F7)
    (bar3_time + 2.0, 60, 0.2, 95),  # E (F7)
    (bar3_time + 2.8, 62, 0.2, 90)   # C (F7)
]

for start, pitch, duration, velocity in sax_notes_bar3:
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Bass line: continue walking line with more chromatic movement
bass_notes_bar3 = [
    (bar3_time, 53, 0.25, 70),    # Bb
    (bar3_time + 0.25, 54, 0.25, 75),  # B
    (bar3_time + 0.5, 55, 0.25, 70),  # C
    (bar3_time + 0.75, 53, 0.25, 75),  # Bb
    (bar3_time + 1.0, 52, 0.25, 70),  # A
    (bar3_time + 1.25, 53, 0.25, 75),  # Bb
    (bar3_time + 1.5, 54, 0.25, 70),  # B
    (bar3_time + 1.75, 53, 0.25, 75),  # Bb
    (bar3_time + 2.0, 52, 0.25, 70),  # A
    (bar3_time + 2.25, 53, 0.25, 75),  # Bb
    (bar3_time + 2.5, 54, 0.25, 70),  # B
    (bar3_time + 2.75, 53, 0.25, 75)   # Bb
]

for start, pitch, duration, velocity in bass_notes_bar3:
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Piano: comp on 2 and 4 again, but with more dissonance this time
piano_notes_bar3 = []

# Bar 3, beat 2
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=64, start=bar3_time + 0.75, end=bar3_time + 1.0))  # F
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=69, start=bar3_time + 0.75, end=bar3_time + 1.0))  # C
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=67, start=bar3_time + 0.75, end=bar3_time + 1.0))  # A

# Bar 3, beat 4
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=62, start=bar3_time + 2.25, end=bar3_time + 2.5))  # E
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=64, start=bar3_time + 2.25, end=bar3_time + 2.5))  # F
piano_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=69, start=bar3_time + 2.25, end=bar3_time + 2.5))  # C

for note in piano_notes_bar3:
    piano_instrument.notes.append(note)

# ---------------------------
# BAR 4 - End with question on sax, no resolution
bar4_time = bar3_time + BEAT_TIME

# Tenor sax: end with a question, no resolution
sax_notes_bar4 = [
    (bar4_time + 0.0, 62, 0.4, 90),  # C (F7)
    (bar4_time + 1.2, 67, 0.3, 80),  # G (F7)
    (bar4_time + 2.0, 60, 0.2, 95),  # E (F7)
    (bar4_time + 2.8, 62, 0.2, 90)   # C (F7)
]

for start, pitch, duration, velocity in sax_notes_bar4:
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Bass line: continue walking line
bass_notes_bar4 = [
    (bar4_time, 53, 0.25, 70),    # Bb
    (bar4_time + 0.25, 54, 0.25, 75),  # B
    (bar4_time + 0.5, 55, 0.25, 70),  # C
    (bar4_time + 0.75, 53, 0.25, 75),  # Bb
    (bar4_time + 1.0, 52, 0.25, 70),  # A
    (bar4_time + 1.25, 53, 0.25, 75),  # Bb
    (bar4_time + 1.5, 54, 0.25, 70),  # B
    (bar4_time + 1.75, 53, 0.25, 75),  # Bb
    (bar4_time + 2.0, 52, 0.25, 70),  # A
    (bar4_time + 2.25, 53, 0.25, 75),  # Bb
    (bar4_time + 2.5, 54, 0.25, 70),  # B
    (bar4_time + 2.75, 53, 0.25, 75)   # Bb
]

for start, pitch, duration, velocity in bass_notes_bar4:
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Piano: comp on 2 and 4 again, but with a slight dissonance
piano_notes_bar4 = []

# Bar 4, beat 2
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=64, start=bar4_time + 0.75, end=bar4_time + 1.0))  # F
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=69, start=bar4_time + 0.75, end=bar4_time + 1.0))  # C
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=67, start=bar4_time + 0.75, end=bar4_time + 1.0))  # A

# Bar 4, beat 4
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=62, start=bar4_time + 2.25, end=bar4_time + 2.5))  # E
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=64, start=bar4_time + 2.25, end=bar4_time + 2.5))  # F
piano_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=69, start=bar4_time + 2.25, end=bar4_time + 2.5))  # C

for note in piano_notes_bar4:
    piano_instrument.notes.append(note)

# ---------------------------
# Save the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file written as 'jazz_intro.mid'")
