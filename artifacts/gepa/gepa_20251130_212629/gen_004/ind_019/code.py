
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb

# Define the time signature (4/4)
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define the instruments
# 1. Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = Instrument(program=drums_program, is_drum=True)
pm.instruments.append(drum_instrument)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Tenor Sax (Dante)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Define the beat length (0.375 seconds per beat at 160 BPM)
beat_length = 0.375  # seconds per beat

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_1_start = 0.0

# Kick on beat 1
drum_instrument.notes.append(Note(36, 60, bar_1_start, bar_1_start + 0.1))

# Kick on beat 3
drum_instrument.notes.append(Note(36, 60, bar_1_start + 2 * beat_length, bar_1_start + 2 * beat_length + 0.1))

# Snare on beat 2
drum_instrument.notes.append(Note(38, 60, bar_1_start + 1 * beat_length, bar_1_start + 1 * beat_length + 0.1))

# Snare on beat 4
drum_instrument.notes.append(Note(38, 60, bar_1_start + 3 * beat_length, bar_1_start + 3 * beat_length + 0.1))

# Hihat on every eighth note
for i in range(8):
    start = bar_1_start + i * beat_length / 2
    drum_instrument.notes.append(Note(42, 60, start, start + 0.05))

# Bar 2: All instruments in
# Tenor Sax (Dante) plays the melody
bar_2_start = bar_1_start + 1.5  # 1.5 seconds

# Tenor sax motif: F, Bb, Ab, rest
sax_instrument.notes.append(Note(66, 60, bar_2_start, bar_2_start + 0.375))  # F
sax_instrument.notes.append(Note(64, 62, bar_2_start + 0.75, bar_2_start + 1.125))  # Bb
sax_instrument.notes.append(Note(62, 63, bar_2_start + 1.5, bar_2_start + 1.875))  # Ab
# Rest for the last 0.375 seconds

# Bass line: walking line with chromatic approaches
# F, Gb, Ab, Bb, B, Db, Eb, F
bass_notes = [53, 52, 51, 50, 49, 48, 47, 53]
for i, note in enumerate(bass_notes):
    start = bar_2_start + i * beat_length
    duration = beat_length
    bass_instrument.notes.append(Note(note, 60, start, start + duration))

# Piano chord: 7th chords on 2 and 4
# Bar 2: 2nd beat: F7 (F, A, C, Eb), 4th beat: Bb7 (Bb, D, F, Ab)

# 2nd beat: F7
piano_notes = [53, 58, 60, 57]
for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_2_start + 1 * beat_length, bar_2_start + 1 * beat_length + 0.1))

# 4th beat: Bb7
piano_notes = [50, 55, 53, 51]
for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_2_start + 3 * beat_length, bar_2_start + 3 * beat_length + 0.1))

# Bar 3: Tenor sax motif continues
bar_3_start = bar_2_start + 1.5

# Tenor sax: Repeat the motif but ends with a resolution
# F, Bb, Ab, F
sax_instrument.notes.append(Note(66, 60, bar_3_start, bar_3_start + 0.375))  # F
sax_instrument.notes.append(Note(64, 62, bar_3_start + 0.75, bar_3_start + 1.125))  # Bb
sax_instrument.notes.append(Note(62, 63, bar_3_start + 1.5, bar_3_start + 1.875))  # Ab
sax_instrument.notes.append(Note(66, 60, bar_3_start + 1.875, bar_3_start + 2.25))  # F

# Bass line (same as Bar 2, shifted)
for i, note in enumerate(bass_notes):
    start = bar_3_start + i * beat_length
    duration = beat_length
    bass_instrument.notes.append(Note(note, 60, start, start + duration))

# Piano: 7th chords again
# 2nd beat: F7, 4th beat: Bb7
# 2nd beat: F7
for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_3_start + 1 * beat_length, bar_3_start + 1 * beat_length + 0.1))

# 4th beat: Bb7
for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_3_start + 3 * beat_length, bar_3_start + 3 * beat_length + 0.1))

# Bar 4: Tenor sax resolves, everyone fades out
bar_4_start = bar_3_start + 1.5

# Tenor sax: Long note on F, resolves
sax_instrument.notes.append(Note(66, 60, bar_4_start, bar_4_start + 0.75))  # F

# Bass line: F, Gb, Ab, Bb
bass_notes = [53, 52, 51, 50]
for i, note in enumerate(bass_notes):
    start = bar_4_start + i * beat_length
    duration = beat_length
    bass_instrument.notes.append(Note(note, 60, start, start + duration))

# Piano: 7th chords again
# 2nd beat: F7, 4th beat: Bb7
for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_4_start + 1 * beat_length, bar_4_start + 1 * beat_length + 0.1))

for note in piano_notes:
    piano_instrument.notes.append(Note(note, 60, bar_4_start + 3 * beat_length, bar_4_start + 3 * beat_length + 0.1))

# Drums: same pattern as Bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Kick on beat 1
drum_instrument.notes.append(Note(36, 60, bar_4_start, bar_4_start + 0.1))

# Kick on beat 3
drum_instrument.notes.append(Note(36, 60, bar_4_start + 2 * beat_length, bar_4_start + 2 * beat_length + 0.1))

# Snare on beat 2
drum_instrument.notes.append(Note(38, 60, bar_4_start + 1 * beat_length, bar_4_start + 1 * beat_length + 0.1))

# Snare on beat 4
drum_instrument.notes.append(Note(38, 60, bar_4_start + 3 * beat_length, bar_4_start + 3 * beat_length + 0.1))

# Hihat on every eighth note
for i in range(8):
    start = bar_4_start + i * beat_length / 2
    drum_instrument.notes.append(Note(42, 60, start, start + 0.05))

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
