
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
time_per_bar = 60.0 / tempo * 4  # 6 seconds for 4 bars

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Set the time signature
midi.time_signature_changes.append(pretty_midi.TimeSignature(numerator=time_signature[0], denominator=time_signature[1], time=0))

# Define a function to create a note
def create_note(pitch, start, end, velocity=100):
    return Note(pitch=pitch, start=start, end=end, velocity=velocity)

# Define the four bars
bar_length = time_per_bar / 4  # 1.5 seconds per bar

# Drums
drum_program = Program(program_number=10, is_drum=True)
drum_instrument = Instrument(program=drum_program)

# Kick on 1 & 3, Snare on 2 & 4, Hihat on every eighth
for bar in range(4):
    for beat in [0, 2]:  # 1 & 3
        drum_instrument.notes.append(create_note(36, bar * bar_length + beat * bar_length / 4, bar * bar_length + beat * bar_length / 4 + 0.1))
    for beat in [1, 3]:  # 2 & 4
        drum_instrument.notes.append(create_note(38, bar * bar_length + beat * bar_length / 4, bar * bar_length + beat * bar_length / 4 + 0.1))
    for eighth in range(8):
        drum_instrument.notes.append(create_note(42, bar * bar_length + eighth * bar_length / 8, bar * bar_length + eighth * bar_length / 8 + 0.05))

midi.instruments.append(drum_instrument)

# Bass
bass_program = Program(program_number=33)
bass_instrument = Instrument(program=bass_program)

# Chromatic walking line: Dm7 -> C -> B -> A -> G -> F# -> E -> D -> C
# Let's make it a bit "off" to add tension
chromatic_line = [2, 1, 0, -1, -2, -3, -4, -5, -6]
chromatic_line_pitches = [62 + x for x in chromatic_line]  # D is MIDI 62

# Map each beat to a note, with a little rest in between
for bar in range(4):
    for i, pitch in enumerate(chromatic_line_pitches):
        if i % 2 == 0:  # Play on every other beat
            start = bar * bar_length + (i // 2) * (bar_length / 4)
            end = start + 0.3
            bass_instrument.notes.append(create_note(pitch, start, end, velocity=90))

midi.instruments.append(bass_instrument)

# Piano
piano_program = Program(program_number=0)
piano_instrument = Instrument(program=piano_program)

# 7th chords on beats 2 and 4 (Cm7, A7, Gm7, F7)
piano_chords = [
    [60, 63, 67, 70],  # Cm7
    [65, 68, 72, 76],  # A7
    [62, 65, 69, 72],  # Gm7
    [67, 70, 74, 77]   # F7
]

# Play on beats 2 and 4 of each bar
for bar in range(4):
    for i, chord in enumerate(piano_chords):
        start = bar * bar_length + (i + 1) * (bar_length / 4)  # beat 2 and 4
        end = start + 0.8
        for pitch in chord:
            piano_instrument.notes.append(create_note(pitch, start, end, velocity=100))

midi.instruments.append(piano_instrument)

# Saxophone (Tenor)
sax_program = Program(program_number=64)
sax_instrument = Instrument(program=sax_program)

# Create a short motif that starts, leaves it hanging, and returns
# A motif in D minor: D - C - B - A (MIDI 62, 60, 59, 57) with rests

# Bar 1: Just a rest, let the drums and bass build
# Bar 2: Start the motif
# Bar 3: Continue the motif
# Bar 4: End with a question — a note that doesn't resolve

# Bar 1: Rest
# Bar 2: Start the motif
sax_instrument.notes.append(create_note(62, 1.5, 1.7, velocity=100))  # D
sax_instrument.notes.append(create_note(60, 2.0, 2.2, velocity=100))  # C
sax_instrument.notes.append(create_note(59, 2.5, 2.7, velocity=100))  # B
sax_instrument.notes.append(create_note(57, 3.0, 3.2, velocity=100))  # A

# Bar 3: Continue the motif, slightly altered
sax_instrument.notes.append(create_note(62, 3.5, 3.7, velocity=100))  # D
sax_instrument.notes.append(create_note(60, 4.0, 4.2, velocity=100))  # C
sax_instrument.notes.append(create_note(59, 4.5, 4.7, velocity=100))  # B
sax_instrument.notes.append(create_note(57, 5.0, 5.2, velocity=100))  # A

# Bar 4: End with a question — leave it hanging
sax_instrument.notes.append(create_note(62, 5.5, 5.7, velocity=100))  # D
sax_instrument.notes.append(create_note(60, 6.0, 6.15, velocity=100))  # C (short)

midi.instruments.append(sax_instrument)

# Save the MIDI
midi.write("dante_intro.mid")

print("MIDI file created as 'dante_intro.mid'")
