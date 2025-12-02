
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
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.375), (38, 3.75), (42, 3.75),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line in F
bass_notes = [
    (17, 1.5), (18, 1.75), (19, 2.0), (21, 2.25),
    (22, 2.5), (23, 2.75), (24, 3.0), (25, 3.25),
    (27, 3.5), (28, 3.75), (29, 4.0), (31, 4.25),
    (32, 4.5), (33, 4.75), (34, 5.0), (35, 5.25),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.75), (71, 1.75), (72, 1.75), (76, 1.75),
    # Bar 3
    (67, 3.25), (71, 3.25), (72, 3.25), (76, 3.25),
    # Bar 4
    (67, 4.75), (71, 4.75), (72, 4.75), (76, 4.75),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Saxophone - motif in F
# Bar 2: Start of motif
sax_notes = [
    (66, 1.5), (69, 1.75), (67, 2.0), (66, 2.25),
    # Bar 3: No sax
    # Bar 4: Return and finish it
    (69, 4.5), (68, 4.75), (66, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    # Bar 3
    (36, 3.5), (38, 3.875), (42, 3.875),
    (36, 4.625), (38, 5.0), (42, 5.0),
    # Bar 4
    (36, 5.5), (38, 5.875), (42, 5.875),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
