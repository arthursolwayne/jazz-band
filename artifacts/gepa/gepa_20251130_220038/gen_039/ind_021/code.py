
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define key
key = 'F major'

# Define the four bars (each bar is 1.5 seconds at 160 BPM)
bar_duration = 1.5
total_duration = bar_duration * 4

# Instruments
# -------------------------------
# 1. Drums (Little Ray)
# 2. Bass (Marcus)
# 3. Piano (Diane)
# 4. Tenor Sax (Dante)

# -------------------------------
# 1. Drums - Little Ray
drums = pretty_midi.Instrument(program=0)
pm.instruments.append(drums)

# Kick on 1 and 3
for bar in range(4):
    kick_time = bar * bar_duration + 0.0
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05))
    kick_time = bar * bar_duration + 0.75
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.05))

# Snare on 2 and 4
for bar in range(4):
    snare_time = bar * bar_duration + 0.5
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.05))
    snare_time = bar * bar_duration + 1.25
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.05))

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(0, 8):
        hi_hat_time = bar * bar_duration + i * 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hi_hat_time, end=hi_hat_time + 0.025))

# -------------------------------
# 2. Bass - Marcus
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Walking bass line in F major
# F -> G -> A -> Bb -> C -> D -> E -> F
# Bar 1
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=0.0, end=0.375))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=0.375, end=0.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=0.75, end=1.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.125, end=1.5))  # G

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0))  # D

# Bar 3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5))  # G

# Bar 4
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0))  # G

# -------------------------------
# 3. Piano - Diane
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Diane plays 7th chords on 2 and 4
# Bar 1: Rest
# Bar 2: F7 (F, A, C, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + 0.25))

# Bar 3: C7 (C, E, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.0 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.0 + 0.25))

# Bar 4: F7 again
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.5 + 0.25))

# -------------------------------
# 4. Tenor Sax - Dante
sax = pretty_midi.Instrument(program=64)
pm.instruments.append(sax)

# Tenor sax motif: F -> G -> A -> G -> F
# Start at bar 2, after the setup

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5))  # G

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0))  # G

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))  # G

# Save the MIDI file
pm.write("dante_intro.mid")
