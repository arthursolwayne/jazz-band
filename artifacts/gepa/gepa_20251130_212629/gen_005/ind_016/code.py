
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
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, D minor
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62), (1.875, 61), (2.25, 60), (2.625, 59),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 58), (3.375, 57), (3.75, 56), (4.125, 55),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 54), (4.875, 53), (5.25, 52), (5.625, 51)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 67), (1.5, 71), (1.5, 69), (1.5, 72),  # D7
    (2.25, 67), (2.25, 71), (2.25, 69), (2.25, 72),  # D7
    # Bar 3 (3.0 - 4.5s)
    (3.0, 67), (3.0, 71), (3.0, 69), (3.0, 72),  # D7
    (3.75, 67), (3.75, 71), (3.75, 69), (3.75, 72),  # D7
    # Bar 4 (4.5 - 6.0s)
    (4.5, 67), (4.5, 71), (4.5, 69), (4.5, 72),  # D7
    (5.25, 67), (5.25, 71), (5.25, 69), (5.25, 72)   # D7
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Drums: continue pattern
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D minor motif: D, F, Eb, C
sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 64), (2.625, 60),  # Start the motif
    (3.0, 62), (3.375, 65), (3.75, 64), (4.125, 60),  # Repeat the motif
    (4.5, 62), (4.875, 65), (5.25, 64), (5.625, 60)   # Finish it
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
