
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (60, 1.5, 0.375), (61, 1.875, 0.375), (62, 2.25, 0.375), (64, 2.625, 0.375),
    # Bar 3
    (65, 3.0, 0.375), (67, 3.375, 0.375), (68, 3.75, 0.375), (69, 4.125, 0.375),
    # Bar 4
    (70, 4.5, 0.375), (71, 4.875, 0.375), (72, 5.25, 0.375), (74, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    (64, 1.875, 0.375), (67, 1.875, 0.375), (71, 1.875, 0.375), (72, 1.875, 0.375),
    (64, 2.625, 0.375), (67, 2.625, 0.375), (71, 2.625, 0.375), (72, 2.625, 0.375),
    # Bar 3
    (64, 3.0, 0.375), (67, 3.0, 0.375), (71, 3.0, 0.375), (72, 3.0, 0.375),
    (64, 3.75, 0.375), (67, 3.75, 0.375), (71, 3.75, 0.375), (72, 3.75, 0.375),
    # Bar 4
    (64, 4.5, 0.375), (67, 4.5, 0.375), (71, 4.5, 0.375), (72, 4.5, 0.375),
    (64, 5.25, 0.375), (67, 5.25, 0.375), (71, 5.25, 0.375), (72, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C (60), E (64), Bb (62), rest
sax_notes = [
    (60, 1.5, 0.375),
    (64, 1.875, 0.375),
    (62, 2.25, 0.375),
    (60, 3.0, 0.375),
    (64, 3.375, 0.375),
    (62, 3.75, 0.375),
    (60, 4.5, 0.375),
    (64, 4.875, 0.375),
    (62, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_notes = [
        (start, 0.1875), (start + 0.1875, 0.1875),
        (start + 0.375, 0.1875), (start + 0.5625, 0.1875),
        (start + 0.75, 0.1875), (start + 0.9375, 0.1875),
        (start + 1.125, 0.1875), (start + 1.3125, 0.1875)
    ]
    for h_start, h_duration in hihat_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=h_start, end=h_start + h_duration))
    # Add kick and snare
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dantes_intro.mid")
