
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
    (0.75, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100),
    (1.125, 38, 100),
    # Hi-hat on every eighth
    (0.0, 42, 80),
    (0.375, 42, 80),
    (0.75, 42, 80),
    (1.125, 42, 80),
    (1.5, 42, 80)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 100),  # D
    (1.75, 63, 100),  # Eb
    (2.0, 64, 100),   # E
    (2.25, 65, 100),  # F
    (2.5, 67, 100),   # G
    (2.75, 69, 100),  # A
    (3.0, 71, 100),   # Bb
    (3.25, 72, 100),  # B
    (3.5, 74, 100),   # C
    (3.75, 76, 100),  # Db
    (4.0, 77, 100),   # D
    (4.25, 79, 100),  # Eb
    (4.5, 81, 100),   # F
    (4.75, 83, 100),  # G
    (5.0, 85, 100),   # A
    (5.25, 87, 100),  # Bb
    (5.5, 89, 100),   # B
    (5.75, 91, 100)   # C
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - D7 (D, F#, A, C)
    (1.5, 62, 100),
    (1.5, 67, 100),
    (1.5, 72, 100),
    (1.5, 76, 100),
    # Bar 3 - G7 (G, Bb, D, F)
    (2.5, 67, 100),
    (2.5, 71, 100),
    (2.5, 76, 100),
    (2.5, 79, 100),
    # Bar 4 - C7 (C, E, G, Bb)
    (3.5, 64, 100),
    (3.5, 69, 100),
    (3.5, 74, 100),
    (3.5, 77, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick=36, snare=38, hihat=42
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append((start + 0.0, 36, 100))
    drum_notes.append((start + 0.75, 36, 100))
    # Snare on 2 and 4
    drum_notes.append((start + 0.375, 38, 100))
    drum_notes.append((start + 1.125, 38, 100))
    # Hi-hat on every eighth
    for i in range(0, 8):
        drum_notes.append((start + i * 0.375, 42, 80))

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start motif (D, F#, Bb)
sax_notes = [
    (1.5, 62, 100),
    (1.5 + 0.25, 67, 100),
    (1.5 + 0.5, 71, 100),
    # Leave it hanging
    (1.5 + 0.75, 67, 60),
    (1.5 + 1.0, 67, 0),
    # Bar 3: Continue motif (G, A, D)
    (2.5, 67, 100),
    (2.5 + 0.25, 72, 100),
    (2.5 + 0.5, 76, 100),
    # Bar 4: Finish motif (F#, Bb, D)
    (3.5, 67, 100),
    (3.5 + 0.25, 71, 100),
    (3.5 + 0.5, 62, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.15))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
