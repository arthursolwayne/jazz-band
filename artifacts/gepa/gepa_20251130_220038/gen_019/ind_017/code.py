
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Fm key
bass_notes = [
    (43, 1.5, 0.375), (44, 1.875, 0.375), (42, 2.25, 0.375), (40, 2.625, 0.375),  # Fm7
    (43, 3.0, 0.375), (45, 3.375, 0.375), (44, 3.75, 0.375), (42, 4.125, 0.375),  # Bb7
    (43, 4.5, 0.375), (44, 4.875, 0.375), (42, 5.25, 0.375), (40, 5.625, 0.375)   # Fm7
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.125), (64, 1.5, 0.125), (67, 1.5, 0.125), (69, 1.5, 0.125),  # Fm7
    (66, 2.25, 0.125), (69, 2.25, 0.125), (71, 2.25, 0.125), (72, 2.25, 0.125),  # Bb7
    (60, 3.0, 0.125), (64, 3.0, 0.125), (67, 3.0, 0.125), (69, 3.0, 0.125),  # Fm7
    (66, 3.75, 0.125), (69, 3.75, 0.125), (71, 3.75, 0.125), (72, 3.75, 0.125),  # Bb7
    (60, 4.5, 0.125), (64, 4.5, 0.125), (67, 4.5, 0.125), (69, 4.5, 0.125)   # Fm7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm, start it, leave it hanging, come back and finish it
sax_notes = [
    (60, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375), (60, 2.625, 0.375),  # Fm motif
    (60, 3.0, 0.375), (63, 3.375, 0.375), (62, 3.75, 0.375), (60, 4.125, 0.375),  # repeat motif
    (60, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375), (60, 5.625, 0.375)   # finish motif
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, bar_start, 0.375), (42, bar_start, 0.125),
        (38, bar_start + 0.375, 0.375), (42, bar_start + 0.375, 0.125),
        (36, bar_start + 0.75, 0.375), (42, bar_start + 0.75, 0.125),
        (38, bar_start + 1.125, 0.375), (42, bar_start + 1.125, 0.125)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
