
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.25), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (62, 3.5), (64, 3.75), (62, 4.0), (60, 4.25),
    (62, 4.5), (64, 4.75), (62, 5.0), (60, 5.25),
    (62, 5.5), (64, 5.75), (62, 6.0)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Diane: 7th chords on 2 and 4, Dm7, Gm7, Cm7, Fm7
piano_notes = [
    # Bar 2
    (62, 1.75), (67, 1.75), (74, 1.75), (79, 1.75),
    (65, 2.25), (70, 2.25), (77, 2.25), (82, 2.25),
    # Bar 3
    (62, 3.25), (67, 3.25), (74, 3.25), (79, 3.25),
    (65, 3.75), (70, 3.75), (77, 3.75), (82, 3.75),
    # Bar 4
    (62, 4.25), (67, 4.25), (74, 4.25), (79, 4.25),
    (65, 4.75), (70, 4.75), (77, 4.75), (82, 4.75)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (36, 2.25), (38, 2.5), (42, 2.25), (42, 2.375), (42, 2.5), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (36, 3.75), (38, 4.0), (42, 3.75), (42, 3.875), (42, 4.0), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (36, 5.25), (38, 5.5), (42, 5.25), (42, 5.375), (42, 5.5), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax, one short motif, make it sing
# Motif: Dm - F - Eb - D (D, F, Eb, D)
sax_notes = [
    (62, 1.5), (66, 1.75), (64, 2.0), (62, 2.25),  # First phrase
    (62, 3.5), (66, 3.75), (64, 4.0), (62, 4.25),  # Second phrase
    (62, 5.5)  # Leave it hanging
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
