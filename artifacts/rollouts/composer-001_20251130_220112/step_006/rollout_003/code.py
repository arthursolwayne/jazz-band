
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (47, 2.25, 0.375), (46, 2.625, 0.375),
    (48, 3.0, 0.375), (49, 3.375, 0.375), (47, 3.75, 0.375), (46, 4.125, 0.375),
    (48, 4.5, 0.375), (49, 4.875, 0.375), (47, 5.25, 0.375), (46, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Fm7, Bb7, Fm7, Bb7
piano_notes = [
    # Bar 2
    (53, 1.875, 0.375), (50, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375),
    (58, 3.375, 0.375), (55, 3.375, 0.375), (60, 3.375, 0.375), (63, 3.375, 0.375),
    # Bar 3
    (53, 3.75, 0.375), (50, 3.75, 0.375), (57, 3.75, 0.375), (60, 3.75, 0.375),
    (58, 5.25, 0.375), (55, 5.25, 0.375), (60, 5.25, 0.375), (63, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, start on bar 2, leave it hanging
sax_notes = [
    (59, 1.5, 0.375), (61, 1.875, 0.375), (57, 2.25, 0.375),
    (59, 2.625, 0.375), (61, 2.75, 0.125)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
