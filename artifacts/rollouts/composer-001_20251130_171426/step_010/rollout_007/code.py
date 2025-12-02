
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (37, 1.5, 0.375), (39, 1.875, 0.375), (40, 2.25, 0.375), (41, 2.625, 0.375),
    (42, 3.0, 0.375), (43, 3.375, 0.375), (44, 3.75, 0.375), (45, 4.125, 0.375),
    (46, 4.5, 0.375), (48, 4.875, 0.375), (49, 5.25, 0.375), (50, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (62, 2.25, 0.125), (65, 2.25, 0.125), (67, 2.25, 0.125), (69, 2.25, 0.125),
    (62, 2.625, 0.125), (65, 2.625, 0.125), (67, 2.625, 0.125), (69, 2.625, 0.125),
    # Bar 3: Bb7 on 2 and 4
    (60, 3.75, 0.125), (63, 3.75, 0.125), (65, 3.75, 0.125), (67, 3.75, 0.125),
    (60, 4.125, 0.125), (63, 4.125, 0.125), (65, 4.125, 0.125), (67, 4.125, 0.125),
    # Bar 4: F7 on 2 and 4
    (62, 5.25, 0.125), (65, 5.25, 0.125), (67, 5.25, 0.125), (69, 5.25, 0.125),
    (62, 5.625, 0.125), (65, 5.625, 0.125), (67, 5.625, 0.125), (69, 5.625, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.125),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 4.5, 0.125),
    (36, 4.875, 0.375), (38, 5.25, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif in F, short and haunting
# Phrase: F, Bb, G, C (F7 chord) - start, leave it hanging, come back
sax_notes = [
    (65, 1.5, 0.375), (62, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375),
    (65, 3.0, 0.375), (62, 3.375, 0.375), (67, 3.75, 0.375), (69, 4.125, 0.375),
    (65, 4.5, 0.375), (62, 4.875, 0.375), (67, 5.25, 0.375), (69, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
