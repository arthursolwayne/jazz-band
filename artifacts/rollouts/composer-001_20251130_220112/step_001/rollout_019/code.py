
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
    (36, 0.0, 1.0),   # Kick on 1
    (42, 0.0, 0.5),   # Hihat on 1
    (38, 0.5, 1.0),   # Snare on 2
    (42, 0.5, 1.0),   # Hihat on 2
    (36, 1.0, 1.5),   # Kick on 3
    (42, 1.0, 1.5),   # Hihat on 3
    (38, 1.5, 2.0),   # Snare on 4
    (42, 1.5, 2.0),   # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm
bass_notes = [
    (64, 1.5, 1.75),  # F
    (62, 1.75, 2.0),  # D
    (63, 2.0, 2.25),  # Eb
    (61, 2.25, 2.5),  # C
    (64, 2.5, 2.75),  # F
    (65, 2.75, 3.0),  # G
    (63, 3.0, 3.25),  # Eb
    (62, 3.25, 3.5),  # D
    (64, 3.5, 3.75),  # F
    (66, 3.75, 4.0),  # Ab
    (63, 4.0, 4.25),  # Eb
    (62, 4.25, 4.5),  # D
    (64, 4.5, 4.75),  # F
    (67, 4.75, 5.0),  # Bb
    (63, 5.0, 5.25),  # Eb
    (62, 5.25, 5.5),  # D
    (64, 5.5, 5.75),  # F
    (65, 5.75, 6.0),  # G
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane - Piano comping on 2 and 4
piano_notes = [
    # Bar 2
    (76, 1.75, 2.0),  # Bb7
    (74, 1.75, 2.0),
    (71, 1.75, 2.0),
    (64, 1.75, 2.0),
    # Bar 3
    (76, 3.25, 3.5),  # Bb7
    (74, 3.25, 3.5),
    (71, 3.25, 3.5),
    (64, 3.25, 3.5),
    # Bar 4
    (76, 5.25, 5.5),  # Bb7
    (74, 5.25, 5.5),
    (71, 5.25, 5.5),
    (64, 5.25, 5.5),
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Dante - Tenor sax melody
sax_notes = [
    (65, 1.5, 1.75),  # G
    (62, 1.75, 2.0),  # Eb
    (64, 2.0, 2.25),  # F
    (65, 2.25, 2.5),  # G
    (62, 2.5, 2.75),  # Eb
    (64, 2.75, 3.0),  # F
    (66, 3.0, 3.25),  # Ab
    (65, 3.25, 3.5),  # G
    (64, 3.5, 3.75),  # F
    (62, 3.75, 4.0),  # Eb
    (64, 4.0, 4.25),  # F
    (65, 4.25, 4.5),  # G
    (66, 4.5, 4.75),  # Ab
    (65, 4.75, 5.0),  # G
    (64, 5.0, 5.25),  # F
    (62, 5.25, 5.5),  # Eb
    (64, 5.5, 5.75),  # F
    (66, 5.75, 6.0),  # Ab
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75),  # Kick on 1
    (42, 1.5, 2.0),  # Hihat on 1
    (38, 2.0, 2.25),  # Snare on 2
    (42, 2.0, 2.25),  # Hihat on 2
    (36, 2.25, 2.5),  # Kick on 3
    (42, 2.25, 2.5),  # Hihat on 3
    (38, 2.5, 2.75),  # Snare on 4
    (42, 2.5, 2.75),  # Hihat on 4
    # Bar 3
    (36, 3.0, 3.25),  # Kick on 1
    (42, 3.0, 3.25),  # Hihat on 1
    (38, 3.25, 3.5),  # Snare on 2
    (42, 3.25, 3.5),  # Hihat on 2
    (36, 3.5, 3.75),  # Kick on 3
    (42, 3.5, 3.75),  # Hihat on 3
    (38, 3.75, 4.0),  # Snare on 4
    (42, 3.75, 4.0),  # Hihat on 4
    # Bar 4
    (36, 4.5, 4.75),  # Kick on 1
    (42, 4.5, 4.75),  # Hihat on 1
    (38, 4.75, 5.0),  # Snare on 2
    (42, 4.75, 5.0),  # Hihat on 2
    (36, 5.0, 5.25),  # Kick on 3
    (42, 5.0, 5.25),  # Hihat on 3
    (38, 5.25, 5.5),  # Snare on 4
    (42, 5.25, 5.5),  # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
