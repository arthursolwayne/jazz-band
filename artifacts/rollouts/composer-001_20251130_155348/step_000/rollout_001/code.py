
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (43, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (43, 3.25),
    (45, 3.5), (46, 3.75), (44, 4.0), (43, 4.25),
    (45, 4.5), (46, 4.75), (44, 5.0), (43, 5.25)
]
for note, time in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    (64, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),
    # Bar 3: Bb7 on 2 and 4
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),
    (62, 3.5), (65, 3.5), (67, 3.5), (69, 3.5),
    # Bar 4: D7 on 2 and 4
    (67, 4.0), (70, 4.0), (72, 4.0), (74, 4.0),
    (67, 4.5), (70, 4.5), (72, 4.5), (74, 4.5)
]
for note, time in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax, one short motif, make it sing
sax_notes = [
    # Bar 2: F (G#) on beat 1
    (76, 1.5), (76, 1.5),
    # Bar 2: G# (A) on beat 2
    (78, 1.75), (78, 1.75),
    # Bar 2: A (Bb) on beat 3
    (79, 2.0), (79, 2.0),
    # Bar 2: Bb (B) on beat 4
    (80, 2.25), (80, 2.25),
    # Bar 3: F (G#) on beat 1
    (76, 2.5), (76, 2.5),
    # Bar 3: G# (A) on beat 2
    (78, 2.75), (78, 2.75),
    # Bar 3: A (Bb) on beat 3
    (79, 3.0), (79, 3.0),
    # Bar 3: Bb (B) on beat 4
    (80, 3.25), (80, 3.25),
    # Bar 4: F (G#) on beat 1
    (76, 3.5), (76, 3.5),
    # Bar 4: G# (A) on beat 2
    (78, 3.75), (78, 3.75),
    # Bar 4: A (Bb) on beat 3
    (79, 4.0), (79, 4.0),
    # Bar 4: Bb (B) on beat 4
    (80, 4.25), (80, 4.25)
]
for note, time in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
