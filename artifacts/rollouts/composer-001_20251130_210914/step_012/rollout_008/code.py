
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

# Bass line: Marcus, walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (39, 1.5), (37, 1.875), (38, 2.25), (40, 2.625),
    (41, 3.0), (39, 3.375), (37, 3.75), (36, 4.125),
    (38, 4.5), (40, 4.875), (41, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (42, 2.0), (46, 2.0), (47, 2.0), (50, 2.0),  # F7
    (43, 2.375), (47, 2.375), (48, 2.375), (51, 2.375),  # G7
    # Bar 3
    (42, 3.0), (46, 3.0), (47, 3.0), (50, 3.0),  # F7
    (43, 3.375), (47, 3.375), (48, 3.375), (51, 3.375),  # G7
    # Bar 4
    (42, 4.0), (46, 4.0), (47, 4.0), (50, 4.0),  # F7
    (43, 4.375), (47, 4.375), (48, 4.375), (51, 4.375)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: Dante's motif - one short phrase, sing it, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, Db, D
# Motif: F, Ab, Bb, D (F -> Ab -> Bb -> D)
sax_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (62, 2.625),  # F, Ab, Bb, D
    (53, 3.0), (55, 3.375), (57, 3.75), (62, 4.125),  # Repeat with slight variation
    (53, 4.5), (55, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
