
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

# Bass line: Fm walking line with chromatic approaches
bass_notes = [
    (44, 1.5), (45, 1.875), (43, 2.25), (41, 2.625),
    (44, 3.0), (45, 3.375), (43, 3.75), (41, 4.125),
    (44, 4.5), (45, 4.875), (43, 5.25), (41, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (48, 2.0), (50, 2.0), (52, 2.0), (54, 2.0),  # F7
    # Bar 3
    (55, 3.0), (57, 3.0), (59, 3.0), (61, 3.0),  # Bb7
    # Bar 4
    (55, 4.0), (57, 4.0), (59, 4.0), (61, 4.0)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (50, 1.5), (52, 1.75), (50, 2.0),
    (48, 2.25), (50, 2.5), (52, 2.75),
    (50, 3.0), (52, 3.25), (50, 3.5),
    (48, 3.75), (50, 4.0), (52, 4.25),
    (50, 4.5), (52, 4.75), (50, 5.0),
    (48, 5.25), (50, 5.5), (52, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
