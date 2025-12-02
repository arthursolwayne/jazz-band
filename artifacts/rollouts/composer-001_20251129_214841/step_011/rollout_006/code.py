
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),    # Kick on 1
    (38, 0.75, 0.75),   # Snare on 2
    (42, 0.0, 1.5),     # Hihat on every 8th
    (42, 0.375, 1.5),
    (42, 0.75, 1.5),
    (42, 1.125, 1.5),
    (36, 1.5, 1.5),     # Kick on 3
    (38, 1.5, 1.5),     # Snare on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, start, end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 1.75),    # C
    (61, 1.75, 2.0),    # C#
    (62, 2.0, 2.25),    # D
    (63, 2.25, 2.5),    # D#
    (64, 2.5, 2.75),    # E
    (65, 2.75, 3.0),    # F
    (66, 3.0, 3.25),    # F#
    (67, 3.25, 3.5),    # G
    (68, 3.5, 3.75),    # G#
    (69, 3.75, 4.0),    # A
    (70, 4.0, 4.25),    # A#
    (71, 4.25, 4.5),    # B
    (72, 4.5, 4.75),    # C
    (73, 4.75, 5.0),    # C#
    (74, 5.0, 5.25),    # D
    (75, 5.25, 5.5),    # D#
    (76, 5.5, 5.75),    # E
    (77, 5.75, 6.0),    # F
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(80, note, start, end))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75, 2.0),    # C
    (64, 1.75, 2.0),    # E
    (67, 1.75, 2.0),    # G
    (71, 1.75, 2.0),    # B
    # Bar 3
    (60, 3.25, 3.5),    # C
    (64, 3.25, 3.5),    # E
    (67, 3.25, 3.5),    # G
    (71, 3.25, 3.5),    # B
    # Bar 4
    (60, 4.75, 5.0),    # C
    (64, 4.75, 5.0),    # E
    (67, 4.75, 5.0),    # G
    (71, 4.75, 5.0),    # B
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(80, note, start, end))

# Sax (Dante) - motif in C, short and singable
sax_notes = [
    (60, 1.5, 1.75),   # C
    (62, 1.75, 2.0),   # D
    (64, 2.0, 2.25),   # E
    (60, 2.25, 2.5),   # C
    (62, 2.5, 2.75),   # D
    (64, 2.75, 3.0),   # E
    (65, 3.0, 3.25),   # F
    (67, 3.25, 3.5),   # G
    (69, 3.5, 3.75),   # A
    (67, 3.75, 4.0),   # G
    (69, 4.0, 4.25),   # A
    (67, 4.25, 4.5),   # G
    (65, 4.5, 4.75),   # F
    (64, 4.75, 5.0),   # E
    (62, 5.0, 5.25),   # D
    (60, 5.25, 5.5),   # C
    (62, 5.5, 5.75),   # D
    (64, 5.75, 6.0),   # E
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, start, end))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75),    # Kick on 1
    (38, 2.0, 2.25),    # Snare on 2
    (42, 1.5, 2.0),     # Hihat on every 8th
    (42, 1.875, 2.0),
    (42, 2.25, 2.5),
    (42, 2.625, 2.75),
    (36, 2.75, 3.0),    # Kick on 3
    (38, 3.0, 3.25),    # Snare on 4
    # Bar 3
    (36, 3.5, 3.75),    # Kick on 1
    (38, 4.0, 4.25),    # Snare on 2
    (42, 3.5, 4.0),     # Hihat on every 8th
    (42, 3.875, 4.0),
    (42, 4.25, 4.5),
    (42, 4.625, 4.75),
    (36, 4.75, 5.0),    # Kick on 3
    (38, 5.0, 5.25),    # Snare on 4
    # Bar 4
    (36, 5.5, 5.75),    # Kick on 1
    (38, 6.0, 6.25),    # Snare on 2
    (42, 5.5, 6.0),     # Hihat on every 8th
    (42, 5.875, 6.0),
    (42, 6.25, 6.5),
    (42, 6.625, 6.75),
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, start, end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.midi")
