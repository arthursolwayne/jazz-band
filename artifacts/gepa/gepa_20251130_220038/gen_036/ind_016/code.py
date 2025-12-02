
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
    (36, 0.0),    # Kick on 1
    (38, 0.5),    # Snare on 2
    (42, 0.0),    # Hihat on 1
    (42, 0.25),   # Hihat on &
    (42, 0.5),    # Hihat on 2
    (42, 0.75),   # Hihat on &
    (42, 1.0),    # Hihat on 3
    (42, 1.25),   # Hihat on &
    (42, 1.5),    # Hihat on 4
    (36, 1.0),    # Kick on 3
    (38, 1.5),    # Snare on 4
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# F minor walking bass line with chromatic approaches
bass_notes = [
    (45, 1.5),   # F
    (46, 1.75),  # Gb
    (47, 2.0),   # G
    (44, 2.25),  # E
    (45, 2.5),   # F
    (46, 2.75),  # Gb
    (47, 3.0),   # G
    (44, 3.25),  # E
    (45, 3.5),   # F
    (46, 3.75),  # Gb
    (47, 4.0),   # G
    (44, 4.25),  # E
    (45, 4.5),   # F
    (46, 4.75),  # Gb
    (47, 5.0),   # G
    (44, 5.25),  # E
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# F7, Bb7 on 2 and 4
piano_notes = [
    (53, 1.75, 0.25),  # F7 (F, A, C, Eb) - F
    (57, 1.75, 0.25),  # A
    (59, 1.75, 0.25),  # C
    (60, 1.75, 0.25),  # Eb
    (50, 2.25, 0.25),  # Bb7 (Bb, D, F, Ab) - Bb
    (53, 2.25, 0.25),  # D
    (59, 2.25, 0.25),  # F
    (61, 2.25, 0.25),  # Ab
    (53, 3.75, 0.25),  # F7 again on 2
    (57, 3.75, 0.25),
    (59, 3.75, 0.25),
    (60, 3.75, 0.25),
    (50, 4.25, 0.25),  # Bb7 again on 4
    (53, 4.25, 0.25),
    (59, 4.25, 0.25),
    (61, 4.25, 0.25),
]

for pitch, time, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + duration))

# Dante: Tenor sax melody. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, Gb, G, E (F minor feel)
# Start on bar 2 with the motif, leave it hanging on the third note (G), then return on bar 4
sax_notes = [
    (53, 1.75, 0.25),  # F
    (54, 2.0, 0.25),   # Gb
    (55, 2.25, 0.25),  # G
    (52, 2.5, 0.25),   # E
    (53, 3.5, 0.25),   # F again
    (54, 3.75, 0.25),  # Gb
    (55, 4.0, 0.25),   # G
    (52, 4.25, 0.25),  # E
    (53, 5.0, 0.25),   # F
    (54, 5.25, 0.25),  # Gb
    (55, 5.5, 0.25),   # G
    (52, 5.75, 0.25),  # E
]

for pitch, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + duration))

# Drums continue through bars 2-4
# Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for i in range(2):
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start + time, end=bar_start + time + 0.125))
    bar_start += 1.5

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
