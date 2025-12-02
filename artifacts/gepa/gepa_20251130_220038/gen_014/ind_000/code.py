
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif (D, F, G, Bb)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # G
    (66, 2.625, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (60, 1.875, 0.375),  # C
    (62, 2.25, 0.375),  # Bb
    (57, 2.625, 0.375),  # A
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (64, 1.875, 0.375),  # F
    (67, 1.875, 0.375),  # A
    (71, 1.875, 0.375),  # C
    (69, 1.875, 0.375),  # Bb
    (66, 2.625, 0.375),  # Bb
    (69, 2.625, 0.375),  # D
    (72, 2.625, 0.375),  # F
    (70, 2.625, 0.375),  # Eb
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation (D, F, G, Bb)
sax_notes = [
    (62, 3.0, 0.375),  # D
    (64, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # G
    (66, 4.125, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    (62, 3.0, 0.375),  # D
    (60, 3.375, 0.375),  # C
    (62, 3.75, 0.375),  # Bb
    (57, 4.125, 0.375),  # A
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (64, 3.375, 0.375),  # F
    (67, 3.375, 0.375),  # A
    (71, 3.375, 0.375),  # C
    (69, 3.375, 0.375),  # Bb
    (66, 4.125, 0.375),  # Bb
    (69, 4.125, 0.375),  # D
    (72, 4.125, 0.375),  # F
    (70, 4.125, 0.375),  # Eb
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif with resolution (G, A, Bb, D)
sax_notes = [
    (67, 4.5, 0.375),  # G
    (69, 4.875, 0.375),  # A
    (66, 5.25, 0.375),  # Bb
    (62, 5.625, 0.375),  # D
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    (62, 4.5, 0.375),  # D
    (60, 4.875, 0.375),  # C
    (62, 5.25, 0.375),  # Bb
    (57, 5.625, 0.375),  # A
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (64, 4.875, 0.375),  # F
    (67, 4.875, 0.375),  # A
    (71, 4.875, 0.375),  # C
    (69, 4.875, 0.375),  # Bb
    (66, 5.625, 0.375),  # Bb
    (69, 5.625, 0.375),  # D
    (72, 5.625, 0.375),  # F
    (70, 5.625, 0.375),  # Eb
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on &
    (42, 4.875, 0.1875),  # Hihat on 2
    (42, 5.0625, 0.1875),  # Hihat on &
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on &
    (42, 5.625, 0.1875),  # Hihat on 4
    (36, 5.625, 0.375),  # Kick on 3
    (38, 6.0, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
