
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick
    (42, 0.0, 0.125),
    (42, 0.125, 0.125),
    (42, 0.25, 0.125),
    (42, 0.375, 0.125),
    (38, 0.5, 0.375),  # Snare
    (42, 0.5, 0.125),
    (42, 0.625, 0.125),
    (42, 0.75, 0.125),
    (42, 0.875, 0.125),
    (36, 1.0, 0.375),  # Kick
    (42, 1.0, 0.125),
    (42, 1.125, 0.125),
    (42, 1.25, 0.125),
    (42, 1.375, 0.125),
    (38, 1.5, 0.375)   # Snare
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax phrase: Dm7 -> G7 -> Cm7 -> F7, with a short, fragmented motif
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# Motif: D (1.5s), F (1.625s), A (1.75s), C (1.875s), then a rest until 2.0s
sax_notes = [
    (62, 1.5, 0.125),  # D
    (64, 1.625, 0.125), # F
    (67, 1.75, 0.125),  # A
    (67, 1.875, 0.125), # A
    (67, 2.0, 0.125)   # A
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line with chromatic approaches
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# Chromatic approaches on the 2nd and 4th beats
bass_notes = [
    (62, 1.5, 0.25),   # D
    (63, 1.75, 0.25),  # chromatic up to F
    (64, 2.0, 0.25),   # F
    (65, 2.25, 0.25),  # chromatic up to A
    (67, 2.5, 0.25),   # A
    (68, 2.75, 0.25),  # chromatic up to C
    (69, 3.0, 0.25)    # C
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 1.75, 0.25),  # F7 (F, A, C, Eb)
    (65, 1.75, 0.25),
    (67, 1.75, 0.25),
    (69, 1.75, 0.25),
    (64, 2.25, 0.25),  # F7 again
    (65, 2.25, 0.25),
    (67, 2.25, 0.25),
    (69, 2.25, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Repeat the motif but with a slight variation
sax_notes = [
    (62, 3.0, 0.125),  # D
    (64, 3.125, 0.125), # F
    (67, 3.25, 0.125),  # A
    (67, 3.375, 0.125), # A
    (67, 3.5, 0.125)   # A
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Continue walking
bass_notes = [
    (69, 3.0, 0.25),   # C
    (70, 3.25, 0.25),  # chromatic up to Eb
    (69, 3.5, 0.25),   # Eb
    (71, 3.75, 0.25),  # chromatic up to G
    (72, 4.0, 0.25),   # G
    (73, 4.25, 0.25),  # chromatic up to Bb
    (71, 4.5, 0.25)    # Bb
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 3.25, 0.25),  # F7
    (65, 3.25, 0.25),
    (67, 3.25, 0.25),
    (69, 3.25, 0.25),
    (64, 3.75, 0.25),
    (65, 3.75, 0.25),
    (67, 3.75, 0.25),
    (69, 3.75, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick
    (42, 3.0, 0.125),
    (42, 3.125, 0.125),
    (42, 3.25, 0.125),
    (42, 3.375, 0.125),
    (38, 3.5, 0.375),  # Snare
    (42, 3.5, 0.125),
    (42, 3.625, 0.125),
    (42, 3.75, 0.125),
    (42, 3.875, 0.125),
    (36, 4.0, 0.375),  # Kick
    (42, 4.0, 0.125),
    (42, 4.125, 0.125),
    (42, 4.25, 0.125),
    (42, 4.375, 0.125),
    (38, 4.5, 0.375)   # Snare
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: End with a question, hang on A
sax_notes = [
    (67, 4.5, 0.125),
    (67, 4.625, 0.125),
    (67, 4.75, 0.125),
    (67, 4.875, 0.125),
    (67, 5.0, 0.125),
    (67, 5.125, 0.125),
    (67, 5.25, 0.125),
    (67, 5.375, 0.125)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: End with a chromatic approach to D
bass_notes = [
    (71, 4.5, 0.25),   # Bb
    (72, 4.75, 0.25),  # chromatic up to C
    (69, 5.0, 0.25),   # C
    (67, 5.25, 0.25),  # chromatic down to A
    (64, 5.5, 0.25),   # A
    (62, 5.75, 0.25)   # chromatic down to D
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 4.75, 0.25),  # F7
    (65, 4.75, 0.25),
    (67, 4.75, 0.25),
    (69, 4.75, 0.25),
    (64, 5.25, 0.25),
    (65, 5.25, 0.25),
    (67, 5.25, 0.25),
    (69, 5.25, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick
    (42, 4.5, 0.125),
    (42, 4.625, 0.125),
    (42, 4.75, 0.125),
    (42, 4.875, 0.125),
    (38, 5.0, 0.375),  # Snare
    (42, 5.0, 0.125),
    (42, 5.125, 0.125),
    (42, 5.25, 0.125),
    (42, 5.375, 0.125),
    (36, 5.5, 0.375),  # Kick
    (42, 5.5, 0.125),
    (42, 5.625, 0.125),
    (42, 5.75, 0.125),
    (42, 5.875, 0.125),
    (38, 6.0, 0.375)   # Snare
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
