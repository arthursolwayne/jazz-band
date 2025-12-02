
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (63, 2.25), (62, 2.625),
    # Bar 3
    (65, 3.0), (64, 3.375), (63, 3.75), (62, 4.125),
    # Bar 4
    (66, 4.5), (65, 4.875), (64, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.875), (71, 1.875), (72, 1.875), (69, 1.875),
    # Bar 3
    (67, 3.375), (71, 3.375), (72, 3.375), (69, 3.375),
    # Bar 4
    (67, 4.875), (71, 4.875), (72, 4.875), (69, 4.875)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dorian mode, D Dorian = D, E, F, G, A, B, C
sax_notes = [
    # Bar 2
    (62, 1.5), (64, 1.75), (62, 2.0),
    # Bar 3
    (67, 3.0), (65, 3.25), (67, 3.5),
    # Bar 4
    (65, 4.5), (67, 4.75), (65, 5.0)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
