
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
drum_notes = [
    (36, 0.0, 1.0),     # Kick on beat 1
    (38, 0.5, 1.0),     # Snare on beat 2
    (42, 0.0, 1.0),     # Hihat on beat 1
    (42, 0.25, 0.25),   # Hihat on beat 1 &
    (42, 0.5, 0.25),    # Hihat on beat 2 &
    (42, 0.75, 0.25),   # Hihat on beat 3 &
    (42, 1.0, 0.25),    # Hihat on beat 3 &
    (36, 1.0, 1.0),     # Kick on beat 3
    (38, 1.5, 1.0),     # Snare on beat 4
    (42, 1.0, 0.25),    # Hihat on beat 3 &
    (42, 1.25, 0.25),   # Hihat on beat 3 &
    (42, 1.5, 0.25),    # Hihat on beat 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, chromatic approach to Gm7
bass_notes = [
    (45, 1.5, 0.375),  # F (root)
    (47, 1.875, 0.375), # Ab (chromatic approach to G)
    (48, 2.25, 0.375),  # G (target)
    (47, 2.625, 0.375), # Ab (chromatic approach to A)
    (50, 3.0, 0.375),   # A (target)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 2
piano_notes = [
    # F7 on beat 2
    (53, 1.875, 0.375),  # F
    (55, 1.875, 0.375),  # A
    (57, 1.875, 0.375),  # C
    (60, 1.875, 0.375),  # E
    # Bb7 on beat 4
    (58, 3.0, 0.375),    # Bb
    (60, 3.0, 0.375),    # D
    (62, 3.0, 0.375),    # F
    (64, 3.0, 0.375),    # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif on bar 2
sax_notes = [
    (62, 1.5, 0.375),  # G
    (66, 1.875, 0.375), # Bb
    (67, 2.25, 0.375),  # B
    (66, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, chromatic approach to Cm7
bass_notes = [
    (50, 3.0, 0.375),   # A (root)
    (52, 3.375, 0.375), # C (chromatic approach to B)
    (51, 3.75, 0.375),  # B (target)
    (50, 4.125, 0.375), # A (chromatic approach to Ab)
    (48, 4.5, 0.375),   # G (target)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 3
piano_notes = [
    # C7 on beat 2
    (55, 3.375, 0.375),  # C
    (57, 3.375, 0.375),  # E
    (58, 3.375, 0.375),  # G
    (60, 3.375, 0.375),  # Bb
    # F7 on beat 4
    (53, 4.5, 0.375),    # F
    (55, 4.5, 0.375),    # A
    (57, 4.5, 0.375),    # C
    (60, 4.5, 0.375),    # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif on bar 3
sax_notes = [
    (62, 3.0, 0.375),   # G
    (66, 3.375, 0.375),  # Bb
    (67, 3.75, 0.375),   # B
    (66, 4.125, 0.375),  # Bb
    (62, 4.5, 0.375),    # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F, chromatic approach to Gm7
bass_notes = [
    (48, 4.5, 0.375),   # G (root)
    (50, 4.875, 0.375), # A (chromatic approach to Ab)
    (49, 5.25, 0.375),  # Ab (target)
    (48, 5.625, 0.375), # G (chromatic approach to F)
    (45, 6.0, 0.375),   # F (target)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on bar 4
piano_notes = [
    # G7 on beat 2
    (58, 4.875, 0.375),  # G
    (60, 4.875, 0.375),  # Bb
    (62, 4.875, 0.375),  # D
    (64, 4.875, 0.375),  # F
    # C7 on beat 4
    (55, 6.0, 0.375),    # C
    (57, 6.0, 0.375),    # E
    (58, 6.0, 0.375),    # G
    (60, 6.0, 0.375),    # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif on bar 4
sax_notes = [
    (62, 4.5, 0.375),   # G
    (66, 4.875, 0.375),  # Bb
    (67, 5.25, 0.375),   # B
    (66, 5.625, 0.375),  # Bb
    (62, 6.0, 0.375),    # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_bar = bar * 1.5
    # Kick on beat 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar, end=start_bar + 1.0))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar + 1.5, end=start_bar + 2.5))
    # Snare on beat 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_bar + 0.5, end=start_bar + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_bar + 2.0, end=start_bar + 3.0))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_bar + i * 0.5, end=start_bar + i * 0.5 + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
