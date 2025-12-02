
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
# F7 chord: F, A, C, E, Bb
bass_notes = [
    (1.5, 65), (1.75, 66), (2.0, 64), (2.25, 65),  # F, Gb, Eb, F
    (2.5, 66), (2.75, 67), (3.0, 65), (3.25, 66),  # Gb, G, F, Gb
    (3.5, 64), (3.75, 65), (4.0, 66), (4.25, 67),  # Eb, F, Gb, G
    (4.5, 65), (4.75, 66), (5.0, 64), (5.25, 65)   # F, Gb, Eb, F
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
# F7: F, A, C, E
piano_notes = [
    (1.5, 77), (1.5, 82), (1.5, 79), (1.5, 83),  # F, A, C, E
    (2.25, 79), (2.25, 83), (2.25, 80), (2.25, 84),  # Bb, D, F, A
    (3.0, 77), (3.0, 82), (3.0, 79), (3.0, 83),  # F, A, C, E
    (3.75, 79), (3.75, 83), (3.75, 80), (3.75, 84),  # Bb, D, F, A
    (4.5, 77), (4.5, 82), (4.5, 79), (4.5, 83)   # F, A, C, E
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (2.875, 38), (3.125, 42), (3.5, 36), (3.875, 42),
    (4.125, 38), (4.375, 42), (4.75, 36), (5.125, 42),
    (5.375, 38), (5.625, 42), (6.0, 36), (6.375, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, Eb (F7 arpeggio), then repeat with a twist
sax_notes = [
    (1.5, 87), (1.75, 80), (2.0, 82), (2.25, 84),  # F, Bb, C, Eb
    (2.5, 87), (2.75, 80), (3.0, 82), (3.25, 84),  # F, Bb, C, Eb
    (3.5, 87), (3.75, 80), (4.0, 82), (4.25, 84),  # F, Bb, C, Eb
    (4.5, 87), (4.75, 80), (5.0, 82), (5.25, 84)   # F, Bb, C, Eb
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
