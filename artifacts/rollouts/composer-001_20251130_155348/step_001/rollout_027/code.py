
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
    (0.0, 36, 100),     # Kick on 1
    (0.75, 42, 100),    # Hihat on &1
    (1.0, 38, 100),     # Snare on 2
    (1.25, 42, 100),    # Hihat on &2
    (1.5, 36, 100),     # Kick on 3
    (1.75, 42, 100),    # Hihat on &3
    (2.0, 38, 100),     # Snare on 4
    (2.25, 42, 100)     # Hihat on &4
]
for start, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62, 100),     # D
    (1.75, 61, 100),    # C
    (2.0, 63, 100),     # Eb
    (2.25, 62, 100),    # D
    # Bar 3
    (2.5, 60, 100),     # C
    (2.75, 61, 100),    # C#
    (3.0, 62, 100),     # D
    (3.25, 63, 100),    # Eb
    # Bar 4
    (3.5, 63, 100),     # Eb
    (3.75, 62, 100),    # D
    (4.0, 60, 100),     # C
    (4.25, 59, 100)     # B
]
for start, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    (1.75, 62, 100),    # D
    (1.75, 60, 100),    # C
    (1.75, 57, 100),    # A
    (1.75, 55, 100),    # F
    # Bar 3: Dm7 again
    (2.75, 62, 100),
    (2.75, 60, 100),
    (2.75, 57, 100),
    (2.75, 55, 100),
    # Bar 4: Dm7 again
    (3.75, 62, 100),
    (3.75, 60, 100),
    (3.75, 57, 100),
    (3.75, 55, 100)
]
for start, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Motif
# Bar 2: Motif starts (D, F, Bb, D)
sax_notes = [
    (1.5, 62, 100),     # D
    (1.75, 65, 100),    # F
    (2.0, 60, 100),     # Bb
    (2.25, 62, 100),    # D
    # Bar 3: Motif repeats with variation (D, F, Bb, Eb)
    (2.5, 62, 100),
    (2.75, 65, 100),
    (3.0, 60, 100),
    (3.25, 64, 100),
    # Bar 4: Motif returns (D, F, Bb, D)
    (3.5, 62, 100),
    (3.75, 65, 100),
    (4.0, 60, 100),
    (4.25, 62, 100)
]
for start, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums: Continue hihat, kick, snare
drum_notes = [
    # Bar 2
    (1.5, 36, 100),     # Kick on 1
    (1.75, 42, 100),    # Hihat on &1
    (2.0, 38, 100),     # Snare on 2
    (2.25, 42, 100),    # Hihat on &2
    (2.5, 36, 100),     # Kick on 3
    (2.75, 42, 100),    # Hihat on &3
    (3.0, 38, 100),     # Snare on 4
    (3.25, 42, 100),    # Hihat on &4
    # Bar 3
    (3.5, 36, 100),     # Kick on 1
    (3.75, 42, 100),    # Hihat on &1
    (4.0, 38, 100),     # Snare on 2
    (4.25, 42, 100),    # Hihat on &2
    (4.5, 36, 100),     # Kick on 3
    (4.75, 42, 100),    # Hihat on &3
    (5.0, 38, 100),     # Snare on 4
    (5.25, 42, 100),    # Hihat on &4
]
for start, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
