
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

# Drums: Bar 1
drum_notes = [
    (36, 0.0, 1.0),   # Kick on beat 1
    (42, 0.0, 1.0),   # Hihat on beat 1
    (36, 1.125, 1.0), # Kick on beat 3
    (42, 1.125, 1.0)  # Hihat on beat 3
]
for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    (59, 1.5, 0.375),    # E♭ (Fm7)
    (60, 1.875, 0.375),  # F (root)
    (62, 2.25, 0.375),   # G (chromatic)
    (60, 2.625, 0.375),  # F (restatement)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Walking line with chromatic approach
bass_notes = [
    (53, 1.5, 0.375),    # A♭ (Fm7)
    (55, 1.875, 0.375),  # B♭ (chromatic)
    (57, 2.25, 0.375),   # C (Fm7)
    (59, 2.625, 0.375),  # D♭ (chromatic)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375),  # F (Fm7)
    (64, 1.875, 0.375),  # A♭ (Fm7)
    (67, 1.875, 0.375),  # C (Fm7)
    (70, 1.875, 0.375),  # D (Fm7)

    (60, 2.625, 0.375),  # F (Fm7)
    (64, 2.625, 0.375),  # A♭ (Fm7)
    (67, 2.625, 0.375),  # C (Fm7)
    (70, 2.625, 0.375),  # D (Fm7)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 1.0),     # Kick on beat 1
    (38, 1.5, 1.0),     # Snare on beat 1
    (42, 1.5, 1.0),     # Hihat on beat 1
    (36, 2.25, 1.0),    # Kick on beat 3
    (38, 2.25, 1.0),    # Snare on beat 3
    (42, 2.25, 1.0),    # Hihat on beat 3
]
for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif with a slight variation
sax_notes = [
    (62, 3.0, 0.375),    # G
    (64, 3.375, 0.375),  # A♭
    (62, 3.75, 0.375),   # G
    (60, 4.125, 0.375),  # F
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Chromatic walking
bass_notes = [
    (60, 3.0, 0.375),    # F (Fm7)
    (61, 3.375, 0.375),  # F♯ (chromatic)
    (59, 3.75, 0.375),   # E♭ (chromatic)
    (57, 4.125, 0.375),  # D (Fm7)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 3.375, 0.375),  # F (Fm7)
    (64, 3.375, 0.375),  # A♭ (Fm7)
    (67, 3.375, 0.375),  # C (Fm7)
    (70, 3.375, 0.375),  # D (Fm7)

    (60, 4.125, 0.375),  # F (Fm7)
    (64, 4.125, 0.375),  # A♭ (Fm7)
    (67, 4.125, 0.375),  # C (Fm7)
    (70, 4.125, 0.375),  # D (Fm7)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 1.0),     # Kick on beat 1
    (38, 3.0, 1.0),     # Snare on beat 1
    (42, 3.0, 1.0),     # Hihat on beat 1
    (36, 3.75, 1.0),    # Kick on beat 3
    (38, 3.75, 1.0),    # Snare on beat 3
    (42, 3.75, 1.0),    # Hihat on beat 3
]
for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a rest and a glimmer
sax_notes = [
    (60, 4.5, 0.375),    # F (end on the root)
    (62, 4.875, 0.375),  # G (final chromatic touch)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bass: Final chromatic resolution
bass_notes = [
    (57, 4.5, 0.375),    # D (Fm7)
    (59, 4.875, 0.375),  # E♭ (Fm7)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: Final 7th chord on 2 and 4
piano_notes = [
    (60, 4.875, 0.375),  # F (Fm7)
    (64, 4.875, 0.375),  # A♭ (Fm7)
    (67, 4.875, 0.375),  # C (Fm7)
    (70, 4.875, 0.375),  # D (Fm7)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 1.0),     # Kick on beat 1
    (38, 4.5, 1.0),     # Snare on beat 1
    (42, 4.5, 1.0),     # Hihat on beat 1
    (36, 5.25, 1.0),    # Kick on beat 3
    (38, 5.25, 1.0),    # Snare on beat 3
    (42, 5.25, 1.0),    # Hihat on beat 3
]
for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
