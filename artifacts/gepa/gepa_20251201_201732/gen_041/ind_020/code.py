
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 36),
    (1.875, 38), (2.25, 42), (2.625, 38), (3.0, 42),
    (3.375, 36), (3.75, 42), (4.125, 36), (4.5, 42),
    (4.875, 38), (5.25, 42), (5.625, 38), (6.0, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 42),
    (3.0, 43), (3.375, 45), (3.75, 43), (4.125, 42),
    (4.5, 43), (4.875, 45), (5.25, 43), (5.625, 42)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes.extend([(2.0, 62), (2.0, 67), (2.0, 71), (2.0, 76)])
# Bar 3: Bm7 (B, D, F#, A)
piano_notes.extend([(3.0, 69), (3.0, 74), (3.0, 77), (3.0, 81)])
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([(4.0, 71), (4.0, 76), (4.0, 79), (4.0, 83)])
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), D (62), G (67) - 1st bar
#        D (62), F# (67), G (67), A (71) - 2nd bar
#        D (62), F# (67), D (62), G (67) - 3rd bar
#        D (62), F# (67), Bb (70), D (62) - 4th bar
sax_notes = [
    (2.0, 62), (2.0, 67), (2.0, 62), (2.0, 67),
    (2.5, 62), (2.5, 67), (2.5, 67), (2.5, 71),
    (3.0, 62), (3.0, 67), (3.0, 62), (3.0, 67),
    (3.5, 62), (3.5, 67), (3.5, 70), (3.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
