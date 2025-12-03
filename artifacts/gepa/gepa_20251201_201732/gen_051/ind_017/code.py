
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
    (0.75, 42, 80),  # Hihat on &1
    (1.125, 42, 80), # Hihat on &2
    (1.5, 38, 100)   # Snare on 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 80),  # D2
    (1.75, 40, 70),  # Eb2 (chromatic approach)
    (2.0, 43, 80),  # G2
    (2.25, 38, 80)  # D2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, resolve on last chord
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (1.5, 62, 100),  # D4
    (1.5, 67, 100),  # F4
    (1.5, 71, 100),  # A4
    (1.5, 72, 100),  # C5
    # Bar 3: Gm7 (G-Bb-D-F)
    (2.0, 67, 100),  # G4
    (2.0, 71, 100),  # Bb4
    (2.0, 76, 100),  # D5
    (2.0, 79, 100),  # F5
    # Bar 4: Cm7 (C-Eb-G-Bb)
    (2.5, 60, 100),  # C4
    (2.5, 64, 100),  # Eb4
    (2.5, 71, 100),  # G4
    (2.5, 73, 100)   # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 80),  # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 80),  # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 80),  # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 80)   # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: D - F - G (Dm scale)
sax_notes = [
    (1.5, 62, 110),  # D4
    (1.75, 65, 100),  # F4
    (2.0, 67, 100),  # G4
    (2.25, 62, 100),  # D4 (rest)
    (2.5, 62, 110),  # D4 (repeat)
    (2.75, 65, 100),  # F4
    (3.0, 67, 100),  # G4
    (3.25, 62, 100)  # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 43, 80),  # G2
    (3.25, 41, 70),  # Ab2 (chromatic approach)
    (3.5, 38, 80),  # D2
    (3.75, 43, 80)  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, resolve on last chord
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    (3.0, 67, 100),  # G4
    (3.0, 71, 100),  # Bb4
    (3.0, 76, 100),  # D5
    (3.0, 79, 100),  # F5
    # Bar 4: Cm7 (C-Eb-G-Bb)
    (3.5, 60, 100),  # C4
    (3.5, 64, 100),  # Eb4
    (3.5, 71, 100),  # G4
    (3.5, 73, 100)   # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.25, 42, 80),  # Hihat on &1
    (3.5, 38, 100),  # Snare on 2
    (3.75, 42, 80),  # Hihat on &2
    (4.0, 36, 100),  # Kick on 3
    (4.25, 42, 80),  # Hihat on &3
    (4.5, 38, 100),  # Snare on 4
    (4.75, 42, 80)   # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 3: G - Bb - C (Gm scale)
sax_notes = [
    (3.0, 67, 110),  # G4
    (3.25, 71, 100),  # Bb4
    (3.5, 69, 100),  # C5 (rest)
    (3.75, 67, 100),  # G4 (rest)
    (4.0, 67, 110),  # G4
    (4.25, 71, 100),  # Bb4
    (4.5, 69, 100),  # C5
    (4.75, 67, 100)  # G4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 38, 80),  # D2
    (4.75, 40, 70),  # Eb2 (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Open voicings, resolve on last chord
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    (4.5, 60, 100),  # C4
    (4.5, 64, 100),  # Eb4
    (4.5, 71, 100),  # G4
    (4.5, 73, 100)   # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.75, 42, 80),  # Hihat on &1
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 4: C - Eb - F (Cm scale)
sax_notes = [
    (4.5, 60, 110),  # C4
    (4.75, 64, 100),  # Eb4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
