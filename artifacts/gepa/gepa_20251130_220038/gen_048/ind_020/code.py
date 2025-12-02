
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 38), (0.375, 42), (0.75, 38), (1.125, 42), (1.5, 36),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 39), (1.875, 40), (2.25, 41), (2.625, 39),
    (3.0, 40), (3.375, 41), (3.75, 42), (4.125, 40),
    # Bar 3 (3.0 - 4.5s)
    (4.5, 39), (4.875, 40), (5.25, 41), (5.625, 39),
    (6.0, 40), (6.375, 41), (6.75, 42), (7.125, 40),
    # Bar 4 (4.5 - 6.0s)
    (7.5, 39), (7.875, 40), (8.25, 41), (8.625, 39),
    (9.0, 40), (9.375, 41), (9.75, 42), (10.125, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.5, 69), (1.5, 71), (1.5, 76),  # Fm7
    (2.0, 64), (2.0, 69), (2.0, 71), (2.0, 76),  # Fm7
    (2.5, 64), (2.5, 69), (2.5, 71), (2.5, 76),  # Fm7
    (3.0, 64), (3.0, 69), (3.0, 71), (3.0, 76),  # Fm7

    # Bar 3 (3.0 - 4.5s)
    (3.0, 64), (3.0, 69), (3.0, 71), (3.0, 76),  # Fm7
    (3.5, 64), (3.5, 69), (3.5, 71), (3.5, 76),  # Fm7
    (4.0, 64), (4.0, 69), (4.0, 71), (4.0, 76),  # Fm7
    (4.5, 64), (4.5, 69), (4.5, 71), (4.5, 76),  # Fm7

    # Bar 4 (4.5 - 6.0s)
    (4.5, 64), (4.5, 69), (4.5, 71), (4.5, 76),  # Fm7
    (5.0, 64), (5.0, 69), (5.0, 71), (5.0, 76),  # Fm7
    (5.5, 64), (5.5, 69), (5.5, 71), (5.5, 76),  # Fm7
    (6.0, 64), (6.0, 69), (6.0, 71), (6.0, 76)   # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): Motif - short, singable, starts on F, ends on G#
sax_notes = [
    (1.5, 65), (1.75, 68), (2.0, 71), (2.25, 72),  # F -> A -> C -> C#
    (2.5, 68), (2.75, 65), (3.0, 68), (3.25, 71),  # A -> F -> A -> C
    (3.5, 71), (3.75, 72), (4.0, 68), (4.25, 65),  # C -> C# -> A -> F
    (4.5, 65), (4.75, 68), (5.0, 71), (5.25, 72),  # F -> A -> C -> C#
    (5.5, 68), (5.75, 65), (6.0, 68), (6.25, 71)   # A -> F -> A -> C
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums continue for the full 6 seconds
drum_notes_second_half = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42), (3.0, 36),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42), (3.0, 42),
    
    # Bar 3 (3.0 - 4.5s)
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42), (4.5, 36),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42),
    
    # Bar 4 (4.5 - 6.0s)
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42), (6.0, 36),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42)
]
for time, note in drum_notes_second_half:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
