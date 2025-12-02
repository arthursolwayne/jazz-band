
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 &
    (42, 0.1875, 0.1875),# Hihat on 2 &
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 &
    (42, 0.5625, 0.1875),# Hihat on 3 &
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 &
    (42, 0.9375, 0.1875),# Hihat on 4 &
    (38, 1.125, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (Walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    (37, 1.5, 0.375),  # F -> E
    (36, 1.875, 0.375), # E -> D
    (34, 2.25, 0.375),  # D -> C
    (35, 2.625, 0.375), # C -> Db
    # Bar 3
    (36, 3.0, 0.375),  # Db -> C
    (38, 3.375, 0.375), # C -> D
    (39, 3.75, 0.375),  # D -> E
    (40, 4.125, 0.375), # E -> F
    # Bar 4
    (41, 4.5, 0.375),  # F -> G
    (40, 4.875, 0.375), # G -> F
    (39, 5.25, 0.375),  # F -> E
    (38, 5.625, 0.375)  # E -> D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (43, 1.875, 0.375),  # F7 on 2
    (45, 1.875, 0.375),
    (47, 1.875, 0.375),
    (50, 1.875, 0.375),
    (43, 3.0, 0.375),    # F7 on 4
    (45, 3.0, 0.375),
    (47, 3.0, 0.375),
    (50, 3.0, 0.375),
    # Bar 3
    (43, 3.375, 0.375),  # F7 on 2
    (45, 3.375, 0.375),
    (47, 3.375, 0.375),
    (50, 3.375, 0.375),
    (43, 4.5, 0.375),    # F7 on 4
    (45, 4.5, 0.375),
    (47, 4.5, 0.375),
    (50, 4.5, 0.375),
    # Bar 4
    (43, 4.875, 0.375),  # F7 on 2
    (45, 4.875, 0.375),
    (47, 4.875, 0.375),
    (50, 4.875, 0.375),
    (43, 6.0, 0.375),    # F7 on 4
    (45, 6.0, 0.375),
    (47, 6.0, 0.375),
    (50, 6.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante (Melody: One short motif, make it sing)
sax_notes = [
    # Bar 2
    (50, 1.5, 0.375),    # F
    (52, 1.875, 0.375),  # G
    (50, 2.25, 0.375),   # F
    (48, 2.625, 0.375),  # E
    # Bar 3
    (50, 3.0, 0.375),    # F
    (52, 3.375, 0.375),  # G
    (50, 3.75, 0.375),   # F
    (48, 4.125, 0.375),  # E
    # Bar 4
    (50, 4.5, 0.375),    # F
    (52, 4.875, 0.375),  # G
    (50, 5.25, 0.375),   # F
    (48, 5.625, 0.375)   # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.5, end=start_time + 1.5 + 0.375))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.75 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 1.875 + 0.375))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
