
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

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (64, 4.875, 0.375), (63, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (69, 1.875, 0.375), (67, 1.875, 0.375), (65, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 3
    (69, 3.375, 0.375), (67, 3.375, 0.375), (65, 3.375, 0.375), (62, 3.375, 0.375),
    # Bar 4
    (69, 4.875, 0.375), (67, 4.875, 0.375), (65, 4.875, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kicks = [(36, start + 0.0, 0.375), (36, start + 0.75, 0.375)]
    # Snare on 2 and 4
    snares = [(38, start + 0.375, 0.375), (38, start + 1.125, 0.375)]
    # Hihat on every eighth
    hi_hats = [(42, start + i * 0.125, 0.125) for i in range(12)]
    for note, start_time, duration in kicks + snares + hi_hats:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Sax: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D D# F A
sax_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (65, 2.25, 0.375), (69, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (65, 3.75, 0.375), (69, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
