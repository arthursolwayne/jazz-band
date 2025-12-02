
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 0.375), (42, 0.0, 0.375),
    (38, 0.375, 0.375), (42, 0.375, 0.375),
    (36, 0.75, 0.375), (42, 0.75, 0.375),
    (38, 1.125, 0.375), (42, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Sax starts the motif - Fm7 (F, Ab, Bb, D)
# Motif: F, Eb, D, C (descending chromatic to C)
sax_notes = [
    (84, 1.5, 0.375),   # F
    (81, 1.875, 0.375), # Eb
    (80, 2.25, 0.375),  # D
    (79, 2.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - Walking line in Fm
# F, Gb, Ab, A
bass_notes = [
    (53, 1.5, 0.375),   # F
    (52, 1.875, 0.375), # Gb
    (51, 2.25, 0.375),  # Ab
    (50, 2.625, 0.375)  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, D)
# Chord on beat 2 (1.875) and beat 4 (2.625)
piano_notes = [
    (84, 1.875, 0.375), # F
    (81, 1.875, 0.375), # Ab
    (82, 1.875, 0.375), # Bb
    (86, 1.875, 0.375), # D

    (84, 2.625, 0.375), # F
    (81, 2.625, 0.375), # Ab
    (82, 2.625, 0.375), # Bb
    (86, 2.625, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 2
drum_notes = [
    (36, 1.5, 0.375), (42, 1.5, 0.375),
    (38, 1.875, 0.375), (42, 1.875, 0.375),
    (36, 2.25, 0.375), (42, 2.25, 0.375),
    (38, 2.625, 0.375), (42, 2.625, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Sax continues motif

# Bar 3 - Sax: Repeat the motif on the next measure
sax_notes = [
    (84, 3.0, 0.375),   # F
    (81, 3.375, 0.375), # Eb
    (80, 3.75, 0.375),  # D
    (79, 4.125, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - Walking line in Fm
# Bb, B, C, C#
bass_notes = [
    (82, 3.0, 0.375),   # Bb
    (83, 3.375, 0.375), # B
    (84, 3.75, 0.375),  # C
    (85, 4.125, 0.375)  # C#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, D)
# Chord on beat 2 (3.375) and beat 4 (4.125)
piano_notes = [
    (84, 3.375, 0.375), # F
    (81, 3.375, 0.375), # Ab
    (82, 3.375, 0.375), # Bb
    (86, 3.375, 0.375), # D

    (84, 4.125, 0.375), # F
    (81, 4.125, 0.375), # Ab
    (82, 4.125, 0.375), # Bb
    (86, 4.125, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 3
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.375),
    (38, 3.375, 0.375), (42, 3.375, 0.375),
    (36, 3.75, 0.375), (42, 3.75, 0.375),
    (38, 4.125, 0.375), (42, 4.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Sax finishes motif with a resolution

# Bar 4 - Sax: Motif resolution to Bb
sax_notes = [
    (84, 4.5, 0.375),   # F
    (81, 4.875, 0.375), # Eb
    (80, 5.25, 0.375),  # D
    (82, 5.625, 0.375)  # Bb (resolve to Bb)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - Walking line in Fm
# D, Eb, F, Gb
bass_notes = [
    (86, 4.5, 0.375),   # D
    (81, 4.875, 0.375), # Eb
    (53, 5.25, 0.375),  # F
    (52, 5.625, 0.375)  # Gb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, D)
# Chord on beat 2 (4.875) and beat 4 (5.625)
piano_notes = [
    (84, 4.875, 0.375), # F
    (81, 4.875, 0.375), # Ab
    (82, 4.875, 0.375), # Bb
    (86, 4.875, 0.375), # D

    (84, 5.625, 0.375), # F
    (81, 5.625, 0.375), # Ab
    (82, 5.625, 0.375), # Bb
    (86, 5.625, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 4
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.375),
    (38, 4.875, 0.375), (42, 4.875, 0.375),
    (36, 5.25, 0.375), (42, 5.25, 0.375),
    (38, 5.625, 0.375), (42, 5.625, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
