
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
    (36, 0.0, 1.0),     # Kick on 1
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.0, 1.0),     # Hihat on 1
    (42, 0.25, 1.0),    # Hihat on &
    (42, 0.5, 1.0),     # Hihat on 2
    (42, 0.75, 1.0),    # Hihat on 2&
    (42, 1.0, 1.0),     # Hihat on 3
    (42, 1.25, 1.0),    # Hihat on 3&
    (42, 1.5, 1.0),     # Hihat on 4
    (36, 1.0, 1.0),     # Kick on 3
    (38, 1.5, 1.0)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5, 0.5),  # F
    (49, 2.0, 0.5),  # Gb
    (50, 2.5, 0.5),  # G
    (51, 3.0, 0.5)   # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 2.0, 0.5),  # Gm7 (F, Ab, C, Eb)
    (50, 2.0, 0.5),  # F
    (53, 2.0, 0.5),  # Ab
    (55, 2.0, 0.5),  # C
    (57, 2.0, 0.5),  # Eb
    (50, 3.0, 0.5),  # Gm7 on 4
    (50, 3.0, 0.5),  # F
    (53, 3.0, 0.5),  # Ab
    (55, 3.0, 0.5),  # C
    (57, 3.0, 0.5)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody starts, sparse and expressive
sax_notes = [
    (62, 1.5, 0.5),  # G (Fm scale)
    (64, 2.0, 0.5),  # A
    (60, 2.5, 0.5),  # E
    (62, 3.0, 0.5)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, same approach
bass_notes = [
    (51, 3.0, 0.5),  # Ab
    (52, 3.5, 0.5),  # Bb
    (53, 4.0, 0.5),  # B
    (55, 4.5, 0.5)   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (57, 3.5, 0.5),  # Eb7 (Ab, C, Eb, G)
    (57, 3.5, 0.5),  # Eb
    (59, 3.5, 0.5),  # G
    (60, 3.5, 0.5),  # Ab
    (62, 3.5, 0.5),  # Bb
    (57, 4.5, 0.5),  # Eb7 on 4
    (57, 4.5, 0.5),  # Eb
    (59, 4.5, 0.5),  # G
    (60, 4.5, 0.5),  # Ab
    (62, 4.5, 0.5)   # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody continues, a bit more tension
sax_notes = [
    (64, 3.0, 0.5),  # A
    (67, 3.5, 0.5),  # C
    (64, 4.0, 0.5),  # A
    (62, 4.5, 0.5)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: same pattern, but a bit more energy
drum_notes = [
    (36, 3.0, 1.0),     # Kick on 1
    (38, 3.5, 1.0),     # Snare on 2
    (42, 3.0, 1.0),     # Hihat on 1
    (42, 3.25, 1.0),    # Hihat on &
    (42, 3.5, 1.0),     # Hihat on 2
    (42, 3.75, 1.0),    # Hihat on 2&
    (42, 4.0, 1.0),     # Hihat on 3
    (42, 4.25, 1.0),    # Hihat on 3&
    (42, 4.5, 1.0),     # Hihat on 4
    (36, 4.0, 1.0),     # Kick on 3
    (38, 4.5, 1.0)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, same approach
bass_notes = [
    (55, 4.5, 0.5),  # C
    (56, 5.0, 0.5),  # Db
    (57, 5.5, 0.5),  # D
    (59, 6.0, 0.5)   # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 5.0, 0.5),  # Ab7 (C, Eb, G, Bb)
    (53, 5.0, 0.5),  # Ab
    (55, 5.0, 0.5),  # C
    (57, 5.0, 0.5),  # G
    (59, 5.0, 0.5),  # Bb
    (53, 6.0, 0.5),  # Ab7 on 4
    (53, 6.0, 0.5),  # Ab
    (55, 6.0, 0.5),  # C
    (57, 6.0, 0.5),  # G
    (59, 6.0, 0.5)   # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody ends with a lingering question
sax_notes = [
    (64, 4.5, 0.5),  # A
    (67, 5.0, 0.5),  # C
    (64, 5.5, 0.5),  # A
    (62, 6.0, 0.5)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: same pattern
drum_notes = [
    (36, 4.5, 1.0),     # Kick on 1
    (38, 5.0, 1.0),     # Snare on 2
    (42, 4.5, 1.0),     # Hihat on 1
    (42, 4.75, 1.0),    # Hihat on &
    (42, 5.0, 1.0),     # Hihat on 2
    (42, 5.25, 1.0),    # Hihat on 2&
    (42, 5.5, 1.0),     # Hihat on 3
    (42, 5.75, 1.0),    # Hihat on 3&
    (42, 6.0, 1.0),     # Hihat on 4
    (36, 5.5, 1.0),     # Kick on 3
    (38, 6.0, 1.0)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dantes_intro.mid")
