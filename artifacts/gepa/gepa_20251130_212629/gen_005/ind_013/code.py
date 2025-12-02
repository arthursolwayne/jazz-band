
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass = pretty_midi.Instrument(program=bass_program)
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
piano = pretty_midi.Instrument(program=piano_program)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Time in seconds per beat: 60 / 160 = 0.375
beat_duration = 0.375
bar_duration = beat_duration * 4  # 1.5s per bar

# FUNCTION: Add a note to an instrument
def add_note(instrument, note_number, start, duration):
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    instrument.notes.append(note)

# 1. Bar 1: Drums only — set the mood
# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
bar_1_start = 0.0

# Kick on 1
add_note(drums, pretty_midi.note_number_to_name(36), bar_1_start, beat_duration)
# Snare on 2
add_note(drums, pretty_midi.note_number_to_name(38), bar_1_start + beat_duration, beat_duration)
# Kick on 3
add_note(drums, pretty_midi.note_number_to_name(36), bar_1_start + beat_duration * 2, beat_duration)
# Snare on 4
add_note(drums, pretty_midi.note_number_to_name(38), bar_1_start + beat_duration * 3, beat_duration)
# Hihat on every eighth
for i in range(8):
    add_note(drums, pretty_midi.note_number_to_name(42), bar_1_start + i * beat_duration / 2, beat_duration / 2)

# 2. Bar 2: Everyone comes in, sax starts the motif in F
bar_2_start = bar_duration

# Bass line (walking, chromatic)
# F -> G -> Ab -> Bb -> C -> D -> Eb -> F
notes = [71, 72, 70, 69, 72, 74, 72, 71]  # F, G, Ab, Bb, C, D, Eb, F
for i, note in enumerate(notes):
    add_note(bass, note, bar_2_start + i * beat_duration, beat_duration)

# Piano comping – 7th chords on 2 & 4
# F7 (F, A, C, Eb) on beat 2
add_note(piano, 71, bar_2_start + beat_duration, beat_duration)
add_note(piano, 74, bar_2_start + beat_duration, beat_duration)
add_note(piano, 72, bar_2_start + beat_duration, beat_duration)
add_note(piano, 69, bar_2_start + beat_duration, beat_duration)
# F7 again on beat 4
add_note(piano, 71, bar_2_start + beat_duration * 3, beat_duration)
add_note(piano, 74, bar_2_start + beat_duration * 3, beat_duration)
add_note(piano, 72, bar_2_start + beat_duration * 3, beat_duration)
add_note(piano, 69, bar_2_start + beat_duration * 3, beat_duration)

# Saxophone motif: F -> Bb -> D -> rest
add_note(sax, 71, bar_2_start, beat_duration)  # F
add_note(sax, 69, bar_2_start + beat_duration, beat_duration)  # Bb
add_note(sax, 74, bar_2_start + beat_duration * 2, beat_duration)  # D
# Rest on final beat

# 3. Bar 3: Sax continues, bass moves, piano continues comping

bar_3_start = bar_2_start + bar_duration

# Bass line: F -> G -> Ab -> Bb, then chromatic up
notes = [71, 72, 70, 69, 70, 72, 74, 72]
for i, note in enumerate(notes):
    add_note(bass, note, bar_3_start + i * beat_duration, beat_duration)

# Piano continues comping (F7 on 2 and 4)
add_note(piano, 71, bar_3_start + beat_duration, beat_duration)
add_note(piano, 74, bar_3_start + beat_duration, beat_duration)
add_note(piano, 72, bar_3_start + beat_duration, beat_duration)
add_note(piano, 69, bar_3_start + beat_duration, beat_duration)
add_note(piano, 71, bar_3_start + beat_duration * 3, beat_duration)
add_note(piano, 74, bar_3_start + beat_duration * 3, beat_duration)
add_note(piano, 72, bar_3_start + beat_duration * 3, beat_duration)
add_note(piano, 69, bar_3_start + beat_duration * 3, beat_duration)

# Saxophone continues with motif variation
# F -> Bb -> C -> rest
add_note(sax, 71, bar_3_start, beat_duration)  # F
add_note(sax, 69, bar_3_start + beat_duration, beat_duration)  # Bb
add_note(sax, 72, bar_3_start + beat_duration * 2, beat_duration)  # C
# Rest on 4

# 4. Bar 4: Resolution, sax completes the motif

bar_4_start = bar_3_start + bar_duration

# Bass line: F -> G -> Ab -> Bb -> C -> D -> Eb -> F
notes = [71, 72, 70, 69, 72, 74, 72, 71]
for i, note in enumerate(notes):
    add_note(bass, note, bar_4_start + i * beat_duration, beat_duration)

# Piano continues comping
add_note(piano, 71, bar_4_start + beat_duration, beat_duration)
add_note(piano, 74, bar_4_start + beat_duration, beat_duration)
add_note(piano, 72, bar_4_start + beat_duration, beat_duration)
add_note(piano, 69, bar_4_start + beat_duration, beat_duration)
add_note(piano, 71, bar_4_start + beat_duration * 3, beat_duration)
add_note(piano, 74, bar_4_start + beat_duration * 3, beat_duration)
add_note(piano, 72, bar_4_start + beat_duration * 3, beat_duration)
add_note(piano, 69, bar_4_start + beat_duration * 3, beat_duration)

# Saxophone completes motif: F -> Bb -> D -> F
add_note(sax, 71, bar_4_start + beat_duration * 2, beat_duration)  # D
add_note(sax, 71, bar_4_start + beat_duration * 3, beat_duration)  # F

# Add the drum pattern again to complete the 4-bar cycle
bar_1_start = bar_4_start
# Kick on 1
add_note(drums, pretty_midi.note_number_to_name(36), bar_1_start, beat_duration)
# Snare on 2
add_note(drums, pretty_midi.note_number_to_name(38), bar_1_start + beat_duration, beat_duration)
# Kick on 3
add_note(drums, pretty_midi.note_number_to_name(36), bar_1_start + beat_duration * 2, beat_duration)
# Snare on 4
add_note(drums, pretty_midi.note_number_to_name(38), bar_1_start + beat_duration * 3, beat_duration)
# Hihat on every eighth
for i in range(8):
    add_note(drums, pretty_midi.note_number_to_name(42), bar_1_start + i * beat_duration / 2, beat_duration / 2)

# Save the MIDI file
pm.write('jazz_intro.mid')
