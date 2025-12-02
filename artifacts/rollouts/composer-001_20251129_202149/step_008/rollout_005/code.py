
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
]

for time, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 60), (1.75, 61), (2.0, 62), (2.25, 63),
    # Bar 3
    (2.5, 63), (2.75, 62), (3.0, 61), (3.25, 60),
    # Bar 4
    (3.5, 60), (3.75, 61), (4.0, 62), (4.25, 63),
]
for time, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 64), (1.75, 67), (1.75, 71), (1.75, 72),
    (2.25, 64), (2.25, 67), (2.25, 71), (2.25, 72),
    # Bar 3
    (2.75, 65), (2.75, 68), (2.75, 72), (2.75, 73),
    (3.25, 65), (3.25, 68), (3.25, 72), (3.25, 73),
    # Bar 4
    (3.75, 66), (3.75, 69), (3.75, 73), (3.75, 74),
    (4.25, 66), (4.25, 69), (4.25, 73), (4.25, 74),
]
for time, note in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (1.5, 62), (1.75, 64), (2.0, 62), (2.25, 64),
    # Bar 3
    (2.75, 65), (3.0, 67), (3.25, 65), (3.5, 67),
    # Bar 4
    (3.75, 69), (4.0, 71), (4.25, 69), (4.5, 71),
]
for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums continue: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42),
]
for time, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
