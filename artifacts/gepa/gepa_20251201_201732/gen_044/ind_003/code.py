
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

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (42, 2.625),
    (43, 3.0), (41, 3.375), (40, 3.75), (38, 4.125),
    (40, 4.5), (42, 4.875), (43, 5.25), (41, 5.625)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F#)
piano_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3: Gm7 (Bb, D, G, B)
    (60, 3.0), (62, 3.0), (67, 3.0), (69, 3.0),
    # Bar 4: Cm7 (Eb, G, C, Eb)
    (61, 4.5), (67, 4.5), (60, 4.5), (61, 4.5)
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3: 3.0 - 4.5
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: 4.5 - 6.0
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax - one short motif, make it sing.
# Start it, leave it hanging, come back and finish it.
sax_notes = [
    (67, 1.5), (71, 1.625), (67, 1.75),
    (71, 2.125), (67, 2.25), (69, 2.5),
    (71, 2.875), (67, 3.0)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
