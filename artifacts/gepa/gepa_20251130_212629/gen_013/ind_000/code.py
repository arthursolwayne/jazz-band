
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

# Bass line (Marcus): walking line, chromatic approaches, never same note twice
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),
    (64, 3.0), (65, 3.375), (62, 3.75), (64, 4.125),
    (65, 4.5), (67, 4.875), (64, 5.25), (65, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7 at bar 2
    (69, 3.0), (72, 3.0), (76, 3.0), (77, 3.0),  # G7 at bar 3
    (64, 4.0), (67, 4.0), (71, 4.0), (72, 4.0)   # D7 at bar 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (64, 2.625),
    (62, 3.0), (64, 3.375), (65, 3.75), (64, 4.125),
    (62, 4.5), (64, 4.875), (65, 5.25), (64, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
