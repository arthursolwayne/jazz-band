
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define the key: F major
key = 'F'

# Define the note lengths and timing
# Tempo: 160 BPM => 0.375 seconds per beat
beat_length = 0.375
bar_length = beat_length * 4  # 1.5 seconds per bar

# Define instruments
# 1. Drums (program 36)
drum_program = pretty_midi.Instrument(program=36)
# 2. Bass (program 33)
bass_program = pretty_midi.Instrument(program=33)
# 3. Piano (program 0)
piano_program = pretty_midi.Instrument(program=0)
# 4. Tenor sax (program 64)
sax_program = pretty_midi.Instrument(program=64)

# Key scale: F major (F, G, A, Bb, C, D, E)
f_major = [72, 74, 76, 77, 79, 81, 83]  # MIDI notes

# Define a simple walking bass line (chromatic approach, no repeats)
def bass_line():
    return [
        (79, 0.0),     # C (beat 1)
        (78, 0.0),     # Bb (beat 2)
        (77, 0.0),     # A (beat 3)
        (76, 0.0),     # G (beat 4)
        (78, 0.0),     # Bb (beat 1)
        (79, 0.0),     # C (beat 2)
        (81, 0.0),     # D (beat 3)
        (83, 0.0),     # E (beat 4)
        (81, 0.0),     # D (beat 1)
        (79, 0.0),     # C (beat 2)
        (77, 0.0),     # A (beat 3)
        (76, 0.0),     # G (beat 4)
        (77, 0.0),     # A (beat 1)
        (79, 0.0),     # C (beat 2)
        (81, 0.0),     # D (beat 3)
        (83, 0.0)      # E (beat 4)
    ]

# Define piano chords (7th chords, comp on beats 2 and 4)
def piano_chords():
    return [
        (77, 79, 82, 83, 0.0),     # G7 (beat 2)
        (76, 79, 81, 83, 0.0),     # Am7 (beat 4)
        (77, 79, 82, 83, 0.0),     # G7 (beat 2)
        (76, 79, 81, 83, 0.0),     # Am7 (beat 4)
        (77, 79, 82, 83, 0.0),     # G7 (beat 2)
        (76, 79, 81, 83, 0.0)      # Am7 (beat 4)
    ]

# Define drum pattern: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
def drum_pattern():
    return [
        (36, 0.0),     # Kick on beat 1
        (38, 0.0),     # Snare on beat 2
        (42, 0.0),     # Hi-hat on beat 2.5
        (42, 0.0),     # Hi-hat on beat 3
        (36, 0.0),     # Kick on beat 3
        (38, 0.0),     # Snare on beat 4
        (42, 0.0),     # Hi-hat on beat 4.5
        (42, 0.0)      # Hi-hat on beat 5
    ]

# Define the sax motif: a short phrase with space and tension
def sax_motif():
    return [
        (76, 0.3),     # A (beat 1)
        (72, 0.25),    # F (beat 1.3)
        (76, 0.25),    # A (beat 1.5)
        (74, 0.1),     # G (beat 1.6)
        (76, 0.2),     # A (beat 1.8)
        (74, 0.1),     # G (beat 1.9)
        (72, 0.2),     # F (beat 2.1)
    ]

# Add the bass line to the bass instrument
for note, time in bass_line():
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + beat_length)
    bass_program.notes.append(bass_note)

# Add piano chords
for chord in piano_chords():
    for note in chord:
        piano_note = pretty_midi.Note(velocity=85, pitch=note, start=int(chord[4]) * beat_length, end=int(chord[4]) * beat_length + beat_length / 2)
        piano_program.notes.append(piano_note)

# Add drum patterns
for note, time in drum_pattern():
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time * beat_length, end=time * beat_length + 0.05)
    drum_program.notes.append(drum_note)

# Add the sax motif
for note, duration in sax_motif():
    start_time = 0.0
    for i, (n, d) in enumerate(sax_motif()):
        if i == 0:
            start_time = 0.0
        else:
            start_time = sax_motif[i-1][1] + sax_motif[i-1][2]
        sax_note = pretty_midi.Note(velocity=105, pitch=note, start=start_time, end=start_time + duration)
        sax_program.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.append(drum_program)
midi.instruments.append(bass_program)
midi.instruments.append(piano_program)
midi.instruments.append(sax_program)

# Save the MIDI file
midi.write("dante_intro.mid")

print("MIDI file written to 'dante_intro.mid'")
