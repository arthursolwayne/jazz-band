
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 42), (1.75, 43), (2.0, 41), (2.25, 40),
    (2.5, 42), (2.75, 43), (3.0, 41), (3.25, 40),
    (3.5, 42), (3.75, 43), (4.0, 41), (4.25, 40),
    (4.5, 42), (4.75, 43), (5.0, 41), (5.25, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62), (2.0, 67), (2.0, 72), (2.0, 76),
    # Bar 3
    (3.0, 60), (3.0, 65), (3.0, 70), (3.0, 74),
    # Bar 4
    (4.0, 62), (4.0, 67), (4.0, 72), (4.0, 76)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F7, A7, G7, Bb7 (F, A, G, Bb)
# Bar 2: F, A, G (start it)
# Bar 3: Bb (leave it hanging)
# Bar 4: F, A, G, Bb (finish it)

sax_notes = [
    (2.0, 77),  # F7
    (2.25, 82), # A7
    (2.5, 81),  # G7
    (3.0, 80),  # Bb7 (hanging)
    (3.5, 77),  # F7
    (3.75, 82), # A7
    (4.0, 81),  # G7
    (4.25, 80)  # Bb7
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
