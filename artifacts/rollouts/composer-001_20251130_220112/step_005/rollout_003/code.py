
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

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (44, 1.5), (45, 1.75), (43, 2.0), (41, 2.25),  # Fm walking
    (44, 2.5), (45, 2.75), (43, 3.0), (41, 3.25),
    (44, 3.5), (45, 3.75), (43, 4.0), (41, 4.25),
    (44, 4.5), (45, 4.75), (43, 5.0), (41, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.75), (60, 1.75), (62, 1.75), (64, 1.75),  # F7
    # Bar 3
    (59, 3.25), (62, 3.25), (64, 3.25), (66, 3.25),  # Bb7
    # Bar 4
    (57, 4.75), (60, 4.75), (62, 4.75), (64, 4.75)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing
# Start with a Bb, then A, then F, leave it hanging
sax_notes = [
    (62, 1.5), (60, 1.75), (57, 2.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add the final note of the motif back in on the last bar
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75))

midi.instruments.extend([sax, bass, piano, drums])
