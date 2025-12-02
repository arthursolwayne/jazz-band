
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - bass line (walking, chromatic approaches)
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375),  # Gb
    (66, 2.25, 0.375),  # G
    (67, 2.625, 0.375),  # Ab
    (64, 3.0, 0.375),  # F
    (65, 3.375, 0.375),  # Gb
    (66, 3.75, 0.375),  # G
    (67, 4.125, 0.375),  # Ab
    (64, 4.5, 0.375),  # F
    (65, 4.875, 0.375),  # Gb
    (66, 5.25, 0.375),  # G
    (67, 5.625, 0.375),  # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane - piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    (64, 1.5, 0.375),  # F7 - F
    (67, 1.5, 0.375),  # F7 - A
    (69, 1.5, 0.375),  # F7 - C
    (71, 1.5, 0.375),  # F7 - Eb
    # Bar 3
    (64, 3.0, 0.375),  # F7 - F
    (67, 3.0, 0.375),  # F7 - A
    (69, 3.0, 0.375),  # F7 - C
    (71, 3.0, 0.375),  # F7 - Eb
    # Bar 4
    (64, 4.5, 0.375),  # F7 - F
    (67, 4.5, 0.375),  # F7 - A
    (69, 4.5, 0.375),  # F7 - C
    (71, 4.5, 0.375),  # F7 - Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 1.5, 0.375),  # Kick 1
    (42, 1.5, 0.375),  # Hihat 1
    (38, 1.875, 0.375),  # Snare 2
    (42, 1.875, 0.375),  # Hihat 2
    (36, 2.25, 0.375),  # Kick 3
    (42, 2.25, 0.375),  # Hihat 3
    (38, 2.625, 0.375),  # Snare 4
    (42, 2.625, 0.375),  # Hihat 4
    (36, 3.0, 0.375),  # Kick 1
    (42, 3.0, 0.375),  # Hihat 1
    (38, 3.375, 0.375),  # Snare 2
    (42, 3.375, 0.375),  # Hihat 2
    (36, 3.75, 0.375),  # Kick 3
    (42, 3.75, 0.375),  # Hihat 3
    (38, 4.125, 0.375),  # Snare 4
    (42, 4.125, 0.375),  # Hihat 4
    (36, 4.5, 0.375),  # Kick 1
    (42, 4.5, 0.375),  # Hihat 1
    (38, 4.875, 0.375),  # Snare 2
    (42, 4.875, 0.375),  # Hihat 2
    (36, 5.25, 0.375),  # Kick 3
    (42, 5.25, 0.375),  # Hihat 3
    (38, 5.625, 0.375),  # Snare 4
    (42, 5.625, 0.375),  # Hihat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - sax melody (one short motif, make it sing)
sax_notes = [
    (62, 1.5, 0.375),  # G
    (64, 1.875, 0.375),  # F
    (62, 2.25, 0.375),  # G
    (64, 2.625, 0.375),  # F
    (66, 3.0, 0.375),  # G
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),  # G
    (60, 4.125, 0.375),  # E
    (62, 4.5, 0.375),  # G
    (64, 4.875, 0.375),  # F
    (62, 5.25, 0.375),  # G
    (64, 5.625, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
