
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875), (42, 2.0), (42, 2.125),
    (42, 2.25), (42, 2.375)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm7 = F Ab C Eb
# Walking bass line in Fm
bass_notes = [
    (53, 1.5), (54, 1.75), (51, 2.0), (50, 2.25),
    (53, 2.5), (54, 2.75), (51, 3.0), (50, 3.25),
    (53, 3.5), (54, 3.75), (51, 4.0), (50, 4.25),
    (53, 4.5), (54, 4.75), (51, 5.0), (50, 5.25)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords, comp on 2 and 4
# Fm7 (F Ab C Eb), Bb7 (Bb D F Ab), Eb7 (Eb G Bb D), Ab7 (Ab C Eb G)
piano_notes = [
    # Bar 2
    (53, 1.75), (57, 1.75), (60, 1.75), (62, 1.75),
    (59, 2.0), (62, 2.0), (64, 2.0), (66, 2.0),
    # Bar 3
    (56, 2.75), (60, 2.75), (62, 2.75), (65, 2.75),
    (59, 3.0), (62, 3.0), (64, 3.0), (66, 3.0),
    # Bar 4
    (53, 3.75), (57, 3.75), (60, 3.75), (62, 3.75),
    (59, 4.0), (62, 4.0), (64, 4.0), (66, 4.0)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5), (38, 1.75), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375), (36, 2.75), (38, 3.0),
    (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375), (42, 3.5), (42, 3.625),
    (42, 3.75), (42, 3.875),
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0), (38, 3.25), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875), (36, 4.25), (38, 4.5),
    (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875), (42, 5.0), (42, 5.125),
    (42, 5.25), (42, 5.375),
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5), (38, 4.75), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375), (36, 5.75), (38, 6.0),
    (42, 6.0), (42, 6.125), (42, 6.25), (42, 6.375), (42, 6.5), (42, 6.625),
    (42, 6.75), (42, 6.875)
]

for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, C, F (in 16th notes)
sax_notes = [
    (53, 1.5), (55, 1.625), (57, 1.75), (60, 1.875),
    (53, 2.5), (55, 2.625), (57, 2.75), (60, 2.875),
    (53, 3.5), (55, 3.625), (57, 3.75), (60, 3.875),
    (53, 4.5), (55, 4.625), (57, 4.75), (60, 4.875)
]

for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
