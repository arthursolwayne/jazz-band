
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# F minor key, walking bass line in Fm7 -> Bb7 -> Eb7 -> Am7
bass_notes = [
    (1.5, 70), (1.75, 69), (2.0, 71), (2.25, 72),
    (2.5, 72), (2.75, 71), (3.0, 69), (3.25, 68),
    (3.5, 68), (3.75, 69), (4.0, 71), (4.25, 72),
    (4.5, 72), (4.75, 71), (5.0, 69), (5.25, 68)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 69), (1.5, 71),  # F7
    (2.0, 64), (2.0, 67), (2.0, 69), (2.0, 71),  # F7
    (2.5, 60), (2.5, 64), (2.5, 67), (2.5, 69),  # Bb7
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 69),  # Bb7
    (3.5, 57), (3.5, 60), (3.5, 64), (3.5, 67),  # Eb7
    (4.0, 57), (4.0, 60), (4.0, 64), (4.0, 67),  # Eb7
    (4.5, 55), (4.5, 58), (4.5, 62), (4.5, 65),  # Am7
    (5.0, 55), (5.0, 58), (5.0, 62), (5.0, 65)   # Am7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, short motif, make it sing
# Motif: F - Bb - Eb - D (half note, half note, quarter note, eighth note)
sax_notes = [
    (1.5, 87), (2.0, 87), (2.5, 83), (3.0, 82),  # F - Bb - Eb - D
    (3.5, 87), (4.0, 87), (4.5, 83), (5.0, 82)   # Repeat
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5 if note in [87, 83] else time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
