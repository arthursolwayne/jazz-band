
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
bar1 = [
    (0.0, 36, 100),   # Kick on 1
    (0.375, 42, 100), # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100), # Hihat on 4
    (1.5, 36, 100)    # Kick on 1 (next bar)
]

for time, note, velocity in bar1:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes

bass_line = [
    (1.5, 62, 100, 0.25),  # D
    (1.75, 63, 100, 0.25),  # Eb
    (2.0, 64, 100, 0.25),   # E
    (2.25, 65, 100, 0.25),  # F
    (2.5, 67, 100, 0.25),   # G
    (2.75, 69, 100, 0.25),  # A
    (3.0, 71, 100, 0.25),   # Bb
    (3.25, 72, 100, 0.25),  # B
    (3.5, 74, 100, 0.25),   # C
    (3.75, 76, 100, 0.25),  # D
    (4.0, 77, 100, 0.25),   # Eb
    (4.25, 79, 100, 0.25),  # F
    (4.5, 81, 100, 0.25),   # G
    (4.75, 83, 100, 0.25),  # A
    (5.0, 84, 100, 0.25),   # Bb
    (5.25, 86, 100, 0.25),  # C
    (5.5, 88, 100, 0.25),   # D
    (5.75, 89, 100, 0.25)   # Eb
]

for time, note, velocity, duration in bass_line:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + duration))

# Piano: 7th chords, comp on 2 and 4 (bar 2-4)
# Bar 2 (1.5 - 2.0s): D7 (F# - C# - F - D)
piano.notes.append(pretty_midi.Note(100, 62, 1.75, 1.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 66, 1.75, 1.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 67, 1.75, 1.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 72, 1.75, 1.75 + 0.25))

# Bar 3 (2.5 - 3.0s): G7 (B - F - D - G)
piano.notes.append(pretty_midi.Note(100, 67, 2.75, 2.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 71, 2.75, 2.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 72, 2.75, 2.75 + 0.25))
piano.notes.append(pretty_midi.Note(100, 76, 2.75, 2.75 + 0.25))

# Bar 4 (4.0 - 4.5s): Bb7 (D - A - F - Bb)
piano.notes.append(pretty_midi.Note(100, 62, 4.25, 4.25 + 0.25))
piano.notes.append(pretty_midi.Note(100, 69, 4.25, 4.25 + 0.25))
piano.notes.append(pretty_midi.Note(100, 71, 4.25, 4.25 + 0.25))
piano.notes.append(pretty_midi.Note(100, 74, 4.25, 4.25 + 0.25))

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 2.0s): D - F# - G - D
sax.notes.append(pretty_midi.Note(100, 62, 1.5, 1.5 + 0.25))
sax.notes.append(pretty_midi.Note(100, 66, 1.75, 1.75 + 0.25))
sax.notes.append(pretty_midi.Note(100, 67, 2.0, 2.0 + 0.25))
sax.notes.append(pretty_midi.Note(100, 62, 2.25, 2.25 + 0.25))

# Bar 3 (2.5 - 3.0s): G - B - C - G
sax.notes.append(pretty_midi.Note(100, 67, 2.5, 2.5 + 0.25))
sax.notes.append(pretty_midi.Note(100, 71, 2.75, 2.75 + 0.25))
sax.notes.append(pretty_midi.Note(100, 72, 3.0, 3.0 + 0.25))
sax.notes.append(pretty_midi.Note(100, 67, 3.25, 3.25 + 0.25))

# Bar 4 (4.0 - 4.5s): Bb - D - Eb - Bb
sax.notes.append(pretty_midi.Note(100, 74, 4.0, 4.0 + 0.25))
sax.notes.append(pretty_midi.Note(100, 62, 4.25, 4.25 + 0.25))
sax.notes.append(pretty_midi.Note(100, 63, 4.5, 4.5 + 0.25))
sax.notes.append(pretty_midi.Note(100, 74, 4.75, 4.75 + 0.25))

# Drums in Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, start_time, start_time + 0.125))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(100, 42, start_time + 0.375, start_time + 0.375 + 0.125))
    # Snare on 3
    drums.notes.append(pretty_midi.Note(100, 38, start_time + 0.75, start_time + 0.75 + 0.125))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(100, 42, start_time + 1.125, start_time + 1.125 + 0.125))
    # Kick on 1 of next bar
    if bar < 4:
        drums.notes.append(pretty_midi.Note(100, 36, start_time + 1.5, start_time + 1.5 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
