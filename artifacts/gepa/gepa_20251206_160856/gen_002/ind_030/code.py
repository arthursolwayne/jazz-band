
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

for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 41),
    (3.0, 38), (3.375, 40), (3.75, 43), (4.125, 41)
]

for start, note in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 64)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    (2.625, 71), (2.625, 76), (2.625, 69), (2.625, 62)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    (3.75, 60), (3.75, 64), (3.75, 67), (3.75, 61)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Dante: Tenor sax motif, make it sing
sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 62), (2.625, 65),
    (3.0, 62), (3.375, 65), (3.75, 62), (4.125, 65),
    (4.5, 62), (4.875, 65), (5.25, 62), (5.625, 65)
]

for start, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
