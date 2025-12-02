
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (42, 1.125, 0.1875), # Hihat on 4
    (38, 1.5, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D-F#-G-A-D)
bass_notes = [
    (62, 1.5, 0.375), # D
    (64, 1.875, 0.375), # F#
    (65, 2.25, 0.375), # G
    (67, 2.625, 0.375), # A
    (62, 3.0, 0.375), # D
    (64, 3.375, 0.375), # F#
    (65, 3.75, 0.375), # G
    (67, 4.125, 0.375), # A
    (62, 4.5, 0.375), # D
    (64, 4.875, 0.375), # F#
    (65, 5.25, 0.375), # G
    (67, 5.625, 0.375)  # A
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.1875), # D7: D
    (67, 1.5, 0.1875), # A
    (64, 1.5, 0.1875), # F#
    (69, 1.5, 0.1875), # C
    (62, 2.25, 0.1875), # D
    (67, 2.25, 0.1875), # A
    (64, 2.25, 0.1875), # F#
    (69, 2.25, 0.1875), # C
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.1875), # D7: D
    (67, 3.0, 0.1875), # A
    (64, 3.0, 0.1875), # F#
    (69, 3.0, 0.1875), # C
    (62, 3.75, 0.1875), # D
    (67, 3.75, 0.1875), # A
    (64, 3.75, 0.1875), # F#
    (69, 3.75, 0.1875), # C
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.1875), # D7: D
    (67, 4.5, 0.1875), # A
    (64, 4.5, 0.1875), # F#
    (69, 4.5, 0.1875), # C
    (62, 5.25, 0.1875), # D
    (67, 5.25, 0.1875), # A
    (64, 5.25, 0.1875), # F#
    (69, 5.25, 0.1875), # C
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1 & 2
    (42, 1.6875, 0.1875),
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875),
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875),
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante: Saxophone motif – D to Bb to G to E (1.5 - 2.25s), then leave it hanging (2.25 - 3.0s)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (60, 1.875, 0.375),  # Bb
    (65, 2.25, 0.375),  # G
    (64, 2.625, 0.375),  # E
    (62, 2.625, 0.375),  # D (rest)
    (62, 2.625, 0.375),  # D (rest)
    (62, 2.625, 0.375),  # D (rest)
    (62, 2.625, 0.375)   # D (rest)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo_intro.mid')
