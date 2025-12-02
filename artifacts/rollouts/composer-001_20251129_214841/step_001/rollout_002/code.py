
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125), (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125), (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60) -> E (64) -> Bb (62) -> D (67), legato
sax_notes = [
    (60, 1.5, 0.75), (64, 2.25, 0.75), (62, 3.0, 0.75)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C minor (C Eb F G)
bass_notes = [
    (60, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375), (67, 2.625, 0.375),
    (60, 3.0, 0.375), (63, 3.375, 0.375), (62, 3.75, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (C7, F7)
piano_notes = [
    # C7 (C, E, Bb, B)
    (60, 2.25, 0.375), (64, 2.25, 0.375), (62, 2.25, 0.375), (63, 2.25, 0.375),
    # F7 (F, A, D, E)
    (65, 3.0, 0.375), (69, 3.0, 0.375), (67, 3.0, 0.375), (68, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but shift up a 3rd (E -> G -> D -> F#)
sax_notes = [
    (64, 3.0, 0.75), (67, 3.75, 0.75), (65, 4.5, 0.75)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C minor (C Eb F G)
bass_notes = [
    (60, 3.0, 0.375), (63, 3.375, 0.375), (62, 3.75, 0.375), (67, 4.125, 0.375),
    (60, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (F7, Bb7)
piano_notes = [
    # F7 (F, A, D, E)
    (65, 3.75, 0.375), (69, 3.75, 0.375), (67, 3.75, 0.375), (68, 3.75, 0.375),
    # Bb7 (Bb, D, F, G)
    (62, 4.5, 0.375), (67, 4.5, 0.375), (65, 4.5, 0.375), (67, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif but shift up a 3rd (G -> B -> F -> A)
sax_notes = [
    (67, 4.5, 0.75), (71, 5.25, 0.75), (69, 6.0, 0.75)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C minor (C Eb F G)
bass_notes = [
    (60, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375), (67, 5.625, 0.375),
    (60, 6.0, 0.375), (63, 6.375, 0.375), (62, 6.75, 0.375), (67, 7.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bb7, E7)
piano_notes = [
    # Bb7 (Bb, D, F, G)
    (62, 5.25, 0.375), (67, 5.25, 0.375), (65, 5.25, 0.375), (67, 5.25, 0.375),
    # E7 (E, G, B, C)
    (64, 6.0, 0.375), (67, 6.0, 0.375), (69, 6.0, 0.375), (71, 6.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: same pattern as bar 1
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
