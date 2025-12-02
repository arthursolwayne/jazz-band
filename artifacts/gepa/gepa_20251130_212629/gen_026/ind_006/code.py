
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    (36, 0.0, 1.0),  # Kick on beat 1
    (38, 0.5, 1.0),  # Snare on beat 2
    (42, 0.0, 1.0),  # Hihat on beat 1
    (42, 0.25, 1.0), # Hihat on "and" of 1
    (42, 0.5, 1.0),  # Hihat on beat 2
    (42, 0.75, 1.0), # Hihat on "and" of 2
    (36, 1.0, 1.0),  # Kick on beat 3
    (38, 1.5, 1.0),  # Snare on beat 4
    (42, 1.0, 1.0),  # Hihat on beat 3
    (42, 1.25, 1.0), # Hihat on "and" of 3
    (42, 1.5, 1.0),  # Hihat on beat 4
    (42, 1.75, 1.0)  # Hihat on "and" of 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375), # F#
    (44, 2.25, 0.375),  # E
    (45, 2.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),  # A (F7)
    (67, 1.5, 0.375),  # C
    (69, 1.5, 0.375),  # D
    (60, 1.5, 0.375),  # F
    (62, 2.25, 0.375), # A (F7)
    (67, 2.25, 0.375), # C
    (69, 2.25, 0.375), # D
    (60, 2.25, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Motif - start it, leave it hanging
sax_notes = [
    (66, 1.5, 0.25),  # G
    (68, 1.75, 0.25), # A
    (69, 2.0, 0.25),  # A#
    (68, 2.25, 0.25)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    (45, 3.0, 0.375),  # F
    (46, 3.375, 0.375), # F#
    (44, 3.75, 0.375),  # E
    (45, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.0, 0.375),  # A (F7)
    (67, 3.0, 0.375),  # C
    (69, 3.0, 0.375),  # D
    (60, 3.0, 0.375),  # F
    (62, 3.75, 0.375), # A (F7)
    (67, 3.75, 0.375), # C
    (69, 3.75, 0.375), # D
    (60, 3.75, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 1.0),  # Kick on beat 1
    (38, 3.5, 1.0),  # Snare on beat 2
    (42, 3.0, 1.0),  # Hihat on beat 1
    (42, 3.25, 1.0), # Hihat on "and" of 1
    (42, 3.5, 1.0),  # Hihat on beat 2
    (42, 3.75, 1.0), # Hihat on "and" of 2
    (36, 4.0, 1.0),  # Kick on beat 3
    (38, 4.5, 1.0),  # Snare on beat 4
    (42, 4.0, 1.0),  # Hihat on beat 3
    (42, 4.25, 1.0), # Hihat on "and" of 3
    (42, 4.5, 1.0),  # Hihat on beat 4
    (42, 4.75, 1.0)  # Hihat on "and" of 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    (45, 4.5, 0.375),  # F
    (46, 4.875, 0.375), # F#
    (44, 5.25, 0.375),  # E
    (45, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.5, 0.375),  # A (F7)
    (67, 4.5, 0.375),  # C
    (69, 4.5, 0.375),  # D
    (60, 4.5, 0.375),  # F
    (62, 5.25, 0.375), # A (F7)
    (67, 5.25, 0.375), # C
    (69, 5.25, 0.375), # D
    (60, 5.25, 0.375)  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),  # Kick on beat 1
    (38, 5.0, 1.0),  # Snare on beat 2
    (42, 4.5, 1.0),  # Hihat on beat 1
    (42, 4.75, 1.0), # Hihat on "and" of 1
    (42, 5.0, 1.0),  # Hihat on beat 2
    (42, 5.25, 1.0), # Hihat on "and" of 2
    (36, 5.5, 1.0),  # Kick on beat 3
    (38, 6.0, 1.0),  # Snare on beat 4
    (42, 5.5, 1.0),  # Hihat on beat 3
    (42, 5.75, 1.0), # Hihat on "and" of 3
    (42, 6.0, 1.0),  # Hihat on beat 4
    (42, 6.25, 1.0)  # Hihat on "and" of 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Dante: Motif - finish it, end with a question
sax_notes = [
    (66, 4.5, 0.25),  # G
    (68, 4.75, 0.25), # A
    (69, 5.0, 0.25),  # A#
    (68, 5.25, 0.25), # A
    (67, 5.5, 0.375)  # G#
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
