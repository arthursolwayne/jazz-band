
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

# Bar 1
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (42, 0.9375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # Gb
    (47, 2.25, 0.375),  # G
    (44, 2.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    (53, 1.875, 0.375),  # F
    (57, 1.875, 0.375),  # Bb
    (60, 1.875, 0.375),  # E
    (62, 1.875, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: F7 on beat 4 (same chord)
piano_notes = [
    (53, 2.625, 0.375),  # F
    (57, 2.625, 0.375),  # Bb
    (60, 2.625, 0.375),  # E
    (62, 2.625, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - F, G, Ab, F (starts on beat 2)
sax_notes = [
    (53, 1.875, 0.375),  # F
    (55, 2.25, 0.375),   # G
    (56, 2.625, 0.375),  # Ab
    (53, 3.0, 0.375)     # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 3.0, 0.375),  # F
    (46, 3.375, 0.375),  # Gb
    (47, 3.75, 0.375),  # G
    (44, 4.125, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 3: F7 on beat 2
piano_notes = [
    (53, 3.375, 0.375),  # F
    (57, 3.375, 0.375),  # Bb
    (60, 3.375, 0.375),  # E
    (62, 3.375, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: F7 on beat 4 (same chord)
piano_notes = [
    (53, 4.125, 0.375),  # F
    (57, 4.125, 0.375),  # Bb
    (60, 4.125, 0.375),  # E
    (62, 4.125, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif again on beat 2
sax_notes = [
    (53, 3.375, 0.375),  # F
    (55, 3.75, 0.375),   # G
    (56, 4.125, 0.375),  # Ab
    (53, 4.5, 0.375)     # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 0.1875),  # Hihat on 3 & 4
    (42, 5.4375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 4.5, 0.375),  # F
    (46, 4.875, 0.375),  # Gb
    (47, 5.25, 0.375),  # G
    (44, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 4: F7 on beat 2
piano_notes = [
    (53, 4.875, 0.375),  # F
    (57, 4.875, 0.375),  # Bb
    (60, 4.875, 0.375),  # E
    (62, 4.875, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: F7 on beat 4 (same chord)
piano_notes = [
    (53, 5.625, 0.375),  # F
    (57, 5.625, 0.375),  # Bb
    (60, 5.625, 0.375),  # E
    (62, 5.625, 0.375)   # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif again on beat 2
sax_notes = [
    (53, 4.875, 0.375),  # F
    (55, 5.25, 0.375),   # G
    (56, 5.625, 0.375),  # Ab
    (53, 6.0, 0.375)     # F (end of bar)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
