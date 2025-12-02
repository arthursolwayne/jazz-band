
import pretty_midi
from pretty_midi import Instrument, Note

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signatures = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Set key signature to D minor (1 flat)
pm.key_signatures = [pretty_midi.KeySignature(key_number=3, time=0)]  # D minor

# Create instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)  # Acoustic Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Sax

pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# TEMPO = 160 BPM => 60 / 160 = 0.375 seconds per beat
# 4 bars = 6.0 seconds
# Each bar = 1.5 seconds
# Each beat = 0.375 seconds
# Each eighth note = 0.1875 seconds

# Bar 1: Little Ray (drums) only - snare on 2 and 4, kick on 1 and 3, hihat on every eighth
bar_length = 1.5  # in seconds
beat_length = 0.375  # in seconds

# Bar 1: Drums only
drum_notes = []

# Kick on 1 and 3
drum_notes.append(Note(36, 0, 0, beat_length))  # Kick on beat 1
drum_notes.append(Note(36, 0, beat_length * 2, beat_length))  # Kick on beat 3

# Snare on 2 and 4
drum_notes.append(Note(38, 0, beat_length, beat_length))  # Snare on beat 2
drum_notes.append(Note(38, 0, beat_length * 3, beat_length))  # Snare on beat 4

# Hi-hat on every eighth note
for i in range(8):
    drum_notes.append(Note(42, 0, i * beat_length / 2, beat_length / 2))

drums_instrument.notes.extend(drum_notes)

# Bar 2: All instruments in. Tenor sax takes the melody.

# Bass line: Walking line, chromatic approaches, never repeating a note
# Dm7: D, F, A, C
# Walking bass line: D, F, G, A, Bb, C, B, A
# Dm7: 0, 3, 5, 7

# Time: bar 1 ends at 1.5s, bar 2 starts at 1.5s
# Positions are in seconds
bass_notes = []

# Start time of bar 2: 1.5s
start_time = 1.5

# Bass line: D (0), F (3), G (5), A (7), Bb (8), C (10), B (11), A (7)
times = [start_time + (i * beat_length) for i in range(8)]
notes = [0, 3, 5, 7, 8, 10, 11, 7]  # MIDI note numbers (Dm7 bass line)

for t, n in zip(times, notes):
    bass_notes.append(Note(n, 100, t, beat_length))

bass_instrument.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D, F, A, C
# bar 2: Dm7 on beat 2, G7 on beat 4
piano_notes = []

# Dm7 on beat 2 (start_time + 0.375 * 2 = 2.25s)
# D (D4 = 62), F (65), A (69), C (60)
for note in [62, 65, 69, 60]:
    piano_notes.append(Note(note, 100, start_time + beat_length * 2, beat_length))

# G7 on beat 4 (start_time + beat_length * 4 = 1.5 + 1.5 = 3.0s)
# G (67), B (71), D (62), F (65)
for note in [67, 71, 62, 65]:
    piano_notes.append(Note(note, 100, start_time + beat_length * 4, beat_length))

piano_instrument.notes.extend(piano_notes)

# Tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Dm7 scale: D, E, F, G, A, B, C, D
# Motif: D (62), E (64), F (65), [rest] -> D (62), E (64), F (65), G (67), A (69)
# Time: bar 2 starts at 1.5s
sax_notes = []

# First phrase: D, E, F, rest
sax_notes.append(Note(62, 120, start_time, beat_length * 0.75))  # D for 0.75 beats
sax_notes.append(Note(64, 120, start_time + beat_length * 0.75, beat_length * 0.75))  # E for 0.75 beats
sax_notes.append(Note(65, 120, start_time + beat_length * 1.5, beat_length * 0.75))  # F for 0.75 beats

# Rest for 0.75 beats (beat 2)
# Then return and finish the motif: D, E, F, G, A
sax_notes.append(Note(62, 120, start_time + beat_length * 2.25, beat_length * 0.75))  # D
sax_notes.append(Note(64, 120, start_time + beat_length * 3.0, beat_length * 0.75))  # E
sax_notes.append(Note(65, 120, start_time + beat_length * 3.75, beat_length * 0.75))  # F
sax_notes.append(Note(67, 120, start_time + beat_length * 4.5, beat_length * 0.75))  # G
sax_notes.append(Note(69, 120, start_time + beat_length * 5.25, beat_length * 0.75))  # A

sax_instrument.notes.extend(sax_notes)

# Write to a MIDI file
pm.write("jazz_intro_dmin.mid")
