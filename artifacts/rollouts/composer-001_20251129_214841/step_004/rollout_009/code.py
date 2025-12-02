
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: C (60) - E (64) - G (67) - B (71) - C (60)
sax_notes = [
    (60, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375), (71, 2.625, 0.375),
    (60, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line
bass_notes = [
    (60, 1.5, 0.375), (62, 1.875, 0.375), (63, 2.25, 0.375), (65, 2.625, 0.375),
    (67, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# C7 on beat 2 (1.875s), E7 on beat 4 (2.625s)
piano_notes = [
    # C7: C (60), E (64), B (71), D (62)
    (60, 1.875, 0.375), (64, 1.875, 0.375), (71, 1.875, 0.375), (62, 1.875, 0.375),
    # E7: E (64), G (67), D (62), F (65)
    (64, 2.625, 0.375), (67, 2.625, 0.375), (62, 2.625, 0.375), (65, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.125),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 2.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Repeat the motif, but with a slight variation
sax_notes = [
    (60, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375), (71, 4.125, 0.375),
    (60, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line
bass_notes = [
    (67, 3.0, 0.375), (69, 3.375, 0.375), (70, 3.75, 0.375), (72, 4.125, 0.375),
    (74, 4.5, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# C7 on beat 2 (3.375s), E7 on beat 4 (4.125s)
piano_notes = [
    # C7: C (60), E (64), B (71), D (62)
    (60, 3.375, 0.375), (64, 3.375, 0.375), (71, 3.375, 0.375), (62, 3.375, 0.375),
    # E7: E (64), G (67), D (62), F (65)
    (64, 4.125, 0.375), (67, 4.125, 0.375), (62, 4.125, 0.375), (65, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.125),
    (36, 4.125, 0.375), (38, 4.5, 0.375), (42, 4.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: End the motif
sax_notes = [
    (60, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375), (71, 5.625, 0.375),
    (60, 6.0, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line
bass_notes = [
    (74, 4.5, 0.375), (76, 4.875, 0.375), (77, 5.25, 0.375), (79, 5.625, 0.375),
    (81, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# C7 on beat 2 (4.875s), E7 on beat 4 (5.625s)
piano_notes = [
    # C7: C (60), E (64), B (71), D (62)
    (60, 4.875, 0.375), (64, 4.875, 0.375), (71, 4.875, 0.375), (62, 4.875, 0.375),
    # E7: E (64), G (67), D (62), F (65)
    (64, 5.625, 0.375), (67, 5.625, 0.375), (62, 5.625, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.125),
    (36, 5.625, 0.375), (38, 6.0, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
