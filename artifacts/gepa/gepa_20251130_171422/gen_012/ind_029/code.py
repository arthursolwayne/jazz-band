
import pretty_midi
from pretty_midi import Note, Instrument

# Settings
tempo = 160
time_signature = (4, 4)
key = 'F minor'

# Create a MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define time intervals
bar_length = 6.0 / 4  # 6 seconds for 4 bars
beat_length = bar_length / 4  # 1.5 seconds per bar, 0.375 seconds per beat

# Create instruments
# Drums
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drums)

# Bass
bass = Instrument(program=pretty_midi.instrument_name_to_program('Double Bass'))
pm.instruments.append(bass)

# Piano
piano = Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
pm.instruments.append(piano)

# Tenor Sax
sax = Instrument(program=pretty_midi.instrument_name_to_program('Soprano Sax'))
pm.instruments.append(sax)

# Time: 0s
# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Drums - Bar 1
drum_notes = [
    (0, 36, 100, 0),   # Kick on 1
    (0, 38, 100, beat_length * 0.5),  # Snare on 2
    (0, 42, 100, beat_length * 1),  # Hihat on 3 (8th note)
    (0, 36, 100, beat_length * 1.5),  # Kick on 3
    (0, 38, 100, beat_length * 2),  # Snare on 4
    (0, 42, 100, beat_length * 2.5),  # Hihat on 6
    (0, 42, 100, beat_length * 3),  # Hihat on 7
    (0, 42, 100, beat_length * 3.5),  # Hihat on 8
]

for note in drum_notes:
    start, pitch, velocity, time = note
    drums.notes.append(Note(pitch=pitch, start=bar_length * 0 + time, end=bar_length * 0 + time + 0.1, velocity=velocity))

# Bar 2: Bass, Piano, Sax

# Bass Line in F minor (walking line)
bass_notes = [
    (1, 71, 80, 0),  # F (71) - 1
    (1, 70, 80, beat_length * 1),  # Eb (70) - & 2
    (1, 69, 80, beat_length * 1.5),  # D (69) - 3
    (1, 73, 80, beat_length * 2),  # G (73) - & 4
    (1, 71, 80, beat_length * 3),  # F (71) - 1
    (1, 70, 80, beat_length * 4),  # Eb (70) - & 2
    (1, 69, 80, beat_length * 4.5),  # D (69) - 3
    (1, 73, 80, beat_length * 5),  # G (73) - & 4
    (1, 71, 80, beat_length * 6),  # F (71) - 1
    (1, 70, 80, beat_length * 7),  # Eb (70) - & 2
    (1, 69, 80, beat_length * 7.5),  # D (69) - 3
    (1, 73, 80, beat_length * 8),  # G (73) - & 4
]

for note in bass_notes:
    start, pitch, velocity, time = note
    bass.notes.append(Note(pitch=pitch, start=bar_length * 1 + time, end=bar_length * 1 + time + 0.1, velocity=velocity))

# Piano - 7th chords, comping on 2 and 4
piano_notes = [
    # F7 on 2
    (2, 65, 100, 0),  # F (65)
    (2, 69, 100, 0),  # Bb (69)
    (2, 71, 100, 0),  # C (71)
    (2, 72, 100, 0),  # Db (72)
    # F7 on 4
    (4, 65, 100, beat_length * 2),
    (4, 69, 100, beat_length * 2),
    (4, 71, 100, beat_length * 2),
    (4, 72, 100, beat_length * 2),
    # G7 on 2 of bar 3
    (2, 67, 100, beat_length * 4),
    (2, 71, 100, beat_length * 4),
    (2, 72, 100, beat_length * 4),
    (2, 74, 100, beat_length * 4),
    # G7 on 4 of bar 3
    (4, 67, 100, beat_length * 6),
    (4, 71, 100, beat_length * 6),
    (4, 72, 100, beat_length * 6),
    (4, 74, 100, beat_length * 6),
]

for note in piano_notes:
    start, pitch, velocity, time = note
    piano.notes.append(Note(pitch=pitch, start=bar_length * 1 + time, end=bar_length * 1 + time + 0.1, velocity=velocity))

# Tenor Sax - Your motif
# F - Eb - D - G (Fm7 with a chromatic approach)
sax_notes = [
    (1, 65, 100, 0),  # F on 1
    (1, 64, 100, 0.25),  # Eb
    (1, 63, 100, 0.5),  # D
    (1, 67, 100, 0.75),  # G
    (1, 65, 100, 1.0),  # F (repeat)
    (1, 64, 100, 1.25),  # Eb
    (1, 63, 100, 1.5),  # D
    (1, 67, 100, 1.75),  # G
]

for note in sax_notes:
    start, pitch, velocity, time = note
    sax.notes.append(Note(pitch=pitch, start=bar_length * 1 + time, end=bar_length * 1 + time + 0.1, velocity=velocity))

# Save the MIDI
pm.write('jazz_intro_Fm.mid')
