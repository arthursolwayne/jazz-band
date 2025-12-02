
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define a function to convert beats to seconds
def beat_to_time(beat):
    return beat * (60 / 160)

# ---------------------------
# 1. Little Ray (Drums) - Bar 1
# ---------------------------

# Create an instrument for drums
drum_program = pretty_midi.Instrument(program=program_numbers['drums'])
pm.instruments.append(drum_program)

# Bar 1: Kick on 1 & 3, snare on 2 & 4, hihat every 8th
for beat in range(4):
    time = beat_to_time(beat)
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        drum_program.notes.append(Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        drum_program.notes.append(Note(velocity=110, pitch=38, start=time, end=time + 0.375))
    # Hi-hat on every 8th
    for i in range(2):
        hihat_time = time + (i * 0.1875)
        drum_program.notes.append(Note(velocity=95, pitch=42, start=hihat_time, end=hihat_time + 0.1875))

# ---------------------------
# 2. Marcus (Bass) - Bars 1–4
# ---------------------------

# Bass line in F major, walking, chromatic approaches
bass_program = Instrument(program=Program(33))  # Acoustic Bass
pm.instruments.append(bass_program)

# Walking bass line in F major
bass_notes = [
    (beat_to_time(0), 53),  # F
    (beat_to_time(0.25), 52),  # E
    (beat_to_time(0.5), 53),  # F
    (beat_to_time(0.75), 55),  # G
    (beat_to_time(1), 57),    # A
    (beat_to_time(1.25), 55),  # G
    (beat_to_time(1.5), 53),  # F
    (beat_to_time(1.75), 52),  # E
    (beat_to_time(2), 53),    # F
    (beat_to_time(2.25), 52),  # E
    (beat_to_time(2.5), 53),  # F
    (beat_to_time(2.75), 55),  # G
    (beat_to_time(3), 57),    # A
    (beat_to_time(3.25), 55),  # G
    (beat_to_time(3.5), 53),  # F
    (beat_to_time(3.75), 52),  # E
]

for time, pitch in bass_notes:
    bass_program.notes.append(Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# ---------------------------
# 3. Diane (Piano) - Bars 2–4
# ---------------------------

# Piano line with 7th chords on 2 and 4
piano_program = Instrument(program=Program(0))  # Acoustic Grand Piano
pm.instruments.append(piano_program)

# F7 on beat 2
note_times = [beat_to_time(1), beat_to_time(2), beat_to_time(3)]
for time in note_times:
    chord = [65, 69, 72, 76]  # F7 (F, A, C, E)
    for pitch in chord:
        piano_program.notes.append(Note(velocity=100, pitch=pitch, start=time, end=time + 0.375))

# ---------------------------
# 4. You (Tenor Sax) - Bars 2–4
# ---------------------------

# Tenor sax line: a short, melodic motif that lingers and resolves
sax_program = Instrument(program=Program(69))  # Tenor Saxophone
pm.instruments.append(sax_program)

# Tenor sax motif (F, G, A, F — with space, tension, and resolution)
melody_notes = [
    (beat_to_time(1), 66),  # G
    (beat_to_time(1.5), 68),  # A
    (beat_to_time(2), 65),   # F
    (beat_to_time(2.25), 67), # G
    (beat_to_time(2.5), 68),  # A
    (beat_to_time(2.75), 65), # F
]

for time, pitch in melody_notes:
    sax_program.notes.append(Note(velocity=105, pitch=pitch, start=time, end=time + 0.25))

# ---------------------------
# Save the MIDI
# ---------------------------

pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
