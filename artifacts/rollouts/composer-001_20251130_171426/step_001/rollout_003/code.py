
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875)
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass (walking line in Fm, chromatic approaches)
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (47, 2.25, 0.375), (46, 2.625, 0.375),
    (48, 2.8125, 0.375), (49, 3.1875, 0.375), (47, 3.5625, 0.375), (46, 3.9375, 0.375),
    (48, 4.3125, 0.375), (49, 4.6875, 0.375), (47, 5.0625, 0.375), (46, 5.4375, 0.375)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (53, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375), (62, 1.5, 0.375),
    (59, 1.875, 0.375), (63, 1.875, 0.375), (64, 1.875, 0.375),
    (57, 2.25, 0.375), (60, 2.25, 0.375), (62, 2.25, 0.375), (63, 2.25, 0.375),
    (59, 2.625, 0.375), (63, 2.625, 0.375), (64, 2.625, 0.375),
    # Bar 3
    (53, 3.1875, 0.375), (57, 3.1875, 0.375), (60, 3.1875, 0.375), (62, 3.1875, 0.375),
    (59, 3.5625, 0.375), (63, 3.5625, 0.375), (64, 3.5625, 0.375),
    (57, 3.9375, 0.375), (60, 3.9375, 0.375), (62, 3.9375, 0.375), (63, 3.9375, 0.375),
    (59, 4.3125, 0.375), (63, 4.3125, 0.375), (64, 4.3125, 0.375),
    # Bar 4
    (53, 4.6875, 0.375), (57, 4.6875, 0.375), (60, 4.6875, 0.375), (62, 4.6875, 0.375),
    (59, 5.0625, 0.375), (63, 5.0625, 0.375), (64, 5.0625, 0.375),
    (57, 5.4375, 0.375), (60, 5.4375, 0.375), (62, 5.4375, 0.375), (63, 5.4375, 0.375)
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Dante - Sax (Motif: start, leave it hanging, come back and finish)
sax_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (64, 2.25, 0.375),
    (62, 2.625, 0.375), (65, 3.1875, 0.375), (67, 3.5625, 0.375),
    (64, 3.9375, 0.375), (62, 4.3125, 0.375), (65, 4.6875, 0.375),
    (67, 5.0625, 0.375), (64, 5.4375, 0.375)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875), (36, 3.375, 0.375),
    (38, 3.75, 0.375), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    # Bar 3
    (36, 3.375, 0.375), (38, 3.75, 0.375), (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875), (42, 3.75, 0.1875), (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875), (42, 4.3125, 0.1875), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (36, 5.4375, 0.375), (38, 5.8125, 0.375), (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
