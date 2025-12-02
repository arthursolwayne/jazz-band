
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
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (37, 1.5, 1.5), (39, 1.875, 1.875), (40, 2.25, 2.25), (41, 2.625, 2.625),
    (42, 3.0, 3.0), (44, 3.375, 3.375), (45, 3.75, 3.75), (46, 4.125, 4.125),
    (47, 4.5, 4.5), (49, 4.875, 4.875), (50, 5.25, 5.25), (51, 5.625, 5.625)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 1.5), (64, 1.5, 1.5), (67, 1.5, 1.5), (69, 1.5, 1.5),
    # Bar 3
    (62, 3.0, 3.0), (66, 3.0, 3.0), (69, 3.0, 3.0), (71, 3.0, 3.0),
    # Bar 4
    (60, 4.5, 4.5), (64, 4.5, 4.5), (67, 4.5, 4.5), (69, 4.5, 4.5)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.5), (38, 1.875, 1.875), (42, 1.5, 1.6875),
    (36, 3.0, 3.0), (38, 3.375, 3.375), (42, 3.0, 3.1875),
    (36, 4.5, 4.5), (38, 4.875, 4.875), (42, 4.5, 4.6875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.625), (66, 1.875, 2.0), (64, 2.25, 2.4375), (62, 2.625, 2.8125),
    (66, 3.0, 3.125), (64, 3.375, 3.5), (62, 3.75, 3.875), (66, 4.125, 4.25),
    (64, 4.5, 4.625), (62, 4.875, 5.0)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
