
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (1.5, 70), (1.875, 69), (2.25, 71), (2.625, 70),
    (3.0, 70), (3.375, 69), (3.75, 71), (4.125, 70),
    (4.5, 69), (4.875, 68), (5.25, 70), (5.625, 69)
]
for start, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(n)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (2.25, 64), (2.25, 67), (2.25, 69), (2.25, 71),  # C7
    (3.0, 64), (3.0, 67), (3.0, 69), (3.0, 71),    # C7
    (3.75, 64), (3.75, 67), (3.75, 69), (3.75, 71),  # C7
    (4.5, 64), (4.5, 67), (4.5, 69), (4.5, 71)     # C7
]
for start, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(n)

# Sax (Dante): One short motif, make it sing
sax_notes = [
    (1.5, 66), (1.75, 69), (2.0, 67), (2.25, 69),  # motif
    (2.5, 66), (2.75, 69), (3.0, 67), (3.25, 69),  # repeat
    (3.5, 66), (3.75, 69), (4.0, 67), (4.25, 69),  # repeat
    (4.5, 66), (4.75, 69), (5.0, 67), (5.25, 69)   # repeat
]
for start, note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(n)

# Drums continue (bars 2-4)
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
