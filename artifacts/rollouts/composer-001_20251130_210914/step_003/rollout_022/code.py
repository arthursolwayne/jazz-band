
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeats
bass_notes = [
    # Bar 2
    (64, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375), (60, 2.625, 0.375),
    # Bar 3
    (61, 3.0, 0.375), (63, 3.375, 0.375), (64, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (60, 4.5, 0.375), (61, 4.875, 0.375), (62, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (47, 1.875, 0.25), (50, 1.875, 0.25), (53, 1.875, 0.25), (55, 1.875, 0.25),
    # Bar 3
    (47, 3.375, 0.25), (50, 3.375, 0.25), (53, 3.375, 0.25), (55, 3.375, 0.25),
    # Bar 4
    (47, 4.875, 0.25), (50, 4.875, 0.25), (53, 4.875, 0.25), (55, 4.875, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Dante: Tenor sax — short motif, make it sing
# Start with Fm7 (F, Ab, Bb, D) in the first bar
# Follow with a chromatic descending line, leave it hanging
sax_notes = [
    (64, 1.5, 0.25), (61, 1.75, 0.25), (60, 2.0, 0.25), (58, 2.25, 0.25),
    (60, 2.5, 0.25), (58, 2.75, 0.25), (57, 3.0, 0.25), (55, 3.25, 0.25),
    (57, 3.5, 0.25), (55, 3.75, 0.25), (54, 4.0, 0.25), (52, 4.25, 0.25),
    (54, 4.5, 0.25), (52, 4.75, 0.25), (51, 5.0, 0.25), (49, 5.25, 0.25),
    (51, 5.5, 0.25), (49, 5.75, 0.25)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
