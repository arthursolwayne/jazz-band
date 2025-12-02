
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (1.875, 42), (2.25, 38), (2.625, 42), (3.0, 36), (3.375, 42),
    (3.75, 36), (4.125, 42), (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42), (7.5, 38),
    (7.875, 42), (8.25, 38), (8.625, 42), (9.0, 36), (9.375, 42),
    (9.75, 36), (10.125, 42), (10.5, 38), (10.875, 42), (11.25, 38), (11.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [
    (1.5, 62), (1.875, 60), (2.25, 59), (2.625, 62), (3.0, 62), (3.375, 60), (3.75, 59), (4.125, 62),
    (4.5, 62), (4.875, 60), (5.25, 59), (5.625, 62), (6.0, 62), (6.375, 60), (6.75, 59), (7.125, 62),
    (7.5, 62), (7.875, 60), (8.25, 59), (8.625, 62), (9.0, 62), (9.375, 60), (9.75, 59), (10.125, 62),
    (10.5, 62), (10.875, 60), (11.25, 59), (11.625, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 70), (1.5, 72), # Dm7
    (2.25, 64), (2.25, 67), (2.25, 70), (2.25, 72), # Dm7
    (3.0, 64), (3.0, 67), (3.0, 70), (3.0, 72), # Dm7
    (3.75, 64), (3.75, 67), (3.75, 70), (3.75, 72), # Dm7
    (4.5, 64), (4.5, 67), (4.5, 70), (4.5, 72), # Dm7
    (5.25, 64), (5.25, 67), (5.25, 70), (5.25, 72), # Dm7
    (6.0, 64), (6.0, 67), (6.0, 70), (6.0, 72), # Dm7
    (6.75, 64), (6.75, 67), (6.75, 70), (6.75, 72), # Dm7
    (7.5, 64), (7.5, 67), (7.5, 70), (7.5, 72), # Dm7
    (8.25, 64), (8.25, 67), (8.25, 70), (8.25, 72), # Dm7
    (9.0, 64), (9.0, 67), (9.0, 70), (9.0, 72), # Dm7
    (9.75, 64), (9.75, 67), (9.75, 70), (9.75, 72), # Dm7
    (10.5, 64), (10.5, 67), (10.5, 70), (10.5, 72), # Dm7
    (11.25, 64), (11.25, 67), (11.25, 70), (11.25, 72) # Dm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax - short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    (1.5, 74), (1.875, 76), (2.25, 72), (2.625, 74), (3.0, 76), (3.375, 74),
    # Bar 3: Leave it hanging
    (3.75, 72), (4.125, 74), (4.5, 76), (4.875, 74), (5.25, 72), (5.625, 74),
    # Bar 4: Finish it
    (6.0, 72), (6.375, 74), (6.75, 76), (7.125, 74), (7.5, 72), (7.875, 74),
    (8.25, 72), (8.625, 74), (9.0, 76), (9.375, 74), (9.75, 72), (10.125, 74)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
