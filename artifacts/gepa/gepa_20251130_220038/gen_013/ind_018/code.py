
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    # Bar 3
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),
    # Bar 4
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)
]

for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),
    (69, 2.375), (72, 2.375),
    # Bar 3
    (64, 3.5), (67, 3.5), (71, 3.5), (72, 3.5),
    (69, 3.875), (72, 3.875),
    # Bar 4
    (64, 5.0), (67, 5.0), (71, 5.0), (72, 5.0),
    (69, 5.375), (72, 5.375)
]

for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start motif
    (67, 1.5), (69, 1.875), (67, 2.25),
    # Bar 3 - Leave it hanging
    (69, 3.0),
    # Bar 4 - Come back and finish it
    (67, 4.5), (69, 4.875), (67, 5.25)
]

for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
