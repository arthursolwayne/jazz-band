
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 71), (1.5, 76),  # Fm7 (F, Ab, C, D)
    (2.25, 64), (2.25, 67), (2.25, 71), (2.25, 79),  # Bb7 (Bb, D, F, Ab)
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 76)   # Fm7 again
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 41), (2.625, 38),  # F, Gb, G, F (chromatic approach)
    (3.0, 41), (3.375, 43), (3.75, 41), (4.125, 38)   # G, A, G, F
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 66), (1.75, 62), (2.0, 69),  # F, Bb, F, C (first phrase)
    (2.625, 62), (2.75, 66), (2.875, 62), (3.0, 69)  # F, Bb, F, C (second phrase)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 79),  # Bb7
    (3.75, 64), (3.75, 67), (3.75, 71), (3.75, 76)  # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 41), (3.375, 43), (3.75, 41), (4.125, 38),  # G, A, G, F
    (4.5, 38), (4.875, 40), (5.25, 41), (5.625, 38)   # F, Gb, G, F
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (4.5, 64), (4.5, 67), (4.5, 71), (4.5, 79),  # Bb7
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 76)  # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 41), (4.875, 43), (5.25, 41), (5.625, 38)  # G, A, G, F
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (4.5, 62), (4.625, 66), (4.75, 62), (5.0, 69),  # F, Bb, F, C (first phrase)
    (5.625, 62), (5.75, 66), (5.875, 62), (6.0, 69)  # F, Bb, F, C (second phrase)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
