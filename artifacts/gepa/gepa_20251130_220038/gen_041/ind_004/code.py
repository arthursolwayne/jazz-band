
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
]

for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 70), (1.875, 69), (2.25, 71), (2.625, 72),
    # Bar 3
    (3.0, 72), (3.375, 71), (3.75, 70), (4.125, 69),
    # Bar 4
    (4.5, 69), (4.875, 70), (5.25, 71), (5.625, 72),
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 67), (1.875, 69), (1.875, 71),
    (2.625, 64), (2.625, 67), (2.625, 69), (2.625, 71),
    # Bar 3
    (3.375, 64), (3.375, 67), (3.375, 69), (3.375, 71),
    (4.125, 64), (4.125, 67), (4.125, 69), (4.125, 71),
    # Bar 4
    (4.875, 64), (4.875, 67), (4.875, 69), (4.875, 71),
    (5.625, 64), (5.625, 67), (5.625, 69), (5.625, 71),
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: short motif, start it, leave it hanging
sax_notes = [
    (1.5, 62), (1.5 + 0.25, 65), (1.5 + 0.5, 67), (1.5 + 0.75, 69),
    (1.5 + 1.0, 71), (1.5 + 1.25, 69), (1.5 + 1.5, 67), (1.5 + 1.75, 65),
    (1.5 + 2.0, 62), (1.5 + 2.25, 64), (1.5 + 2.5, 66), (1.5 + 2.75, 68),
    (1.5 + 3.0, 70), (1.5 + 3.25, 68), (1.5 + 3.5, 66), (1.5 + 3.75, 64),
    (1.5 + 4.0, 62), (1.5 + 4.25, 65), (1.5 + 4.5, 67), (1.5 + 4.75, 69)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
