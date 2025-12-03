
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

# Drums: Bar 1
drums_notes = [
    (0.0, 36, 100),     # Kick on 1
    (0.75, 42, 80),     # Hihat on &1
    (1.0, 38, 100),     # Snare on 2
    (1.25, 42, 80),     # Hihat on &2
    (1.5, 36, 100),     # Kick on 3
    (1.75, 42, 80),     # Hihat on &3
    (2.0, 38, 100),     # Snare on 4
    (2.25, 42, 80)      # Hihat on &4
]
for time, note, velocity in drums_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 2: Everyone in. Sax melody, bass walking, piano comp, drums continue

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    (1.5, 43, 90),     # D2
    (1.75, 41, 90),    # F2 (chromatic approach)
    (2.0, 38, 90),     # G2
    (2.25, 40, 90),    # A2
    (2.5, 38, 90),     # G2
    (2.75, 41, 90),    # F2
    (3.0, 43, 90),     # D2
    (3.25, 42, 90)     # E2 (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano comp (open voicings, resolve on the last beat)
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62, 90),     # D4
    (1.5, 65, 90),     # F4
    (1.5, 69, 90),     # A4
    (1.5, 67, 90),     # C4
    # Bar 3: Gm7 (G, Bb, D, F)
    (2.5, 67, 90),     # G4
    (2.5, 72, 90),     # Bb4
    (2.5, 69, 90),     # D4
    (2.5, 65, 90),     # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.5, 60, 90),     # C4
    (3.5, 64, 90),     # Eb4
    (3.5, 67, 90),     # G4
    (3.5, 72, 90),     # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax melody (Dm, one short motif, make it sing)
sax_notes = [
    (1.5, 62, 100),     # D4 (start of motif)
    (1.75, 65, 100),    # F4
    (2.0, 67, 100),     # G4
    (2.25, 65, 100),    # F4
    (2.5, 62, 100),     # D4
    (2.75, 64, 100),    # Eb4
    (3.0, 67, 100),     # G4
    (3.25, 65, 100),    # F4
    (3.5, 62, 100),     # D4 (resolves)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 2-4
drums_notes = [
    # Bar 2
    (1.5, 36, 100),     # Kick on 1
    (1.75, 42, 80),     # Hihat on &1
    (2.0, 38, 100),     # Snare on 2
    (2.25, 42, 80),     # Hihat on &2
    (2.5, 36, 100),     # Kick on 3
    (2.75, 42, 80),     # Hihat on &3
    (3.0, 38, 100),     # Snare on 4
    (3.25, 42, 80),     # Hihat on &4

    # Bar 3
    (3.5, 36, 100),     # Kick on 1
    (3.75, 42, 80),     # Hihat on &1
    (4.0, 38, 100),     # Snare on 2
    (4.25, 42, 80),     # Hihat on &2
    (4.5, 36, 100),     # Kick on 3
    (4.75, 42, 80),     # Hihat on &3
    (5.0, 38, 100),     # Snare on 4
    (5.25, 42, 80),     # Hihat on &4

    # Bar 4
    (5.5, 36, 100),     # Kick on 1
    (5.75, 42, 80),     # Hihat on &1
    (6.0, 38, 100),     # Snare on 2
    (6.25, 42, 80),     # Hihat on &2
    (6.5, 36, 100),     # Kick on 3
    (6.75, 42, 80),     # Hihat on &3
    (7.0, 38, 100),     # Snare on 4
    (7.25, 42, 80)      # Hihat on &4
]
for time, note, velocity in drums_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
