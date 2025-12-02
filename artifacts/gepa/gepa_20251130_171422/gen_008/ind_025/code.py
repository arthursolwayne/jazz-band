
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F major
key = 'F'

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Set time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set tempo
midi.time_signature_changes[0].tempo = 160

# Define the tempo: 160 BPM = 0.375 seconds per beat
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar

# Start time (in seconds)
time = 0.0

# Little Ray - Drums: First bar (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Start with a sparse, building rhythm

# Kick on beat 1 and 3 at bar 1
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + beat * 2, end=time + beat * 2 + 0.1)
drums.notes.append(kick1)
drums.notes.append(kick2)

# Snare on beat 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=time + beat, end=time + beat + 0.1)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=time + beat * 3, end=time + beat * 3 + 0.1)
drums.notes.append(snare1)
drums.notes.append(snare2)

# Hi-hat on every eighth, starting with a soft opening rhythm
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat / 2, end=time + beat / 2 + 0.1)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat, end=time + beat + 0.1)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat + beat / 2, end=time + beat + beat / 2 + 0.1)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 2, end=time + beat * 2 + 0.1)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 2 + beat / 2, end=time + beat * 2 + beat / 2 + 0.1)
hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 3, end=time + beat * 3 + 0.1)
hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * 3 + beat / 2, end=time + beat * 3 + beat / 2 + 0.1)
drums.notes.extend([hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

time += bar

# Bar 2: Bass enters with walking line, chromatic approach
# F major scale: F, G, A, Bb, B, C, D, E
# Walking line: F, G, A, Bb -> C, B, A, G -> F, G, A, Bb -> C, B, A, G (ending on G)

# Bass line
bass_notes = [
    (F, 0.0),
    (G, 0.375),
    (A, 0.75),
    (Bb, 1.125),
    (C, 1.5),
    (B, 1.875),
    (A, 2.25),
    (G, 2.625),
    (F, 3.0),
    (G, 3.375),
    (A, 3.75),
    (Bb, 4.125),
    (C, 4.5),
    (B, 4.875),
    (A, 5.25),
    (G, 5.625)
]

# Convert to MIDI note numbers
note_map = {
    'F': 65, 'G': 67, 'A': 69, 'Bb': 70, 'B': 71, 'C': 72, 'D': 74, 'E': 76
}

for pitch, start in bass_notes:
    note_number = note_map[pitch]
    end = start + 0.25
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start + time, end=end + time)
    bass.notes.append(note)

time += bar

# Bar 3: Piano enters with 7th chords on 2 and 4
# F7, Bb7, D7, G7 (root motion: F -> Bb -> D -> G)
# Chords on 2 and 4
# F7: F, A, C, Eb (7th)
# Bb7: Bb, D, F, Ab
# D7: D, F#, A, C
# G7: G, B, D, F

# Convert to MIDI note numbers
chord_map = {
    'F7': [65, 68, 72, 69],
    'Bb7': [70, 74, 65, 71],
    'D7': [62, 67, 72, 65],
    'G7': [67, 71, 72, 65]
}

# Time for chords: on beat 2 and 4
chord_times = [
    (time + beat, 1.0),  # F7 on beat 2
    (time + beat * 3, 1.0),  # Bb7 on beat 4
    (time + 2 * bar + beat, 1.0),  # D7 on beat 2 of bar 3
    (time + 2 * bar + beat * 3, 1.0)  # G7 on beat 4 of bar 3
]

for chord, start in chord_times:
    chord_notes = chord_map[chord]
    for note in chord_notes:
        piano_note = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.5)
        piano.notes.append(piano_note)

# Bar 4: Tenor sax enters with a melodic motif
# Motif: F, Bb, C, F (motif that starts and ends on F)
# Use dynamic phrasing, with space between notes

sax_notes = [
    (F, 0.0, 100),
    (Bb, 0.5, 90),
    (C, 1.0, 110),
    (F, 1.5, 100)
]

for pitch, start, velocity in sax_notes:
    note_number = note_map[pitch]
    end = start + 0.25
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start + time, end=end + time)
    sax.notes.append(note)

# Save the MIDI file
midi.write("dante_intro.mid")
