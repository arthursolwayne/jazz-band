
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
    (36, 0.0, 0.375), (42, 0.0, 0.1875),
    (38, 0.375, 0.375), (42, 0.375, 0.1875),
    (36, 0.75, 0.375), (42, 0.75, 0.1875),
    (38, 1.125, 0.375), (42, 1.125, 0.1875),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Chromatic walking line, no repeated notes
bass_notes = [
    (44, 1.5, 0.375), (45, 1.875, 0.375),
    (46, 2.25, 0.375), (47, 2.625, 0.375),
    (48, 2.625, 0.375), (49, 3.0, 0.375),
    (50, 3.375, 0.375), (51, 3.75, 0.375),
    (52, 4.125, 0.375), (53, 4.5, 0.375),
    (54, 4.875, 0.375), (55, 5.25, 0.375),
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-2.25s)
    (62, 1.5, 0.375), (66, 1.5, 0.375), (67, 1.5, 0.375),
    # Bar 3 (2.625-3.375s)
    (62, 2.625, 0.375), (66, 2.625, 0.375), (67, 2.625, 0.375),
    # Bar 4 (4.125-4.875s)
    (62, 4.125, 0.375), (66, 4.125, 0.375), (67, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One motif, start it, leave it hanging, come back and finish
sax_notes = [
    (66, 1.5, 0.375), (69, 1.875, 0.375), (67, 2.25, 0.375),
    (66, 2.625, 0.375), (69, 2.625, 0.375),
    (67, 3.0, 0.375), (66, 3.375, 0.375), (69, 3.75, 0.375),
    (67, 4.125, 0.375), (69, 4.5, 0.375), (67, 4.875, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue with same pattern for bars 2-4
for i in range(2):
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5 + (i * 1.5), end=start + duration + 1.5 + (i * 1.5)))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
