
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (59, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (62, 4.125, 0.375),
    (64, 4.5, 0.375), (65, 4.875, 0.375), (63, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.5, 0.1875), (67, 1.5, 0.1875), (71, 1.5, 0.1875), (72, 1.5, 0.1875),
    (64, 2.25, 0.1875), (67, 2.25, 0.1875), (71, 2.25, 0.1875), (72, 2.25, 0.1875),
    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.1875), (67, 3.0, 0.1875), (71, 3.0, 0.1875), (72, 3.0, 0.1875),
    (64, 3.75, 0.1875), (67, 3.75, 0.1875), (71, 3.75, 0.1875), (72, 3.75, 0.1875),
    # Bar 4 (4.5 - 6.0s)
    (64, 4.5, 0.1875), (67, 4.5, 0.1875), (71, 4.5, 0.1875), (72, 4.5, 0.1875),
    (64, 5.25, 0.1875), (67, 5.25, 0.1875), (71, 5.25, 0.1875), (72, 5.25, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - your motif: short, melodic, leaves it hanging
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (62, 2.25, 0.375),
    (60, 2.625, 0.375), (62, 3.0, 0.375), (64, 3.375, 0.375),
    (62, 3.75, 0.375), (60, 4.125, 0.375), (62, 4.5, 0.375),
    (64, 4.875, 0.375), (62, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums continue with the same pattern through bars 2-4
for i in range(2):
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5 + i * 1.5, end=start + duration + 1.5 + i * 1.5))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
