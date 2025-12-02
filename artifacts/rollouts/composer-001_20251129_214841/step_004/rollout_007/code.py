
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, dur in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (62, 2.25, 0.375), (63, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (66, 3.75, 0.375), (67, 4.125, 0.375),
    (68, 4.5, 0.375), (69, 4.875, 0.375), (70, 5.25, 0.375), (71, 5.625, 0.375)
]
for note, start, dur in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 2.25, 0.375), (64, 2.25, 0.375), (67, 2.25, 0.375),
    (69, 2.25, 0.375),
    # Bar 3: C7 on beat 2
    (60, 3.75, 0.375), (64, 3.75, 0.375), (67, 3.75, 0.375),
    (69, 3.75, 0.375),
    # Bar 4: C7 on beat 2
    (60, 5.25, 0.375), (64, 5.25, 0.375), (67, 5.25, 0.375),
    (69, 5.25, 0.375)
]
for note, start, dur in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    piano.notes.append(pn)

# Sax: motif in C (C, D#, E, C), start at 1.5, leave it hanging
sax_notes = [
    (60, 1.5, 0.375),
    (63, 1.875, 0.375),
    (64, 2.25, 0.375),
    (60, 2.625, 0.375),
    # Repeat the motif, but start at 3.0
    (60, 3.0, 0.375),
    (63, 3.375, 0.375),
    (64, 3.75, 0.375),
    (60, 4.125, 0.375),
    # Finale at 4.5
    (60, 4.5, 0.375),
    (63, 4.875, 0.375),
    (64, 5.25, 0.375),
    (60, 5.625, 0.375)
]
for note, start, dur in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    sax.notes.append(sn)

# Drum fills: bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875),
        (36, start + 1.5, 0.375), (38, start + 1.875, 0.375), (42, start + 1.5, 0.1875)
    ]
    for note, s, d in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
