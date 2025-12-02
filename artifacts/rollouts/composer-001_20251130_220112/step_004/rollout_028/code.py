
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

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.75), (50, 2.0), (51, 2.25),
    (52, 2.5), (53, 2.75), (51, 3.0), (50, 3.25),
    (49, 3.5), (48, 3.75), (47, 4.0), (46, 4.25),
    (45, 4.5), (44, 4.75), (45, 5.0), (46, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (45, 2.0), (48, 2.0), (50, 2.0), (52, 2.0),  # F7
    (45, 2.5), (48, 2.5), (50, 2.5), (52, 2.5),  # F7
    # Bar 3
    (50, 3.0), (53, 3.0), (55, 3.0), (57, 3.0),  # C7
    (50, 3.5), (53, 3.5), (55, 3.5), (57, 3.5),  # C7
    # Bar 4
    (46, 4.0), (49, 4.0), (51, 4.0), (53, 4.0),  # Gm7
    (46, 4.5), (49, 4.5), (51, 4.5), (53, 4.5)   # Gm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax, one short motif, make it sing
sax_notes = [
    (55, 1.5), (57, 1.75), (55, 2.0),  # Start of motif
    (53, 2.5), (55, 2.75), (53, 3.0),  # Continue
    (55, 3.5), (57, 3.75), (55, 4.0),  # Continue
    (53, 4.5), (55, 4.75), (57, 5.0)   # End of motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
