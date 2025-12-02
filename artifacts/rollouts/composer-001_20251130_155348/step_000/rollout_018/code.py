
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

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (47, 2.25),  # F, Gb, E, G
    (48, 2.5), (49, 2.75), (47, 3.0), (50, 3.25),  # Ab, A, G, Bb
    (51, 3.5), (52, 3.75), (50, 4.0), (53, 4.25),  # B, Bb, A, B
    (54, 4.5), (55, 4.75), (53, 5.0), (56, 5.25)   # C, C#, B, D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.75), (60, 1.75), (62, 1.75), (64, 1.75),  # F7
    # Bar 3
    (60, 2.75), (63, 2.75), (65, 2.75), (67, 2.75),  # A7
    # Bar 4
    (62, 3.75), (65, 3.75), (67, 3.75), (69, 3.75)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5), (64, 1.625), (62, 1.75), (60, 1.875),  # F, G, F, E
    (62, 2.5), (64, 2.625), (62, 2.75), (60, 2.875),  # F, G, F, E
    (62, 3.5), (64, 3.625), (62, 3.75), (60, 3.875),  # F, G, F, E
    (62, 4.5), (64, 4.625), (62, 4.75), (60, 4.875)   # F, G, F, E
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
