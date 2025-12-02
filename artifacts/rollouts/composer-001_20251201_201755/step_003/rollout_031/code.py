
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
    (0.75, 42, 100), # Hihat on & 2
    (1.0, 38, 100),  # Snare on beat 2
    (1.25, 42, 100), # Hihat on & 3
    (1.5, 36, 100)   # Kick on beat 3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, roots and fifths with chromatic approaches
# Time signature: 4/4, 160 BPM -> 1 beat = 0.375s, 1 bar = 1.5s
bass_notes = [
    (1.5, 69, 100),  # F2 (root)
    (1.875, 71, 100), # G2 (fifth)
    (2.25, 70, 100),  # G#2 (chromatic approach)
    (2.625, 69, 100), # F2 (root)
    (3.0, 71, 100),   # G2 (fifth)
    (3.375, 73, 100), # A2 (chromatic approach)
    (3.75, 71, 100),  # G2 (fifth)
    (4.125, 72, 100), # A#2 (chromatic approach)
    (4.5, 71, 100),   # G2 (fifth)
    (4.875, 74, 100), # Bb2 (chromatic approach)
    (5.25, 72, 100),  # A#2 (chromatic approach)
    (5.625, 71, 100), # G2 (fifth)
    (6.0, 69, 100)    # F2 (root)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Piano (Diane): open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 76, 100),  # F (F4)
    (1.5, 82, 100),  # A (A4)
    (1.5, 78, 100),  # C (C5)
    (1.5, 83, 100),  # E (E5)
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (3.0, 81, 100),  # Bb (Bb4)
    (3.0, 84, 100),  # D (D5)
    (3.0, 76, 100),  # F (F4)
    (3.0, 80, 100),  # Ab (Ab4)
    # Bar 4: Em7 (E, G, B, D)
    (4.5, 83, 100),  # E (E5)
    (4.5, 86, 100),  # G (G5)
    (4.5, 88, 100),  # B (B5)
    (4.5, 84, 100)   # D (D5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.875, 42, 100), # Hihat on & 2
    (2.25, 38, 100),  # Snare on beat 2
    (2.625, 42, 100), # Hihat on & 3
    (3.0, 36, 100),  # Kick on beat 3
    (3.375, 42, 100), # Hihat on & 4
    (3.75, 38, 100),  # Snare on beat 4
    (4.125, 42, 100), # Hihat on & 1
    (4.5, 36, 100),  # Kick on beat 1
    (4.875, 42, 100), # Hihat on & 2
    (5.25, 38, 100),  # Snare on beat 2
    (5.625, 42, 100), # Hihat on & 3
    (6.0, 36, 100)   # Kick on beat 3
]
for note in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (F4) -> G (G4) -> F (F4) -> G (G4) -> F (F4)
# Start on bar 2, end on bar 4
sax_notes = [
    (1.5, 76, 100),  # F (F4)
    (1.875, 77, 100), # G (G4)
    (2.25, 76, 100),  # F (F4)
    (2.625, 77, 100), # G (G4)
    (3.0, 76, 100),   # F (F4)
    (3.375, 77, 100), # G (G4)
    (3.75, 76, 100),  # F (F4)
    (4.125, 77, 100), # G (G4)
    (4.5, 76, 100),   # F (F4)
    (4.875, 77, 100), # G (G4)
    (5.25, 76, 100),  # F (F4)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[0], start=note[1], end=note[1] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
