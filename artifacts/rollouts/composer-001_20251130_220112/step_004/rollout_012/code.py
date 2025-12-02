
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 1.5, 0.375), (52, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (51, 2.625, 0.375), (52, 2.625, 0.375), (53, 2.625, 0.375), (54, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (53, 1.5, 0.375), (58, 1.5, 0.375), (57, 1.5, 0.375), (55, 1.5, 0.375),
    # Bar 3: Ab7 (Ab, C, Eb, Gb)
    (50, 2.625, 0.375), (57, 2.625, 0.375), (55, 2.625, 0.375), (52, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: Motif - F, Gb, Ab, A, F (starts on 1.5s, ends on 2.25s)
sax_notes = [
    (53, 1.5, 0.375), (52, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (53, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 3.0, 0.375), (52, 3.375, 0.375), (50, 3.75, 0.375), (51, 4.125, 0.375),
    (51, 4.125, 0.375), (52, 4.125, 0.375), (53, 4.125, 0.375), (54, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, Eb)
    (53, 3.0, 0.375), (58, 3.0, 0.375), (57, 3.0, 0.375), (55, 3.0, 0.375),
    # Bar 4: Ab7 (Ab, C, Eb, Gb)
    (50, 4.125, 0.375), (57, 4.125, 0.375), (55, 4.125, 0.375), (52, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drum fill continues
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (42, 4.125, 0.1875), (42, 4.3125, 0.1875), (42, 4.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 4.5, 0.375), (52, 4.875, 0.375), (50, 5.25, 0.375), (51, 5.625, 0.375),
    (51, 5.625, 0.375), (52, 5.625, 0.375), (53, 5.625, 0.375), (54, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 (F, A, C, Eb)
    (53, 4.5, 0.375), (58, 4.5, 0.375), (57, 4.5, 0.375), (55, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: Repeat motif, ends on 5.25s (Ab)
sax_notes = [
    (53, 4.5, 0.375), (52, 4.875, 0.375), (50, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drum fill continues
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
