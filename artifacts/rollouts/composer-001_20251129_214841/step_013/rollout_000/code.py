
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.375, 0.1875),
    (42, 0.75, 0.1875),
    (42, 1.125, 0.1875),
    (36, 1.5, 0.375),  # Kick on beat 3
    (38, 1.875, 0.375), # Snare on beat 4
    (42, 1.5, 0.1875), # Hihat on 3 & 4
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5, 0.375),  # C
    (65, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # G
    (65, 2.625, 0.375), # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking line with chromatic approaches)
bass_notes = [
    (48, 1.5, 0.375),  # C
    (49, 1.875, 0.375), # C#
    (50, 2.25, 0.375),  # D
    (51, 2.625, 0.375), # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 1.875, 0.375),  # C7 (C, E, Bb)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (60, 2.625, 0.375),  # C7 again
    (64, 2.625, 0.375),
    (67, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),  # Kick on beat 1
    (38, 1.875, 0.375), # Snare on beat 2
    (42, 1.5, 0.1875), # Hihat on 1 & 2
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (36, 2.25, 0.375),  # Kick on beat 3
    (38, 2.625, 0.375), # Snare on beat 4
    (42, 2.25, 0.1875), # Hihat on 3 & 4
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continues
sax_notes = [
    (62, 3.0, 0.375),  # C
    (65, 3.375, 0.375), # E
    (67, 3.75, 0.375),  # G
    (65, 4.125, 0.375), # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking line with chromatic approaches)
bass_notes = [
    (52, 3.0, 0.375),  # E
    (53, 3.375, 0.375), # F
    (55, 3.75, 0.375),  # G
    (57, 4.125, 0.375), # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 3.375, 0.375),  # C7 (C, E, Bb)
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (60, 4.125, 0.375),  # C7 again
    (64, 4.125, 0.375),
    (67, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),  # Kick on beat 1
    (38, 3.375, 0.375), # Snare on beat 2
    (42, 3.0, 0.1875), # Hihat on 1 & 2
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (36, 3.75, 0.375),  # Kick on beat 3
    (38, 4.125, 0.375), # Snare on beat 4
    (42, 3.75, 0.1875), # Hihat on 3 & 4
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody concludes with resolution
sax_notes = [
    (62, 4.5, 0.375),  # C
    (65, 4.875, 0.375), # E
    (67, 5.25, 0.375),  # G
    (62, 5.625, 0.375), # C (resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking line with chromatic approaches)
bass_notes = [
    (58, 4.5, 0.375),  # Bb
    (59, 4.875, 0.375), # B
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375), # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 4.875, 0.375),  # C7 (C, E, Bb)
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (60, 5.625, 0.375),  # C7 again
    (64, 5.625, 0.375),
    (67, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),  # Kick on beat 1
    (38, 4.875, 0.375), # Snare on beat 2
    (42, 4.5, 0.1875), # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (36, 5.25, 0.375),  # Kick on beat 3
    (38, 5.625, 0.375), # Snare on beat 4
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
