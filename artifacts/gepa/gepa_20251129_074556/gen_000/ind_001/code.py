
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
piano = pretty_midi.Instrument(program=0)

# Define note durations and timing
bar_length = 60.0 / 120  # 0.5 seconds per beat
note_length = bar_length / 4  # quarter note

# Bar 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=note_length))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=note_length, end=note_length*2))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*2, end=note_length*3))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=note_length*3, end=note_length*4))  # C

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=note_length*4, end=note_length*5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*5, end=note_length*6))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=note_length*6, end=note_length*7))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*7, end=note_length*8))  # G

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=note_length*8, end=note_length*9))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=note_length*9, end=note_length*10))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*10, end=note_length*11))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=note_length*11, end=note_length*12))  # B

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*12, end=note_length*13))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=note_length*13, end=note_length*14))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=note_length*14, end=note_length*15))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=note_length*15, end=note_length*16))  # G

midi.instruments.append(piano)
