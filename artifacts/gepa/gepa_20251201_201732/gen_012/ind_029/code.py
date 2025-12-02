
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
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),  # Snare on 3
    (1.75, 42, 100), # Hihat on &3
    (2.125, 42, 100), # Hihat on &4
    (2.5, 36, 100),  # Kick on 4
    (2.75, 42, 100), # Hihat on &4
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
bass_notes = [
    (1.5, 38, 100),  # D2 (root) on 1
    (2.0, 40, 100),  # F (chromatic approach) on &
    (2.25, 43, 100), # A (fifth) on 2
    (2.75, 40, 100), # F on &
    (3.0, 38, 100),  # D2 on 3
    (3.5, 40, 100),  # F on &
    (3.75, 43, 100), # A on 4
    (4.25, 40, 100), # F on &
    (4.5, 38, 100),  # D2 on 1
    (5.0, 40, 100),  # F on &
    (5.25, 43, 100), # A on 2
    (5.75, 40, 100), # F on &
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano - Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62, 100),  # D4
    (1.5, 64, 100),  # F4
    (1.5, 67, 100),  # A4
    (1.5, 69, 100),  # C5
    # Bar 3: G7 (G, B, D, F)
    (3.0, 67, 100),  # G4
    (3.0, 71, 100),  # B4
    (3.0, 69, 100),  # D5
    (3.0, 64, 100),  # F4
    # Bar 4: Cmaj7 (C, E, G, B)
    (4.5, 60, 100),  # C4
    (4.5, 64, 100),  # E4
    (4.5, 67, 100),  # G4
    (4.5, 71, 100),  # B4
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Drums - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.125, 42, 100), # Hihat on &2
    (2.5, 38, 100),  # Snare on 2
    (2.75, 42, 100), # Hihat on &2
    (3.125, 42, 100), # Hihat on &3
    (3.5, 36, 100),  # Kick on 3
    (3.75, 42, 100), # Hihat on &3
    (4.125, 42, 100), # Hihat on &4
    (4.5, 38, 100),  # Snare on 4
    (4.75, 42, 100), # Hihat on &4
    (5.125, 42, 100), # Hihat on &4
    (5.5, 36, 100),  # Kick on 4
    (5.75, 42, 100), # Hihat on &4
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    (1.5, 62, 100),  # D4
    (1.75, 64, 100), # F4
    (2.0, 62, 100),  # D4
    (2.5, 62, 100),  # D4
    (2.75, 64, 100), # F4
    (3.0, 62, 100),  # D4
    (3.5, 62, 100),  # D4
    (3.75, 64, 100), # F4
    (4.0, 62, 100),  # D4
    (4.5, 62, 100),  # D4
    (4.75, 64, 100), # F4
    (5.0, 62, 100),  # D4
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
