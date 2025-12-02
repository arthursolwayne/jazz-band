
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
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 36),
    (1.875, 38), (2.25, 42), (2.625, 42), (3.0, 42),
    (3.375, 36), (3.75, 38), (4.125, 42), (4.5, 42), (4.875, 42),
    (5.25, 36), (5.625, 38), (6.0, 42)
]

for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62), (1.875, 63), (2.25, 64), (2.625, 65),
    (3.0, 67), (3.375, 68), (3.75, 70), (4.125, 71),
    (4.5, 72), (4.875, 71), (5.25, 70), (5.625, 68),
    (6.0, 67)
]

for time, note in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords comping on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 72), (1.5, 74),  # D7
    (2.25, 67), (2.25, 71), (2.25, 72), (2.25, 74),  # D7
    (3.0, 67), (3.0, 71), (3.0, 72), (3.0, 74),  # D7
    (3.75, 67), (3.75, 71), (3.75, 72), (3.75, 74),  # D7
    (4.5, 67), (4.5, 71), (4.5, 72), (4.5, 74),  # D7
    (5.25, 67), (5.25, 71), (5.25, 72), (5.25, 74)   # D7
]

for time, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Dante: Tenor sax, short motif that sings and builds
sax_notes = [
    (1.5, 65), (1.625, 67), (1.75, 71), (1.875, 72),  # D, E, G, A
    (2.25, 69), (2.375, 67), (2.5, 64), (2.625, 65),  # Bb, G, D, D
    (3.0, 65), (3.125, 67), (3.25, 71), (3.375, 72),  # D, E, G, A
    (4.5, 65), (4.625, 67), (4.75, 71), (4.875, 72),  # D, E, G, A
    (5.25, 69), (5.375, 67), (5.5, 64), (5.625, 65)   # Bb, G, D, D
]

for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
