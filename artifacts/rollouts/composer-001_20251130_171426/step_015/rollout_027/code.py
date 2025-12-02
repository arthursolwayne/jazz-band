
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: All instruments enter
# Sax motif: Fm7 -> Bb -> Ab -> G -> F (melodic idea, no scale runs)
sax_notes = [
    (185, 1.5, 0.375), (172, 1.875, 0.375), (165, 2.25, 0.375), (162, 2.625, 0.375), (185, 2.625, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Marcus: Walking bass line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (70, 1.5, 0.375), (68, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375),
    (65, 3.0, 0.375), (66, 3.375, 0.375), (68, 3.75, 0.375), (66, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Comping on 2 and 4 with 7th chords in Fm
piano_notes = [
    # Bar 2, beat 2: Fm7 (F, Ab, Bb, Db)
    (70, 1.875, 0.375), (67, 1.875, 0.375), (65, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 2, beat 4: Bb7 (Bb, Db, F, Ab)
    (65, 2.625, 0.375), (62, 2.625, 0.375), (70, 2.625, 0.375), (67, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Sax repeats motif, slightly transposed
sax_notes = [
    (179, 3.0, 0.375), (166, 3.375, 0.375), (162, 3.75, 0.375), (159, 4.125, 0.375), (179, 4.125, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Marcus continues walking line
bass_notes = [
    (69, 3.0, 0.375), (66, 3.375, 0.375), (68, 3.75, 0.375), (65, 4.125, 0.375),
    (67, 4.5, 0.375), (68, 4.875, 0.375), (69, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 3: Diane comps again
piano_notes = [
    # Bar 3, beat 2: Bb7
    (65, 3.375, 0.375), (62, 3.375, 0.375), (70, 3.375, 0.375), (67, 3.375, 0.375),
    # Bar 3, beat 4: Fm7
    (70, 4.125, 0.375), (67, 4.125, 0.375), (65, 4.125, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Sax resolves the motif, opens up
sax_notes = [
    (185, 4.5, 0.375), (172, 4.875, 0.375), (165, 5.25, 0.375), (162, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Marcus continues walking line
bass_notes = [
    (69, 4.5, 0.375), (66, 4.875, 0.375), (68, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 4: Diane comps on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Eb7 (Eb, Gb, Bb, Db)
    (63, 4.875, 0.375), (60, 4.875, 0.375), (65, 4.875, 0.375), (62, 4.875, 0.375),
    # Bar 4, beat 4: Fm7
    (70, 5.625, 0.375), (67, 5.625, 0.375), (65, 5.625, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Drums continue
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
