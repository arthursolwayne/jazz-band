
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

# Bass line (Marcus): Fm7 -> Bb7 -> Eb7 -> Ab7
# Walking line with chromatic approaches
bass_notes = [
    (53, 1.5), (50, 1.875), (51, 2.25), (52, 2.625),
    (55, 3.0), (52, 3.375), (53, 3.75), (54, 4.125),
    (57, 4.5), (54, 4.875), (55, 5.25), (56, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 3.0), (53, 3.0), (57, 3.0), (60, 3.0),
    (55, 3.375), (58, 3.375), (62, 3.375), (64, 3.375),
    # Bar 3
    (55, 4.5), (58, 4.5), (62, 4.5), (64, 4.5),
    (52, 4.875), (55, 4.875), (59, 4.875), (62, 4.875),
    # Bar 4
    (52, 6.0), (55, 6.0), (59, 6.0), (62, 6.0),
    (57, 6.375), (60, 6.375), (64, 6.375), (67, 6.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): motif in Fm
# Start on F, move to Ab, then G, then back to F
sax_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (53, 2.625),
    (53, 3.0), (55, 3.375), (57, 3.75), (53, 4.125),
    (53, 4.5), (55, 4.875), (57, 5.25), (53, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums continue for bars 2-4
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
