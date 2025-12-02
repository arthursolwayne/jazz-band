
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160
time_signature = (4, 4)

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define the beat duration in seconds (60 / tempo)
beat = 60.0 / tempo
bar = 4 * beat  # 4 beats per bar

# 4 bars = 6 seconds
total_time = 4 * beat

# Define instruments
bass_program = Program(33)  # Electric Bass
piano_program = Program(0)  # Acoustic Piano
drums_program = Program(10)  # Acoustic Drums
sax_program = Program(64)    # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
drum_instrument = Instrument(program=drums_program)
sax_instrument = Instrument(program=sax_program)

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)
pm.instruments.append(sax_instrument)

# Bar 1: Drums only — sparse, rhythmic, waiting
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0

# Kick on beat 1 and 3
drum_instrument.notes.append(Note(36, 100, bar1_start, bar1_start + 0.1))
drum_instrument.notes.append(Note(36, 100, bar1_start + 2 * beat, bar1_start + 2 * beat + 0.1))

# Snare on beat 2 and 4
drum_instrument.notes.append(Note(38, 100, bar1_start + beat, bar1_start + beat + 0.1))
drum_instrument.notes.append(Note(38, 100, bar1_start + 3 * beat, bar1_start + 3 * beat + 0.1))

# Hi-hat on every eighth
for i in range(8):
    drum_instrument.notes.append(Note(42, 80, bar1_start + i * beat / 2, bar1_start + i * beat / 2 + 0.05))

# Bar 2: Bass enters — walking line with chromatic approaches
bar2_start = bar1_start + bar

# Bass line in Dm (D - Eb - F - G)
# Walking line: D, Eb, F, G, Ab, Bb, B, C
# Chromatic approach on the second beat
bass_line = [
    (62, bar2_start + 0 * beat, bar2_start + 0 * beat + 0.5),  # D
    (63, bar2_start + 1 * beat, bar2_start + 1 * beat + 0.5),  # Eb
    (64, bar2_start + 2 * beat, bar2_start + 2 * beat + 0.5),  # F
    (65, bar2_start + 3 * beat, bar2_start + 3 * beat + 0.5),  # G
    (66, bar2_start + 4 * beat, bar2_start + 4 * beat + 0.5),  # Ab
    (67, bar2_start + 5 * beat, bar2_start + 5 * beat + 0.5),  # Bb
    (68, bar2_start + 6 * beat, bar2_start + 6 * beat + 0.5),  # B
    (69, bar2_start + 7 * beat, bar2_start + 7 * beat + 0.5),  # C
]

for note, start, end in bass_line:
    bass_instrument.notes.append(Note(note, 90, start, end))

# Bar 3: Piano enters — 7th chords on 2 and 4
bar3_start = bar2_start + bar

# Dm7 = D, F, A, C
# Comp on 2 and 4
piano_notes = [
    # Beat 2: Dm7, root on beat 2
    (62, bar3_start + 1 * beat, bar3_start + 1 * beat + 0.3),
    (64, bar3_start + 1 * beat, bar3_start + 1 * beat + 0.3),
    (67, bar3_start + 1 * beat, bar3_start + 1 * beat + 0.3),
    (69, bar3_start + 1 * beat, bar3_start + 1 * beat + 0.3),

    # Beat 4: Dm7, root on beat 4
    (62, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.3),
    (64, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.3),
    (67, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.3),
    (69, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.3),
]

for note, start, end in piano_notes:
    piano_instrument.notes.append(Note(note, 90, start, end))

# Bar 4: Sax enters — short, singing motif
bar4_start = bar3_start + bar

# Motif: D - Bb - C, ends on rest
# D = 62, Bb = 67, C = 69

sax_notes = [
    (62, bar4_start + 0.1, bar4_start + 0.5),  # D
    (67, bar4_start + 0.7, bar4_start + 1.1),  # Bb
    (69, bar4_start + 1.3, bar4_start + 1.7),  # C
]

for note, start, end in sax_notes:
    sax_instrument.notes.append(Note(note, 100, start, end))

# Save the MIDI file
pm.write("dante_intro_dminor.mid")
print("MIDI file generated: dante_intro_dminor.mid")
