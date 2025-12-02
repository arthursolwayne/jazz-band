
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125), (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125), (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking in Fm, chromatic approach
bass_notes = [
    (42, 1.5, 0.375), (43, 1.875, 0.375), (41, 2.25, 0.375), (40, 2.625, 0.375),
    (39, 3.0, 0.375), (40, 3.375, 0.375), (41, 3.75, 0.375), (42, 4.125, 0.375),
    (43, 4.5, 0.375), (42, 4.875, 0.375), (41, 5.25, 0.375), (40, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = []
# Bar 2
piano_notes.extend([
    (42, 1.5, 0.375), (45, 1.5, 0.375), (47, 1.5, 0.375), (50, 1.5, 0.375),
    (52, 1.875, 0.375), (55, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375)
])
# Bar 3
piano_notes.extend([
    (42, 2.25, 0.375), (45, 2.25, 0.375), (47, 2.25, 0.375), (50, 2.25, 0.375),
    (52, 2.625, 0.375), (55, 2.625, 0.375), (57, 2.625, 0.375), (60, 2.625, 0.375)
])
# Bar 4
piano_notes.extend([
    (42, 3.0, 0.375), (45, 3.0, 0.375), (47, 3.0, 0.375), (50, 3.0, 0.375),
    (52, 3.375, 0.375), (55, 3.375, 0.375), (57, 3.375, 0.375), (60, 3.375, 0.375)
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start, 0.375), (38, bar_start + 0.375, 0.375),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375),
        (42, bar_start, 0.125), (42, bar_start + 0.125, 0.125), (42, bar_start + 0.25, 0.125), (42, bar_start + 0.375, 0.125),
        (42, bar_start + 0.5, 0.125), (42, bar_start + 0.625, 0.125), (42, bar_start + 0.75, 0.125), (42, bar_start + 0.875, 0.125),
        (42, bar_start + 1.0, 0.125), (42, bar_start + 1.125, 0.125), (42, bar_start + 1.25, 0.125), (42, bar_start + 1.375, 0.125)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (45, 1.5, 0.375), (47, 1.875, 0.375), (45, 2.25, 0.375), (43, 2.625, 0.375),
    (45, 3.0, 0.375), (47, 3.375, 0.375), (45, 3.75, 0.375), (43, 4.125, 0.375),
    (45, 4.5, 0.375), (47, 4.875, 0.375), (45, 5.25, 0.375), (43, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
