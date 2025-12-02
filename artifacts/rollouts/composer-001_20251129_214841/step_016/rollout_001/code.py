
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (62, 2.25, 0.375), (63, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (66, 3.75, 0.375), (67, 4.125, 0.375),
    (68, 4.5, 0.375), (69, 4.875, 0.375), (70, 5.25, 0.375), (71, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.25, 0.1875), (67, 2.25, 0.1875), (71, 2.25, 0.1875), (72, 2.25, 0.1875),
    # Bar 3
    (64, 3.75, 0.1875), (67, 3.75, 0.1875), (71, 3.75, 0.1875), (72, 3.75, 0.1875),
    # Bar 4
    (64, 5.25, 0.1875), (67, 5.25, 0.1875), (71, 5.25, 0.1875), (72, 5.25, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    for beat in [0, 1, 2, 3]:
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append((36, time, 0.375))
        elif beat == 1 or beat == 3:
            drum_notes.append((38, time, 0.375))
        drum_notes.append((42, time, 0.1875))
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - B - D (C6, E6, B5, D6), 1st bar, then repeat starting on B5 in bar 3
sax_notes = [
    # Bar 2
    (84, 1.5, 0.375), (87, 1.875, 0.375), (82, 2.25, 0.375), (85, 2.625, 0.375),
    # Bar 3
    (82, 3.0, 0.375), (87, 3.375, 0.375), (84, 3.75, 0.375), (87, 4.125, 0.375),
    # Bar 4
    (84, 4.5, 0.375), (87, 4.875, 0.375), (82, 5.25, 0.375), (85, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
