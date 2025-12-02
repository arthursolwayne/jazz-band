
import pretty_midi
import numpy as np
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define tempo and time divisions
tempo = 160  # BPM
time_signature = (4, 4)
time_per_beat = 60.0 / tempo  # seconds per beat

# Create a new instrument for each player
sax_instrument = Instrument(program=64)  # Tenor sax
bass_instrument = Instrument(program=33)  # Double bass
piano_instrument = Instrument(program=0)  # Acoustic piano
drum_instrument = Instrument(program=0)   # Drums

pm.instruments.append(sax_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)

# Helper function to add a note
def add_note(instrument, pitch, start, duration, velocity=100):
    note = Note(pitch=pitch, start=start, end=start + duration, velocity=velocity)
    instrument.notes.append(note)

# == BAR 1: DRUMS ONLY - TENSION AND ANTICIPATION ==
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add subtle rhythmic displacement for tension

# Set bar duration
bar_duration = 4 * time_per_beat  # 4 beats per bar

# Bar 1 = 0.0 to bar_duration (6.0 seconds)

# Kick on 1 and 3, but slightly displaced
kick1 = 0.0 + 0.05  # displaced
kick2 = 2.0 + 0.05
add_note(drum_instrument, 36, kick1, 0.1, velocity=100)
add_note(drum_instrument, 36, kick2, 0.1, velocity=100)

# Snare on 2 and 4, displaced back slightly
snare1 = 1.0 - 0.05
snare2 = 3.0 - 0.05
add_note(drum_instrument, 38, snare1, 0.08, velocity=100)
add_note(drum_instrument, 38, snare2, 0.08, velocity=100)

# Hihat on every eighth, but with some variation
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for t in hihat_times:
    add_note(drum_instrument, 42, t, 0.05, velocity=80)

# == BAR 2–4: SAX, PIANO, BASS - A QUESTION IN Fm ==
# Bar 2: Start of sax melody
# Bar 3: Continue the phrase
# Bar 4: End with a question, not a resolution

# Fm scale: F, Gb, Ab, Bb, B, Db, Eb, F

# Saxophone melody (Bar 2–4, 12 beats total, 3 bars)
# Phrase starts with a triplet feel, ends with a suspension

start_time = bar_duration

# Saxophone: Motif starts on beat 1 of bar 2
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb

melody = [
    # Bar 2
    Note(71, start_time, start_time + 0.3, 100),  # F (71)
    Note(70, start_time + 0.3, start_time + 0.6, 100),  # Gb
    Note(68, start_time + 0.6, start_time + 0.9, 100),  # Ab
    Note(67, start_time + 0.9, start_time + 1.2, 100),  # Bb

    # Bar 3
    Note(69, start_time + 1.2, start_time + 1.5, 100),  # B
    Note(66, start_time + 1.5, start_time + 1.8, 100),  # Db
    Note(64, start_time + 1.8, start_time + 2.2, 100),  # Eb
    Note(64, start_time + 2.2, start_time + 2.6, 100),  # Eb (sustained)

    # Bar 4
    Note(71, start_time + 2.6, start_time + 3.0, 100),  # F
    Note(69, start_time + 3.0, start_time + 3.3, 100),  # B
    Note(67, start_time + 3.3, start_time + 3.7, 100),  # Bb
    Note(68, start_time + 3.7, start_time + 4.1, 100),  # Ab (suspension, not resolved)
]

for note in melody:
    sax_instrument.notes.append(note)

# Bass: Walking line with chromatic approaches
# Starting from F (71)
bass_walk = [
    # Bar 2
    Note(48, start_time, start_time + 0.25, 80),  # F
    Note(49, start_time + 0.25, start_time + 0.5, 80),  # F#
    Note(50, start_time + 0.5, start_time + 0.75, 80),  # G
    Note(51, start_time + 0.75, start_time + 1.0, 80),  # G#

    # Bar 3
    Note(52, start_time + 1.0, start_time + 1.25, 80),  # A
    Note(53, start_time + 1.25, start_time + 1.5, 80),  # A#
    Note(54, start_time + 1.5, start_time + 1.75, 80),  # B
    Note(55, start_time + 1.75, start_time + 2.0, 80),  # B#

    # Bar 4
    Note(56, start_time + 2.0, start_time + 2.25, 80),  # C
    Note(57, start_time + 2.25, start_time + 2.5, 80),  # C#
    Note(58, start_time + 2.5, start_time + 2.75, 80),  # D
    Note(59, start_time + 2.75, start_time + 3.0, 80),  # D#
]

for note in bass_walk:
    bass_instrument.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab
# F7 again

piano_comp = [
    # Bar 2 - comp on beat 2
    Note(71, start_time + 0.75, start_time + 0.85, 90),  # F
    Note(74, start_time + 0.75, start_time + 0.85, 90),  # A
    Note(72, start_time + 0.75, start_time + 0.85, 90),  # C
    Note(68, start_time + 0.75, start_time + 0.85, 90),  # Eb

    # Bar 3 - comp on beat 2
    Note(67, start_time + 1.75, start_time + 1.85, 90),  # Bb
    Note(69, start_time + 1.75, start_time + 1.85, 90),  # D
    Note(71, start_time + 1.75, start_time + 1.85, 90),  # F
    Note(68, start_time + 1.75, start_time + 1.85, 90),  # Ab

    # Bar 4 - comp on beat 2
    Note(71, start_time + 2.75, start_time + 2.85, 90),  # F
    Note(74, start_time + 2.75, start_time + 2.85, 90),  # A
    Note(72, start_time + 2.75, start_time + 2.85, 90),  # C
    Note(68, start_time + 2.75, start_time + 2.85, 90),  # Eb
]

for note in piano_comp:
    piano_instrument.notes.append(note)

# Save the MIDI file
pm.write("waynes_intro.mid")
print("MIDI file 'waynes_intro.mid' created.")
