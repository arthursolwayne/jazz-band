
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (1.875, 42), (2.25, 38), (2.625, 42),
]

for start, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 37), (2.25, 38), (2.625, 39),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 40), (3.375, 41), (3.75, 42), (4.125, 43),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 44), (4.875, 45), (5.25, 46), (5.625, 47),
]

for start, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.875, 34), (1.875, 38), (1.875, 42), # F7
    # Bar 3 (3.0 - 4.5s)
    (3.375, 34), (3.375, 38), (3.375, 42), # F7
    # Bar 4 (4.5 - 6.0s)
    (4.875, 34), (4.875, 38), (4.875, 42), # F7
]

for start, note in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.875, 66), (2.25, 62), (2.625, 66),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.875, 66), (5.25, 62), (5.625, 66),
]

for start, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (4.875, 42), (5.25, 38), (5.625, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (6.375, 42), (6.75, 38), (7.125, 42),
]

for start, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
