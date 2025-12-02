
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
    (0.0, 36, 100),     # Kick on 1
    (0.375, 42, 100),   # Hihat on &1
    (0.75, 38, 100),    # Snare on 2
    (1.125, 42, 100),   # Hihat on &2
    (1.5, 36, 100),     # Kick on 3
    (1.875, 42, 100),   # Hihat on &3
    (2.25, 38, 100),    # Snare on 4
    (2.625, 42, 100)    # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bar 2: Everyone in (1.5 - 3.0s)
# Marcus on bass - walking line, chromatic approach to F
bass_notes = [
    (1.5, 64, 80),  # F3
    (1.75, 65, 80),  # F#3 (chromatic approach)
    (2.0, 65, 80),   # F#3
    (2.25, 64, 80),  # F3
    (2.5, 64, 80),   # F3
    (2.75, 65, 80),  # F#3
    (3.0, 64, 80)    # F3
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Diane on piano - 7th chords comp on 2 and 4, F7 on 1, F7 on 3
piano_notes = [
    (1.5, 62, 90),   # F (F7 chord)
    (1.75, 67, 90),  # C
    (1.75, 69, 90),  # E
    (1.75, 71, 90),  # A
    (2.25, 62, 90),  # F (F7 chord)
    (2.25, 67, 90),  # C
    (2.25, 69, 90),  # E
    (2.25, 71, 90),  # A
    (2.75, 62, 90),  # F (F7 chord)
    (2.75, 67, 90),  # C
    (2.75, 69, 90),  # E
    (2.75, 71, 90),  # A
    (3.0, 62, 90),   # F (F7 chord)
    (3.0, 67, 90),   # C
    (3.0, 69, 90),   # E
    (3.0, 71, 90)    # A
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Dante on sax - sparse melody, starts on beat 2, ends on beat 4
sax_notes = [
    (1.75, 66, 100),  # A (F7 chord)
    (2.0, 69, 100),   # C (melodic leap)
    (2.5, 67, 100),   # Bb (chromatic passing)
    (3.0, 69, 100)    # C (resolution)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 3: Everyone in (3.0 - 4.5s)
# Marcus continues walking line
bass_notes = [
    (3.0, 64, 80),  # F3
    (3.25, 65, 80),  # F#3
    (3.5, 65, 80),   # F#3
    (3.75, 64, 80),  # F3
    (4.0, 64, 80),   # F3
    (4.25, 65, 80),  # F#3
    (4.5, 64, 80)    # F3
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Diane continues comping
piano_notes = [
    (3.0, 62, 90),   # F
    (3.25, 67, 90),  # C
    (3.25, 69, 90),  # E
    (3.25, 71, 90),  # A
    (3.75, 62, 90),  # F
    (3.75, 67, 90),  # C
    (3.75, 69, 90),  # E
    (3.75, 71, 90),  # A
    (4.25, 62, 90),  # F
    (4.25, 67, 90),  # C
    (4.25, 69, 90),  # E
    (4.25, 71, 90),  # A
    (4.5, 62, 90),   # F
    (4.5, 67, 90),   # C
    (4.5, 69, 90),   # E
    (4.5, 71, 90)    # A
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Dante continues melody with variation
sax_notes = [
    (3.25, 67, 100),  # Bb (chromatic)
    (3.5, 69, 100),   # C
    (4.0, 66, 100),   # A
    (4.25, 64, 100)   # F (resolve)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 4: Everyone in (4.5 - 6.0s)
# Marcus continues walking line
bass_notes = [
    (4.5, 64, 80),  # F3
    (4.75, 65, 80),  # F#3
    (5.0, 65, 80),   # F#3
    (5.25, 64, 80),  # F3
    (5.5, 64, 80),   # F3
    (5.75, 65, 80),  # F#3
    (6.0, 64, 80)    # F3
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Diane continues comping
piano_notes = [
    (4.5, 62, 90),   # F
    (4.75, 67, 90),  # C
    (4.75, 69, 90),  # E
    (4.75, 71, 90),  # A
    (5.25, 62, 90),  # F
    (5.25, 67, 90),  # C
    (5.25, 69, 90),  # E
    (5.25, 71, 90),  # A
    (5.75, 62, 90),  # F
    (5.75, 67, 90),  # C
    (5.75, 69, 90),  # E
    (5.75, 71, 90),  # A
    (6.0, 62, 90),   # F
    (6.0, 67, 90),   # C
    (6.0, 69, 90),   # E
    (6.0, 71, 90)    # A
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Dante completes the motif and leaves it hanging
sax_notes = [
    (4.75, 67, 100),  # Bb
    (5.0, 69, 100),   # C
    (5.5, 64, 100),   # F (resolve)
    (5.75, 67, 100)   # Bb (leave it hanging)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums continue
drum_notes = [
    (4.5, 36, 100),     # Kick on 1
    (4.875, 42, 100),   # Hihat on &1
    (5.25, 38, 100),    # Snare on 2
    (5.625, 42, 100),   # Hihat on &2
    (6.0, 36, 100),     # Kick on 3
    (6.375, 42, 100),   # Hihat on &3
    (6.75, 38, 100),    # Snare on 4
    (7.125, 42, 100)    # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
