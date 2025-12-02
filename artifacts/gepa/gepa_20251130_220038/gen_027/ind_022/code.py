
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.25, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D (root)
    (1.875, 61, 100), # C# (chromatic approach)
    (2.25, 64, 100),  # F (3rd)
    (2.625, 63, 100), # E (chromatic approach)
    (3.0, 62, 100),   # D (root)
    (3.375, 61, 100), # C# (chromatic approach)
    (3.75, 64, 100),  # F (3rd)
    (4.125, 63, 100), # E (chromatic approach)
    (4.5, 62, 100),   # D (root)
    (4.875, 61, 100), # C# (chromatic approach)
    (5.25, 64, 100),  # F (3rd)
    (5.625, 63, 100)  # E (chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.75, 67, 100), # F7 (F, A, C, E)
    (1.75, 69, 100),
    (1.75, 71, 100),
    (1.75, 74, 100),
    # Bar 3 (2.25 - 3.0s)
    (2.5, 67, 100),
    (2.5, 69, 100),
    (2.5, 71, 100),
    (2.5, 74, 100),
    # Bar 4 (3.0 - 3.75s)
    (3.25, 67, 100),
    (3.25, 69, 100),
    (3.25, 71, 100),
    (3.25, 74, 100)
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, start, start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(100, 38, start + 0.75, start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(100, 36, start + 1.125, start + 1.125 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, start + 1.5, start + 1.5 + 0.375))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(100, 42, start + i * 0.375, start + i * 0.375 + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 = D F A C
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.5, 62, 100),  # D
    (1.6875, 64, 100), # F
    (1.875, 67, 100),  # A
    (2.0625, 69, 100), # C
    # Bar 3 (2.25 - 3.0s) - rest
    # Bar 4 (3.0 - 3.75s)
    (3.0, 62, 100),  # D
    (3.1875, 64, 100), # F
    (3.375, 67, 100),  # A
    (3.5625, 69, 100)  # C
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
