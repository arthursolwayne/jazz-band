
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
    (0.0, 36), (0.25, 38), (0.375, 42), (0.5, 36), (0.75, 38), (0.875, 42),
    (1.0, 36), (1.25, 38), (1.375, 42), (1.5, 36), (1.75, 38), (1.875, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 70), (1.75, 69), (2.0, 70), (2.25, 71),  # F - E - F - F#
    # Bar 3
    (2.5, 71), (2.75, 70), (3.0, 69), (3.25, 68),  # F# - F - E - D
    # Bar 4
    (3.5, 68), (3.75, 69), (4.0, 70), (4.25, 71)   # D - E - F - F#
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2: F7 (F A C E)
    (1.5, 77), (1.5, 74), (1.5, 72), (1.5, 71),
    # Bar 3: Bb7 (Bb D F A)
    (2.5, 70), (2.5, 68), (2.5, 72), (2.5, 74),
    # Bar 4: Gm7 (G Bb D F)
    (3.5, 76), (3.5, 71), (3.5, 72), (3.5, 72)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    (1.5, 72),  # F
    (1.6, 74),  # A
    (1.7, 72),  # F
    # Bar 3: Rest
    (2.5, 72),  # F
    (2.6, 74),  # A
    (2.7, 72),  # F
    # Bar 4: Finish the motif
    (3.5, 72),  # F
    (3.6, 74),  # A
    (3.7, 72),  # F
    (3.8, 69),  # D
    (3.9, 72)   # F
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1))

# Drums: Continue pattern for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.75, 38), (1.875, 42), (2.0, 36), (2.25, 38), (2.375, 42),
    (2.5, 36), (2.75, 38), (2.875, 42), (3.0, 36), (3.25, 38), (3.375, 42),
    # Bar 3
    (3.5, 36), (3.75, 38), (3.875, 42), (4.0, 36), (4.25, 38), (4.375, 42),
    (4.5, 36), (4.75, 38), (4.875, 42), (5.0, 36), (5.25, 38), (5.375, 42),
    # Bar 4
    (5.5, 36), (5.75, 38), (5.875, 42), (6.0, 36), (6.25, 38), (6.375, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
