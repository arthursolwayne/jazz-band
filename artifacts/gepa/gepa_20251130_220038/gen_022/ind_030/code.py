
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
    (38, 1.5, 0.375)  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E, Bb
# Walking bass line in F: F, Gb, G, Ab, A, Bb, B, C, C#, D, Eb, E, F, Gb, G, Ab
bass_notes = [
    (70, 1.5, 0.375),  # F
    (69, 1.875, 0.375),  # Gb
    (71, 2.25, 0.375),  # G
    (70, 2.625, 0.375),  # Ab
    (72, 3.0, 0.375),  # A
    (70, 3.375, 0.375),  # Bb
    (71, 3.75, 0.375),  # B
    (72, 4.125, 0.375),  # C
    (73, 4.5, 0.375),  # C#
    (72, 4.875, 0.375),  # D
    (71, 5.25, 0.375),  # Eb
    (72, 5.625, 0.375),  # E
    (70, 6.0, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, E, Bb
# Fmaj7: F, A, C, E
# Bbm7: Bb, D, F, Ab
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (65, 1.5, 0.1875),  # F
    (69, 1.5, 0.1875),  # A
    (67, 1.5, 0.1875),  # C
    (69, 1.5, 0.1875),  # E
    (62, 1.5, 0.1875),  # Bb
    # Bar 3 (2.25 - 3.0s)
    (62, 2.25, 0.1875),  # Bb
    (66, 2.25, 0.1875),  # D
    (65, 2.25, 0.1875),  # F
    (67, 2.25, 0.1875),  # Ab
    # Bar 4 (3.0 - 3.75s)
    (65, 3.0, 0.1875),  # F
    (69, 3.0, 0.1875),  # A
    (67, 3.0, 0.1875),  # C
    (69, 3.0, 0.1875),  # E
    (62, 3.0, 0.1875),  # Bb
    # Bar 4 (3.75 - 4.5s)
    (62, 3.75, 0.1875),  # Bb
    (66, 3.75, 0.1875),  # D
    (65, 3.75, 0.1875),  # F
    (67, 3.75, 0.1875),  # Ab
    # Bar 4 (4.5 - 5.25s)
    (65, 4.5, 0.1875),  # F
    (69, 4.5, 0.1875),  # A
    (67, 4.5, 0.1875),  # C
    (69, 4.5, 0.1875),  # E
    (62, 4.5, 0.1875),  # Bb
    # Bar 4 (5.25 - 6.0s)
    (62, 5.25, 0.1875),  # Bb
    (66, 5.25, 0.1875),  # D
    (65, 5.25, 0.1875),  # F
    (67, 5.25, 0.1875)  # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, E (F7) with a syncopated start
# Bar 2: F, Bb, C, E
# Bar 3: F, Bb, C, E
# Bar 4: F, Bb, C, E
sax_notes = [
    (70, 1.5, 0.1875),  # F
    (65, 1.875, 0.1875),  # Bb
    (72, 2.25, 0.1875),  # C
    (69, 2.625, 0.1875),  # E
    (70, 3.0, 0.1875),  # F
    (65, 3.375, 0.1875),  # Bb
    (72, 3.75, 0.1875),  # C
    (69, 4.125, 0.1875),  # E
    (70, 4.5, 0.1875),  # F
    (65, 4.875, 0.1875),  # Bb
    (72, 5.25, 0.1875),  # C
    (69, 5.625, 0.1875)  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drum fill for bar 4 (snare on 4)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.625 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
