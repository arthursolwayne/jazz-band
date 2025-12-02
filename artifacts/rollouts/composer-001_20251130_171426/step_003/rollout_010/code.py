
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

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (53, 1.5), (54, 1.875), (51, 2.25), (52, 2.625),
    (53, 3.0), (54, 3.375), (51, 3.75), (52, 4.125),
    (53, 4.5), (54, 4.875), (51, 5.25), (52, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 2.0), (65, 2.0), (67, 2.0), (71, 2.0),
    (62, 3.0), (65, 3.0), (67, 3.0), (71, 3.0),
    (62, 4.0), (65, 4.0), (67, 4.0), (71, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (66, 1.5, 0.375), (69, 1.875, 0.375), (67, 2.25, 0.375),  # First phrase
    (66, 2.625, 0.375), (69, 2.625, 0.375), (67, 2.625, 0.375),  # Rest on last note
    (66, 3.0, 0.375), (69, 3.375, 0.375), (67, 3.75, 0.375),  # Repeat phrase
    (66, 4.125, 0.375), (69, 4.5, 0.375), (67, 4.875, 0.375)   # Final resolution
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
