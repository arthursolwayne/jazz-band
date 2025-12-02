
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

# Bass line (Marcus)
# Walking line with chromatic approaches
bass_notes = [
    (37, 1.5), (38, 1.75), (39, 2.0), (40, 2.25),
    (41, 2.5), (42, 2.75), (43, 3.0), (44, 3.25),
    (45, 3.5), (46, 3.75), (47, 4.0), (48, 4.25),
    (49, 4.5), (50, 4.75), (51, 5.0), (52, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane)
# 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75),
    # Bar 3
    (62, 3.25), (66, 3.25), (69, 3.25), (72, 3.25),
    # Bar 4
    (64, 4.75), (68, 4.75), (71, 4.75), (75, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (65, 2.25),
    (62, 3.5), (64, 3.75), (67, 4.0), (69, 4.25),
    (67, 5.0), (65, 5.25), (62, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
