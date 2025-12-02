
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# F7 chord: F A C E (root, 3, 5, 7)
# Walking bass line (F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#)
bass_notes = [
    # Bar 2
    (53, 1.5), (52, 1.875), (51, 2.25), (50, 2.625),
    # Bar 3
    (49, 3.0), (48, 3.375), (53, 3.75), (55, 4.125),
    # Bar 4
    (53, 4.5), (52, 4.875), (51, 5.25), (50, 5.625),
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
# F7 chord: F A C E
# Bar 2: F7 on beat 2, play chord on 2 and 4
piano_notes = [
    # Bar 2
    (53, 2.0), (58, 2.0), (60, 2.0), (64, 2.0),
    (53, 2.5), (58, 2.5), (60, 2.5), (64, 2.5),
    # Bar 3
    (53, 3.0), (58, 3.0), (60, 3.0), (64, 3.0),
    (53, 3.5), (58, 3.5), (60, 3.5), (64, 3.5),
    # Bar 4
    (53, 4.0), (58, 4.0), (60, 4.0), (64, 4.0),
    (53, 4.5), (58, 4.5), (60, 4.5), (64, 4.5),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4 (fill the bar)
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 3
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): One short motif, make it sing
# F Bb D F (F6 chord), but with a twist on the third bar
sax_notes = [
    (53, 1.5), (50, 1.875), (55, 2.25), (53, 2.625),
    (53, 3.0), (50, 3.375), (55, 3.75), (53, 4.125),
    (53, 4.5), (50, 4.875), (55, 5.25), (53, 5.625),
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
