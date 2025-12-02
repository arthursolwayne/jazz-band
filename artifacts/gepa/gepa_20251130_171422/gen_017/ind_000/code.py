
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
    (42, 0.0, 0.1875),   # Hihat on 1& 
    (42, 0.1875, 0.1875),# Hihat on 2
    (38, 0.375, 0.375),  # Snare on 3
    (42, 0.375, 0.1875), # Hihat on 3&
    (42, 0.5625, 0.1875),# Hihat on 4
    (36, 0.75, 0.375),   # Kick on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking line in F)
bass_notes = [
    (45, 1.5, 0.375),    # F
    (46, 1.875, 0.375),  # G
    (47, 2.25, 0.375),   # A
    (44, 2.625, 0.375),  # E
    (45, 2.625, 0.375),  # F
    (46, 3.0, 0.375),    # G
    (47, 3.375, 0.375),  # A
    (44, 3.75, 0.375),   # E
    (45, 3.75, 0.375),   # F
    (46, 4.125, 0.375),  # G
    (47, 4.5, 0.375),    # A
    (44, 4.875, 0.375),  # E
    (45, 4.875, 0.375),  # F
    (46, 5.25, 0.375),   # G
    (47, 5.625, 0.375),  # A
    (44, 6.0, 0.375)     # E
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.5, 0.375),    # F7: F, A, C, Eb
    (53, 1.5, 0.375),
    (55, 1.5, 0.375),
    (57, 1.5, 0.375),
    # Bar 3
    (50, 3.0, 0.375),
    (53, 3.0, 0.375),
    (55, 3.0, 0.375),
    (57, 3.0, 0.375),
    # Bar 4
    (50, 4.5, 0.375),
    (53, 4.5, 0.375),
    (55, 4.5, 0.375),
    (57, 4.5, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625))
    # Hihat on every eighth
    for i in range(0, 8):
        start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.1875))

# Sax: Motif in F
sax_notes = [
    # Bar 2
    (50, 1.5, 0.375),    # F
    (53, 1.875, 0.375),  # A
    (55, 2.25, 0.375),   # C
    (50, 2.625, 0.375),  # F
    # Bar 3
    (53, 3.0, 0.375),    # A
    (57, 3.375, 0.375),  # E
    (55, 3.75, 0.375),   # C
    (50, 4.125, 0.375),  # F
    # Bar 4
    (53, 4.5, 0.375),    # A
    (57, 4.875, 0.375),  # E
    (55, 5.25, 0.375),   # C
    (50, 5.625, 0.375)   # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
