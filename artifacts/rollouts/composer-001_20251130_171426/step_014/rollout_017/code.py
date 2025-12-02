
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approached
bass_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (62, 2.625),  # Dm7
    (64, 3.0), (65, 3.375), (67, 3.75), (64, 4.125),  # G7
    (67, 4.5), (69, 4.875), (67, 5.25), (64, 5.625)   # Cm7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 2.0), (67, 2.0), (70, 2.0), (64, 2.0),  # Dm7
    (67, 3.0), (71, 3.0), (74, 3.0), (69, 3.0),  # G7
    # Bar 3
    (67, 4.0), (72, 4.0), (74, 4.0), (69, 4.0),  # Cm7
    (67, 5.0), (71, 5.0), (74, 5.0), (69, 5.0)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif in Dm, short, singable
# Dm7 -> G7 -> Cm7 -> G7
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (69, 2.625),
    (67, 3.0), (71, 3.375), (72, 3.75), (69, 4.125),
    (67, 4.5), (69, 4.875), (72, 5.25), (71, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
