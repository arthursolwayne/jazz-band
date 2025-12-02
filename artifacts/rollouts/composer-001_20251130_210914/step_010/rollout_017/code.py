
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.125, 0.25),  # Hihat on 1&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.875, 0.25),  # Hihat on 3&
    (38, 1.125, 0.375), # Snare on 2
    (42, 1.25, 0.25),   # Hihat on 2&
    (38, 1.75, 0.375),  # Snare on 4
    (42, 1.875, 0.25)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (45, 1.5, 0.375),   # F
    (46, 1.875, 0.375), # Gb
    (47, 2.25, 0.375),  # G
    (45, 2.625, 0.375), # F
    # Bar 3
    (47, 3.0, 0.375),   # G
    (49, 3.375, 0.375), # A
    (48, 3.75, 0.375),  # Ab
    (46, 4.125, 0.375), # Gb
    # Bar 4
    (46, 4.5, 0.375),   # Gb
    (45, 4.875, 0.375), # F
    (47, 5.25, 0.375),  # G
    (48, 5.625, 0.375)  # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.375),  # F7 (F, A, C, Eb)
    (52, 1.875, 0.375),
    (55, 1.875, 0.375),
    (57, 1.875, 0.375),
    # Bar 3
    (50, 3.375, 0.375),  # F7
    (52, 3.375, 0.375),
    (55, 3.375, 0.375),
    (57, 3.375, 0.375),
    # Bar 4
    (50, 4.875, 0.375),  # F7
    (52, 4.875, 0.375),
    (55, 4.875, 0.375),
    (57, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.5),     # F (start of motif)
    (65, 2.0, 0.5),     # A (middle of motif)
    (64, 2.5, 0.5),     # G (hanging note)
    (62, 3.0, 0.5),     # F (return)
    (65, 3.5, 0.5),     # A
    (67, 4.0, 0.5),     # Bb
    (65, 4.5, 0.5),     # A
    (62, 5.0, 0.5)      # F (finish)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.125, end=start + 0.25))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on 2&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.875, end=start + 1.0))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Hihat on 3&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.25, end=start + 1.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25))
    # Hihat on 4&
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
