
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100),  # Hihat on 4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
bass_notes = [
    # Bar 2: D2 (38), F2 (41), D2 (38), E2 (40)
    (1.5, 38, 100), (2.0, 41, 100), (2.5, 38, 100), (3.0, 40, 100),
    # Bar 3: G2 (43), Bb2 (45), G2 (43), A2 (47)
    (3.5, 43, 100), (4.0, 45, 100), (4.5, 43, 100), (5.0, 47, 100),
    # Bar 4: D2 (38), F2 (41), D2 (38), C2 (37)
    (5.5, 38, 100), (6.0, 41, 100), (6.5, 38, 100), (7.0, 37, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Diane on piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C) - open voicing
    (1.5, 62, 100), (1.5, 64, 100), (1.5, 67, 100), (1.5, 69, 100),
    # Bar 3: G7 (G, B, D, F) - open voicing
    (3.5, 67, 100), (3.5, 71, 100), (3.5, 69, 100), (3.5, 64, 100),
    # Bar 4: Cm7 (C, Eb, G, Bb) - open voicing
    (5.5, 60, 100), (5.5, 63, 100), (5.5, 67, 100), (5.5, 69, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36, 100), (1.875, 42, 100), (2.25, 38, 100), (2.625, 42, 100),
    # Bar 3
    (3.5, 36, 100), (3.875, 42, 100), (4.25, 38, 100), (4.625, 42, 100),
    # Bar 4
    (5.5, 36, 100), (5.875, 42, 100), (6.25, 38, 100), (6.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (Dm)
    (1.5, 65, 100),  # D4
    (1.75, 67, 100),  # F4
    (2.0, 65, 100),  # D4
    (2.25, 67, 100),  # F4
    (2.5, 69, 100),  # A4
    (2.75, 67, 100),  # F4
    (3.0, 65, 100),  # D4
    (3.25, 64, 100),  # C4
    # Bar 3: Silence
    # Bar 4: Finish motif
    (5.5, 65, 100),  # D4
    (5.75, 67, 100),  # F4
    (6.0, 69, 100),  # A4
    (6.25, 65, 100),  # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
