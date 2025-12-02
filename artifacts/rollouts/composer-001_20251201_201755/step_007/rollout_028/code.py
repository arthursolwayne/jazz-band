
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
    (0.0, 36),  # Kick on 1
    (0.375, 42),  # Hihat on &
    (0.75, 38),  # Snare on 2
    (1.125, 42),  # Hihat on &
    (1.5, 36),  # Kick on 3
    (1.875, 42),  # Hihat on &
    (2.25, 38),  # Snare on 4
    (2.625, 42)   # Hihat on &
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (Walking line, D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), chromatic approach from G2
    (1.5, 38), (1.5, 41), (1.5, 42),
    # Bar 3: G2 (fifth), Bb2 (chromatic), C2 (root)
    (3.0, 43), (3.0, 42), (3.0, 38),
    # Bar 4: C2 (root), D2 (chromatic), F#2 (fifth)
    (4.5, 38), (4.5, 39), (4.5, 41)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2: Dm7 - D, F, A, C
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 69),
    # Bar 3: G7 (no 3rd) - G, B, D, F
    (3.0, 67), (3.0, 71), (3.0, 69), (3.0, 64),
    # Bar 4: Cm7 - C, Eb, G, Bb
    (4.5, 60), (4.5, 63), (4.5, 67), (4.5, 62)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Little Ray on drums (Bar 2-4)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (start + 0.0, 36),  # Kick on 1
        (start + 0.375, 42),  # Hihat on &
        (start + 0.75, 38),  # Snare on 2
        (start + 1.125, 42),  # Hihat on &
        (start + 1.5, 36),  # Kick on 3
        (start + 1.875, 42),  # Hihat on &
        (start + 2.25, 38),  # Snare on 4
        (start + 2.625, 42)   # Hihat on &
    ]
    for time, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D (sax in Bb, so D = F, F = G, G = A, D = F)
sax_notes = [
    # Bar 2: D (F), F (G), G (A), D (F) - start the motif
    (1.5, 66), (1.5, 68), (1.5, 70), (1.5, 66),
    # Bar 3: rest, leave it hanging
    # Bar 4: repeat the motif with a slight variation
    (4.5, 66), (4.5, 68), (4.5, 70), (4.5, 66)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
