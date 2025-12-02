
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key signature to F minor
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define instruments
sax_instrument = Instrument(program=64, is_drum=False)
bass_instrument = Instrument(program=33, is_drum=False)
piano_instrument = Instrument(program=0, is_drum=False)
drum_instrument = Instrument(program=0, is_drum=True)

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drum_instrument]

# Time per bar in seconds (160 BPM = 60 / 160 = 0.375 seconds per beat)
bar_length = 1.5  # 4 beats per bar, 0.375 per beat
beat_length = 0.375

# Define the key
key = 'Fm'
root = pretty_midi.note_number_from_name('F')
scale_degrees = [0, 2, 3, 5, 7, 8, 10]  # Fm scale: F, Gb, G, Ab, Bb, B, C

# Define the saxophone motif (Bar 1: rest, Bar 2-4: motif with rests and unique durations)
sax_notes = []

# Bar 1: saxophone rests
# Drums start alone in bar 1
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
kick_notes = [bar_1_start + 0.0, bar_1_start + 1.125]
snare_notes = [bar_1_start + 0.375, bar_1_start + 1.5]
hihat_notes = [bar_1_start + 0.0, bar_1_start + 0.375, bar_1_start + 0.75, bar_1_start + 1.125, bar_1_start + 1.5, bar_1_start + 1.875]

for time in kick_notes:
    drum_instrument.notes.append(Note(36, 48, time, time + 0.125))  # Kick drum
for time in snare_notes:
    drum_instrument.notes.append(Note(38, 60, time, time + 0.125))  # Snare
for time in hihat_notes:
    drum_instrument.notes.append(Note(42, 60, time, time + 0.0625))  # Hihat

# Bar 2: saxophone motif starts
bar_2_start = bar_length  # 1.5 seconds

# Saxophone motif: F (root), Bb (5th), Ab (b6), rest, F (root)
# Unique durations: 0.25, 0.5, 0.75, rest, 0.25
sax_notes.append(Note(root, 85, bar_2_start, bar_2_start + 0.25))  # F
sax_notes.append(Note(root + 7, 85, bar_2_start + 0.25, bar_2_start + 0.25 + 0.5))  # Bb
sax_notes.append(Note(root + 5, 85, bar_2_start + 0.75, bar_2_start + 0.75 + 0.75))  # Ab
sax_notes.append(Note(root, 85, bar_2_start + 1.5, bar_2_start + 1.5 + 0.25))  # F (resolution)

for note in sax_notes:
    sax_instrument.notes.append(note)

# Bass line: chromatic walking line, unique rhythms
bass_notes = []

# Bar 2
bass_notes.append(Note(root + 1, 40, bar_2_start + 0.0, bar_2_start + 0.25))
bass_notes.append(Note(root + 2, 40, bar_2_start + 0.375, bar_2_start + 0.5))
bass_notes.append(Note(root + 3, 40, bar_2_start + 0.75, bar_2_start + 0.875))
bass_notes.append(Note(root + 4, 40, bar_2_start + 1.125, bar_2_start + 1.25))
bass_notes.append(Note(root + 5, 40, bar_2_start + 1.5, bar_2_start + 1.625))

# Bar 3 (1.5 to 3.0)
bass_notes.append(Note(root + 6, 40, bar_2_start + 1.875, bar_2_start + 2.0))
bass_notes.append(Note(root + 7, 40, bar_2_start + 2.25, bar_2_start + 2.375))
bass_notes.append(Note(root + 8, 40, bar_2_start + 2.625, bar_2_start + 2.75))
bass_notes.append(Note(root + 9, 40, bar_2_start + 3.0, bar_2_start + 3.125))

# Bar 4 (3.0 to 4.5)
bass_notes.append(Note(root + 10, 40, bar_2_start + 3.375, bar_2_start + 3.5))
bass_notes.append(Note(root + 11, 40, bar_2_start + 3.75, bar_2_start + 3.875))
bass_notes.append(Note(root + 12, 40, bar_2_start + 4.125, bar_2_start + 4.25))
bass_notes.append(Note(root + 13, 40, bar_2_start + 4.5, bar_2_start + 4.625))

for note in bass_notes:
    bass_instrument.notes.append(note)

# Piano comping: 7th chords on 2 and 4
piano_notes = []

# Bar 2: 7th chord on 2 (beat 2) and 4 (beat 4)
bar_2_beat_2 = bar_2_start + 0.375
bar_2_beat_4 = bar_2_start + 1.125

# Fm7: F, Ab, Bb, C
piano_notes.append(Note(root, 60, bar_2_beat_2, bar_2_beat_2 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_2_beat_2, bar_2_beat_2 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_2_beat_2, bar_2_beat_2 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_2_beat_2, bar_2_beat_2 + 0.25))

piano_notes.append(Note(root, 60, bar_2_beat_4, bar_2_beat_4 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_2_beat_4, bar_2_beat_4 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_2_beat_4, bar_2_beat_4 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_2_beat_4, bar_2_beat_4 + 0.25))

# Bar 3: same structure
bar_3_beat_2 = bar_2_start + 1.875
bar_3_beat_4 = bar_2_start + 2.625

piano_notes.append(Note(root, 60, bar_3_beat_2, bar_3_beat_2 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_3_beat_2, bar_3_beat_2 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_3_beat_2, bar_3_beat_2 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_3_beat_2, bar_3_beat_2 + 0.25))

piano_notes.append(Note(root, 60, bar_3_beat_4, bar_3_beat_4 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_3_beat_4, bar_3_beat_4 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_3_beat_4, bar_3_beat_4 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_3_beat_4, bar_3_beat_4 + 0.25))

# Bar 4: same structure
bar_4_beat_2 = bar_2_start + 3.375
bar_4_beat_4 = bar_2_start + 4.125

piano_notes.append(Note(root, 60, bar_4_beat_2, bar_4_beat_2 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_4_beat_2, bar_4_beat_2 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_4_beat_2, bar_4_beat_2 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_4_beat_2, bar_4_beat_2 + 0.25))

piano_notes.append(Note(root, 60, bar_4_beat_4, bar_4_beat_4 + 0.25))
piano_notes.append(Note(root + 5, 60, bar_4_beat_4, bar_4_beat_4 + 0.25))
piano_notes.append(Note(root + 7, 60, bar_4_beat_4, bar_4_beat_4 + 0.25))
piano_notes.append(Note(root + 9, 60, bar_4_beat_4, bar_4_beat_4 + 0.25))

for note in piano_notes:
    piano_instrument.notes.append(note)

# Write the MIDI to a file
pm.write("dante_intro.mid")
