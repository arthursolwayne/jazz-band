
import pretty_midi
from pretty_midi import Note, Instrument

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
saxophone = Instrument(program=saxophone_program, is_drum=False)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = Instrument(program=bass_program, is_drum=False)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = Instrument(program=piano_program, is_drum=False)
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = Instrument(program=drums_program, is_drum=True)

# Add instruments to MIDI
midi.instruments = [saxophone, bass, piano, drums]

# BPM = 160, 4/4 time
# 4 bars = 6 seconds
# Each beat = 0.375 seconds, each bar = 1.5 seconds

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = Note(36, 100, bar1_start, bar1_start + 0.1)
kick2 = Note(36, 100, bar1_start + 0.75, bar1_start + 0.85)
drums.notes.append(kick1)
drums.notes.append(kick2)

# Snare on 2 and 4
snare1 = Note(38, 100, bar1_start + 0.375, bar1_start + 0.475)
snare2 = Note(38, 100, bar1_start + 1.125, bar1_start + 1.225)
drums.notes.append(snare1)
drums.notes.append(snare2)

# Hi-hat on every eighth
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for time in hihat_notes:
    hihat = Note(42, 100, time, time + 0.05)
    drums.notes.append(hihat)

# Bar 2-4: Full quartet

bar2_start = 1.5
bar4_end = 4.5

# Bass: Walking line, chromatic approaches, no repeated notes
# D minor scale: D, Eb, F, G, Ab, Bb, C
# Walking bass line: D - Eb - F - G - Ab - Bb - C - D (octave)

bass_notes = [
    Note(62, 70, bar2_start, bar2_start + 0.375),   # D
    Note(63, 70, bar2_start + 0.375, bar2_start + 0.75),  # Eb
    Note(64, 70, bar2_start + 0.75, bar2_start + 1.125),  # F
    Note(65, 70, bar2_start + 1.125, bar2_start + 1.5),   # G
    Note(66, 70, bar2_start + 1.5, bar2_start + 1.875),   # Ab
    Note(67, 70, bar2_start + 1.875, bar2_start + 2.25),  # Bb
    Note(68, 70, bar2_start + 2.25, bar2_start + 2.625),  # C
    Note(62, 70, bar2_start + 2.625, bar2_start + 3),     # D
    Note(63, 70, bar2_start + 3, bar2_start + 3.375),     # Eb
    Note(64, 70, bar2_start + 3.375, bar2_start + 3.75),   # F
    Note(65, 70, bar2_start + 3.75, bar2_start + 4.125),   # G
    Note(66, 70, bar2_start + 4.125, bar2_start + 4.5),    # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Comp on 2 and 4 (bar 2, bar 3, bar 4)
# D minor 7: D, F, Ab, C

def add_piano_chord(note, time, duration):
    root = Note(note, 80, time, time + duration)
    third = Note(note + 3, 80, time, time + duration)
    fifth = Note(note + 7, 80, time, time + duration)
    seventh = Note(note + 10, 80, time, time + duration)
    piano.notes.extend([root, third, fifth, seventh])

# Bar 2, beat 2
add_piano_chord(62, bar2_start + 0.375, 0.375)
# Bar 3, beat 2
add_piano_chord(62, bar2_start + 1.875, 0.375)
# Bar 4, beat 2
add_piano_chord(62, bar2_start + 3.375, 0.375)

# Saxophone: Motif with unique durations and a rest
# D - G - Bb - rest - F - Ab - D

# Bar 2: D
sax_note1 = Note(62, 100, bar2_start, bar2_start + 0.4)
saxophone.notes.append(sax_note1)

# Bar 2: G
sax_note2 = Note(67, 100, bar2_start + 0.6, bar2_start + 0.8)
saxophone.notes.append(sax_note2)

# Bar 2: Bb
sax_note3 = Note(67, 100, bar2_start + 1.0, bar2_start + 1.2)
saxophone.notes.append(sax_note3)

# Bar 3: Rest
sax_rest = Note(62, 0, bar2_start + 1.5, bar2_start + 1.5)
saxophone.notes.append(sax_rest)

# Bar 3: F
sax_note4 = Note(64, 100, bar2_start + 1.6, bar2_start + 1.8)
saxophone.notes.append(sax_note4)

# Bar 3: Ab
sax_note5 = Note(66, 100, bar2_start + 2.0, bar2_start + 2.2)
saxophone.notes.append(sax_note5)

# Bar 4: D
sax_note6 = Note(62, 100, bar2_start + 3.0, bar2_start + 3.2)
saxophone.notes.append(sax_note6)

# Drums in bar 2-4
# Kick on 1 and 3 each bar
for bar in range(2, 5):
    bar_start = bar1_end + (bar - 2) * 1.5
    kick1 = Note(36, 100, bar_start, bar_start + 0.1)
    kick2 = Note(36, 100, bar_start + 0.75, bar_start + 0.85)
    drums.notes.append(kick1)
    drums.notes.append(kick2)

    # Snare on 2 and 4
    snare1 = Note(38, 100, bar_start + 0.375, bar_start + 0.475)
    snare2 = Note(38, 100, bar_start + 1.125, bar_start + 1.225)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

    # Hi-hat on every eighth
    hihat_notes = [bar_start + i * 0.375 for i in range(4)]
    for time in hihat_notes:
        hihat = Note(42, 100, time, time + 0.05)
        drums.notes.append(hihat)

# Write the MIDI file
midi.write("jazz_intro.mid")
