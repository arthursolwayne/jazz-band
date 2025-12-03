
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
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on &1
    (1.125, 42, 100), # Hihat on &2
    (1.5, 38, 100),   # Snare on 3
    (1.875, 42, 100), # Hihat on &3
    (2.25, 42, 100),  # Hihat on &4
    (2.625, 42, 100), # Hihat on &4
    (3.0, 36, 100),   # Kick on 1 (next bar)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),   # D2 (root)
    (1.875, 40, 100), # Eb2 (chromatic approach)
    (2.25, 41, 100),  # E2 (fifth)
    (2.625, 40, 100), # Eb2 (chromatic approach)
    (3.0, 38, 100),   # D2 (root)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (1.5, 62, 100),   # D4
    (1.5, 64, 100),   # F4
    (1.5, 67, 100),   # A4
    (1.5, 72, 100),   # C5
    (1.875, 62, 100), # D4 (comp on 2)
    (1.875, 67, 100), # A4
    (2.25, 65, 100),  # G4 (chromatic approach)
    (2.625, 62, 100), # D4 (comp on 4)
    (2.625, 67, 100), # A4
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# You: Tenor sax, one short motif, make it sing
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67, 100),   # A4 (start motif)
    (1.875, 67, 100), # A4 (repeat)
    (2.25, 67, 100),  # A4 (repeat)
    (2.625, 67, 100), # A4 (repeat)
    (3.0, 64, 100),   # F4 (resolve)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 38, 100),   # D2 (root)
    (3.375, 40, 100), # Eb2 (chromatic approach)
    (3.75, 41, 100),  # E2 (fifth)
    (4.125, 40, 100), # Eb2 (chromatic approach)
    (4.5, 38, 100),   # D2 (root)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    (3.0, 67, 100),   # G4
    (3.0, 71, 100),   # Bb4
    (3.0, 69, 100),   # D4
    (3.0, 76, 100),   # F5
    (3.375, 67, 100), # G4 (comp on 2)
    (3.375, 69, 100), # D4
    (3.75, 70, 100),  # Eb4 (chromatic approach)
    (4.125, 67, 100), # G4 (comp on 4)
    (4.125, 69, 100), # D4
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# You: Tenor sax, continue motif
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (3.0, 67, 100),   # A4 (start motif)
    (3.375, 67, 100), # A4 (repeat)
    (3.75, 67, 100),  # A4 (repeat)
    (4.125, 67, 100), # A4 (repeat)
    (4.5, 64, 100),   # F4 (resolve)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 38, 100),   # D2 (root)
    (4.875, 40, 100), # Eb2 (chromatic approach)
    (5.25, 41, 100),  # E2 (fifth)
    (5.625, 40, 100), # Eb2 (chromatic approach)
    (6.0, 38, 100),   # D2 (root)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    (4.5, 60, 100),   # C4
    (4.5, 63, 100),   # Eb4
    (4.5, 67, 100),   # G4
    (4.5, 71, 100),   # Bb4
    (4.875, 60, 100), # C4 (comp on 2)
    (4.875, 67, 100), # G4
    (5.25, 64, 100),  # F4 (chromatic approach)
    (5.625, 60, 100), # C4 (comp on 4)
    (5.625, 67, 100), # G4
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# You: Tenor sax, complete the motif
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (4.5, 67, 100),   # A4 (start motif)
    (4.875, 67, 100), # A4 (repeat)
    (5.25, 67, 100),  # A4 (repeat)
    (5.625, 67, 100), # A4 (repeat)
    (6.0, 64, 100),   # F4 (resolve)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),   # Kick on 1
    (4.875, 42, 100), # Hihat on &1
    (5.25, 42, 100),  # Hihat on &2
    (5.625, 38, 100), # Snare on 3
    (5.875, 42, 100), # Hihat on &3
    (6.25, 42, 100),  # Hihat on &4
    (6.625, 42, 100), # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
