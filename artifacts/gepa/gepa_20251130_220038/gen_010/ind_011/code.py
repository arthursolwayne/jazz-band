
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

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (44, 2.25, 0.375), (43, 2.625, 0.375),
    (45, 3.0, 0.375), (46, 3.375, 0.375), (44, 3.75, 0.375), (43, 4.125, 0.375),
    (45, 4.5, 0.375), (46, 4.875, 0.375), (44, 5.25, 0.375), (43, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping in F
# F7, Bb7, F7, Bb7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (53, 1.5, 0.375), (50, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375),
    (53, 2.25, 0.375), (50, 2.25, 0.375), (57, 2.25, 0.375), (60, 2.25, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (53, 3.0, 0.375), (50, 3.0, 0.375), (57, 3.0, 0.375), (60, 3.0, 0.375),
    (53, 3.75, 0.375), (50, 3.75, 0.375), (57, 3.75, 0.375), (60, 3.75, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (53, 4.5, 0.375), (50, 4.5, 0.375), (57, 4.5, 0.375), (60, 4.5, 0.375),
    (53, 5.25, 0.375), (50, 5.25, 0.375), (57, 5.25, 0.375), (60, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif in F, one short phrase, leave it hanging
# F, Bb, E, D, F
sax_notes = [
    (66, 1.5, 0.375), (62, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    (66, 3.0, 0.375), (62, 3.375, 0.375), (61, 3.75, 0.375), (60, 4.125, 0.375),
    (66, 4.5, 0.375), (62, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continued for bars 2-4
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
