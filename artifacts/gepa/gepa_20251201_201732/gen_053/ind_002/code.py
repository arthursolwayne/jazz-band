
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 80), # Hihat on 2
    (0.75, 38, 100), # Snare on 2
    (1.125, 42, 80), # Hihat on 3
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 80), # Hihat on 4
    (2.25, 38, 100), # Snare on 4
    (2.625, 42, 80)  # Hihat on 4
]

for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2 (root)
    (1.875, 41, 80), # C#2 (chromatic approach)
    (2.25, 43, 100), # F2 (fifth)
    (2.625, 42, 80), # E2 (chromatic approach)
    (3.0, 38, 100),  # D2
    (3.375, 41, 80), # C#2
    (3.75, 43, 100), # F2
    (4.125, 42, 80), # E2
    (4.5, 38, 100),  # D2
    (4.875, 41, 80), # C#2
    (5.25, 43, 100), # F2
    (5.625, 42, 80)  # E2
]

for note in bass_notes:
    bn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    bass.notes.append(bn)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62, 100),  # D4
    (1.5, 65, 80),   # F4
    (1.5, 69, 80),   # A4
    (1.5, 67, 80),   # C4
    # Bar 3: B7 (B, D#, F#, A)
    (2.25, 71, 100), # B4
    (2.25, 76, 80),  # D#4
    (2.25, 78, 80),  # F#4
    (2.25, 74, 80),  # A4
    # Bar 4: Gm7 (G, Bb, D, F)
    (3.0, 67, 100),  # G4
    (3.0, 71, 80),   # Bb4
    (3.0, 69, 80),   # D4
    (3.0, 67, 80),   # F4
]

for note in piano_notes:
    pn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    piano.notes.append(pn)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick
    (1.875, 42, 80), # Hihat
    (2.25, 38, 100), # Snare
    (2.625, 42, 80), # Hihat
    (3.0, 36, 100),  # Kick
    (3.375, 42, 80), # Hihat
    (3.75, 38, 100), # Snare
    (4.125, 42, 80), # Hihat
    # Bar 3
    (4.5, 36, 100),  # Kick
    (4.875, 42, 80), # Hihat
    (5.25, 38, 100), # Snare
    (5.625, 42, 80), # Hihat
    (6.0, 36, 100),  # Kick
    (6.375, 42, 80), # Hihat
    (6.75, 38, 100), # Snare
    (7.125, 42, 80)  # Hihat
]

for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    drums.notes.append(dr)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4, F4, Eb4, D4 — a haunting, unresolved line
sax_notes = [
    (1.5, 62, 100),  # D4
    (1.75, 65, 100), # F4
    (2.0, 62, 100),  # Eb4
    (2.25, 62, 100), # D4
    (3.0, 62, 100),  # D4
    (3.25, 65, 100), # F4
    (3.5, 62, 100),  # Eb4
    (3.75, 62, 100), # D4
    (4.5, 62, 100),  # D4
    (4.75, 65, 100), # F4
    (5.0, 62, 100),  # Eb4
    (5.25, 62, 100)  # D4
]

for note in sax_notes:
    sn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
