
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Sax: motif in F minor
sax_notes = [
    (60, 1.5, 0.25), (62, 1.75, 0.25), (60, 2.0, 0.25), (62, 2.25, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line, chromatic approaches
bass_notes = [
    (45, 1.5, 0.25), (46, 1.75, 0.25), (47, 2.0, 0.25), (48, 2.25, 0.25)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 1.75, 0.25), (67, 1.75, 0.25), (69, 1.75, 0.25), (71, 1.75, 0.25),
    (64, 2.25, 0.25), (67, 2.25, 0.25), (69, 2.25, 0.25), (71, 2.25, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax: repeat and expand motif
sax_notes = [
    (60, 3.0, 0.25), (62, 3.25, 0.25), (60, 3.5, 0.25), (62, 3.75, 0.25),
    (64, 4.0, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line, chromatic approaches
bass_notes = [
    (48, 3.0, 0.25), (49, 3.25, 0.25), (50, 3.5, 0.25), (51, 3.75, 0.25),
    (52, 4.0, 0.25)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 3.25, 0.25), (67, 3.25, 0.25), (69, 3.25, 0.25), (71, 3.25, 0.25),
    (64, 3.75, 0.25), (67, 3.75, 0.25), (69, 3.75, 0.25), (71, 3.75, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    (64, 4.5, 0.25), (62, 4.75, 0.25), (60, 5.0, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line, chromatic approaches
bass_notes = [
    (52, 4.5, 0.25), (51, 4.75, 0.25), (50, 5.0, 0.25), (49, 5.25, 0.25),
    (48, 5.5, 0.25)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 4.75, 0.25), (67, 4.75, 0.25), (69, 4.75, 0.25), (71, 4.75, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
