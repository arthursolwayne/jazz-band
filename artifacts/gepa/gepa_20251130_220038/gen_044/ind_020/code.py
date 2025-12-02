
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

# Bass line (Marcus): walking line in Fm, chromatic approaches
bass_notes = [
    (43, 1.5), (44, 1.875), (42, 2.25), (41, 2.625),
    (43, 2.75), (44, 3.125), (42, 3.5), (41, 3.875),
    (43, 4.0), (44, 4.375), (42, 4.75), (41, 5.125),
    (43, 5.25), (44, 5.625), (42, 6.0), (41, 6.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    (53, 1.875), (50, 1.875), (57, 1.875), (59, 1.875),
    # Bar 3: Bb7
    (62, 3.125), (59, 3.125), (64, 3.125), (66, 3.125),
    # Bar 4: Eb7
    (65, 4.375), (62, 4.375), (67, 4.375), (69, 4.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums (Little Ray): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (57, 1.5), (59, 1.625), (57, 1.75),
    (55, 2.0), (57, 2.125), (59, 2.25),
    (57, 2.5), (59, 2.625), (61, 2.75),
    (59, 3.0), (57, 3.125), (55, 3.25),
    (57, 3.5), (59, 3.625), (61, 3.75),
    (59, 4.0), (57, 4.125), (55, 4.25),
    (57, 4.5), (59, 4.625), (61, 4.75),
    (59, 5.0), (57, 5.125), (55, 5.25),
    (57, 5.5), (59, 5.625), (61, 5.75),
    (59, 6.0), (57, 6.125), (55, 6.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
