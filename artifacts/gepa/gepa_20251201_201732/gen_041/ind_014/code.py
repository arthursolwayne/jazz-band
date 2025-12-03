
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (F, C, Bb, D)
    (53, 1.5), (58, 1.875), (57, 2.25), (60, 2.625),
    # Bar 3 (Bb, F, E, G)
    (57, 3.0), (53, 3.375), (52, 3.75), (55, 4.125),
    # Bar 4 (G, D, C, F)
    (60, 4.5), (65, 4.875), (64, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (53, 1.5), (58, 1.5), (60, 1.5), (64, 1.5), 
    # Bar 3: Bbmaj7 (Bb, D, F, A)
    (57, 3.0), (62, 3.0), (53, 3.0), (58, 3.0),
    # Bar 4: G7 (G, B, D, F)
    (60, 4.5), (65, 4.5), (62, 4.5), (53, 4.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), G (55), A (58) on 1, 2, 3 of bar 2; repeat on 1, 2, 3 of bar 4
sax_notes = [
    # Bar 2
    (53, 1.5), (55, 1.875), (58, 2.25),
    # Bar 4
    (53, 4.5), (55, 4.875), (58, 5.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
