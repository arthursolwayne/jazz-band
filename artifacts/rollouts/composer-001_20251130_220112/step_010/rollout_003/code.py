
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

# Drums - Bar 1
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2 (Walking line, chromatic approaches)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375)  # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Bar 2 (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 (D, F#, A, C)
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # F#
    (69, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # C
    # D7 again on beat 4
    (62, 2.625, 0.375),  # D
    (67, 2.625, 0.375),  # F#
    (69, 2.625, 0.375),  # A
    (64, 2.625, 0.375)   # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 2 (Melody - First part of motif)
sax_notes = [
    (65, 1.5, 0.375),  # E
    (67, 1.875, 0.375),  # F#
    (69, 2.25, 0.375),  # A
    (67, 2.625, 0.375)   # F#
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (Walking line, chromatic approaches)
bass_notes = [
    (65, 3.0, 0.375),  # F
    (66, 3.375, 0.375),  # F#
    (67, 3.75, 0.375),  # G
    (69, 4.125, 0.375)  # A
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Bar 3 (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 (D, F#, A, C)
    (62, 3.0, 0.375),  # D
    (67, 3.0, 0.375),  # F#
    (69, 3.0, 0.375),  # A
    (64, 3.0, 0.375),  # C
    # D7 again on beat 4
    (62, 4.125, 0.375),  # D
    (67, 4.125, 0.375),  # F#
    (69, 4.125, 0.375),  # A
    (64, 4.125, 0.375)   # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 3 (Melody - Second part of motif, leave it hanging)
sax_notes = [
    (65, 3.0, 0.375),  # E
    (67, 3.375, 0.375),  # F#
    (69, 3.75, 0.375),  # A
    (67, 4.125, 0.375)   # F#
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (Walking line, chromatic approaches)
bass_notes = [
    (69, 4.5, 0.375),  # A
    (71, 4.875, 0.375),  # B
    (72, 5.25, 0.375),  # C
    (74, 5.625, 0.375)  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Bar 4 (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 (D, F#, A, C)
    (62, 4.5, 0.375),  # D
    (67, 4.5, 0.375),  # F#
    (69, 4.5, 0.375),  # A
    (64, 4.5, 0.375),  # C
    # D7 again on beat 4
    (62, 5.625, 0.375),  # D
    (67, 5.625, 0.375),  # F#
    (69, 5.625, 0.375),  # A
    (64, 5.625, 0.375)   # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums - Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Bar 4 (Melody - Return to start of motif, finish it)
sax_notes = [
    (65, 4.5, 0.375),  # E
    (67, 4.875, 0.375),  # F#
    (69, 5.25, 0.375),  # A
    (67, 5.625, 0.375)   # F#
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
