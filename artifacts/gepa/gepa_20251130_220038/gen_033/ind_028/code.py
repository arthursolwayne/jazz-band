
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
# Bass: Walking line in Fm, chromatic approaches

# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
bass_notes = [
    (70, 1.5), (69, 1.875), (67, 2.25), (65, 2.625),  # F, Gb, Ab, Bb
    (62, 3.0), (60, 3.375), (58, 3.75), (55, 4.125),  # B, Db, Eb, F
    (70, 4.5), (69, 4.875), (67, 5.25), (65, 5.625),  # F, Gb, Ab, Bb
    (62, 6.0), (60, 6.375), (58, 6.75), (55, 7.125)   # B, Db, Eb, F
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4

# Fm7 = F, Ab, Bb, Db
# Bbm7 = Bb, Db, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, B, Db, E
piano_notes = [
    # Bar 2
    (53, 1.5), (60, 1.5), (64, 1.5), (61, 1.5),  # Fm7
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # Bbm7
    # Bar 3
    (60, 3.0), (64, 3.0), (69, 3.0), (71, 3.0),  # Eb7
    (64, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),  # Bbm7
    # Bar 4
    (64, 4.5), (67, 4.5), (69, 4.5), (71, 4.5),  # Bbm7
    (64, 5.0), (67, 5.0), (69, 5.0), (71, 5.0),  # Bbm7
    (60, 5.5), (64, 5.5), (69, 5.5), (71, 5.5),  # Eb7
    (64, 6.0), (67, 6.0), (69, 6.0), (71, 6.0)   # Bbm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing

# Fm motif: F, Ab, Bb, Eb (F - Ab - Bb - Eb)
sax_notes = [
    (70, 1.5), (67, 1.875), (64, 2.25), (60, 2.625),  # Melody
    (70, 3.0), (67, 3.375), (64, 3.75), (60, 4.125),  # Repeat melody
    (70, 4.5), (67, 4.875), (64, 5.25), (60, 5.625)   # Repeat melody
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums continue with same pattern in bars 2-4
for i in range(2, 4):
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + i * 1.5, end=time + i * 1.5 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
