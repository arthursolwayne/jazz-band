
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
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),
    (43, 4.5), (45, 4.875), (47, 5.25), (46, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 2.0), (64, 2.0), (67, 2.0), (69, 2.0),  # C7
    # Bar 3
    (62, 3.5), (66, 3.5), (69, 3.5), (71, 3.5),  # D7
    # Bar 4
    (64, 5.0), (67, 5.0), (71, 5.0), (72, 5.0)   # E7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0),  # Start motif
    (64, 2.25), (65, 2.5), (64, 2.75),  # Continue
    (62, 3.0), (64, 3.25), (62, 3.5),  # Repeat
    (64, 3.75), (65, 4.0), (64, 4.25),  # Continue
    (62, 4.5), (64, 4.75), (62, 5.0),  # Repeat
    (64, 5.25), (65, 5.5), (64, 5.75)   # End
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
