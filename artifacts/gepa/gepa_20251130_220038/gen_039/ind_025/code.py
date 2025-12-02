
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62), (1.875, 60), (2.25, 59), (2.625, 62),
    (3.0, 64), (3.375, 62), (3.75, 60), (4.125, 59),
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 60),
    (6.0, 59)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 62), (1.5, 67), (1.5, 70),  # Dm7
    (1.875, 62), (1.875, 67), (1.875, 70),  # Dm7
    (2.25, 62), (2.25, 67), (2.25, 70),  # Dm7
    (2.625, 62), (2.625, 67), (2.625, 70),  # Dm7

    # Bar 3
    (3.0, 62), (3.0, 67), (3.0, 70),  # Dm7
    (3.375, 62), (3.375, 67), (3.375, 70),  # Dm7
    (3.75, 62), (3.75, 67), (3.75, 70),  # Dm7
    (4.125, 62), (4.125, 67), (4.125, 70),  # Dm7

    # Bar 4
    (4.5, 62), (4.5, 67), (4.5, 70),  # Dm7
    (4.875, 62), (4.875, 67), (4.875, 70),  # Dm7
    (5.25, 62), (5.25, 67), (5.25, 70),  # Dm7
    (5.625, 62), (5.625, 67), (5.625, 70),  # Dm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Saxophone - short motif, restrained, emotional
sax_notes = [
    (1.5, 62), (1.875, 64), (2.25, 62), (2.625, 60),
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 60),
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 60)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
