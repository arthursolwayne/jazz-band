
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
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (34, 1.5), (35, 1.875), (33, 2.25), (32, 2.625),  # Fm7
    # Bar 3
    (30, 3.0), (31, 3.375), (29, 3.75), (28, 4.125),  # Bb7
    # Bar 4
    (29, 4.5), (30, 4.875), (32, 5.25), (33, 5.625)   # D7
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (45, 1.875), (42, 1.875), (40, 1.875), (38, 1.875),  # F7
    (45, 2.625), (42, 2.625), (40, 2.625), (38, 2.625),  # F7
    # Bar 3
    (47, 3.375), (44, 3.375), (41, 3.375), (39, 3.375),  # Bb7
    (47, 4.125), (44, 4.125), (41, 4.125), (39, 4.125),  # Bb7
    # Bar 4
    (49, 4.875), (46, 4.875), (43, 4.875), (41, 4.875),  # D7
    (49, 5.625), (46, 5.625), (43, 5.625), (41, 5.625)   # D7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Saxophone: Motif - start it, leave it hanging, come back and finish it
# Fm7 -> Bb7 -> D7 -> Fm7
sax_notes = [
    (45, 1.5), (41, 1.75), (40, 1.875), (43, 2.0),   # Fm7
    (47, 3.0), (43, 3.25), (42, 3.375), (45, 3.5),   # Bb7
    (49, 4.5), (45, 4.75), (44, 4.875), (47, 5.0),   # D7
    (45, 5.5), (41, 5.75), (40, 5.875), (43, 6.0)    # Fm7
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Add drum fills for bars 2-4
# Bar 2
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
