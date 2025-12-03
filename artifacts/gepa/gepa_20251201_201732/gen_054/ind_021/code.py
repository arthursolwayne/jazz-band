
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),    # Kick on 1
    (0.5, 42, 100),    # Hihat on &1
    (0.75, 38, 100),   # Snare on 2
    (1.0, 42, 100),    # Hihat on &2
    (1.25, 36, 100),   # Kick on 3
    (1.5, 42, 100)     # Hihat on &3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
drum_notes = [
    (1.5, 36, 100),    # Kick on 1
    (2.0, 38, 100),    # Snare on 2
    (2.5, 36, 100),    # Kick on 3
    (3.0, 38, 100),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    (1.5, 62, 100),    # D (Dm7)
    (1.5, 67, 100),    # F
    (1.5, 71, 100),    # A
    (1.5, 74, 100),    # C
    (2.0, 67, 100),    # G (G7)
    (2.0, 71, 100),    # B
    (2.0, 74, 100),    # D
    (2.0, 76, 100),    # F#
    (2.5, 60, 100),    # C (Cm7)
    (2.5, 64, 100),    # Eb
    (2.5, 67, 100),    # G
    (2.5, 71, 100),    # Bb
    (3.0, 65, 100),    # F (F7)
    (3.0, 69, 100),    # A
    (3.0, 72, 100),    # C
    (3.0, 76, 100),    # E
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Bass: Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (1.5, 50, 80),     # D
    (2.0, 67, 80),     # G
    (2.5, 60, 80),     # C
    (3.0, 65, 80),     # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Sax: Melodic motif - begin, leave it hanging
sax_notes = [
    (1.5, 62, 100),    # D (start of motif)
    (1.75, 67, 100),   # F (suspend)
    (2.0, 64, 100),    # Eb (tension)
    (2.5, 62, 100),    # D (return)
    (2.75, 67, 100),   # F (resolve)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
drum_notes = [
    (3.0, 36, 100),    # Kick on 1
    (3.5, 38, 100),    # Snare on 2
    (4.0, 36, 100),    # Kick on 3
    (4.5, 38, 100),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    (3.0, 62, 100),    # D (Dm7)
    (3.0, 67, 100),    # F
    (3.0, 71, 100),    # A
    (3.0, 74, 100),    # C
    (3.5, 67, 100),    # G (G7)
    (3.5, 71, 100),    # B
    (3.5, 74, 100),    # D
    (3.5, 76, 100),    # F#
    (4.0, 60, 100),    # C (Cm7)
    (4.0, 64, 100),    # Eb
    (4.0, 67, 100),    # G
    (4.0, 71, 100),    # Bb
    (4.5, 65, 100),    # F (F7)
    (4.5, 69, 100),    # A
    (4.5, 72, 100),    # C
    (4.5, 76, 100),    # E
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Bass: Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (3.0, 50, 80),     # D
    (3.5, 67, 80),     # G
    (4.0, 60, 80),     # C
    (4.5, 65, 80),     # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Sax: Melodic motif - variation, tension build
sax_notes = [
    (3.0, 67, 100),    # F (continue motif)
    (3.25, 71, 100),   # A (tension)
    (3.5, 69, 100),    # G (subtle resolution)
    (3.75, 67, 100),   # F (suspense)
    (4.0, 64, 100),    # Eb (darkness)
    (4.25, 62, 100),   # D (return)
    (4.5, 67, 100),    # F (hang)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
drum_notes = [
    (4.5, 36, 100),    # Kick on 1
    (5.0, 38, 100),    # Snare on 2
    (5.5, 36, 100),    # Kick on 3
    (6.0, 38, 100),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    (4.5, 62, 100),    # D (Dm7)
    (4.5, 67, 100),    # F
    (4.5, 71, 100),    # A
    (4.5, 74, 100),    # C
    (5.0, 67, 100),    # G (G7)
    (5.0, 71, 100),    # B
    (5.0, 74, 100),    # D
    (5.0, 76, 100),    # F#
    (5.5, 60, 100),    # C (Cm7)
    (5.5, 64, 100),    # Eb
    (5.5, 67, 100),    # G
    (5.5, 71, 100),    # Bb
    (6.0, 65, 100),    # F (F7)
    (6.0, 69, 100),    # A
    (6.0, 72, 100),    # C
    (6.0, 76, 100),    # E
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Bass: Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (4.5, 50, 80),     # D
    (5.0, 67, 80),     # G
    (5.5, 60, 80),     # C
    (6.0, 65, 80),     # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.5
    ))

# Sax: Melodic motif - end with a question
sax_notes = [
    (4.5, 67, 100),    # F (extend)
    (4.75, 69, 100),   # G (tension)
    (5.0, 67, 100),    # F (suspense)
    (5.25, 64, 100),   # Eb (darkness)
    (5.5, 62, 100),    # D (return)
    (5.75, 67, 100),   # F (hang)
    (6.0, 67, 100),    # F (end on unresolved note)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(
        velocity=note[2],
        pitch=note[1],
        start=note[0],
        end=note[0] + 0.25
    ))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
