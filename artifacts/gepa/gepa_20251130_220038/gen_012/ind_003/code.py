
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (36, 1.5, 0.375),    # C
    (37, 1.875, 0.375),  # C#
    (38, 2.25, 0.375),   # D
    (40, 2.625, 0.375),  # D#
    (41, 2.875, 0.375),  # E
    (43, 3.25, 0.375),   # F#
    (44, 3.625, 0.375),  # G
    (46, 4.0, 0.375),    # G#
    (47, 4.375, 0.375),  # A
    (49, 4.75, 0.375),   # A#
    (50, 5.125, 0.375),  # B
    (52, 5.5, 0.375)     # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 & 4
piano_notes = [
    (44, 1.875, 0.375),  # G7 (G, B, D, F)
    (46, 1.875, 0.375),
    (48, 1.875, 0.375),
    (50, 1.875, 0.375),
    (44, 2.625, 0.375),  # G7
    (46, 2.625, 0.375),
    (48, 2.625, 0.375),
    (50, 2.625, 0.375),
    (48, 3.625, 0.375),  # B7 (B, D#, F#, A)
    (50, 3.625, 0.375),
    (52, 3.625, 0.375),
    (54, 3.625, 0.375),
    (48, 4.625, 0.375),  # B7
    (50, 4.625, 0.375),
    (52, 4.625, 0.375),
    (54, 4.625, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 & 3, snare on 2 & 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Saxophone (Dante) - 4-bar motif
sax_notes = [
    (46, 1.5, 0.375),   # A
    (48, 1.875, 0.375), # B
    (46, 2.25, 0.375),  # A
    (44, 2.625, 0.375), # G
    (46, 2.625, 0.375), # A (repeat G)
    (48, 3.0, 0.375),   # B
    (46, 3.375, 0.375), # A
    (44, 3.75, 0.375),  # G
    (45, 4.125, 0.375), # G#
    (47, 4.5, 0.375),   # A
    (45, 4.875, 0.375), # G#
    (47, 5.25, 0.375)   # A
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
