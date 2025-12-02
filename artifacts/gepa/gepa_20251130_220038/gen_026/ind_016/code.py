
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
# Bass: walking line, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375),  # F# (F7 chord)
    (38, 1.875, 0.375),  # G (F7)
    (40, 2.25, 0.375),  # A (F7)
    (39, 2.625, 0.375)   # Ab (chromatic approach to A)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: comp on 2 and 4, 7th chords
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    (71, 1.5, 0.375),  # F
    (74, 1.5, 0.375),  # A
    (76, 1.5, 0.375),  # C
    (70, 1.5, 0.375),  # E♭

    # Bar 3: C7 (C, E, G, B♭)
    (76, 2.25, 0.375),  # C
    (79, 2.25, 0.375),  # E
    (81, 2.25, 0.375),  # G
    (77, 2.25, 0.375),  # B♭

    # Bar 4: A7 (A, C#, E, G)
    (77, 3.0, 0.375),  # A
    (81, 3.0, 0.375),  # C#
    (83, 3.0, 0.375),  # E
    (80, 3.0, 0.375)   # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif - start in the middle, leave it hanging
sax_notes = [
    (67, 1.5, 0.375),  # D (F7 chord)
    (69, 1.875, 0.375),  # E (F7)
    (71, 2.25, 0.375),  # F (C7)
    (73, 2.625, 0.375)   # G (A7)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Drums (3.0 - 4.5s)
for i in range(3):
    start = 3.0 + i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))  # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375))  # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))  # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375))  # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))  # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375))  # Hihat on 4

# Bar 4: Drums (4.5 - 6.0s)
for i in range(3):
    start = 4.5 + i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))  # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375))  # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))  # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375))  # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))  # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375))  # Hihat on 4

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
