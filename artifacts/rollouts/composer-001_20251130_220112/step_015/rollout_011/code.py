
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
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (65, 2.25),
    (67, 2.5), (68, 2.75), (69, 3.0), (70, 3.25),
    (72, 3.5), (73, 3.75), (74, 4.0), (75, 4.25),
    (77, 4.5), (78, 4.75), (79, 5.0), (80, 5.25)
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.0), (71, 2.0), (74, 2.0), (76, 2.0),
    (67, 3.0), (71, 3.0), (74, 3.0), (76, 3.0),
    (67, 4.0), (71, 4.0), (74, 4.0), (76, 4.0)
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Dante: Tenor sax motif in D
sax_notes = [
    (62, 1.5), (65, 1.625), (67, 1.875), (65, 2.0),
    (62, 2.25), (64, 2.5), (67, 2.75), (65, 3.0),
    (62, 3.25), (64, 3.5), (67, 3.75), (65, 4.0),
    (62, 4.25), (64, 4.5), (67, 4.75), (65, 5.0),
    (62, 5.25), (64, 5.5), (67, 5.75), (65, 6.0)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
