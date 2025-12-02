
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.75),    # Kick on 1
    (38, 0.75, 0.75),   # Snare on 2
    (42, 0.0, 1.5),     # Hihat on every eighth
    (42, 0.375, 1.5),
    (42, 0.75, 1.5),
    (42, 1.125, 1.5),
    (36, 1.5, 0.75),    # Kick on 3
    (38, 2.25, 0.75),   # Snare on 4
    (42, 1.5, 3.0),     # Hihat on every eighth
    (42, 1.875, 3.0),
    (42, 2.25, 3.0),
    (42, 2.625, 3.0)
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (60, 1.5, 1.75),   # C
    (61, 1.75, 2.0),   # C#
    (62, 2.0, 2.25),   # D
    (63, 2.25, 2.5),   # D#
    (64, 2.5, 2.75),   # E
    (65, 2.75, 3.0),   # F
    (66, 3.0, 3.25),   # F#
    (67, 3.25, 3.5),   # G
    (68, 3.5, 3.75),   # G#
    (69, 3.75, 4.0),   # A
    (70, 4.0, 4.25),   # A#
    (71, 4.25, 4.5),   # B
    (72, 4.5, 4.75),   # C
    (71, 4.75, 5.0),   # B
    (70, 5.0, 5.25),   # A#
    (69, 5.25, 5.5),   # A
    (68, 5.5, 5.75),   # G#
    (67, 5.75, 6.0),   # G
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75, 2.0),   # C7 (C, E, B)
    (64, 1.75, 2.0),
    (67, 1.75, 2.0),
    # Bar 3
    (60, 3.25, 3.5),   # C7
    (64, 3.25, 3.5),
    (67, 3.25, 3.5),
    # Bar 4
    (60, 4.75, 5.0),   # C7
    (64, 4.75, 5.0),
    (67, 4.75, 5.0),
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.75),   # D
    (64, 1.75, 2.0),   # E
    (62, 2.0, 2.25),   # D
    (60, 2.25, 2.5),   # C
    (62, 2.5, 2.75),   # D
    (64, 2.75, 3.0),   # E
    (62, 3.0, 3.25),   # D
    (60, 3.25, 3.5),   # C
    (62, 3.5, 3.75),   # D
    (64, 3.75, 4.0),   # E
    (62, 4.0, 4.25),   # D
    (60, 4.25, 4.5),   # C
    (62, 4.5, 4.75),   # D
    (64, 4.75, 5.0),   # E
    (62, 5.0, 5.25),   # D
    (60, 5.25, 5.5),   # C
    (62, 5.5, 5.75),   # D
    (64, 5.75, 6.0),   # E
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75),   # Kick on 1
    (38, 2.25, 2.5),   # Snare on 2
    (42, 1.5, 3.0),    # Hihat on every eighth
    (42, 1.875, 3.0),
    (42, 2.25, 3.0),
    (42, 2.625, 3.0),
    (36, 3.0, 3.25),   # Kick on 3
    (38, 3.75, 4.0),   # Snare on 4
    (42, 3.0, 6.0),    # Hihat on every eighth
    (42, 3.375, 6.0),
    (42, 3.75, 6.0),
    (42, 4.125, 6.0),
    (42, 4.5, 6.0),
    (42, 4.875, 6.0),
    (42, 5.25, 6.0),
    (42, 5.625, 6.0),
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
