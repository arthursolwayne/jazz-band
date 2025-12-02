
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2, G2, A2, Bb2, B2, C3, D3, Eb3)
bass_notes = [
    (1.5, 77), (1.875, 78), (2.25, 80), (2.625, 81),
    (3.0, 82), (3.375, 84), (3.75, 86), (4.125, 87)
]
for start, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note_obj)

# Diane: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (1.5, 77), (1.5, 82), (1.5, 87), (1.5, 91),
    (1.875, 77), (1.875, 82), (1.875, 87), (1.875, 91),
    (2.25, 77), (2.25, 82), (2.25, 87), (2.25, 91),
    (2.625, 77), (2.625, 82), (2.625, 87), (2.625, 91)
]
for start, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 76), (3.0, 80), (3.0, 87), (3.0, 88),
    (3.375, 76), (3.375, 80), (3.375, 87), (3.375, 88),
    (3.75, 76), (3.75, 80), (3.75, 87), (3.75, 88),
    (4.125, 76), (4.125, 80), (4.125, 87), (4.125, 88)
]
for start, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# Bar 4: C7 (C, E, G, B)
piano_notes = [
    (4.5, 84), (4.5, 88), (4.5, 91), (4.5, 95),
    (4.875, 84), (4.875, 88), (4.875, 91), (4.875, 95),
    (5.25, 84), (5.25, 88), (5.25, 91), (5.25, 95),
    (5.625, 84), (5.625, 88), (5.625, 91), (5.625, 95)
]
for start, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# Dante: Sax solo (start with F, A, Bb, and end with a suspended line)
sax_notes = [
    (1.5, 87), (1.625, 91), (1.75, 90), (1.875, 90),
    (2.0, 87), (2.125, 91), (2.25, 90), (2.375, 90),
    (2.5, 87), (2.625, 91), (2.75, 90), (2.875, 90),
    (3.0, 87), (3.125, 91), (3.25, 90), (3.375, 90),
    (3.5, 87), (3.625, 91), (3.75, 90), (3.875, 90),
    (4.0, 87), (4.125, 91), (4.25, 90), (4.375, 90),
    (4.5, 87), (4.625, 91), (4.75, 90), (4.875, 90),
    (5.0, 87), (5.125, 91), (5.25, 90), (5.375, 90),
    (5.5, 87), (5.625, 91), (5.75, 90), (5.875, 90)
]
for start, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    sax.notes.append(note_obj)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
