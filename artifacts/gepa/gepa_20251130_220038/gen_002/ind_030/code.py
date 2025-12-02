
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

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    (64, 2.375), (67, 2.375), (69, 2.375), (71, 2.375),
    # Bar 3
    (64, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),
    (64, 3.375), (67, 3.375), (69, 3.375), (71, 3.375),
    # Bar 4
    (64, 4.0), (67, 4.0), (69, 4.0), (71, 4.0),
    (64, 4.375), (67, 4.375), (69, 4.375), (71, 4.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 - G7 - Cmaj7 - F7
# Motif: D, F#, C, D
# Bar 2: D (1.5s), F# (1.875s)
# Bar 3: C (3.0s), D (3.375s)
# Bar 4: D (4.5s), F# (4.875s), C (5.25s), D (5.625s)
sax_notes = [
    (62, 1.5), (66, 1.875),
    (60, 3.0), (62, 3.375),
    (62, 4.5), (66, 4.875), (60, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
