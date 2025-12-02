
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches, no repeated notes
# F A Bb C D Eb F G (F7)
bass_notes = [
    (53, 1.5), (58, 1.75), (57, 2.0), (55, 2.25),
    (57, 2.5), (60, 2.75), (58, 3.0), (55, 3.25),
    (57, 3.5), (60, 3.75), (58, 4.0), (55, 4.25),
    (57, 4.5), (60, 4.75), (58, 5.0), (53, 5.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Diane: 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4, F7 on 2, Gm7 on 4
piano_notes = [
    # Bar 2 (1.5-2.0s): F7 (F A C Eb)
    (53, 1.5), (58, 1.5), (60, 1.5), (62, 1.5),
    # Bar 2 (2.0-2.5s): Rest
    # Bar 3 (2.5-3.0s): Bb7 (Bb D F Ab)
    (58, 2.5), (62, 2.5), (60, 2.5), (64, 2.5),
    # Bar 3 (3.0-3.5s): Rest
    # Bar 4 (3.5-4.0s): F7 (F A C Eb)
    (53, 3.5), (58, 3.5), (60, 3.5), (62, 3.5),
    # Bar 4 (4.0-4.5s): Rest
    # Bar 4 (4.5-5.0s): Gm7 (G Bb D F)
    (55, 4.5), (58, 4.5), (60, 4.5), (60, 4.5),
    # Bar 4 (5.0-5.5s): Rest
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.875), (38, 5.25), (42, 5.25)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Dante: Tenor sax motif - one short phrase, make it sing
# F G A Bb (F7)
sax_notes = [
    (53, 1.5), (55, 1.75), (57, 2.0), (58, 2.25),
    # Let it hang, come back
    (57, 2.5), (55, 2.75), (53, 3.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
