
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in Dm, chromatic approaches, no same note twice
bass_notes = [
    (62, 1.5), (64, 1.875), (61, 2.25), (63, 2.625),
    (65, 3.0), (67, 3.375), (64, 3.75), (66, 4.125),
    (62, 4.5), (64, 4.875), (61, 5.25), (63, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(80, note, time, time + 0.25))

# Diane on piano: 7th chords on 2 and 4, comp on bars 2-4
piano_notes = [
    # Bar 2
    (64, 1.5), (67, 1.5), (69, 1.5), (72, 1.5),  # Dm7
    (67, 2.0), (70, 2.0), (72, 2.0), (74, 2.0),  # G7
    # Bar 3
    (64, 2.5), (67, 2.5), (69, 2.5), (72, 2.5),  # Dm7
    (67, 3.0), (70, 3.0), (72, 3.0), (74, 3.0),  # G7
    # Bar 4
    (64, 3.5), (67, 3.5), (69, 3.5), (72, 3.5),  # Dm7
    (67, 4.0), (70, 4.0), (72, 4.0), (74, 4.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.125))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(100, note, time, time + 0.125))

# Dante on sax: short motif, start it, leave it hanging, come back and finish
# Motif: Dm7 -> G7 -> Dm7 -> G7
sax_notes = [
    (62, 1.5), (65, 1.875),  # Dm7
    (67, 2.25), (69, 2.625),  # G7
    (62, 3.0), (65, 3.375),  # Dm7
    (67, 3.75), (69, 4.125),  # G7
    (62, 4.5), (65, 4.875),  # Dm7
    (67, 5.25), (69, 5.625)   # G7
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(110, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
