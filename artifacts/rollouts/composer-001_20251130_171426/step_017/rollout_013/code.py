
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
    # Kick on 1 and 3
    (0.0, 36, 100),
    (0.75, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100),
    (1.125, 38, 100),
    # Hihat on every eighth
    (0.0, 42, 80),
    (0.375, 42, 80),
    (0.75, 42, 80),
    (1.125, 42, 80),
    (1.5, 42, 80)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm
bass_notes = [
    (1.5, 42, 100),  # F
    (1.75, 40, 100),  # Eb
    (2.0, 38, 100),  # D
    (2.25, 36, 100),  # C
    (2.5, 42, 100),  # F
    (2.75, 40, 100),  # Eb
    (3.0, 38, 100),  # D
    (3.25, 36, 100)  # C
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    (1.75, 42, 100),  # F
    (1.75, 46, 100),  # A
    (1.75, 47, 100),  # Bb
    (1.75, 50, 100),  # D
    # Bar 2, beat 4: Bb7
    (2.25, 47, 100),  # Bb
    (2.25, 50, 100),  # D
    (2.25, 52, 100),  # F
    (2.25, 55, 100),  # A
    # Bar 3, beat 2: Eb7
    (2.75, 40, 100),  # Eb
    (2.75, 44, 100),  # G
    (2.75, 45, 100),  # Ab
    (2.75, 48, 100),  # C
    # Bar 3, beat 4: Ab7
    (3.25, 45, 100),  # Ab
    (3.25, 48, 100),  # C
    (3.25, 50, 100),  # D
    (3.25, 53, 100)   # F
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36, 100),
    (1.875, 38, 100),
    (2.25, 36, 100),
    (2.625, 38, 100),
    (3.0, 42, 80),
    (3.375, 42, 80),
    (3.75, 42, 80),
    (4.125, 42, 80),
    (4.5, 42, 80)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Fm
bass_notes = [
    (3.0, 36, 100),  # C
    (3.25, 38, 100),  # D
    (3.5, 40, 100),  # Eb
    (3.75, 42, 100),  # F
    (4.0, 36, 100),  # C
    (4.25, 38, 100),  # D
    (4.5, 40, 100),  # Eb
    (4.75, 42, 100)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    (3.25, 42, 100),  # F
    (3.25, 46, 100),  # A
    (3.25, 47, 100),  # Bb
    (3.25, 50, 100),  # D
    # Bar 3, beat 4: Bb7
    (3.75, 47, 100),  # Bb
    (3.75, 50, 100),  # D
    (3.75, 52, 100),  # F
    (3.75, 55, 100),  # A
    # Bar 4, beat 2: Eb7
    (4.25, 40, 100),  # Eb
    (4.25, 44, 100),  # G
    (4.25, 45, 100),  # Ab
    (4.25, 48, 100),  # C
    # Bar 4, beat 4: Ab7
    (4.75, 45, 100),  # Ab
    (4.75, 48, 100),  # C
    (4.75, 50, 100),  # D
    (4.75, 53, 100)   # F
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (3.0, 36, 100),
    (3.375, 38, 100),
    (3.75, 36, 100),
    (4.125, 38, 100),
    (4.5, 42, 80),
    (4.875, 42, 80),
    (5.25, 42, 80),
    (5.625, 42, 80),
    (6.0, 42, 80)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.1875))

# Sax: melody (Bar 2 - Bar 4)
# Motif: F (Dante), Bb (Marcus), Eb (Diane), F (Little Ray) — then repeat with variation
sax_notes = [
    # Bar 2, beat 1: F (Dante)
    (1.5, 42, 100),
    # Bar 2, beat 2: Bb (Marcus)
    (1.875, 47, 100),
    # Bar 2, beat 3: Eb (Diane)
    (2.25, 40, 100),
    # Bar 2, beat 4: F (Little Ray)
    (2.625, 42, 100),
    # Bar 3, beat 1: F (Dante)
    (3.0, 42, 100),
    # Bar 3, beat 2: Bb (Marcus)
    (3.375, 47, 100),
    # Bar 3, beat 3: G (Diane)
    (3.75, 44, 100),
    # Bar 3, beat 4: C (Little Ray)
    (4.125, 36, 100),
    # Bar 4, beat 1: F (Dante)
    (4.5, 42, 100),
    # Bar 4, beat 2: Bb (Marcus)
    (4.875, 47, 100),
    # Bar 4, beat 3: Eb (Diane)
    (5.25, 40, 100),
    # Bar 4, beat 4: F (Little Ray)
    (5.625, 42, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
