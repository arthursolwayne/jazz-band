
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (44, 2.25, 0.375), (43, 2.625, 0.375),
    (45, 3.0, 0.375), (46, 3.375, 0.375), (44, 3.75, 0.375), (43, 4.125, 0.375),
    (45, 4.5, 0.375), (46, 4.875, 0.375), (44, 5.25, 0.375), (43, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.1875), (64, 1.5, 0.1875), (67, 1.5, 0.1875), (69, 1.5, 0.1875),
    # Bar 3
    (62, 3.0, 0.1875), (64, 3.0, 0.1875), (67, 3.0, 0.1875), (69, 3.0, 0.1875),
    # Bar 4
    (62, 4.5, 0.1875), (64, 4.5, 0.1875), (67, 4.5, 0.1875), (69, 4.5, 0.1875)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 -> E7 (chromatic approach), then resolve with a rest and repeat
sax_notes = [
    (66, 1.5, 0.1875), (65, 1.6875, 0.1875), (66, 1.875, 0.1875), (65, 2.0625, 0.1875),
    (64, 2.25, 0.1875), (65, 2.4375, 0.1875), (66, 2.625, 0.1875), (67, 2.8125, 0.1875),
    (66, 3.0, 0.1875), (65, 3.1875, 0.1875), (64, 3.375, 0.1875), (63, 3.5625, 0.1875),
    (64, 3.75, 0.1875), (65, 3.9375, 0.1875), (66, 4.125, 0.1875), (67, 4.3125, 0.1875),
    (66, 4.5, 0.1875), (65, 4.6875, 0.1875), (64, 4.875, 0.1875), (63, 5.0625, 0.1875),
    (64, 5.25, 0.1875), (65, 5.4375, 0.1875), (66, 5.625, 0.1875), (67, 5.8125, 0.1875)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
