
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)
piano = pretty_midi.Instrument(program=0)

# Bar 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=1.0))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.0, end=2.0))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=3.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.0))  # C4

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=5.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=6.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=7.0))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=7.0, end=8.0))  # G4

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=8.0, end=9.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=9.0, end=10.0)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=10.0, end=11.0))# B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=11.0, end=12.0))# G4

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=12.0, end=13.0))# C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=13.0, end=14.0))# E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=14.0, end=15.0))# G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=15.0, end=16.0))# C4

midi.instruments.append(piano)
