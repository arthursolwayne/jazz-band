
import pretty_midi

midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)

# Bar 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.5, end=1.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.0, end=1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0))

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0))

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=6.0))

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=6.5, end=7.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=7.0, end=7.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=7.5, end=8.0))

midi.instruments.append(piano)
