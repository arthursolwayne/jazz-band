
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument_group = pretty_midi.Instrument(program=64)  # Tenor Sax
pm.instruments.append(instrument_group)

# Define a function to add a note
def add_note(note_number, start, end, velocity):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    instrument_group.notes.append(note)

# Define a function to add a drum hit
def add_drum(note_number, start, velocity):
    drum_instrument = pretty_midi.Instrument(program=128)
    pm.instruments.append(drum_instrument)
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + 0.1)
    drum_instrument.notes.append(note)

# Define a function to add a piano chord
def add_piano_chord(chord, start, end, velocity):
    piano_instrument = pretty_midi.Instrument(program=0)
    pm.instruments.append(piano_instrument)
    for note in chord:
        add_note(note, start, end, velocity)

# Define a function to add a bass note
def add_bass_note(note_number, start, end, velocity):
    bass_instrument = pretty_midi.Instrument(program=33)
    pm.instruments.append(bass_instrument)
    add_note(note_number, start, end, velocity)

# Set start time
time = 0.0
bar_length = 1.5  # 160 BPM, 4/4 time = 1.5 seconds per bar

# BAR 1: Little Ray on drums alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = time

# Kick on 1
add_drum(36, bar1_start, 100)
# Snare on 2
add_drum(38, bar1_start + 0.75, 100)
# Kick on 3
add_drum(36, bar1_start + 0.75 * 2, 100)
# Snare on 4
add_drum(38, bar1_start + 0.75 * 3, 100)
# Hihat on every eighth
for i in range(8):
    add_drum(42, bar1_start + i * 0.375, 80)

time += bar_length

# BAR 2: Everyone in. You begin the melody
bar2_start = time

# Bass: D2 (MIDI 38), root on 1, chromatic approach on 2
add_bass_note(38, bar2_start, bar2_start + 0.375, 100)
add_bass_note(39, bar2_start + 0.375, bar2_start + 0.75, 100)
add_bass_note(38, bar2_start + 0.75, bar2_start + 1.125, 100)
add_bass_note(40, bar2_start + 1.125, bar2_start + 1.5, 100)

# Piano: Dmaj7 -> E7 -> Gm7 -> A7
# Bar 2: Dmaj7
add_piano_chord([62, 67, 72, 76], bar2_start, bar2_start + 0.75, 90)
# Bar 3: E7
add_piano_chord([64, 69, 71, 76], bar2_start + 0.75, bar2_start + 1.5, 90)

# Tenor: Melody starts — one short motif, leaves it hanging
# Motif: D4, F#4, G4, Bb4 (MIDI 62, 66, 67, 70)
add_note(62, bar2_start, bar2_start + 0.375, 100)
add_note(66, bar2_start + 0.375, bar2_start + 0.75, 100)
add_note(67, bar2_start + 0.75, bar2_start + 1.125, 100)
add_note(70, bar2_start + 1.125, bar2_start + 1.5, 100)

time += bar_length

# BAR 3: Continue the build
bar3_start = time

# Bass: Continue walking line
add_bass_note(41, bar3_start, bar3_start + 0.375, 100)
add_bass_note(42, bar3_start + 0.375, bar3_start + 0.75, 100)
add_bass_note(41, bar3_start + 0.75, bar3_start + 1.125, 100)
add_bass_note(43, bar3_start + 1.125, bar3_start + 1.5, 100)

# Piano: Gm7 -> A7 -> Bm7 -> C#7 (resolving on A7)
add_piano_chord([67, 72, 76, 79], bar3_start, bar3_start + 0.75, 90)
add_piano_chord([69, 74, 76, 81], bar3_start + 0.75, bar3_start + 1.5, 90)

# Tenor: Repeat the motif, but resolve it
add_note(62, bar3_start, bar3_start + 0.375, 100)
add_note(66, bar3_start + 0.375, bar3_start + 0.75, 100)
add_note(67, bar3_start + 0.75, bar3_start + 1.125, 100)
add_note(62, bar3_start + 1.125, bar3_start + 1.5, 100)

time += bar_length

# BAR 4: Resolution
bar4_start = time

# Bass: Final step in the walk
add_bass_note(43, bar4_start, bar4_start + 0.375, 100)
add_bass_note(45, bar4_start + 0.375, bar4_start + 0.75, 100)
add_bass_note(43, bar4_start + 0.75, bar4_start + 1.125, 100)
add_bass_note(44, bar4_start + 1.125, bar4_start + 1.5, 100)

# Piano: A7 on bar 4
add_piano_chord([69, 74, 76, 81], bar4_start, bar4_start + 1.5, 90)

# Tenor: Return the motif, but now with a dynamic shift and resolution
add_note(62, bar4_start, bar4_start + 0.375, 120)
add_note(66, bar4_start + 0.375, bar4_start + 0.75, 120)
add_note(67, bar4_start + 0.75, bar4_start + 1.125, 120)
add_note(62, bar4_start + 1.125, bar4_start + 1.5, 120)

# Drums: Final fill
# Kick on 1, snare on 3, hihat on every eighth
add_drum(36, bar4_start, 100)
for i in range(8):
    add_drum(42, bar4_start + i * 0.375, 80)
add_drum(38, bar4_start + 0.75 * 2, 100)

# Save the MIDI file
pm.write("jazz_intro.mid")
