
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
    (36, 0.0),
    (38, 0.375),
    (42, 0.0),
    (42, 0.375),
    (42, 0.75),
    (42, 1.125),
    (36, 1.5),
    (38, 1.875),
    (42, 1.5),
    (42, 1.875),
    (42, 2.25),
    (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (39, 1.5), (40, 1.875), (41, 2.25), (42, 2.625),
    (42, 3.0), (41, 3.375), (40, 3.75), (39, 4.125),
    (39, 4.5), (40, 4.875), (41, 5.25), (42, 5.625),
    (42, 6.0), (41, 6.375), (40, 6.75), (39, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords on 2 and 4, Fm7, Bbm7, Ebm7, Abm7
piano_notes = [
    # Bar 2: Fm7 - 2nd beat
    (53, 3.0), (50, 3.0), (47, 3.0), (44, 3.0),
    # Bar 2: Bbm7 - 4th beat
    (51, 3.375), (48, 3.375), (45, 3.375), (41, 3.375),
    # Bar 3: Ebm7 - 2nd beat
    (52, 4.5), (49, 4.5), (46, 4.5), (42, 4.5),
    # Bar 3: Abm7 - 4th beat
    (53, 4.875), (50, 4.875), (47, 4.875), (44, 4.875),
    # Bar 4: Fm7 - 2nd beat
    (53, 6.0), (50, 6.0), (47, 6.0), (44, 6.0),
    # Bar 4: Bbm7 - 4th beat
    (51, 6.375), (48, 6.375), (45, 6.375), (41, 6.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5),
    (42, 1.875), (42, 2.25), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.0),
    (42, 3.375), (42, 3.75), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.5),
    (42, 4.875), (42, 5.25), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.0),
    (42, 6.375), (42, 6.75), (42, 7.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax melody in Fm
# Motif: Fm - G - Ab - Bb (Dante's voice)
# Start on beat 2 of bar 2, leave it hanging
sax_notes = [
    (62, 3.0), (64, 3.375), (65, 3.75), (63, 4.125),
    (62, 4.5), (64, 4.875), (65, 5.25), (63, 5.625),
    (62, 6.0), (64, 6.375), (65, 6.75), (63, 7.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('fmintrous.mid')
