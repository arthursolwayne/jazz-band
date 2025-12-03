
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
    (0.375, 42, 100), # Hihat on &1
    (0.75, 38, 100),  # Snare on beat 2
    (1.125, 42, 100), # Hihat on &2
    (1.5, 36, 100),   # Kick on beat 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 38, 100),  # Snare on beat 4
    (2.625, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2 (root)
    (1.75, 39, 100), # Eb2 (chromatic approach)
    (2.0, 43, 100),  # A2 (fifth)
    (2.25, 42, 100), # G2 (chromatic approach)
    (2.5, 38, 100),  # D2 (root)
    (2.75, 39, 100), # Eb2 (chromatic approach)
    (3.0, 43, 100),  # A2 (fifth)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62, 100),  # D4
    (1.5, 65, 100),  # F4
    (1.5, 69, 100),  # A4
    (1.5, 72, 100),  # C5

    # Bar 3: G7 (G, B, D, F)
    (2.5, 67, 100),  # G4
    (2.5, 71, 100),  # B4
    (2.5, 69, 100),  # D4
    (2.5, 65, 100),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.5, 60, 100),  # C4
    (3.5, 64, 100),  # Eb4
    (3.5, 67, 100),  # G4
    (3.5, 62, 100),  # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 110),  # E4
    (1.75, 67, 110), # G4
    (2.0, 65, 110),  # E4
    (2.5, 67, 110),  # G4
    (3.0, 69, 110),  # A4
    (3.25, 67, 110), # G4
    (3.5, 65, 110),  # E4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.375, 42, 100), # Hihat on &1
    (3.75, 38, 100),  # Snare on beat 2
    (4.125, 42, 100), # Hihat on &2
    (4.5, 36, 100),   # Kick on beat 3
    (4.875, 42, 100), # Hihat on &3
    (5.25, 38, 100),  # Snare on beat 4
    (5.625, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (4.875, 42, 100), # Hihat on &1
    (5.25, 38, 100),  # Snare on beat 2
    (5.625, 42, 100), # Hihat on &2
    (6.0, 36, 100),   # Kick on beat 3
    (6.375, 42, 100), # Hihat on &3
    (6.75, 38, 100),  # Snare on beat 4
    (7.125, 42, 100)  # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bar 3 and 4: Bass (3.0 - 6.0s)
bass_notes = [
    (3.0, 38, 100),  # D2 (root)
    (3.25, 39, 100), # Eb2 (chromatic approach)
    (3.5, 43, 100),  # A2 (fifth)
    (3.75, 42, 100), # G2 (chromatic approach)
    (4.0, 38, 100),  # D2 (root)
    (4.25, 39, 100), # Eb2 (chromatic approach)
    (4.5, 43, 100),  # A2 (fifth)
    (4.75, 42, 100), # G2 (chromatic approach)
    (5.0, 38, 100),  # D2 (root)
    (5.25, 39, 100), # Eb2 (chromatic approach)
    (5.5, 43, 100),  # A2 (fifth)
    (5.75, 42, 100), # G2 (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Piano (3.0 - 4.5s)
# Dm7 -> G7 (already added earlier)

# Bar 4: Piano (4.5 - 6.0s)
# Cm7 -> Dm7 (already added earlier)

# Bar 3: Sax (3.0 - 4.5s)
sax_notes = [
    (3.0, 69, 110),  # A4
    (3.25, 67, 110), # G4
    (3.5, 65, 110),  # E4
    (3.75, 67, 110), # G4
    (4.0, 69, 110),  # A4
    (4.25, 67, 110), # G4
    (4.5, 65, 110),  # E4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
