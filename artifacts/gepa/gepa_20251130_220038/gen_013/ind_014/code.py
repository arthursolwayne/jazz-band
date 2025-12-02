
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (61, 2.625),
    (62, 3.0), (63, 3.375), (60, 3.75), (59, 4.125),
    (60, 4.5), (61, 4.875), (62, 5.25), (63, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D F A C
# Dm7 -> Gm7 -> Am7 -> Dm7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 2.0), (64, 2.0), (67, 2.0), (69, 2.0),  # Dm7
    (67, 2.375), (69, 2.375), (71, 2.375), (72, 2.375),  # Gm7
    # Bar 3 (3.0 - 4.5s)
    (67, 3.375), (69, 3.375), (71, 3.375), (72, 3.375),  # Gm7
    (69, 3.75), (71, 3.75), (74, 3.75), (76, 3.75),  # Am7
    # Bar 4 (4.5 - 6.0s)
    (69, 5.0), (71, 5.0), (74, 5.0), (76, 5.0),  # Am7
    (62, 5.375), (64, 5.375), (67, 5.375), (69, 5.375)   # Dm7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C
# Motif: D F G A (D F G A) -> D F G A -> D F G A -> resolves on D
sax_notes = [
    (62, 1.5), (64, 1.625), (67, 1.75), (69, 1.875),  # D F G A
    (62, 2.25), (64, 2.375), (67, 2.5), (69, 2.625),  # D F G A
    (62, 3.0), (64, 3.125), (67, 3.25), (69, 3.375),  # D F G A
    (62, 3.75), (64, 3.875), (67, 4.0), (69, 4.125),  # D F G A
    (62, 4.5), (64, 4.625), (67, 4.75), (69, 4.875),  # D F G A
    (62, 5.25), (64, 5.375), (67, 5.5), (69, 5.625)   # D F G A
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
