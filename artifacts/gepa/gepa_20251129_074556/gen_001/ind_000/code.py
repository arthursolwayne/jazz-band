
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
piano = pretty_midi.Instrument(program=0)

# Define note durations and timing
note_duration = 0.5
bar_length = 4.0  # 4 beats per bar at 120 BPM (each beat is 0.5 seconds)

# Bar 1: Cmaj7 chord (C, E, G, B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.0, end=note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=0.0, end=note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=note_duration))

# Bar 2: Dm7 chord (D, F, A, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_length, end=bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_length, end=bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_length, end=bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar_length, end=bar_length + note_duration))

# Bar 3: G7 chord (G, B, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2 * bar_length, end=2 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2 * bar_length, end=2 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2 * bar_length, end=2 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2 * bar_length, end=2 * bar_length + note_duration))

# Bar 4: Cmaj7 chord (C, E, G, B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3 * bar_length, end=3 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3 * bar_length, end=3 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3 * bar_length, end=3 * bar_length + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3 * bar_length, end=3 * bar_length + note_duration))

midi.instruments.append(piano)
