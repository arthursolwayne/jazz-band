
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
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42),
    (1.5, 36), (1.875, 38), (2.25, 42), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 42), (4.125, 42),
    (4.5, 36), (4.875, 38), (5.25, 42), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 41), (2.25, 43), (2.625, 40),
    (3.0, 42), (3.375, 45), (3.75, 47), (4.125, 44),
    (4.5, 46), (4.875, 49), (5.25, 51), (5.625, 48)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 65), (1.5, 76), (1.5, 69), (1.5, 71),
    # Bar 3: Gm7 (G, Bb, D, F)
    (3.0, 67), (3.0, 76), (3.0, 69), (3.0, 65),
    # Bar 4: C7 (C, E, G, Bb)
    (4.5, 69), (4.5, 76), (4.5, 67), (4.5, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), A (68), G (67), F (65)
sax_notes = [
    (1.5, 65), (1.5, 68), (1.5, 67), (1.5, 65),
    (2.625, 65), (2.625, 68), (2.625, 67), (2.625, 65),
    (3.75, 65), (3.75, 68), (3.75, 67), (3.75, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
