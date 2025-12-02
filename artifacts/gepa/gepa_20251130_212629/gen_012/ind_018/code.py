
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125), (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125), (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (24, 1.5, 0.375), (25, 1.875, 0.375), (23, 2.25, 0.375), (21, 2.625, 0.375),
    (20, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Fm7 on 2, Bb7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Eb) on beat 2 (1.875)
    (65, 1.875, 0.375), (62, 1.875, 0.375), (60, 1.875, 0.375), (59, 1.875, 0.375),
    # Bb7 (Bb, D, F, Ab) on beat 4 (2.625)
    (62, 2.625, 0.375), (64, 2.625, 0.375), (65, 2.625, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375),
    (36, 2.25, 0.375), (38, 2.625, 0.375),
    (42, 1.5, 0.125), (42, 1.625, 0.125), (42, 1.75, 0.125), (42, 1.875, 0.125),
    (42, 2.0, 0.125), (42, 2.125, 0.125), (42, 2.25, 0.125), (42, 2.375, 0.125),
    (42, 2.5, 0.125), (42, 2.625, 0.125), (42, 2.75, 0.125), (42, 2.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: motif in Fm, start on beat 1
# F, Ab, C, Eb - short motif, leave it hanging
sax_notes = [
    (65, 1.5, 0.375), (62, 1.875, 0.375), (60, 2.25, 0.375), (59, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (20, 3.0, 0.375), (22, 3.375, 0.375), (21, 3.75, 0.375), (23, 4.125, 0.375),
    (24, 4.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Fm7 on 2, Bb7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Eb) on beat 2 (3.375)
    (65, 3.375, 0.375), (62, 3.375, 0.375), (60, 3.375, 0.375), (59, 3.375, 0.375),
    # Bb7 (Bb, D, F, Ab) on beat 4 (4.125)
    (62, 4.125, 0.375), (64, 4.125, 0.375), (65, 4.125, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375),
    (36, 3.75, 0.375), (38, 4.125, 0.375),
    (42, 3.0, 0.125), (42, 3.125, 0.125), (42, 3.25, 0.125), (42, 3.375, 0.125),
    (42, 3.5, 0.125), (42, 3.625, 0.125), (42, 3.75, 0.125), (42, 3.875, 0.125),
    (42, 4.0, 0.125), (42, 4.125, 0.125), (42, 4.25, 0.125), (42, 4.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: continue motif, repeat and resolve
sax_notes = [
    (65, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (59, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (24, 4.5, 0.375), (25, 4.875, 0.375), (23, 5.25, 0.375), (21, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Fm7 on 2, Bb7 on 4
piano_notes = [
    # Fm7 (F, Ab, C, Eb) on beat 2 (4.875)
    (65, 4.875, 0.375), (62, 4.875, 0.375), (60, 4.875, 0.375), (59, 4.875, 0.375),
    # Bb7 (Bb, D, F, Ab) on beat 4 (5.625)
    (62, 5.625, 0.375), (64, 5.625, 0.375), (65, 5.625, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375),
    (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 4.5, 0.125), (42, 4.625, 0.125), (42, 4.75, 0.125), (42, 4.875, 0.125),
    (42, 5.0, 0.125), (42, 5.125, 0.125), (42, 5.25, 0.125), (42, 5.375, 0.125),
    (42, 5.5, 0.125), (42, 5.625, 0.125), (42, 5.75, 0.125), (42, 5.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: finish motif and resolve
sax_notes = [
    (65, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
