
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (0.0, 36, 100),
    (0.75, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100),
    (1.125, 38, 100),
    # Hi-hats on every eighth
    (0.0, 42, 100),
    (0.375, 42, 100),
    (0.75, 42, 100),
    (1.125, 42, 100),
    (1.5, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
# Bar 2: D2 (root), F2 (chromatic approach), G2 (fifth), F2 (chromatic)
bass_notes = [
    (1.5, 38, 100, 0.5),
    (1.75, 40, 100, 0.25),
    (2.0, 43, 100, 0.5),
    (2.25, 40, 100, 0.25),
    # Bar 3: G2 (fifth), A2 (chromatic), Bb2 (root), A2 (chromatic)
    (2.5, 43, 100, 0.5),
    (2.75, 45, 100, 0.25),
    (3.0, 38, 100, 0.5),
    (3.25, 45, 100, 0.25),
    # Bar 4: D2 (root), F2 (chromatic), G2 (fifth), F2 (chromatic)
    (3.5, 38, 100, 0.5),
    (3.75, 40, 100, 0.25),
    (4.0, 43, 100, 0.5),
    (4.25, 40, 100, 0.25)
]
for time, note, velocity, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 62, 100, 0.5),  # D4
    (1.5, 65, 100, 0.5),  # F4
    (1.5, 69, 100, 0.5),  # A4
    (1.5, 71, 100, 0.5),  # C5
    # Bar 3: G7 (G, B, D, F)
    (2.5, 67, 100, 0.5),  # G4
    (2.5, 71, 100, 0.5),  # B4
    (2.5, 69, 100, 0.5),  # D5
    (2.5, 65, 100, 0.5),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.5, 60, 100, 0.5),  # C4
    (3.5, 63, 100, 0.5),  # Eb4
    (3.5, 67, 100, 0.5),  # G4
    (3.5, 66, 100, 0.5),  # Bb4
]
for time, note, velocity, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.425))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.175))
    # Hi-hats on every eighth
    for eighth in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + eighth * 0.375, end=start + eighth * 0.375 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 chord: D, F, A, C
# Motif: D4 (62), F4 (65), A4 (69), C5 (71)
sax_notes = [
    (1.5, 62, 100, 0.5),  # D4
    (1.5, 65, 100, 0.5),  # F4
    (1.5, 69, 100, 0.5),  # A4
    (1.5, 71, 100, 0.5),  # C5
    # Leave it hanging
    (2.0, 69, 100, 0.25),  # A4
    (2.5, 62, 100, 0.5),  # D4
    (2.5, 71, 100, 0.5)   # C5
]
for time, note, velocity, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
