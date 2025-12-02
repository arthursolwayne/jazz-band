
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

# Bass: Walking line with chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (43, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (43, 3.25),
    (45, 3.5), (46, 3.75), (44, 4.0), (43, 4.25),
    (45, 4.5), (46, 4.75), (44, 5.0), (43, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (60, 1.75), (64, 1.75), (67, 1.75), (69, 1.75),
    (62, 2.25), (66, 2.25), (69, 2.25), (71, 2.25),
    # Bar 3
    (60, 3.25), (64, 3.25), (67, 3.25), (69, 3.25),
    (62, 3.75), (66, 3.75), (69, 3.75), (71, 3.75),
    # Bar 4
    (60, 4.75), (64, 4.75), (67, 4.75), (69, 4.75),
    (62, 5.25), (66, 5.25), (69, 5.25), (71, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0),
    (69, 2.5), (67, 2.75), (65, 3.0), (62, 3.25),
    (65, 3.5), (67, 3.75), (69, 4.0),
    (67, 4.25), (65, 4.5), (62, 4.75),
    (65, 5.0), (67, 5.25), (69, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
