
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 72), (1.75, 71), (2.0, 70), (2.25, 72),
    (2.5, 74), (2.75, 72), (3.0, 71), (3.25, 70),
    (3.5, 68), (3.75, 69), (4.0, 71), (4.25, 72),
    (4.5, 74), (4.75, 72), (5.0, 71), (5.25, 70)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 64), (2.0, 69), (2.0, 71), (2.0, 76),
    (3.0, 64), (3.0, 69), (3.0, 71), (3.0, 76),
    (4.0, 64), (4.0, 69), (4.0, 71), (4.0, 76)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 chord: F, A, C, E
sax_notes = [
    (1.5, 77), (1.6, 82), (1.7, 79), (1.8, 77),
    (3.0, 77), (3.1, 82), (3.2, 79), (3.3, 77),
    (4.5, 77), (4.6, 82), (4.7, 79), (4.8, 77)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
