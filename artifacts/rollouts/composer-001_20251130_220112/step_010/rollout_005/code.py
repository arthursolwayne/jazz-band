
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

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5), (60, 1.875), (59, 2.25), (57, 2.625),
    # Bar 3
    (55, 3.0), (53, 3.375), (52, 3.75), (50, 4.125),
    # Bar 4
    (48, 4.5), (47, 4.875), (45, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords comping on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 1.875), (65, 1.875), (67, 1.875), (69, 1.875),
    # Bar 3: G7 (G B D F)
    (71, 3.375), (76, 3.375), (74, 3.375), (71, 3.375),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 4.875), (64, 4.875), (67, 4.875), (62, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Motif in Dm, one short phrase, leave it hanging
sax_notes = [
    # Bar 2: Start motif (D, F, G)
    (62, 1.5), (65, 1.75), (67, 2.0),
    # Bar 3: Continue (A, Bb)
    (67, 3.0), (62, 3.25),
    # Bar 4: Finish (C, D)
    (69, 4.5), (62, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums continue for bars 2-4
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
