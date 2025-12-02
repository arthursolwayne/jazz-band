
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (39, 2.25), (41, 2.625),  # Fm7
    (42, 3.0), (43, 3.375), (42, 3.75), (44, 4.125),  # Bbm7
    (45, 4.5), (46, 4.875), (45, 5.25), (47, 5.625)   # Eb7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0)
    (60, 1.5), (64, 1.5), (67, 1.5), (70, 1.5),  # Fm7
    (62, 2.0), (66, 2.0), (69, 2.0), (71, 2.0),  # Bbm7
    # Bar 3 (3.0-4.5)
    (63, 3.0), (67, 3.0), (70, 3.0), (72, 3.0),  # Eb7
    (65, 4.0), (69, 4.0), (71, 4.0), (74, 4.0),  # Ab7
    # Bar 4 (4.5-6.0)
    (60, 4.5), (64, 4.5), (67, 4.5), (70, 4.5),  # Fm7
    (62, 5.5), (66, 5.5), (69, 5.5), (71, 5.5)   # Bbm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Dante on sax: short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, Db, D
# Motif: F - Ab - Bb - F (hanging on Bb)
sax_notes = [
    (53, 1.5, 0.5),  # F
    (57, 2.0, 0.5),  # Ab
    (58, 2.5, 0.5),  # Bb
    (53, 3.0, 0.5)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: fill the bar
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.375), (42, 3.75), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.875), (42, 5.25), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
