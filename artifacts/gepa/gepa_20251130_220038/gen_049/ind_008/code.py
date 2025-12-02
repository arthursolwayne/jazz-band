
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick
    pretty_midi.note_number_to_midi_note(36, start, 1.0, velocity=100, instrument=drums)
    pretty_midi.note_number_to_midi_note(36, start + 0.75, 1.0, velocity=100, instrument=drums)
    # Snare
    pretty_midi.note_number_to_midi_note(38, start + 0.375, 1.0, velocity=100, instrument=drums)
    pretty_midi.note_number_to_midi_note(38, start + 1.125, 1.0, velocity=100, instrument=drums)
    # Hihat
    for i in range(8):
        pretty_midi.note_number_to_midi_note(42, start + i * 0.1875, 0.1875, velocity=80, instrument=drums)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (30, 0.0),   # Fm7 root
    (29, 0.5),   # chromatic approach
    (30, 1.0),   # Fm7 root
    (31, 1.5),   # Fm7 9
    (30, 2.0),   # Fm7 root
    (29, 2.5),   # chromatic approach
    (30, 3.0),   # Fm7 root
    (31, 3.5),   # Fm7 9
    (30, 4.0),   # Fm7 root
    (29, 4.5),   # chromatic approach
    (30, 5.0),   # Fm7 root
    (31, 5.5),   # Fm7 9
]
for note, time in bass_notes:
    pretty_midi.note_number_to_midi_note(note, 1.5 + time, 0.5, velocity=85, instrument=bass)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.5 + 0.375, 0.25),  # Cm7 (Fm7), 2
    (48, 1.5 + 0.375, 0.25),  # Bb
    (50, 1.5 + 0.375, 0.25),  # C
    (47, 1.5 + 0.375, 0.25),  # Ab
    (50, 1.5 + 1.125, 0.25),  # Cm7, 4
    (48, 1.5 + 1.125, 0.25),  # Bb
    (50, 1.5 + 1.125, 0.25),  # C
    (47, 1.5 + 1.125, 0.25),  # Ab
    (50, 1.5 + 2.375, 0.25),  # Cm7, 2
    (48, 1.5 + 2.375, 0.25),  # Bb
    (50, 1.5 + 2.375, 0.25),  # C
    (47, 1.5 + 2.375, 0.25),  # Ab
    (50, 1.5 + 3.125, 0.25),  # Cm7, 4
    (48, 1.5 + 3.125, 0.25),  # Bb
    (50, 1.5 + 3.125, 0.25),  # C
    (47, 1.5 + 3.125, 0.25),  # Ab
]
for note, time, duration in piano_notes:
    pretty_midi.note_number_to_midi_note(note, time, duration, velocity=100, instrument=piano)

# Drums: continue with same pattern
for bar in range(2, 4):
    start = 1.5 + bar * bar_length
    # Kick
    pretty_midi.note_number_to_midi_note(36, start, 1.0, velocity=100, instrument=drums)
    pretty_midi.note_number_to_midi_note(36, start + 0.75, 1.0, velocity=100, instrument=drums)
    # Snare
    pretty_midi.note_number_to_midi_note(38, start + 0.375, 1.0, velocity=100, instrument=drums)
    pretty_midi.note_number_to_midi_note(38, start + 1.125, 1.0, velocity=100, instrument=drums)
    # Hihat
    for i in range(8):
        pretty_midi.note_number_to_midi_note(42, start + i * 0.1875, 0.1875, velocity=80, instrument=drums)

# Sax (Dante): short motif, make it sing
sax_notes = [
    (51, 1.5, 0.5),     # F (Fm7 root)
    (53, 1.5, 0.5),     # A (Fm7 9)
    (50, 1.5, 0.5),     # C (Fm7 7)
    (48, 1.5, 0.5),     # Bb (Fm7)
    (51, 1.5, 0.5),     # F (Fm7 root)
    (53, 1.5, 0.5),     # A (Fm7 9)
    (50, 1.5, 0.5),     # C (Fm7 7)
    (48, 1.5, 0.5),     # Bb (Fm7)
]
for note, time, duration in sax_notes:
    pretty_midi.note_number_to_midi_note(note, time, duration, velocity=100, instrument=sax)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
