
import pretty_midi
import numpy as np
from pretty_midi import Instrument, Note

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key and note numbers
F_MAJOR = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F#
note_numbers = {
    'F': 65,
    'G': 67,
    'A': 69,
    'Bb': 71,
    'B': 72,
    'C': 72,
    'Db': 73,
    'D': 74,
    'Eb': 76,
    'E': 77,
    'F#': 77,
    'G#': 79,
    'Ab': 78
}

# Create instruments
drums_instrument = Instrument(program=10, is_drum=True)
piano_instrument = Instrument(program=0)
bass_instrument = Instrument(program=33)
sax_instrument = Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments = [drums_instrument, piano_instrument, bass_instrument, sax_instrument]

# Define time per bar in seconds
time_per_beat = 60.0 / 160  # 0.375 seconds per beat
time_per_bar = 4 * time_per_beat  # 1.5 seconds per bar
time_per_eighth = time_per_beat / 2  # 0.1875

# Bar 1: Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = time_per_bar

# Drums: Bar 1
drums_instrument.notes.extend([
    Note(36, bar_1_start, bar_1_start + 0.05, velocity=100),  # Kick on 1
    Note(38, bar_1_start + time_per_beat, bar_1_start + time_per_beat + 0.05, velocity=100),  # Snare on 2
    Note(36, bar_1_start + 2 * time_per_beat, bar_1_start + 2 * time_per_beat + 0.05, velocity=100),  # Kick on 3
    Note(38, bar_1_start + 3 * time_per_beat, bar_1_start + 3 * time_per_beat + 0.05, velocity=100),  # Snare on 4
    Note(42, bar_1_start, bar_1_start + time_per_bar, velocity=80)  # Hihat on every eighth
])

# Bar 2-4: Everyone plays — sax melody, bass walking line, piano comping, drums continuing

# Bar 2 Start
bar_2_start = bar_1_end
bar_2_end = bar_1_end + time_per_bar

# Sax melody: A short motif (F - Ab - Bb - F), with a rest in the middle
sax_notes = [
    Note(65, bar_2_start, bar_2_start + 0.2, velocity=100),    # F
    Note(71, bar_2_start + 0.3, bar_2_start + 0.5, velocity=100),  # Ab
    Note(72, bar_2_start + 0.6, bar_2_start + 0.8, velocity=100),  # Bb
    Note(65, bar_2_start + 1.0, bar_2_start + 1.2, velocity=100)   # F
]
sax_instrument.notes.extend(sax_notes)

# Walking bass line (chromatic, never repeating a note)
bass_notes = [
    Note(65, bar_2_start, bar_2_start + 0.2, velocity=100),  # F
    Note(66, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.2, velocity=100),  # F#
    Note(67, bar_2_start + 2 * time_per_beat, bar_2_start + 2 * time_per_beat + 0.2, velocity=100),  # G
    Note(69, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.2, velocity=100),  # A
    Note(65, bar_2_start + 4 * time_per_beat, bar_2_start + 4 * time_per_beat + 0.2, velocity=100),  # F
    Note(66, bar_2_start + 5 * time_per_beat, bar_2_start + 5 * time_per_beat + 0.2, velocity=100),  # F#
    Note(67, bar_2_start + 6 * time_per_beat, bar_2_start + 6 * time_per_beat + 0.2, velocity=100),  # G
    Note(69, bar_2_start + 7 * time_per_beat, bar_2_start + 7 * time_per_beat + 0.2, velocity=100)   # A
]
bass_instrument.notes.extend(bass_notes)

# Piano comping — 7th chords on 2 and 4 (F7 on 2, D7 on 4)
piano_notes = []

# F7 chord on beat 2 (F, A, C, Eb)
piano_notes.extend([
    Note(65, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.2, velocity=90),  # F
    Note(69, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.2, velocity=90),  # A
    Note(72, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.2, velocity=90),  # C
    Note(76, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.2, velocity=90)   # Eb
])

# D7 chord on beat 4 (D, F#, A, C)
piano_notes.extend([
    Note(74, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.2, velocity=90),  # D
    Note(77, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.2, velocity=90),  # F#
    Note(72, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.2, velocity=90),  # A
    Note(76, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.2, velocity=90)   # C
])

piano_instrument.notes.extend(piano_notes)

# Drums continue — bar 2
drums_instrument.notes.extend([
    Note(36, bar_2_start, bar_2_start + 0.05, velocity=100),  # Kick on 1
    Note(38, bar_2_start + time_per_beat, bar_2_start + time_per_beat + 0.05, velocity=100),  # Snare on 2
    Note(36, bar_2_start + 2 * time_per_beat, bar_2_start + 2 * time_per_beat + 0.05, velocity=100),  # Kick on 3
    Note(38, bar_2_start + 3 * time_per_beat, bar_2_start + 3 * time_per_beat + 0.05, velocity=100),  # Snare on 4
    Note(42, bar_2_start, bar_2_start + time_per_bar, velocity=80)  # Hihat on every eighth
])

# Bar 3 and 4: Copy the same rhythm as Bar 2 (Drums, Bass, Piano)
# Drums
drums_instrument.notes.extend([
    Note(36, bar_2_end, bar_2_end + 0.05, velocity=100),  # Kick on 1
    Note(38, bar_2_end + time_per_beat, bar_2_end + time_per_beat + 0.05, velocity=100),  # Snare on 2
    Note(36, bar_2_end + 2 * time_per_beat, bar_2_end + 2 * time_per_beat + 0.05, velocity=100),  # Kick on 3
    Note(38, bar_2_end + 3 * time_per_beat, bar_2_end + 3 * time_per_beat + 0.05, velocity=100),  # Snare on 4
    Note(42, bar_2_end, bar_2_end + time_per_bar, velocity=80)  # Hihat on every eighth
])

# Bass: Repeat the walking line
bass_instrument.notes.extend(bass_notes)

# Piano: Repeat the same comping on 2 and 4
piano_instrument.notes.extend(piano_notes)

# Save the MIDI file
midi.write("the_cellar_intro.mid")
print("MIDI file generated: the_cellar_intro.mid")
