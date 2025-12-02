
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, start in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
bass_notes = [
    (62, 1.5), (63, 1.875), (62, 2.25), (60, 2.625),
    (62, 3.0), (63, 3.375), (62, 3.75), (60, 4.125),
    (62, 4.5), (63, 4.875), (62, 5.25), (60, 5.625)
]
for note, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beats 2 and 4
piano_notes = [
    # Bar 2
    (50, 2.0), (52, 2.0), (55, 2.0), (57, 2.0),
    # Bar 3
    (50, 3.5), (52, 3.5), (55, 3.5), (57, 3.5),
    # Bar 4
    (50, 5.0), (52, 5.0), (55, 5.0), (57, 5.0)
]
for note, start in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.25))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625)
]
for note, start in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C
# Motif: D - F - A, then wait, then resolve on C
sax_notes = [
    (62, 1.5), (64, 1.875), (67, 2.25),
    (69, 3.0), (62, 3.375), (64, 3.75), (67, 4.125), (69, 4.5)
]
for note, start in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
