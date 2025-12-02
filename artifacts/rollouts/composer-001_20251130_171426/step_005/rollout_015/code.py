
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
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (63, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (63, 4.125, 0.375),
    (64, 4.5, 0.375), (65, 4.875, 0.375), (63, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: G7 (G B D F)
    (71, 1.875, 0.375), (74, 1.875, 0.375), (76, 1.875, 0.375), (78, 1.875, 0.375),
    # Bar 3: C7 (C E G B)
    (60, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (71, 3.375, 0.375),
    # Bar 4: F7 (F A C E)
    (77, 4.875, 0.375), (81, 4.875, 0.375), (79, 4.875, 0.375), (83, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif, start it, leave it hanging, come back and finish it
# Dorian mode in D: D E F# G A B C
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (66, 2.25, 0.375),  # D E F#
    (69, 2.625, 0.375), (71, 2.625, 0.375), (72, 3.0, 0.375),  # G B C
    (66, 3.375, 0.375), (69, 3.75, 0.375), (71, 4.125, 0.375),  # F# G B
    (69, 4.5, 0.375), (71, 4.875, 0.375), (66, 5.25, 0.375),    # G B F#
    (64, 5.625, 0.375), (62, 6.0, 0.375)                       # E D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
