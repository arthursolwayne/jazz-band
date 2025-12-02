
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1 & 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (38, 0.75, 0.375),    # Snare on 3
    (42, 0.75, 0.1875),   # Hihat on 3 & 4
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.5, 0.375)      # Kick on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    (57, 1.5, 0.375),     # F
    (58, 1.875, 0.375),   # F#
    (59, 2.25, 0.375),    # G
    (56, 2.625, 0.375)    # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.1875),  # A (F7 chord)
    (67, 1.875, 0.1875),  # C
    (71, 1.875, 0.1875),  # E
    (64, 1.875, 0.1875),  # F
    (69, 2.625, 0.1875),  # Bb (F7 chord)
    (72, 2.625, 0.1875),  # D
    (76, 2.625, 0.1875),  # F
    (67, 2.625, 0.1875)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.5, 0.1875),    # Hihat on 1 & 2
    (42, 1.875, 0.1875),
    (36, 2.25, 0.375),    # Kick on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.25, 0.1875),   # Hihat on 3 & 4
    (42, 2.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax - motif in F
sax_notes = [
    (66, 1.5, 0.375),     # F
    (68, 1.875, 0.375),   # G
    (67, 2.25, 0.375),    # F#
    (66, 2.625, 0.375)    # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass - walking line
bass_notes = [
    (60, 3.0, 0.375),     # A
    (61, 3.375, 0.375),   # Bb
    (62, 3.75, 0.375),    # B
    (59, 4.125, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano - comp on 2 and 4
piano_notes = [
    (62, 3.375, 0.1875),  # A
    (67, 3.375, 0.1875),  # C
    (71, 3.375, 0.1875),  # E
    (64, 3.375, 0.1875),  # F
    (69, 4.125, 0.1875),  # Bb
    (72, 4.125, 0.1875),  # D
    (76, 4.125, 0.1875),  # F
    (67, 4.125, 0.1875)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),     # Kick on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.0, 0.1875),    # Hihat on 1 & 2
    (42, 3.375, 0.1875),
    (36, 3.75, 0.375),    # Kick on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 3.75, 0.1875),   # Hihat on 3 & 4
    (42, 4.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax - motif in F
sax_notes = [
    (66, 3.0, 0.375),     # F
    (68, 3.375, 0.375),   # G
    (67, 3.75, 0.375),    # F#
    (66, 4.125, 0.375)    # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass - walking line
bass_notes = [
    (63, 4.5, 0.375),     # B
    (64, 4.875, 0.375),   # C
    (65, 5.25, 0.375),    # C#
    (62, 5.625, 0.375)    # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano - comp on 2 and 4
piano_notes = [
    (62, 4.875, 0.1875),  # A
    (67, 4.875, 0.1875),  # C
    (71, 4.875, 0.1875),  # E
    (64, 4.875, 0.1875),  # F
    (69, 5.625, 0.1875),  # Bb
    (72, 5.625, 0.1875),  # D
    (76, 5.625, 0.1875),  # F
    (67, 5.625, 0.1875)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),     # Kick on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.5, 0.1875),    # Hihat on 1 & 2
    (42, 4.875, 0.1875),
    (36, 5.25, 0.375),    # Kick on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.25, 0.1875),   # Hihat on 3 & 4
    (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax - motif in F
sax_notes = [
    (66, 4.5, 0.375),     # F
    (68, 4.875, 0.375),   # G
    (67, 5.25, 0.375),    # F#
    (66, 5.625, 0.375)    # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('waynes_moment.mid')
