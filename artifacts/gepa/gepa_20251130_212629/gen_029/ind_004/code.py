
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat 1
    (42, 0.375, 0.375),  # Hihat 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.75, 0.375),  # Hihat 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 1.125, 0.375),  # Hihat 4
    (38, 1.125, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (67, 1.875, 0.375),  # B7
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (74, 1.875, 0.375),
    (67, 2.625, 0.375),  # B7
    (69, 2.625, 0.375),
    (71, 2.625, 0.375),
    (74, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: short motif, start on bar 2
# D (62), F (65), G (67) - with space
sax_notes = [
    (62, 1.5, 0.3),    # D
    (65, 1.9, 0.3),    # F
    (67, 2.3, 0.3)     # G
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (65, 3.0, 0.375),  # F
    (66, 3.375, 0.375),  # F#
    (67, 3.75, 0.375),  # G
    (69, 4.125, 0.375)  # A
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (69, 3.375, 0.375),  # A7
    (71, 3.375, 0.375),
    (74, 3.375, 0.375),
    (76, 3.375, 0.375),
    (69, 4.125, 0.375),  # A7
    (71, 4.125, 0.375),
    (74, 4.125, 0.375),
    (76, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat 1
    (42, 3.375, 0.375),  # Hihat 2
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.75, 0.375),  # Hihat 3
    (36, 3.75, 0.375),  # Kick on 3
    (42, 4.125, 0.375),  # Hihat 4
    (38, 4.125, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: continuation of motif, last note hanging
sax_notes = [
    (69, 3.0, 0.3),    # A
    (67, 3.4, 0.3),    # G
    (65, 3.8, 0.3),    # F
    (62, 4.2, 0.3)     # D
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (69, 4.5, 0.375),  # A
    (70, 4.875, 0.375),  # A#
    (71, 5.25, 0.375),  # B
    (72, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (71, 4.875, 0.375),  # B7
    (74, 4.875, 0.375),
    (76, 4.875, 0.375),
    (79, 4.875, 0.375),
    (71, 5.625, 0.375),  # B7
    (74, 5.625, 0.375),
    (76, 5.625, 0.375),
    (79, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat 1
    (42, 4.875, 0.375),  # Hihat 2
    (38, 4.875, 0.375),  # Snare on 2
    (42, 5.25, 0.375),  # Hihat 3
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.625, 0.375),  # Hihat 4
    (38, 5.625, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: end with a question, not a statement
sax_notes = [
    (65, 4.5, 0.3),    # F
    (62, 4.9, 0.3),    # D
    (67, 5.3, 0.3),    # G
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
