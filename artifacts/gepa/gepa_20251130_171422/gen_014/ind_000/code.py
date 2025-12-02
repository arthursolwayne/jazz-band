
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    (31, 1.5, 0.375),    # Fm7 root
    (33, 1.875, 0.375),  # b9
    (30, 2.25, 0.375),   # E
    (32, 2.625, 0.375),  # b7

    # Bar 3
    (31, 3.0, 0.375),    # Fm7 root
    (34, 3.375, 0.375),  # 11
    (30, 3.75, 0.375),   # E
    (32, 4.125, 0.375),  # b7

    # Bar 4
    (31, 4.5, 0.375),    # Fm7 root
    (33, 4.875, 0.375),  # b9
    (30, 5.25, 0.375),   # E
    (32, 5.625, 0.375),  # b7
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    (39, 1.875, 0.375),  # B7
    (43, 1.875, 0.375),
    (47, 1.875, 0.375),
    (50, 1.875, 0.375),

    # Bar 3
    (39, 3.375, 0.375),  # B7
    (43, 3.375, 0.375),
    (47, 3.375, 0.375),
    (50, 3.375, 0.375),

    # Bar 4
    (39, 4.875, 0.375),  # B7
    (43, 4.875, 0.375),
    (47, 4.875, 0.375),
    (50, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    for i in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + i * 0.375, end=start + i * 0.375 + 0.375))
    # Snare on 2 and 4
    for i in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + i * 0.375, end=start + i * 0.375 + 0.375))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Sax: Dante
sax_notes = [
    (42, 1.5, 0.375),    # Fm7 root
    (44, 1.875, 0.375),  # b9
    (40, 2.25, 0.375),   # E
    (42, 2.625, 0.375),  # Fm7 root

    (40, 3.0, 0.375),    # E
    (42, 3.375, 0.375),  # Fm7 root
    (44, 3.75, 0.375),   # b9
    (40, 4.125, 0.375),  # E

    (42, 4.5, 0.375),    # Fm7 root
    (44, 4.875, 0.375),  # b9
    (40, 5.25, 0.375),   # E
    (42, 5.625, 0.375),  # Fm7 root
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
