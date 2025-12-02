
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2 - G2)
    (1.5, 38), (1.875, 40), (2.25, 38), (2.625, 43),
    # Bar 3 (A2 - D3)
    (3.0, 45), (3.375, 47), (3.75, 45), (4.125, 50),
    # Bar 4 (F#2 - B2)
    (4.5, 42), (4.875, 44), (5.25, 42), (5.625, 47)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano: open voicings, different chords each bar, resolves on the last
# Bar 2: D7 (F# - A - D - F#)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74),
    # Bar 3: A7 (C# - E - A - C#)
    (3.0, 67), (3.0, 72), (3.0, 77), (3.0, 79),
    # Bar 4: F#7 (A - C# - F# - A)
    (4.5, 69), (4.5, 74), (4.5, 79), (4.5, 81)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 1.5))

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (72) - F# (74) - B (76) - D (72)
sax_notes = [
    # Bar 2: Start the motif
    (1.5, 72), (1.5, 74), (1.5, 76), (1.5, 72),
    # Bar 3: Leave it hanging
    (3.0, 72), (3.0, 74), (3.0, 76), (3.0, 72),
    # Bar 4: Return and finish it
    (4.5, 72), (4.5, 74), (4.5, 76), (4.5, 72)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (bar_start, 36), (bar_start + 0.375, 42), (bar_start + 0.75, 36), (bar_start + 1.125, 42),
        (bar_start + 1.5, 38), (bar_start + 1.875, 42), (bar_start + 2.25, 38), (bar_start + 2.625, 42)
    ]
    for start, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
