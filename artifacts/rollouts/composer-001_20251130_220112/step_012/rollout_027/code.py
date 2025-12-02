
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 (F, Ab, Bb, D) -> F, Ab, Bb, D, Gb, Ab, Bb
sax_notes = [
    (77, 1.5, 0.375),   # F
    (70, 1.875, 0.375), # Ab
    (71, 2.25, 0.375),  # Bb
    (69, 2.625, 0.375), # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 1.5, 0.375),   # F
    (62, 1.875, 0.375), # Eb
    (63, 2.25, 0.375),  # D
    (61, 2.625, 0.375), # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (77, 1.875, 0.375), # F7 (F, Ab, C, E)
    (70, 1.875, 0.375),
    (72, 1.875, 0.375),
    (74, 1.875, 0.375),
    (77, 2.625, 0.375),
    (70, 2.625, 0.375),
    (72, 2.625, 0.375),
    (74, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes_bar2 = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Fm7 -> Ab, Bb, C, Eb, F, Ab, Bb
sax_notes = [
    (70, 3.0, 0.375),   # Ab
    (71, 3.375, 0.375), # Bb
    (72, 3.75, 0.375),  # C
    (69, 4.125, 0.375), # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (61, 3.0, 0.375),   # C
    (60, 3.375, 0.375), # Bb
    (62, 3.75, 0.375),  # Eb
    (64, 4.125, 0.375), # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (70, 3.375, 0.375), # Ab7 (Ab, C, Eb, Gb)
    (72, 3.375, 0.375),
    (69, 3.375, 0.375),
    (67, 3.375, 0.375),
    (70, 4.125, 0.375),
    (72, 4.125, 0.375),
    (69, 4.125, 0.375),
    (67, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes_bar3 = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Fm7 -> F, Ab, Bb, D, Gb, Ab, Bb
sax_notes = [
    (77, 4.5, 0.375),   # F
    (70, 4.875, 0.375), # Ab
    (71, 5.25, 0.375),  # Bb
    (69, 5.625, 0.375), # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 4.5, 0.375),   # F
    (62, 4.875, 0.375), # Eb
    (63, 5.25, 0.375),  # D
    (61, 5.625, 0.375), # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (77, 4.875, 0.375), # F7 (F, Ab, C, E)
    (70, 4.875, 0.375),
    (72, 4.875, 0.375),
    (74, 4.875, 0.375),
    (77, 5.625, 0.375),
    (70, 5.625, 0.375),
    (72, 5.625, 0.375),
    (74, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes_bar4 = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375), # Hihat on 4
]
for note, start, duration in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
