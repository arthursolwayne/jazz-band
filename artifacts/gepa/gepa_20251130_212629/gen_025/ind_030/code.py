
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),  # Hihat on 2
    (38, 0.125, 0.375),  # Snare on 2
    (42, 0.25, 0.125),  # Hihat on 3
    (36, 0.375, 0.375),  # Kick on 3
    (42, 0.375, 0.125),  # Hihat on 3
    (42, 0.5, 0.125),  # Hihat on 4
    (38, 0.5, 0.375),  # Snare on 4
    (42, 0.625, 0.125),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),  # Fm root (F) with chromatic approach up
    (40, 1.875, 0.375),  # Eb (chromatic)
    (41, 2.25, 0.375),  # D
    (43, 2.625, 0.375)  # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    (44, 1.875, 0.125),  # Bb (F7 chord: F, Ab, C, Bb)
    (47, 1.875, 0.125),  # C
    (49, 1.875, 0.125),  # Eb
    (50, 1.875, 0.125),  # F
    (44, 2.625, 0.125),  # Bb (F7 again)
    (47, 2.625, 0.125),  # C
    (49, 2.625, 0.125),  # Eb
    (50, 2.625, 0.125)   # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums continues
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.125),  # Hihat on 1
    (42, 1.625, 0.125),  # Hihat on 2
    (38, 1.625, 0.375),  # Snare on 2
    (42, 1.75, 0.125),  # Hihat on 3
    (36, 1.875, 0.375),  # Kick on 3
    (42, 1.875, 0.125),  # Hihat on 3
    (42, 2.0, 0.125),  # Hihat on 4
    (38, 2.0, 0.375),  # Snare on 4
    (42, 2.125, 0.125)  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: Motif starts on bar 2, ends on bar 4 with a question
# Motif: F, Ab, Bb, C -> F, Ab, Bb, B (question)
sax_notes = [
    (53, 1.5, 0.125),  # F
    (51, 1.625, 0.125),  # Ab
    (50, 1.75, 0.125),  # Bb
    (55, 1.875, 0.125),  # C
    (53, 2.25, 0.125),  # F
    (51, 2.375, 0.125),  # Ab
    (50, 2.5, 0.125),  # Bb
    (54, 2.625, 0.125)  # B (question)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (42, 3.0, 0.375),  # C (chromatic approach down)
    (40, 3.375, 0.375),  # Eb
    (41, 3.75, 0.375),  # D
    (43, 4.125, 0.375)  # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    (44, 3.375, 0.125),  # Bb (F7 chord)
    (47, 3.375, 0.125),  # C
    (49, 3.375, 0.125),  # Eb
    (50, 3.375, 0.125),  # F
    (44, 4.125, 0.125),  # Bb (F7 again)
    (47, 4.125, 0.125),  # C
    (49, 4.125, 0.125),  # Eb
    (50, 4.125, 0.125)   # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums continues
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat on 1
    (42, 3.125, 0.125),  # Hihat on 2
    (38, 3.125, 0.375),  # Snare on 2
    (42, 3.25, 0.125),  # Hihat on 3
    (36, 3.375, 0.375),  # Kick on 3
    (42, 3.375, 0.125),  # Hihat on 3
    (42, 3.5, 0.125),  # Hihat on 4
    (38, 3.5, 0.375),  # Snare on 4
    (42, 3.625, 0.125)  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: continuation of motif
# Motif continues, hinting at resolution but holding back
sax_notes = [
    (50, 3.0, 0.125),  # Bb
    (54, 3.125, 0.125),  # B
    (53, 3.25, 0.125),  # F
    (51, 3.375, 0.125),  # Ab
    (50, 3.5, 0.125),  # Bb
    (54, 3.625, 0.125),  # B (ends with question)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (42, 4.5, 0.375),  # C (chromatic approach down)
    (40, 4.875, 0.375),  # Eb
    (41, 5.25, 0.375),  # D
    (43, 5.625, 0.375)  # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    (44, 4.875, 0.125),  # Bb (F7 chord)
    (47, 4.875, 0.125),  # C
    (49, 4.875, 0.125),  # Eb
    (50, 4.875, 0.125),  # F
    (44, 5.625, 0.125),  # Bb (F7 again)
    (47, 5.625, 0.125),  # C
    (49, 5.625, 0.125),  # Eb
    (50, 5.625, 0.125)   # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray on drums continues
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on 1
    (42, 4.625, 0.125),  # Hihat on 2
    (38, 4.625, 0.375),  # Snare on 2
    (42, 4.75, 0.125),  # Hihat on 3
    (36, 4.875, 0.375),  # Kick on 3
    (42, 4.875, 0.125),  # Hihat on 3
    (42, 5.0, 0.125),  # Hihat on 4
    (38, 5.0, 0.375),  # Snare on 4
    (42, 5.125, 0.125)  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: last note of the motif, with space
sax_notes = [
    (54, 5.625, 0.125),  # B (last note of the motif)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
