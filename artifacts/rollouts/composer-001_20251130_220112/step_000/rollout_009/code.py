
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (48, 2.625),
    (53, 3.0), (51, 3.375), (50, 3.75), (48, 4.125),
    (53, 4.5), (51, 4.875), (50, 5.25), (48, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords on 2 and 4 of bars 2 and 3
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 2.625), (51, 2.625), (55, 2.625), (50, 2.625),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 4.125), (62, 4.125), (53, 4.125), (51, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax motif. Start it, leave it hanging, come back and finish it.
# Motif: F, Gb, Ab, Eb (Fm7 interval)
sax_notes = [
    (53, 1.5), (54, 1.5), (55, 1.5), (50, 1.5),
    (53, 2.0), (54, 2.0), (55, 2.0), (50, 2.0),
    (53, 3.0), (54, 3.0), (55, 3.0), (50, 3.0),
    (53, 4.5), (54, 4.5), (55, 4.5), (50, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
