
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    (45, 1.5, 0.375),  # F
    (47, 1.875, 0.375),  # G
    (46, 2.25, 0.375),  # F#
    (44, 2.625, 0.375)   # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 chord
    (57, 1.5, 0.375),  # F
    (62, 1.5, 0.375),  # Bb
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # D
    # Bar 3 - F7 chord
    (57, 2.25, 0.375),  # F
    (62, 2.25, 0.375),  # Bb
    (60, 2.25, 0.375),  # C
    (64, 2.25, 0.375),  # D
    # Bar 4 - F7 chord
    (57, 3.0, 0.375),  # F
    (62, 3.0, 0.375),  # Bb
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Sax: Motif (F, G#, Bb, F)
sax_notes = [
    (57, 1.5, 0.375),  # F
    (61, 1.875, 0.375),  # G#
    (60, 2.25, 0.375),  # Bb
    (57, 2.625, 0.375)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F
bass_notes = [
    (47, 3.0, 0.375),  # G
    (49, 3.375, 0.375),  # A
    (48, 3.75, 0.375),  # Ab
    (46, 4.125, 0.375)   # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 3 - F7 chord
    (57, 3.0, 0.375),  # F
    (62, 3.0, 0.375),  # Bb
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # D
    # Bar 4 - F7 chord
    (57, 3.75, 0.375),  # F
    (62, 3.75, 0.375),  # Bb
    (60, 3.75, 0.375),  # C
    (64, 3.75, 0.375),  # D
    # Bar 4 - F7 chord again
    (57, 4.5, 0.375),  # F
    (62, 4.5, 0.375),  # Bb
    (60, 4.5, 0.375),  # C
    (64, 4.5, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: Full pattern
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F
bass_notes = [
    (49, 4.5, 0.375),  # A
    (47, 4.875, 0.375),  # G
    (45, 5.25, 0.375),  # F
    (44, 5.625, 0.375)   # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords comp on 2 and 4
piano_notes = [
    # Bar 4 - F7 chord
    (57, 4.5, 0.375),  # F
    (62, 4.5, 0.375),  # Bb
    (60, 4.5, 0.375),  # C
    (64, 4.5, 0.375),  # D
    # Bar 4 - F7 chord again
    (57, 5.25, 0.375),  # F
    (62, 5.25, 0.375),  # Bb
    (60, 5.25, 0.375),  # C
    (64, 5.25, 0.375),  # D
    # Bar 4 - F7 chord again
    (57, 5.625, 0.375),  # F
    (62, 5.625, 0.375),  # Bb
    (60, 5.625, 0.375),  # C
    (64, 5.625, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Sax: Motif (F, G#, Bb, F)
sax_notes = [
    (57, 4.5, 0.375),  # F
    (61, 4.875, 0.375),  # G#
    (60, 5.25, 0.375),  # Bb
    (57, 5.625, 0.375)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
