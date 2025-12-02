
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with tempo 160 BPM (which is 160 beats per minute)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time per beat in seconds (60 / 160 = 0.375)
beat_time = 0.375
bar_time = 4 * beat_time  # 1.5 seconds per bar
total_time = 4 * bar_time  # 6 seconds total

# Key: F major
key = 'F'

# Define the instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # for percussion
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drums_instrument = pretty_midi.Instrument(program=drums_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)
pm.instruments.append(sax_instrument)

# ----------------------------
# Bar 1: Little Ray (Drums) – Set the scene with tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# But with subtle timing shifts and dynamic variation

# Hihat on every eighth (16 notes in 4/4 time)
for i in range(0, 16):
    time = i * beat_time / 4  # 0.09375s per eighth note
    if i % 2 == 0:
        velocity = 40  # soft hihat
    else:
        velocity = 50  # slightly louder
    note = pretty_midi.Note(velocity=velocity, pitch=pretty_midi.note_name_to_number('C#5'), start=time, end=time + 0.05)
    drums_instrument.notes.append(note)

# Kick on 1 and 3 (beat 0 and 2)
for i in [0, 2]:
    time = i * beat_time
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('C2'), start=time, end=time + 0.1)
    drums_instrument.notes.append(note)

# Snare on 2 and 4 (beat 1 and 3)
for i in [1, 3]:
    time = i * beat_time
    note = pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('G3'), start=time, end=time + 0.08)
    drums_instrument.notes.append(note)

# ----------------------------
# Bars 2-4: Full ensemble – You on saxophone, with piano, bass, drums

# Define saxophone motif – short, melodic, ends with a question
sax_notes = [
    (0.0, 'G4', 100),     # Start on G4, strong
    (0.375, 'A4', 100),   # Move to A4 on beat 2
    (0.75, 'Bb4', 100),   # Bb4 on beat 3
    (1.125, 'Bb4', 80),   # Sustain Bb4 with decaying volume
    (1.5, 'Bb4', 60),     # End on Bb4, soft and hanging
]

for time, note_name, velocity in sax_notes:
    pitch = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.05)
    sax_instrument.notes.append(note)

# Bass – walking line, chromatic approach
# F major scale: F, G, A, Bb, B, C, D, E
# Walking bass line: F, G, A, Bb, B, C, D, E, F, G, A, Bb, B, C, D, E
# But with chromatic approaches
bass_line = [
    ('F2', 0.0, 80),       # F on beat 0
    ('G2', 0.375, 80),     # G on beat 1
    ('A2', 0.75, 80),      # A on beat 2
    ('Bb2', 1.125, 80),    # Bb on beat 3
    ('B2', 1.5, 80),       # B on beat 0 (bar 2)
    ('C2', 1.875, 80),     # C on beat 1
    ('D2', 2.25, 80),      # D on beat 2
    ('E2', 2.625, 80),     # E on beat 3
    ('F2', 3.0, 80),       # F on beat 0 (bar 3)
    ('G2', 3.375, 80),     # G on beat 1
    ('A2', 3.75, 80),      # A on beat 2
    ('Bb2', 4.125, 80),    # Bb on beat 3
    ('B2', 4.5, 80),       # B on beat 0 (bar 4)
    ('C2', 4.875, 80),     # C on beat 1
    ('D2', 5.25, 80),      # D on beat 2
    ('E2', 5.625, 80),     # E on beat 3
]

for note_name, time, velocity in bass_line:
    pitch = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.05)
    bass_instrument.notes.append(note)

# Piano – 7th chords, comp on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
# Play on beats 2 and 4 only

# Bar 2: F7 on beat 1 (time 1.5)
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (1.5, 'F4', 80),
    (1.5, 'A4', 80),
    (1.5, 'C5', 80),
    (1.5, 'Eb4', 80),
    
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 'Bb4', 80),
    (3.0, 'D4', 80),
    (3.0, 'F4', 80),
    (3.0, 'Ab4', 80),
    
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    (4.5, 'Eb4', 80),
    (4.5, 'G4', 80),
    (4.5, 'Bb4', 80),
    (4.5, 'Db4', 80),
]

for time, note_name, velocity in piano_notes:
    pitch = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.1)
    piano_instrument.notes.append(note)

# ----------------------------
# Output MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been generated.")
