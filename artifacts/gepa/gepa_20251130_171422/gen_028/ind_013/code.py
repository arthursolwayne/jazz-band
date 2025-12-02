
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the tempo in BPM
tempo = 160
tick_per_beat = pm.get_tick_from_time(1.0 / tempo)  # 1 beat = 1.0 / tempo seconds

# Define F major scale
F_major = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F#

# Define instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments = [bass, piano, drums, sax]

# Define bar length in ticks (each bar is 4 beats at 160 BPM)
bar_ticks = 4 * tick_per_beat

# ===============================
# BAR 1: Little Ray (Drums) - Establish the mood with a sparse, mysterious fill
# ===============================

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.5, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.75))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.0, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.25))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=i * 0.25, end=i * 0.25 + 0.125))

# ===============================
# BAR 2-4: Full ensemble
# ===============================

# BAR 2: Marcus (Bass) - Walking line with chromatic approaches
bass_notes = [
    (65, 0.0, 0.25),   # F (beat 1)
    (67, 0.25, 0.5),   # G
    (70, 0.5, 0.75),   # Bb (chromatic approach)
    (69, 0.75, 1.0),   # A
    (72, 1.0, 1.25),   # C
    (74, 1.25, 1.5),   # D
    (76, 1.5, 1.75),   # E
    (77, 1.75, 2.0),   # F#
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Diane (Piano) - 7th chords on 2 and 4, sparse comping
piano_notes = [
    # Bar 2: F7 on beat 2
    (65, 1.0, 1.25),  # F
    (69, 1.0, 1.25),  # A
    (72, 1.0, 1.25),  # C
    (76, 1.0, 1.25),  # E
    (77, 1.0, 1.25),  # F# (7th)
    # Bar 3: Bb7 on beat 4
    (70, 3.0, 3.25),  # Bb
    (72, 3.0, 3.25),  # C
    (74, 3.0, 3.25),  # D
    (77, 3.0, 3.25),  # F#
    (76, 3.0, 3.25),  # E (7th, enharmonic)
    # Bar 4: C7 on beat 2
    (72, 5.0, 5.25),  # C
    (74, 5.0, 5.25),  # D
    (76, 5.0, 5.25),  # E
    (79, 5.0, 5.25),  # G
    (81, 5.0, 5.25),  # B
    (83, 5.0, 5.25),  # D (7th)
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Little Ray (Drums) - Full kit
for i in range(8):
    # Kick on 1 and 3 (same as before)
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.25, end=i * 0.25 + 0.25))
    # Snare on 2 and 4
    elif i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i * 0.25, end=i * 0.25 + 0.25))
    # Hi-hat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=i * 0.25, end=i * 0.25 + 0.125))

# Dante (Tenor Sax) - The melody: sparse, haunting, expressive
sax_notes = [
    (72, 0.0, 0.5),   # C on beat 1 (bar 2)
    (74, 0.5, 1.0),   # D on beat 2
    (76, 1.0, 1.5),   # E on beat 3
    (80, 1.5, 2.0),   # G on beat 4 (bar 2)

    (74, 2.0, 2.5),   # D on beat 1 (bar 3)
    (76, 2.5, 3.0),   # E on beat 2
    (70, 3.0, 3.5),   # Bb on beat 3
    (72, 3.5, 4.0),   # C on beat 4 (bar 3)

    (72, 4.0, 4.5),   # C on beat 1 (bar 4)
    (74, 4.5, 5.0),   # D on beat 2
    (76, 5.0, 5.5),   # E on beat 3
    (77, 5.5, 6.0),   # F# on beat 4 (bar 4, hanging note)
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Save the MIDI file
pm.write('whispers_before_the_storm.mid')

print("MIDI file 'whispers_before_the_storm.mid' has been created.")
