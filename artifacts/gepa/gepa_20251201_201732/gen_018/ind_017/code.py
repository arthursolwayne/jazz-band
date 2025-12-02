
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on beat 2
    (1.25, 38, 100), # Snare on beat 3
    (1.5, 42, 100)   # Hihat on beat 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 42, 100),   # F2 (root)
    (2.0, 44, 100),   # G2 (fifth)
    (2.5, 41, 100),   # E2 (chromatic approach)
    (3.0, 42, 100),   # F2 (root)
    (3.5, 44, 100),   # G2 (fifth)
    (4.0, 46, 100),   # A2 (chromatic approach)
    (4.5, 44, 100),   # G2 (fifth)
    (5.0, 42, 100),   # F2 (root)
    (5.5, 40, 100),   # D2 (chromatic approach)
    (6.0, 42, 100)    # F2 (root)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (1.5, 53, 100), (55, 100), (57, 100), (58, 100),  # F, Ab, C, D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.5, 50, 100), (52, 100), (53, 100), (55, 100),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (3.5, 48, 100), (50, 100), (52, 100), (55, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[1], pitch=note[0], start=note[2], end=note[2] + 0.75))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.5, 42, 100),
    (2.0, 38, 100), (2.0, 42, 100),
    (2.5, 36, 100), (2.5, 42, 100),
    (3.0, 38, 100), (3.0, 42, 100),
    (3.5, 36, 100), (3.5, 42, 100),
    (4.0, 38, 100), (4.0, 42, 100),
    (4.5, 36, 100), (4.5, 42, 100),
    (5.0, 38, 100), (5.0, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, F
sax_notes = [
    (1.5, 53, 100),  # F
    (1.75, 55, 100), # Ab
    (2.0, 52, 100),  # G
    (2.25, 53, 100), # F
    (3.0, 53, 100),  # F (return)
    (3.25, 55, 100), # Ab
    (3.5, 52, 100),  # G
    (3.75, 53, 100)  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
