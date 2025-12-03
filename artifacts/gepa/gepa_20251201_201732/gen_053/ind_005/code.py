
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C
bass_notes = [
    (1.5, 53), (1.875, 51), (2.25, 55), (2.625, 52),
    (3.0, 53), (3.375, 51), (3.75, 55), (4.125, 52),
    (4.5, 53), (4.875, 51), (5.25, 55), (5.625, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    # Bar 2: Fm7
    (1.5, 64), (1.5, 70), (1.5, 76), (1.5, 71),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 71), (3.0, 76), (3.0, 64), (3.0, 70),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (4.5, 76), (4.5, 71), (4.5, 81), (4.5, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Ab (67) - C (69) - rest
sax_notes = [
    (1.5, 65), (1.5 + 0.1875, 67), (1.5 + 0.375, 69),  # first motif
    (3.0, 65), (3.0 + 0.1875, 67), (3.0 + 0.375, 69)   # resolution
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
