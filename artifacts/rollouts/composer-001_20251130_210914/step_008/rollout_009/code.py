
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Tenor motif - start with a short phrase, leave it hanging
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    (65, 2.625, 0.375), (62, 2.75, 0.125), (60, 2.875, 0.125),
    (62, 3.0, 0.375), (65, 3.375, 0.375), (67, 3.75, 0.375),
    (65, 4.125, 0.375), (62, 4.5, 0.375), (60, 4.875, 0.375),
    (62, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bass: Walking line in F major, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (52, 2.625, 0.375),
    (51, 2.75, 0.375), (50, 3.125, 0.375), (49, 3.5, 0.375), (48, 3.875, 0.375),
    (50, 4.25, 0.375), (52, 4.625, 0.375), (53, 5.0, 0.375), (52, 5.375, 0.375),
    (51, 5.75, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.375), (66, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    (62, 3.125, 0.375), (66, 3.125, 0.375), (67, 3.125, 0.375), (69, 3.125, 0.375),
    (62, 4.5, 0.375), (66, 4.5, 0.375), (67, 4.5, 0.375), (69, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 1) * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875),
        (42, start + 1.125, 0.1875), (42, start + 1.3125, 0.1875), (42, start + 1.5, 0.1875)
    ]
    for note, s, d in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
