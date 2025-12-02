
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),    # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1 & 2
    (42, 0.375, 0.375),
    (38, 0.75, 0.75),   # Snare on 2
    (42, 0.75, 0.375),  # Hihat on 2 & 3
    (42, 1.125, 0.375),
    (36, 1.5, 0.75),    # Kick on 3
    (42, 1.5, 0.375),   # Hihat on 3 & 4
    (42, 1.875, 0.375),
    (38, 2.25, 0.75)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),   # C (1)
    (61, 1.875, 0.375), # C# (2)
    (62, 2.25, 0.375),  # D (3)
    (63, 2.625, 0.375), # D# (4)
    (64, 3.0, 0.375),   # E (1)
    (65, 3.375, 0.375), # F (2)
    (66, 3.75, 0.375),  # F# (3)
    (67, 4.125, 0.375), # G (4)
    (68, 4.5, 0.375),   # G# (1)
    (69, 4.875, 0.375), # A (2)
    (70, 5.25, 0.375),  # A# (3)
    (71, 5.625, 0.375)  # B (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (71, 1.5, 0.375),   # B (C7)
    (74, 1.5, 0.375),   # E
    (60, 1.5, 0.375),   # C
    (64, 1.5, 0.375),   # E
    (67, 1.875, 0.375), # G
    (71, 1.875, 0.375), # B
    (64, 1.875, 0.375), # E
    (67, 1.875, 0.375), # G
    # Bar 3
    (62, 2.25, 0.375),  # D (D7)
    (67, 2.25, 0.375),  # G
    (60, 2.25, 0.375),  # C
    (65, 2.25, 0.375),  # F
    (69, 2.625, 0.375), # A
    (72, 2.625, 0.375), # C
    (65, 2.625, 0.375), # F
    (69, 2.625, 0.375), # A
    # Bar 4
    (67, 3.0, 0.375),   # G (G7)
    (71, 3.0, 0.375),   # B
    (60, 3.0, 0.375),   # C
    (64, 3.0, 0.375),   # E
    (72, 3.375, 0.375), # C
    (76, 3.375, 0.375), # F
    (64, 3.375, 0.375), # E
    (72, 3.375, 0.375), # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Dante: short motif, make it sing
sax_notes = [
    (62, 1.5, 0.375),   # D (start motif)
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D (repeat motif)
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.75))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
