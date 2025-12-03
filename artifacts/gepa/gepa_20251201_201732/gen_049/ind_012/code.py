
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # Bar 1
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # Bar 3
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Fm7: F, C, Ab, D
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C, C, Db, D, Eb, E, F, Gb, G
bass_notes = [
    (1.5, 38), (1.875, 37), (2.25, 39), (2.625, 40),  # F, Gb, G, Ab
    (3.0, 41), (3.375, 40), (3.75, 42), (4.125, 42),  # A, Bb, B, C
    (4.5, 42), (4.875, 41), (5.25, 43), (5.625, 44)   # C, Db, D, Eb
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    (1.5, 53), (1.5, 69), (1.5, 60), (1.5, 62),  # F, Ab, C, D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (3.0, 58), (3.0, 62), (3.0, 60), (3.0, 69),  # Bb, D, F, Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (4.5, 55), (4.5, 67), (4.5, 58), (4.5, 62)   # Eb, G, Bb, D
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 1.5))

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (69), Bb (62), F (65)
# Play the motif starting on beat 2 of bar 2 (1.875), then leave it hanging, return on beat 3 of bar 3 (3.75)
sax_notes = [
    (1.875, 65), (1.875, 69), (1.875, 62), (1.875, 65),  # Start motif
    (3.75, 65), (3.75, 69), (3.75, 62), (3.75, 65)     # Finish motif
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
