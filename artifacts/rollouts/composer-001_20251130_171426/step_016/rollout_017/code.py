
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (47, 2.25),
    (48, 2.5), (49, 2.75), (47, 3.0), (50, 3.25),
    (51, 3.5), (52, 3.75), (50, 4.0), (53, 4.25),
    (54, 4.5), (55, 4.75), (53, 5.0), (56, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4, F7, Bb7, C7, E7
piano_notes = [
    # Bar 2 - F7 on beat 2
    (53, 2.0), (57, 2.0), (60, 2.0), (62, 2.0),
    # Bar 2 - C7 on beat 4
    (60, 2.5), (64, 2.5), (67, 2.5), (69, 2.5),
    # Bar 3 - Bb7 on beat 2
    (58, 3.0), (62, 3.0), (65, 3.0), (67, 3.0),
    # Bar 3 - E7 on beat 4
    (64, 3.5), (68, 3.5), (71, 3.5), (73, 3.5),
    # Bar 4 - F7 on beat 2
    (53, 4.0), (57, 4.0), (60, 4.0), (62, 4.0),
    # Bar 4 - C7 on beat 4
    (60, 4.5), (64, 4.5), (67, 4.5), (69, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax melody - one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Start with a descending motif in F minor
    (61, 1.5), (59, 1.875), (57, 2.25), (55, 2.625),
    # Leave it hanging on 55 (E)
    (55, 2.625), (55, 2.625), (55, 2.625),
    # Return with a resolution to F
    (55, 3.0), (57, 3.375), (59, 3.75), (61, 4.125),
    # End with a chromatic run into F7
    (62, 4.5), (61, 4.75), (59, 5.0), (57, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    # Bar 3
    (36, 3.5), (38, 3.875), (42, 3.875),
    (36, 4.625), (38, 5.0), (42, 5.0),
    # Bar 4
    (36, 5.5), (38, 5.875), (42, 5.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
