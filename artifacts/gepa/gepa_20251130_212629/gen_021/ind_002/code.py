
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    (36, 0.375, 100),  # Kick on 1
    (42, 0.375, 90),   # Hihat on 1
    (38, 0.75, 100),   # Snare on 2
    (42, 0.75, 90),    # Hihat on 2
    (36, 1.125, 100),  # Kick on 3
    (42, 1.125, 90),   # Hihat on 3
    (38, 1.5, 100),    # Snare on 4
    (42, 1.5, 90)      # Hihat on 4
]
for note, start, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
# F7 chord: F A C E (root, 3, 5, 7)
bass_notes = [
    (47, 1.5, 90),    # F (root)
    (49, 1.875, 85),  # G (chromatic up)
    (46, 2.25, 80),   # E (7)
    (45, 2.625, 85)   # D (chromatic down)
]
for note, start, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 chord on beat 2
    (53, 1.875, 95),  # A
    (55, 1.875, 90),  # C
    (57, 1.875, 85),  # E
    (50, 1.875, 80),  # F
    # Bar 2: F7 chord on beat 4
    (53, 2.625, 95),  # A
    (55, 2.625, 90),  # C
    (57, 2.625, 85),  # E
    (50, 2.625, 80)   # F
]
for note, start, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: Introduce motif
# Motif: F (beat 1), Bb (beat 2), F (beat 3), rest (beat 4)
sax_notes = [
    (62, 1.5, 100),   # F
    (65, 1.875, 100), # Bb
    (62, 2.25, 100),  # F
]
for note, start, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (50, 3.0, 90),    # F
    (52, 3.375, 85),  # G
    (49, 3.75, 80),   # E
    (48, 4.125, 85)   # D
]
for note, start, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 chord on beat 2
    (53, 3.375, 95),  # A
    (55, 3.375, 90),  # C
    (57, 3.375, 85),  # E
    (50, 3.375, 80),  # F
    # Bar 3: F7 chord on beat 4
    (53, 4.125, 95),  # A
    (55, 4.125, 90),  # C
    (57, 4.125, 85),  # E
    (50, 4.125, 80)   # F
]
for note, start, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: Repeat motif with variation
# Motif: F (beat 1), Bb (beat 2), rest (beat 3), A (beat 4)
sax_notes = [
    (62, 3.0, 100),   # F
    (65, 3.375, 100), # Bb
    (64, 4.5, 100)    # A
]
for note, start, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: continue pattern
drum_notes = [
    (36, 3.0, 100),   # Kick on 1
    (42, 3.0, 90),    # Hihat on 1
    (38, 3.375, 100), # Snare on 2
    (42, 3.375, 90),  # Hihat on 2
    (36, 3.75, 100),  # Kick on 3
    (42, 3.75, 90),   # Hihat on 3
    (38, 4.125, 100), # Snare on 4
    (42, 4.125, 90)   # Hihat on 4
]
for note, start, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (50, 4.5, 90),    # F
    (52, 4.875, 85),  # G
    (49, 5.25, 80),   # E
    (48, 5.625, 85)   # D
]
for note, start, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 chord on beat 2
    (53, 4.875, 95),  # A
    (55, 4.875, 90),  # C
    (57, 4.875, 85),  # E
    (50, 4.875, 80),  # F
    # Bar 4: F7 chord on beat 4
    (53, 5.625, 95),  # A
    (55, 5.625, 90),  # C
    (57, 5.625, 85),  # E
    (50, 5.625, 80)   # F
]
for note, start, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: End with a question
# Motif: Bb (beat 1), F (beat 2), rest (beat 3), rest (beat 4)
sax_notes = [
    (65, 4.5, 100),   # Bb
    (62, 4.875, 100)  # F
]
for note, start, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: continue pattern
drum_notes = [
    (36, 4.5, 100),   # Kick on 1
    (42, 4.5, 90),    # Hihat on 1
    (38, 4.875, 100), # Snare on 2
    (42, 4.875, 90),  # Hihat on 2
    (36, 5.25, 100),  # Kick on 3
    (42, 5.25, 90),   # Hihat on 3
    (38, 5.625, 100), # Snare on 4
    (42, 5.625, 90)   # Hihat on 4
]
for note, start, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save
midi.write("dante_intro.mid")
