
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
    (0.0, 36, 127), (0.375, 42, 127),
    (0.75, 38, 127), (1.125, 42, 127),
    (1.5, 36, 127), (1.875, 42, 127),
    (2.25, 38, 127), (2.625, 42, 127)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 54, 100), (1.875, 53, 100),
    (2.25, 52, 100), (2.625, 55, 100),
    (3.0, 56, 100), (3.375, 55, 100),
    (3.75, 54, 100), (4.125, 53, 100),
    (4.5, 52, 100), (4.875, 55, 100),
    (5.25, 56, 100), (5.625, 57, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Chord on beat 2
    (2.25, 64, 100), (2.25, 67, 100), (2.25, 69, 100), (2.25, 71, 100),
    # Bar 3: Chord on beat 4
    (3.625, 64, 100), (3.625, 67, 100), (3.625, 69, 100), (3.625, 71, 100),
    # Bar 4: Chord on beat 2
    (4.875, 64, 100), (4.875, 67, 100), (4.875, 69, 100), (4.875, 71, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Sax: Short motif, make it sing, leave it hanging
sax_notes = [
    (1.5, 61, 100), (1.75, 63, 100), (2.0, 61, 100),
    (2.5, 63, 100), (2.75, 61, 100), (3.0, 63, 100),
    (4.0, 61, 100), (4.25, 63, 100), (4.5, 61, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
