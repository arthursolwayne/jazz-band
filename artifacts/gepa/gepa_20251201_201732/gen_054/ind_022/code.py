
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 1.0),     # Kick on beat 1
    (38, 0.5, 0.5),     # Snare on beat 2
    (42, 0.0, 1.0),     # Hihat on every eighth
    (42, 0.25, 0.25),
    (42, 0.5, 0.25),
    (42, 0.75, 0.25),
    (36, 1.0, 0.5),     # Kick on beat 3
    (38, 1.5, 0.5),     # Snare on beat 4
    (42, 1.0, 0.5),     # Hihat on beat 3 and 4
    (42, 1.25, 0.25),
    (42, 1.5, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2: Walking line with chromatic approach
bass_notes = [
    (62, 1.5, 0.375),  # D2 (root)
    (63, 1.875, 0.375),# Eb2 (chromatic approach)
    (60, 2.25, 0.375), # C2 (fifth)
    (62, 2.625, 0.375) # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Bar 2: Open voicing, Dm7
piano_notes = [
    (62, 1.5, 0.375),  # D2
    (67, 1.5, 0.375),  # G3
    (71, 1.5, 0.375),  # Bb4
    (74, 1.5, 0.375)   # D5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 2: Motif starts (haunting, incomplete)
sax_notes = [
    (65, 1.5, 0.25),   # Bb3
    (67, 1.75, 0.25),  # D4
    (65, 2.0, 0.25),   # Bb3
    (67, 2.25, 0.25)   # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3: Walking line with chromatic approach
bass_notes = [
    (64, 3.0, 0.375),  # Eb2
    (62, 3.375, 0.375),# D2 (chromatic approach)
    (60, 3.75, 0.375), # C2 (fifth)
    (62, 4.125, 0.375) # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Bar 3: Open voicing, Gm7
piano_notes = [
    (67, 3.0, 0.375),  # G3
    (71, 3.0, 0.375),  # Bb4
    (74, 3.0, 0.375),  # D5
    (76, 3.0, 0.375)   # F5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 3: Motif continues (haunting, incomplete)
sax_notes = [
    (67, 3.0, 0.25),   # D4
    (69, 3.25, 0.25),  # F4
    (67, 3.5, 0.25),   # D4
    (69, 3.75, 0.25)   # F4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4: Walking line with chromatic approach
bass_notes = [
    (62, 4.5, 0.375),  # D2
    (64, 4.875, 0.375),# Eb2 (chromatic approach)
    (60, 5.25, 0.375), # C2 (fifth)
    (62, 5.625, 0.375) # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Bar 4: Open voicing, Bb7
piano_notes = [
    (71, 4.5, 0.375),  # Bb4
    (74, 4.5, 0.375),  # D5
    (76, 4.5, 0.375),  # F5
    (79, 4.5, 0.375)   # Ab5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 4: Motif resolves (haunting, incomplete)
sax_notes = [
    (69, 4.5, 0.25),   # F4
    (67, 4.75, 0.25),  # D4
    (65, 5.0, 0.25),   # Bb3
    (67, 5.25, 0.25)   # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums - Bar 3 and 4
# Bar 3
drum_notes = [
    (36, 3.0, 1.0),     # Kick on beat 1
    (38, 3.5, 0.5),     # Snare on beat 2
    (42, 3.0, 1.0),     # Hihat on every eighth
    (42, 3.25, 0.25),
    (42, 3.5, 0.25),
    (42, 3.75, 0.25),
    (36, 4.0, 0.5),     # Kick on beat 3
    (38, 4.5, 0.5),     # Snare on beat 4
    (42, 4.0, 0.5),     # Hihat on beat 3 and 4
    (42, 4.25, 0.25),
    (42, 4.5, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
drum_notes = [
    (36, 4.5, 1.0),     # Kick on beat 1
    (38, 5.0, 0.5),     # Snare on beat 2
    (42, 4.5, 1.0),     # Hihat on every eighth
    (42, 4.75, 0.25),
    (42, 5.0, 0.25),
    (42, 5.25, 0.25),
    (36, 5.5, 0.5),     # Kick on beat 3
    (38, 6.0, 0.5),     # Snare on beat 4
    (42, 5.5, 0.5),     # Hihat on beat 3 and 4
    (42, 5.75, 0.25),
    (42, 6.0, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
