
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus -- walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 2.875), (47, 3.25), (46, 3.625), (44, 4.0),
    (45, 4.375), (46, 4.75), (44, 5.125), (43, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Diane -- 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    (62, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # F7 on 2
    (62, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),  # F7 on 4
    (62, 4.0), (67, 4.0), (69, 4.0), (71, 4.0),  # F7 on 4
    (62, 5.0), (67, 5.0), (69, 5.0), (71, 5.0)   # F7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Dante -- short motif, one phrase, leave it hanging
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0),  # F - A - B
    (62, 2.25), (65, 2.5), (67, 2.75)  # F - A - B
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

midi.write("dante_intro.mid")
