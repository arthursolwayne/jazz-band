
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
    (1.0, 38, 100),    # Snare on 2
    (1.25, 42, 100),   # Hihat on &2
    (1.5, 36, 100),    # Kick on 3
    (1.75, 42, 100),   # Hihat on &3
    (2.0, 38, 100),    # Snare on 4
    (2.25, 42, 100)    # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62, 100),    # D
    (1.75, 61, 100),   # C#
    (2.0, 63, 100),    # D#
    (2.25, 64, 100),   # E
    (2.5, 65, 100),    # F
    (2.75, 66, 100),   # F#
    (3.0, 67, 100),    # G
    (3.25, 65, 100),   # F
    (3.5, 64, 100),    # E
    (3.75, 63, 100),   # D#
    (4.0, 62, 100),    # D
    (4.25, 61, 100),   # C#
    (4.5, 63, 100),    # D#
    (4.75, 64, 100),   # E
    (5.0, 65, 100),    # F
    (5.25, 66, 100),   # F#
    (5.5, 67, 100),    # G
    (5.75, 65, 100)    # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 67, 100),    # G
    (1.75, 71, 100),    # B
    (1.75, 72, 100),    # C
    (1.75, 74, 100),    # D
    # Bar 3
    (3.25, 67, 100),    # G
    (3.25, 71, 100),    # B
    (3.25, 72, 100),    # C
    (3.25, 74, 100),    # D
    # Bar 4
    (4.75, 67, 100),    # G
    (4.75, 71, 100),    # B
    (4.75, 72, 100),    # C
    (4.75, 74, 100)     # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),    # Kick on 1
    (1.75, 42, 100),   # Hihat on &1
    (2.0, 38, 100),    # Snare on 2
    (2.25, 42, 100),   # Hihat on &2
    (2.5, 36, 100),    # Kick on 3
    (2.75, 42, 100),   # Hihat on &3
    (3.0, 38, 100),    # Snare on 4
    (3.25, 42, 100),   # Hihat on &4
    (3.5, 36, 100),    # Kick on 1
    (3.75, 42, 100),   # Hihat on &1
    (4.0, 38, 100),    # Snare on 2
    (4.25, 42, 100),   # Hihat on &2
    (4.5, 36, 100),    # Kick on 3
    (4.75, 42, 100),   # Hihat on &3
    (5.0, 38, 100),    # Snare on 4
    (5.25, 42, 100),   # Hihat on &4
    (5.5, 36, 100),    # Kick on 1
    (5.75, 42, 100)    # Hihat on &1
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Dante: Tenor sax motif
sax_notes = [
    (1.5, 69, 100),    # A (D7)
    (1.75, 71, 100),   # B (D7)
    (2.0, 67, 100),    # G (Dm7)
    (2.25, 69, 100),   # A (Dm7)
    (2.5, 71, 100),    # B (D7)
    (2.75, 72, 100),   # C (D7)
    (3.0, 69, 100),    # A (D7)
    (3.25, 67, 100),   # G (Dm7)
    (3.5, 69, 100),    # A (D7)
    (3.75, 71, 100),   # B (D7)
    (4.0, 67, 100),    # G (Dm7)
    (4.25, 69, 100),   # A (D7)
    (4.5, 71, 100),    # B (D7)
    (4.75, 72, 100),   # C (D7)
    (5.0, 69, 100),    # A (D7)
    (5.25, 67, 100),   # G (Dm7)
    (5.5, 69, 100),    # A (D7)
    (5.75, 71, 100)    # B (D7)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
