
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

# Bass line: Marcus
bass_notes = [
    (45, 1.5), (47, 1.875), (46, 2.25), (44, 2.625),  # Bar 2
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),  # Bar 3
    (45, 4.5), (47, 4.875), (46, 5.25), (44, 5.625)   # Bar 4
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Diane
piano_notes = [
    # Bar 2: C7, E7, G7, B7 (1.5 - 2.625)
    (72, 1.5), (74, 1.5), (76, 1.5), (79, 1.5),
    # Bar 3: F7, A7, C8, E8 (3.0 - 4.125)
    (77, 3.0), (79, 3.0), (81, 3.0), (84, 3.0),
    # Bar 4: G7, B7, D8, F8 (4.5 - 5.625)
    (76, 4.5), (79, 4.5), (82, 4.5), (85, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Dante
sax_notes = [
    # Bar 2: Motif starts (1.5s)
    (62, 1.5), (66, 1.875), (64, 2.25), (62, 2.625),  # First four notes
    # Bar 3: Return and finish (3.0s)
    (62, 3.0), (66, 3.375), (64, 3.75), (62, 4.125),
    # Bar 4: Repeat motif (4.5s)
    (62, 4.5), (66, 4.875), (64, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
