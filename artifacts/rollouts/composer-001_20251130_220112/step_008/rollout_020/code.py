
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no same note twice
bass_notes = [
    # Bar 2
    (57, 1.5, 0.375), (58, 1.875, 0.375), (57, 2.25, 0.375), (59, 2.625, 0.375),
    # Bar 3
    (60, 3.0, 0.375), (59, 3.375, 0.375), (58, 3.75, 0.375), (57, 4.125, 0.375),
    # Bar 4
    (56, 4.5, 0.375), (57, 4.875, 0.375), (58, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (65, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375),
    (62, 2.625, 0.375), (64, 2.625, 0.375), (66, 2.625, 0.375), (68, 2.625, 0.375),
    # Bar 3
    (65, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375), (71, 3.375, 0.375),
    (62, 4.125, 0.375), (64, 4.125, 0.375), (66, 4.125, 0.375), (68, 4.125, 0.375),
    # Bar 4
    (65, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375), (71, 4.875, 0.375),
    (62, 5.625, 0.375), (64, 5.625, 0.375), (66, 5.625, 0.375), (68, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante): Motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375), (65, 2.625, 0.375),
    # Bar 3
    (62, 3.0, 0.375), (65, 3.375, 0.375), (67, 3.75, 0.375), (65, 4.125, 0.375),
    # Bar 4
    (62, 4.5, 0.375), (65, 4.875, 0.375), (67, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        start_time = start + (i * 0.1875)
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=start_time, end=start_time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
