
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, F - G - Bb - A, with a slight bend on the Bb
sax_notes = [
    (84, 1.5, 0.375), (87, 1.875, 0.375), (81, 2.25, 0.375), (80, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line with chromatic approaches
bass_notes = [
    (53, 1.5, 0.375), (54, 1.875, 0.375), (52, 2.25, 0.375), (55, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375), (71, 1.875, 0.375), (69, 1.875, 0.375), (72, 1.875, 0.375),
    (67, 2.625, 0.375), (71, 2.625, 0.375), (69, 2.625, 0.375), (72, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (42, 1.5, 0.125),
    (38, 1.875, 0.375), (42, 1.875, 0.125),
    (36, 2.25, 0.375), (42, 2.25, 0.125),
    (38, 2.625, 0.375), (42, 2.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but with a slight variation (F - G - Bb - A)
sax_notes = [
    (84, 3.0, 0.375), (87, 3.375, 0.375), (81, 3.75, 0.375), (80, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line with chromatic approaches
bass_notes = [
    (53, 3.0, 0.375), (54, 3.375, 0.375), (52, 3.75, 0.375), (55, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 3.375, 0.375), (71, 3.375, 0.375), (69, 3.375, 0.375), (72, 3.375, 0.375),
    (67, 4.125, 0.375), (71, 4.125, 0.375), (69, 4.125, 0.375), (72, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif with a rest on the last note, leaving it hanging
sax_notes = [
    (80, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line with chromatic approaches
bass_notes = [
    (53, 4.5, 0.375), (54, 4.875, 0.375), (52, 5.25, 0.375), (55, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 4.875, 0.375), (71, 4.875, 0.375), (69, 4.875, 0.375), (72, 4.875, 0.375),
    (67, 5.625, 0.375), (71, 5.625, 0.375), (69, 5.625, 0.375), (72, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
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
