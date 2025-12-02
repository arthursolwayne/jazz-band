
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
    (0.0, 36, 100),    # Kick on beat 1
    (0.75, 42, 100),   # Hihat on &1
    (1.0, 38, 100),    # Snare on beat 2
    (1.5, 36, 100),    # Kick on beat 3
    (1.75, 42, 100),   # Hihat on &3
    (2.0, 38, 100),    # Snare on beat 4
    (2.5, 42, 100),    # Hihat on &4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (1.5, 72, 100),    # D (root)
    (1.75, 70, 100),   # C (chromatic approach)
    (2.0, 74, 100),    # F (5th)
    (2.25, 73, 100),   # E (chromatic approach)
    (2.5, 72, 100),    # D (root)
    (2.75, 70, 100),   # C (chromatic approach)
    (3.0, 77, 100),    # A (7th)
    (3.25, 76, 100),   # G (chromatic approach)
    (3.5, 72, 100),    # D (root)
    (3.75, 70, 100),   # C (chromatic approach)
    (4.0, 74, 100),    # F (5th)
    (4.25, 73, 100),   # E (chromatic approach)
    (4.5, 72, 100),    # D (root)
    (4.75, 70, 100),   # C (chromatic approach)
    (5.0, 77, 100),    # A (7th)
    (5.25, 76, 100),   # G (chromatic approach)
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (2.0, 62, 100),    # D
    (2.0, 64, 100),    # F
    (2.0, 67, 100),    # A
    (2.0, 69, 100),    # C
    # Bar 3: G7 (G, B, D, F)
    (3.5, 67, 100),    # G
    (3.5, 71, 100),    # B
    (3.5, 69, 100),    # D
    (3.5, 64, 100),    # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (5.0, 60, 100),    # C
    (5.0, 61, 100),    # Eb
    (5.0, 67, 100),    # G
    (5.0, 62, 100),    # Bb
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for bars 2-4
drum_notes = [
    (1.5, 36, 100),    # Kick on beat 1
    (1.75, 42, 100),   # Hihat on &1
    (2.0, 38, 100),    # Snare on beat 2
    (2.5, 36, 100),    # Kick on beat 3
    (2.75, 42, 100),   # Hihat on &3
    (3.0, 38, 100),    # Snare on beat 4
    (3.5, 36, 100),    # Kick on beat 1
    (3.75, 42, 100),   # Hihat on &1
    (4.0, 38, 100),    # Snare on beat 2
    (4.5, 36, 100),    # Kick on beat 3
    (4.75, 42, 100),   # Hihat on &3
    (5.0, 38, 100),    # Snare on beat 4
    (5.25, 42, 100),   # Hihat on &4
    (5.5, 42, 100),    # Hihat on &4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Saxophone (Dante) - motif: D, F, A, G (start), then D, F, A, G (end)
# Start at 1.5s, end at 5.5s, with space in between
sax_notes = [
    (1.5, 62, 100),    # D
    (1.6, 64, 100),    # F
    (1.7, 67, 100),    # A
    (1.8, 66, 100),    # G
    (3.0, 62, 100),    # D
    (3.1, 64, 100),    # F
    (3.2, 67, 100),    # A
    (3.3, 66, 100),    # G
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
