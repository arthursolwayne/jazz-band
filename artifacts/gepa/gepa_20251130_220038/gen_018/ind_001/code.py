
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

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (47, 1.75), (46, 2.0), (44, 2.25),
    (45, 2.5), (47, 2.75), (46, 3.0), (44, 3.25),
    (45, 3.5), (47, 3.75), (46, 4.0), (44, 4.25),
    (45, 4.5), (47, 4.75), (46, 5.0), (44, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
# F7 on beat 2, Bb7 on beat 4, repeating
piano_notes = [
    # Bar 2
    (53, 2.0), (60, 2.0), (64, 2.0), (67, 2.0),  # F7
    (58, 2.5), (65, 2.5), (68, 2.5), (71, 2.5),  # Bb7
    # Bar 3
    (53, 3.0), (60, 3.0), (64, 3.0), (67, 3.0),  # F7
    (58, 3.5), (65, 3.5), (68, 3.5), (71, 3.5),  # Bb7
    # Bar 4
    (53, 4.0), (60, 4.0), (64, 4.0), (67, 4.0),  # F7
    (58, 4.5), (65, 4.5), (68, 4.5), (71, 4.5)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# F (66), G (67), Bb (68), F (66)
sax_notes = [
    (66, 1.5), (67, 1.75), (68, 2.0), (66, 2.5),
    (66, 3.0), (67, 3.25), (68, 3.5), (66, 4.0),
    (66, 4.5), (67, 4.75), (68, 5.0), (66, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
