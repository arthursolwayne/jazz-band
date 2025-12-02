
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
drum_notes = [
    # Kick on 1 and 3
    (0.0, 36, 100),
    (0.75, 38, 100),
    (1.125, 42, 100),
    (1.5, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100),
    (0.75, 42, 100),
    (1.125, 38, 100),
    (1.5, 42, 100),
    # Hihat on every eighth
    (0.0, 42, 100),
    (0.375, 42, 100),
    (0.75, 42, 100),
    (1.125, 42, 100),
    (1.5, 42, 100),
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (1.5, 62, 100),  # D
    (1.875, 63, 100), # Eb
    (2.25, 64, 100),  # E
    (2.625, 65, 100), # F
    # Bar 3
    (3.0, 67, 100),  # G
    (3.375, 68, 100), # Ab
    (3.75, 69, 100),  # A
    (4.125, 70, 100), # Bb
    # Bar 4
    (4.5, 72, 100),  # B
    (4.875, 73, 100), # C
    (5.25, 74, 100),  # C#
    (5.625, 76, 100), # D
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (1.5, 62, 100),
    (1.5, 67, 100),
    (1.5, 72, 100),
    (1.5, 76, 100),
    # Bar 3: Bm7 (B, D, F#, A)
    (3.0, 69, 100),
    (3.0, 72, 100),
    (3.0, 76, 100),
    (3.0, 77, 100),
    # Bar 4: G7 (G, B, D, F)
    (4.5, 67, 100),
    (4.5, 72, 100),
    (4.5, 76, 100),
    (4.5, 78, 100),
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: Bar 2-4
drum_notes = [
    # Kick on 1 and 3
    (1.5, 36, 100),
    (2.25, 36, 100),
    (3.0, 36, 100),
    (3.75, 36, 100),
    (4.5, 36, 100),
    (5.25, 36, 100),
    # Snare on 2 and 4
    (1.875, 38, 100),
    (2.625, 38, 100),
    (3.375, 38, 100),
    (4.125, 38, 100),
    (4.875, 38, 100),
    # Hihat on every eighth
    (1.5, 42, 100),
    (1.875, 42, 100),
    (2.25, 42, 100),
    (2.625, 42, 100),
    (3.0, 42, 100),
    (3.375, 42, 100),
    (3.75, 42, 100),
    (4.125, 42, 100),
    (4.5, 42, 100),
    (4.875, 42, 100),
    (5.25, 42, 100),
    (5.625, 42, 100),
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (1.5, 72, 100),
    (1.875, 76, 100),
    (2.25, 72, 100),
    # Bar 3: Leave it hanging
    (3.0, 72, 100),
    (3.375, 76, 100),
    (3.75, 72, 100),
    # Bar 4: Come back and finish it
    (4.5, 72, 100),
    (4.875, 76, 100),
    (5.25, 72, 100),
    (5.625, 76, 100),
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
