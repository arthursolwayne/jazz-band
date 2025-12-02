
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

# Marcus: Walking bass line in Fm
bass_notes = [
    (24, 1.5), (25, 1.875), (22, 2.25), (23, 2.625),
    (24, 3.0), (25, 3.375), (22, 3.75), (23, 4.125),
    (24, 4.5), (25, 4.875), (22, 5.25), (23, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords, comp on 2 and 4
# Fm7 on beat 2, Bbm7 on beat 4, repeated
piano_notes = [
    (44, 2.0), (40, 2.0), (36, 2.0), (33, 2.0),  # Fm7
    (42, 2.0), (38, 2.0), (35, 2.0), (30, 2.0),  # Bbm7
    (44, 3.5), (40, 3.5), (36, 3.5), (33, 3.5),  # Fm7
    (42, 3.5), (38, 3.5), (35, 3.5), (30, 3.5),  # Bbm7
    (44, 5.0), (40, 5.0), (36, 5.0), (33, 5.0),  # Fm7
    (42, 5.0), (38, 5.0), (35, 5.0), (30, 5.0)   # Bbm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Motif in Fm
# Fm - Ab - Bb - D - Fm (descending)
sax_notes = [
    (34, 1.5), (30, 1.875), (31, 2.25), (28, 2.625),
    (34, 3.0), (30, 3.375), (31, 3.75), (28, 4.125),
    (34, 4.5), (30, 4.875), (31, 5.25), (28, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
