
# Bar 1: Drums only
drum_notes = [
    (0.0, 36),  # Kick on downbeat
    (0.25, 42), # Hi-hat on offbeat
    (0.5, 36),  # Kick
    (0.75, 42), # Hi-hat
    (1.0, 36),  # Kick
    (1.25, 42), # Hi-hat
    (1.5, 36)   # Kick
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    drums.notes.append(drum_note)
