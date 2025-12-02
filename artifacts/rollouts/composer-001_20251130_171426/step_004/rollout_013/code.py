
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375), # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    (48, 1.5, 0.375), # G
    (49, 1.875, 0.375), # G#
    (50, 2.25, 0.375), # A
    (51, 2.625, 0.375), # A#
    (52, 3.0, 0.375), # Bb
    (53, 3.375, 0.375), # B
    (55, 3.75, 0.375), # C#
    (56, 4.125, 0.375), # D
    (57, 4.5, 0.375), # D#
    (58, 4.875, 0.375), # E
    (59, 5.25, 0.375), # F
    (60, 5.625, 0.375) # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375), # C7
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    (71, 1.5, 0.375),
    # Bar 3
    (62, 3.0, 0.375), # C7
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    (71, 3.0, 0.375),
    # Bar 4
    (62, 4.5, 0.375), # C7
    (64, 4.5, 0.375),
    (67, 4.5, 0.375),
    (71, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Dante on sax (short motif, make it sing)
sax_notes = [
    (66, 1.5, 0.375), # F
    (68, 1.875, 0.375), # G
    (67, 2.25, 0.375), # F#
    (66, 2.625, 0.375), # F
    (64, 3.0, 0.375), # E
    (66, 3.375, 0.375), # F
    (69, 3.75, 0.375), # G#
    (69, 4.125, 0.375), # G#
    (67, 4.5, 0.375), # F#
    (66, 4.875, 0.375), # F
    (64, 5.25, 0.375), # E
    (62, 5.625, 0.375) # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
