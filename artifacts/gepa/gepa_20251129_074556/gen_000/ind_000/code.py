
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
piano = pretty_midi.Instrument(program=0)

# Define note durations and timing
quarter = 0.5
bar = 2.0

# Bar 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=quarter))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=quarter, end=bar))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar, end=bar + quarter))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar + quarter, end=bar * 2))  # C4

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar * 2, end=bar * 2 + quarter))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar * 2 + quarter, end=bar * 3))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar * 3, end=bar * 3 + quarter))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar * 3 + quarter, end=bar * 4))  # G4

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar * 4, end=bar * 4 + quarter))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar * 4 + quarter, end=bar * 5))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar * 5, end=bar * 5 + quarter))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar * 5 + quarter, end=bar * 6))  # G4

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar * 6, end=bar * 6 + quarter))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar * 6 + quarter, end=bar * 7))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar * 7, end=bar * 7 + quarter))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar * 7 + quarter, end=bar * 8))  # C4

midi.instruments.append(piano)
