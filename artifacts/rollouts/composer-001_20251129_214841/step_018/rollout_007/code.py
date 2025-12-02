
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
drum_notes = [
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

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
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(nt)

# Bass: Walking line in C minor
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # Db
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # Eb
    (64, 3.0, 0.375)    # E
]
for note, start, duration in bass_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nt)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    (60, 1.875, 0.125), (64, 1.875, 0.125), (67, 1.875, 0.125), (62, 1.875, 0.125),
    # Bar 3: C7 again
    (60, 3.0, 0.125), (64, 3.0, 0.125), (67, 3.0, 0.125), (62, 3.0, 0.125)
]
for note, start, duration in piano_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(nt)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with a slight variation
sax_notes = [
    (60, 3.0, 0.375),
    (64, 3.375, 0.375),
    (67, 3.75, 0.375),
    (71, 4.125, 0.375),
    (60, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(nt)

# Bass: Walking line in C minor
bass_notes = [
    (64, 3.0, 0.375),  # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375)    # G#
]
for note, start, duration in bass_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nt)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: C7 (C, E, B, D)
    (60, 3.375, 0.125), (64, 3.375, 0.125), (67, 3.375, 0.125), (62, 3.375, 0.125),
    # Bar 4: C7 again
    (60, 4.5, 0.125), (64, 4.5, 0.125), (67, 4.5, 0.125), (62, 4.5, 0.125)
]
for note, start, duration in piano_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(nt)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    (60, 4.5, 0.375),
    (64, 4.875, 0.375),
    (67, 5.25, 0.375),
    (71, 5.625, 0.375),
    (60, 6.0, 0.375)
]
for note, start, duration in sax_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(nt)

# Bass: Walking line in C minor
bass_notes = [
    (68, 4.5, 0.375),  # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
    (72, 6.0, 0.375)    # C
]
for note, start, duration in bass_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nt)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: C7 (C, E, B, D)
    (60, 4.875, 0.125), (64, 4.875, 0.125), (67, 4.875, 0.125), (62, 4.875, 0.125)
]
for note, start, duration in piano_notes:
    nt = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(nt)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125),
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
