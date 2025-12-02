
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

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (Fm7): F - Gb - Ab - Bb - Bb - Ab - Gb - F
    (53, 1.5), (54, 1.75), (55, 2.0), (57, 2.25),
    (57, 2.5), (55, 2.75), (54, 3.0), (53, 3.25),
    # Bar 3 (Fm7): F - Gb - Ab - Bb - Bb - Ab - Gb - F
    (53, 3.5), (54, 3.75), (55, 4.0), (57, 4.25),
    (57, 4.5), (55, 4.75), (54, 5.0), (53, 5.25),
    # Bar 4 (Fm7): F - Gb - Ab - Bb - Bb - Ab - Gb - F
    (53, 5.5), (54, 5.75), (55, 6.0), (57, 6.25),
    (57, 6.5), (55, 6.75), (54, 7.0), (53, 7.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (Fm7 on beat 2 and 4)
    (53, 2.0), (55, 2.0), (57, 2.0), (59, 2.0),
    (53, 2.5), (55, 2.5), (57, 2.5), (59, 2.5),
    # Bar 3 (Fm7 on beat 2 and 4)
    (53, 4.0), (55, 4.0), (57, 4.0), (59, 4.0),
    (53, 4.5), (55, 4.5), (57, 4.5), (59, 4.5),
    # Bar 4 (Fm7 on beat 2 and 4)
    (53, 6.0), (55, 6.0), (57, 6.0), (59, 6.0),
    (53, 6.5), (55, 6.5), (57, 6.5), (59, 6.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.5), (38, 3.875), (42, 3.875),
    (36, 4.25), (38, 4.625), (42, 4.625),
    # Bar 4
    (36, 5.5), (38, 5.875), (42, 5.875),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif in Fm, one short phrase, make it sing
# Fm motif: F - Gb - Bb - Ab (melodic minor)
sax_notes = [
    (53, 1.5), (54, 1.75), (57, 2.0), (55, 2.25),
    (53, 2.5), (54, 2.75), (57, 3.0), (55, 3.25),
    (53, 3.5), (54, 3.75), (57, 4.0), (55, 4.25),
    (53, 4.5), (54, 4.75), (57, 5.0), (55, 5.25),
    (53, 5.5), (54, 5.75), (57, 6.0), (55, 6.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
