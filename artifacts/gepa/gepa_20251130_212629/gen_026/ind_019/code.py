
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.75),  # Hihat on 1 and 2
    (42, 0.375, 0.75),
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 1.5),  # Hihat on 3 and 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# SAX: Tenor sax, 4-note motif starting on D (D, F#, B, C#), with a short release
# D (D4), F# (F#4), B (B4), C# (C#5), at beat 1, 2, 3, and 4, with slight rhythmic variation
sax_notes = [
    (62, 1.5, 0.35),  # D4 on beat 1
    (66, 1.85, 0.3),  # F#4 on beat 2
    (67, 2.2, 0.3),   # B4 on beat 3
    (69, 2.55, 0.3),  # C#5 on beat 4 (left hanging)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: Marcus plays walking line with chromatic approach
# D (D2), Eb (Eb2), E (E2), F (F2), then chromatic approach to G (G2)
# Bar 2: D, Eb, E, F
bass_notes = [
    (45, 1.5, 0.375),  # D2 on 1
    (46, 1.875, 0.375),  # Eb2 on 2
    (47, 2.25, 0.375),  # E2 on 3
    (48, 2.625, 0.375),  # F2 on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# PIANO: Diane plays 7th chords on 2 and 4
# D7 (D, F#, A, C) on 2, then G7 (G, B, D, F) on 4
piano_notes = [
    # D7 on beat 2 (F#, A, C, D)
    (62, 1.875, 0.375),  # D4
    (66, 1.875, 0.375),  # F#4
    (69, 1.875, 0.375),  # A4
    (67, 1.875, 0.375),  # C4
    # G7 on beat 4 (G, B, D, F)
    (67, 2.625, 0.375),  # G4
    (71, 2.625, 0.375),  # B4
    (69, 2.625, 0.375),  # D4
    (72, 2.625, 0.375),  # F4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Repeat motif, but with a slight delay on the last note
sax_notes = [
    (62, 3.0, 0.35),  # D4 on beat 1
    (66, 3.35, 0.3),  # F#4 on beat 2
    (67, 3.7, 0.3),   # B4 on beat 3
    (69, 4.05, 0.3),  # C#5 on beat 4 (left hanging again)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: Chromatic approach to D (C#, D, Eb, E)
bass_notes = [
    (60, 3.0, 0.375),  # C#3 on 1
    (45, 3.375, 0.375),  # D2 on 2
    (46, 3.75, 0.375),  # Eb2 on 3
    (47, 4.125, 0.375),  # E2 on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# PIANO: Diane plays 7th chords on 2 and 4
# D7 on 2, then C7 (C, Eb, G, Bb) on 4
piano_notes = [
    # D7 on beat 2 (F#, A, C, D)
    (62, 3.375, 0.375),  # D4
    (66, 3.375, 0.375),  # F#4
    (69, 3.375, 0.375),  # A4
    (67, 3.375, 0.375),  # C4
    # C7 on beat 4 (Eb, G, Bb, C)
    (64, 4.125, 0.375),  # Eb4
    (67, 4.125, 0.375),  # G4
    (69, 4.125, 0.375),  # Bb4
    (60, 4.125, 0.375),  # C4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.75),  # Hihat on 1 and 2
    (42, 3.375, 0.75),
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.75, 1.5),  # Hihat on 3 and 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Repeat motif, but with a slight delay on the last note, and a rest on beat 4
sax_notes = [
    (62, 4.5, 0.35),  # D4 on beat 1
    (66, 4.85, 0.3),  # F#4 on beat 2
    (67, 5.2, 0.3),   # B4 on beat 3
    # (69, 5.55, 0.3),  # C#5 on beat 4 (left hanging)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BASS: Marcus plays a chromatic line descending to C
bass_notes = [
    (60, 4.5, 0.375),  # C3 on 1
    (59, 4.875, 0.375),  # B2 on 2
    (58, 5.25, 0.375),  # A2 on 3
    (57, 5.625, 0.375),  # G2 on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# PIANO: Diane plays 7th chords on 2 and 4
# C7 on 2, then B7 (B, D#, F#, A) on 4
piano_notes = [
    # C7 on beat 2 (Eb, G, Bb, C)
    (64, 4.875, 0.375),  # Eb4
    (67, 4.875, 0.375),  # G4
    (69, 4.875, 0.375),  # Bb4
    (60, 4.875, 0.375),  # C4
    # B7 on beat 4 (D#, F#, A, B)
    (69, 5.625, 0.375),  # D#4
    (71, 5.625, 0.375),  # F#4
    (70, 5.625, 0.375),  # A4
    (71, 5.625, 0.375),  # B4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.75),  # Hihat on 1 and 2
    (42, 4.875, 0.75),
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 1.5),  # Hihat on 3 and 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
