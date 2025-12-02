
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.875, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (65, 1.5, 0.375), (66, 1.875, 0.375), (64, 2.25, 0.375), (62, 2.625, 0.375),
    (65, 3.0, 0.375), (67, 3.375, 0.375), (69, 3.75, 0.375), (67, 4.125, 0.375),
    (65, 4.5, 0.375), (66, 4.875, 0.375), (64, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.25, 0.375), (64, 2.25, 0.375), (67, 2.25, 0.375), (72, 2.25, 0.375),  # D7
    (65, 3.0, 0.375), (67, 3.0, 0.375), (70, 3.0, 0.375), (75, 3.0, 0.375),  # G7
    (62, 4.5, 0.375), (64, 4.5, 0.375), (67, 4.5, 0.375), (72, 4.5, 0.375),  # D7
    (65, 5.25, 0.375), (67, 5.25, 0.375), (70, 5.25, 0.375), (75, 5.25, 0.375)   # G7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start_time, 0.375), (38, start_time + 0.375, 0.375), (42, start_time + 0.75, 0.375),
        (36, start_time + 1.125, 0.375), (38, start_time + 1.5, 0.375), (42, start_time + 1.875, 0.375)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), E (64), F (65), D (62)
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375), (62, 2.625, 0.375),  # first motif
    (62, 3.75, 0.375), (64, 4.125, 0.375), (65, 4.5, 0.375), (62, 4.875, 0.375)   # repeat
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
