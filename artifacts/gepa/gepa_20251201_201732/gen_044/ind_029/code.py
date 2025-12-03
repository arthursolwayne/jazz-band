
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
    (0.0, 36, 100),    # Kick on 1
    (0.75, 42, 100),   # Hihat on &1
    (1.125, 42, 100),  # Hihat on &2
    (1.5, 38, 100),    # Snare on 3
    (1.875, 42, 100),  # Hihat on &3
    (2.25, 42, 100),   # Hihat on &4
    (2.625, 42, 100),  # Hihat on &1
    (3.0, 36, 100),    # Kick on 2
    (3.75, 42, 100),   # Hihat on &2
    (4.125, 42, 100),  # Hihat on &3
    (4.5, 38, 100),    # Snare on 3
    (4.875, 42, 100),  # Hihat on &3
    (5.25, 42, 100),   # Hihat on &4
    (5.625, 42, 100),  # Hihat on &1
    (6.0, 36, 100)     # Kick on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),    # D2 - Root
    (1.875, 40, 100),  # Eb2 - chromatic approach
    (2.25, 43, 100),   # G2 - Fifth
    (2.625, 42, 100),  # F2 - chromatic approach
    (3.0, 38, 100),    # D2 - Root
    (3.375, 40, 100),  # Eb2 - chromatic approach
    (3.75, 43, 100),   # G2 - Fifth
    (4.125, 42, 100),  # F2 - chromatic approach
    (4.5, 38, 100),    # D2 - Root
    (4.875, 40, 100),  # Eb2 - chromatic approach
    (5.25, 43, 100),   # G2 - Fifth
    (5.625, 42, 100)   # F2 - chromatic approach
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    (1.5, 62, 100),    # D4 (Dm7)
    (1.5, 67, 100),    # G4
    (1.5, 72, 100),    # C5
    (1.5, 74, 100),    # D5
    (2.25, 62, 100),   # D4 (Dm7)
    (2.25, 67, 100),   # G4
    (2.25, 72, 100),   # C5
    (2.25, 74, 100),   # D5
    (3.0, 62, 100),    # D4 (Dm7)
    (3.0, 67, 100),    # G4
    (3.0, 72, 100),    # C5
    (3.0, 74, 100),    # D5
    (3.75, 62, 100),   # D4 (Dm7)
    (3.75, 67, 100),   # G4
    (3.75, 72, 100),   # C5
    (3.75, 74, 100),   # D5
    (4.5, 62, 100),    # D4 (Dm7)
    (4.5, 67, 100),    # G4
    (4.5, 72, 100),    # C5
    (4.5, 74, 100),    # D5
    (5.25, 62, 100),   # D4 (Dm7)
    (5.25, 67, 100),   # G4
    (5.25, 72, 100),   # C5
    (5.25, 74, 100),   # D5
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax: Tenor motif - short, singable, open-ended
sax_notes = [
    (1.5, 65, 100),    # F4 (Dm7)
    (1.75, 62, 100),   # D4 (Dm7)
    (2.0, 65, 100),    # F4
    (2.25, 62, 100),   # D4
    (3.0, 65, 100),    # F4
    (3.25, 67, 100),   # G4 (Dm7)
    (3.5, 65, 100),    # F4
    (3.75, 62, 100),   # D4
    (4.5, 65, 100),    # F4
    (4.75, 67, 100),   # G4
    (5.0, 65, 100),    # F4
    (5.25, 62, 100)    # D4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Drums for bars 2-4
drum_notes = [
    (1.5, 36, 100),    # Kick on 1
    (1.875, 42, 100),  # Hihat on &1
    (2.25, 38, 100),   # Snare on 2
    (2.625, 42, 100),  # Hihat on &2
    (3.0, 36, 100),    # Kick on 3
    (3.375, 42, 100),  # Hihat on &3
    (3.75, 38, 100),   # Snare on 4
    (4.125, 42, 100),  # Hihat on &4
    (4.5, 36, 100),    # Kick on 1
    (4.875, 42, 100),  # Hihat on &1
    (5.25, 38, 100),   # Snare on 2
    (5.625, 42, 100),  # Hihat on &2
    (6.0, 36, 100)     # Kick on 3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
