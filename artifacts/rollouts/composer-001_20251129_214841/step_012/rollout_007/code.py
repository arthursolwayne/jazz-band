
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1
drums_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on 2
    (42, 0.375, 0.1875),  # Hihat on 3
    (42, 0.5625, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on 4
    (42, 1.5, 0.1875)  # Hihat on 4
]
for note, start, duration in drums_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60) - E (64) - G (67) - B (71) - C (60)
sax_notes = [
    (60, 1.5, 0.375),
    (64, 1.875, 0.375),
    (67, 2.25, 0.375),
    (71, 2.625, 0.375),
    (60, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375),  # E
    (65, 3.0, 0.375)  # F
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375),  # C
    (64, 1.875, 0.375),  # E
    (67, 1.875, 0.375),  # G
    (71, 1.875, 0.375),  # B
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # E
    (67, 3.0, 0.375),  # G
    (71, 3.0, 0.375)  # B
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but an octave lower
sax_notes = [
    (48, 3.0, 0.375),
    (52, 3.375, 0.375),
    (55, 3.75, 0.375),
    (59, 4.125, 0.375),
    (48, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (48, 3.0, 0.375),  # C
    (49, 3.375, 0.375),  # C#
    (50, 3.75, 0.375),  # D
    (52, 4.125, 0.375),  # E
    (53, 4.5, 0.375)  # F
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (48, 3.375, 0.375),  # C
    (52, 3.375, 0.375),  # E
    (55, 3.375, 0.375),  # G
    (59, 3.375, 0.375),  # B
    (48, 4.5, 0.375),  # C
    (52, 4.5, 0.375),  # E
    (55, 4.5, 0.375),  # G
    (59, 4.5, 0.375)  # B
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif in the same octave with slight variation
sax_notes = [
    (48, 4.5, 0.375),
    (52, 4.875, 0.375),
    (55, 5.25, 0.375),
    (59, 5.625, 0.375),
    (48, 6.0, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (48, 4.5, 0.375),  # C
    (49, 4.875, 0.375),  # C#
    (50, 5.25, 0.375),  # D
    (52, 5.625, 0.375),  # E
    (53, 6.0, 0.375)  # F
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (48, 4.875, 0.375),  # C
    (52, 4.875, 0.375),  # E
    (55, 4.875, 0.375),  # G
    (59, 4.875, 0.375),  # B
    (48, 6.0, 0.375),  # C
    (52, 6.0, 0.375),  # E
    (55, 6.0, 0.375),  # G
    (59, 6.0, 0.375)  # B
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 3
drums_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875),  # Hihat on 2
    (42, 3.375, 0.1875),  # Hihat on 3
    (42, 3.5625, 0.1875),  # Hihat on 4
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),  # Hihat on 4
    (42, 4.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drums_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 4
drums_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on 2
    (42, 4.875, 0.1875),  # Hihat on 3
    (42, 5.0625, 0.1875),  # Hihat on 4
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on 4
    (42, 5.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drums_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
