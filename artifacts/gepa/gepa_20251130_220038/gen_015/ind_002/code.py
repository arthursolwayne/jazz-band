
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (1.5, 53), (1.75, 54), (2.0, 55), (2.25, 57),
    (2.5, 59), (2.75, 60), (3.0, 62), (3.25, 63),
    (3.5, 65), (3.75, 67), (4.0, 69), (4.25, 71),
    (4.5, 72), (4.75, 74), (5.0, 76), (5.25, 77)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 62), (2.0, 67), (2.0, 71), (2.0, 76),  # F7
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76),  # F7
    (4.0, 62), (4.0, 67), (4.0, 71), (4.0, 76)   # F7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 66), (1.5 + 0.375, 69), (1.5 + 0.75, 71), (1.5 + 1.125, 69),
    (2.75, 66), (2.75 + 0.375, 69), (2.75 + 0.75, 71), (2.75 + 1.125, 69),
    (4.5, 66), (4.5 + 0.375, 69), (4.5 + 0.75, 71), (4.5 + 1.125, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
