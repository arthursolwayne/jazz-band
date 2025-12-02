
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
    (0.0, 36),  # Kick on 1
    (0.375, 42),  # Hihat on &1
    (0.75, 42),   # Hihat on &2
    (1.125, 38),  # Snare on 2
    (1.5, 36),    # Kick on 3
    (1.875, 42),  # Hihat on &3
    (2.25, 42),   # Hihat on &4
    (2.625, 38)   # Snare on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 64),  # F
    (1.875, 65),  # Gb
    (2.25, 67),  # A
    (2.625, 69),  # Bb
    (3.0, 69),   # Bb
    (3.375, 67),  # A
    (3.75, 65),  # Gb
    (4.125, 64),  # F
    (4.5, 69),   # Bb
    (4.875, 71),  # C
    (5.25, 72),  # C#
    (5.625, 71),  # C
    (6.0, 69),   # Bb
    (6.375, 67),  # A
    (6.75, 65),  # Gb
    (7.125, 64)   # F
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64),  # F7: F, A, C, Eb
    (1.5, 69),
    (1.5, 76),
    (1.5, 67),
    (2.25, 64),  # F7 again
    (2.25, 69),
    (2.25, 76),
    (2.25, 67),
    (3.0, 69),  # Bb7: Bb, D, F, Ab
    (3.0, 71),
    (3.0, 76),
    (3.0, 67),
    (3.75, 69),
    (3.75, 71),
    (3.75, 76),
    (3.75, 67),
    (4.5, 64),  # F7 again
    (4.5, 69),
    (4.5, 76),
    (4.5, 67),
    (5.25, 69),
    (5.25, 71),
    (5.25, 76),
    (5.25, 67),
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66),  # G (F7)
    (1.875, 64),  # F
    (2.25, 69),  # Bb
    (2.625, 64),  # F
    (3.0, 66),  # G
    (3.375, 69),  # Bb
    (3.75, 72),  # D
    (4.125, 69),  # Bb
    (4.5, 66),  # G
    (4.875, 69),  # Bb
    (5.25, 72),  # D
    (5.625, 69),  # Bb
    (6.0, 66),  # G
    (6.375, 64),  # F
    (6.75, 69),  # Bb
    (7.125, 64)   # F
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Drums for bars 2-4 (1.5 - 6.0s)
drum_notes = [
    (1.5, 36),  # Kick on 1
    (1.875, 42),  # Hihat on &1
    (2.25, 42),   # Hihat on &2
    (2.625, 38),  # Snare on 2
    (3.0, 36),    # Kick on 3
    (3.375, 42),  # Hihat on &3
    (3.75, 42),   # Hihat on &4
    (4.125, 38),  # Snare on 4
    (4.5, 36),    # Kick on 1
    (4.875, 42),  # Hihat on &1
    (5.25, 42),   # Hihat on &2
    (5.625, 38),  # Snare on 2
    (6.0, 36),    # Kick on 3
    (6.375, 42),  # Hihat on &3
    (6.75, 42),   # Hihat on &4
    (7.125, 38)   # Snare on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
