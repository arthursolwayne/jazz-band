
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
    (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 6.0s)
# Drums: kick=36, snare=38, hihat=42

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 59), (1.875, 60), (2.25, 58), (2.625, 57),
    # Bar 3
    (3.0, 56), (3.375, 57), (3.75, 58), (4.125, 59),
    # Bar 4
    (4.5, 60), (4.875, 58), (5.25, 57), (5.625, 56)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 76),
    # Bar 3
    (3.375, 62), (3.375, 67), (3.375, 71), (3.375, 76),
    # Bar 4
    (4.875, 62), (4.875, 67), (4.875, 71), (4.875, 76)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax, short motif, sing it, leave it hanging
sax_notes = [
    # Bar 2
    (1.5, 65), (1.625, 67), (1.75, 69), (1.875, 67),
    # Bar 3
    (2.25, 65), (2.375, 67), (2.5, 69), (2.625, 67),
    # Bar 4
    (3.0, 65), (3.125, 67), (3.25, 69), (3.375, 67),
    # Final motif
    (3.75, 65), (3.875, 67), (4.0, 69), (4.125, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
