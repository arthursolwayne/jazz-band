
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
    (36, 0.0, 1.0),   # Kick on 1
    (38, 0.5, 1.0),   # Snare on 2
    (42, 0.0, 1.0),   # Hihat on 1
    (42, 0.25, 1.0),  # Hihat on 1+
    (42, 0.5, 1.0),   # Hihat on 2
    (42, 0.75, 1.0),  # Hihat on 2+
    (42, 1.0, 1.0),   # Hihat on 3
    (42, 1.25, 1.0),  # Hihat on 3+
    (36, 1.5, 1.0),   # Kick on 3
    (38, 1.0, 1.0),   # Snare on 4
    (42, 1.5, 1.0),   # Hihat on 4
    (42, 1.75, 1.0)   # Hihat on 4+
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 1.75),  # D
    (63, 1.75, 2.0),  # Eb
    (61, 2.0, 2.25),  # C
    (62, 2.25, 2.5),  # D
    (63, 2.5, 2.75),  # Eb
    (64, 2.75, 3.0),  # F
    (63, 3.0, 3.25),  # Eb
    (62, 3.25, 3.5),  # D
    (61, 3.5, 3.75),  # C
    (60, 3.75, 4.0),  # B
    (62, 4.0, 4.25),  # D
    (64, 4.25, 4.5),  # F
    (63, 4.5, 4.75),  # Eb
    (62, 4.75, 5.0)   # D
]
for note in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4 (1.5 - 3.0s)
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (62, 1.5, 1.75),      # D
    (67, 1.5, 1.75),      # F#
    (69, 1.5, 1.75),      # A
    (64, 1.5, 1.75),      # C
    # Bar 3: G7 (G, B, D, F)
    (67, 2.5, 2.75),      # G
    (71, 2.5, 2.75),      # B
    (69, 2.5, 2.75),      # D
    (67, 2.5, 2.75),      # F
    # Bar 4: C7 (C, E, G, B)
    (60, 3.5, 3.75),      # C
    (64, 3.5, 3.75),      # E
    (67, 3.5, 3.75),      # G
    (71, 3.5, 3.75),      # B
]
for note in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(pn)

# Sax: One short motif, sparse and expressive (1.5 - 3.0s)
sax_notes = [
    (62, 1.5, 2.0),      # D
    (64, 2.25, 2.5),     # F
    (62, 2.75, 3.0),     # D
    (62, 3.5, 3.75),     # D
    (64, 4.0, 4.25),     # F
    (62, 4.5, 4.75),     # D
    (62, 5.0, 5.25)      # D
]
for note in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sn)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (1.5 - 3.0s)
drum_notes = [
    (36, 1.5, 1.75),     # Kick on 1
    (38, 2.0, 2.25),     # Snare on 2
    (42, 1.5, 1.75),     # Hihat on 1
    (42, 1.75, 2.0),     # Hihat on 1+
    (42, 2.0, 2.25),     # Hihat on 2
    (42, 2.25, 2.5),     # Hihat on 2+
    (42, 2.5, 2.75),     # Hihat on 3
    (42, 2.75, 3.0),     # Hihat on 3+
    (36, 2.75, 3.0),     # Kick on 3
    (38, 3.0, 3.25),     # Snare on 4
    (42, 3.0, 3.25),     # Hihat on 4
    (42, 3.25, 3.5),     # Hihat on 4+
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (64, 3.0, 3.25),  # F
    (63, 3.25, 3.5),  # Eb
    (62, 3.5, 3.75),  # D
    (60, 3.75, 4.0),  # B
    (62, 4.0, 4.25),  # D
    (64, 4.25, 4.5),  # F
    (63, 4.5, 4.75),  # Eb
    (62, 4.75, 5.0),  # D
    (61, 5.0, 5.25),  # C
    (60, 5.25, 5.5),  # B
    (62, 5.5, 5.75),  # D
    (64, 5.75, 6.0)   # F
]
for note in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4 (3.0 - 4.5s)
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    (67, 3.0, 3.25),      # G
    (71, 3.0, 3.25),      # B
    (69, 3.0, 3.25),      # D
    (67, 3.0, 3.25),      # F
    # Bar 4: C7 (C, E, G, B)
    (60, 4.0, 4.25),      # C
    (64, 4.0, 4.25),      # E
    (67, 4.0, 4.25),      # G
    (71, 4.0, 4.25),      # B
]
for note in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(pn)

# Sax: Continue the motif, leave it hanging (3.0 - 4.5s)
sax_notes = [
    (64, 3.0, 3.25),      # F
    (62, 3.25, 3.5),      # D
    (64, 3.5, 3.75),      # F
    (62, 3.75, 4.0),      # D
    (64, 4.0, 4.25),      # F
    (62, 4.25, 4.5),      # D
    (62, 4.5, 4.75),      # D
    (62, 5.0, 5.25),      # D
    (62, 5.5, 5.75),      # D
    (62, 6.0, 6.25)       # D
]
for note in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sn)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 3.25),     # Kick on 1
    (38, 3.5, 3.75),     # Snare on 2
    (42, 3.0, 3.25),     # Hihat on 1
    (42, 3.25, 3.5),     # Hihat on 1+
    (42, 3.5, 3.75),     # Hihat on 2
    (42, 3.75, 4.0),     # Hihat on 2+
    (42, 4.0, 4.25),     # Hihat on 3
    (42, 4.25, 4.5),     # Hihat on 3+
    (36, 4.25, 4.5),     # Kick on 3
    (38, 4.5, 4.75),     # Snare on 4
    (42, 4.5, 4.75),     # Hihat on 4
    (42, 4.75, 5.0),     # Hihat on 4+
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (64, 4.5, 4.75),  # F
    (63, 4.75, 5.0),  # Eb
    (62, 5.0, 5.25),  # D
    (60, 5.25, 5.5),  # B
    (62, 5.5, 5.75),  # D
    (64, 5.75, 6.0),  # F
]
for note in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4 (4.5 - 6.0s)
piano_notes = [
    # Bar 4: C7 (C, E, G, B)
    (60, 4.5, 4.75),      # C
    (64, 4.5, 4.75),      # E
    (67, 4.5, 4.75),      # G
    (71, 4.5, 4.75),      # B
]
for note in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(pn)

# Sax: End with a rest, leave the question (4.5 - 6.0s)
sax_notes = [
    (62, 5.5, 5.75),      # D
    (62, 6.0, 6.25)       # D
]
for note in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sn)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 4.75),     # Kick on 1
    (38, 5.0, 5.25),     # Snare on 2
    (42, 4.5, 4.75),     # Hihat on 1
    (42, 4.75, 5.0),     # Hihat on 1+
    (42, 5.0, 5.25),     # Hihat on 2
    (42, 5.25, 5.5),     # Hihat on 2+
    (42, 5.5, 5.75),     # Hihat on 3
    (42, 5.75, 6.0),     # Hihat on 3+
    (36, 5.75, 6.0),     # Kick on 3
    (38, 6.0, 6.25),     # Snare on 4
    (42, 6.0, 6.25),     # Hihat on 4
    (42, 6.25, 6.5)      # Hihat on 4+
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
