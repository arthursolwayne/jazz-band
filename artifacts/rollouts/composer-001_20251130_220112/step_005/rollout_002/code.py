
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
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.125, 0.875), # Hihat on 1 & 2
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.625, 0.875), # Hihat on 2 & 3
    (36, 1.0, 1.5),     # Kick on 3
    (42, 1.125, 1.375), # Hihat on 3 & 4
    (38, 1.5, 1.5),     # Snare on 4
    (42, 1.625, 1.875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# F7 (F, A, C, E) - key is F
bass_notes = [
    (53, 1.5, 1.75),    # D (chromatic approach to Eb)
    (55, 1.75, 2.0),    # Eb
    (57, 2.0, 2.25),    # F
    (59, 2.25, 2.5),    # G
    (57, 2.5, 2.75),    # F
    (55, 2.75, 3.0),    # Eb
    (53, 3.0, 3.25),    # D
    (52, 3.25, 3.5),    # C
    (53, 3.5, 3.75),    # D
    (55, 3.75, 4.0),    # Eb
    (57, 4.0, 4.25),    # F
    (59, 4.25, 4.5),    # G
    (57, 4.5, 4.75),    # F
    (55, 4.75, 5.0),    # Eb
    (53, 5.0, 5.25),    # D
    (52, 5.25, 5.5),    # C
    (53, 5.5, 5.75),    # D
    (55, 5.75, 6.0)     # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
# F7 = F, A, C, E
piano_notes = [
    (53, 1.75, 2.0),    # F7 on 2
    (58, 1.75, 2.0),
    (60, 1.75, 2.0),
    (64, 1.75, 2.0),
    (53, 2.75, 3.0),    # F7 on 4
    (58, 2.75, 3.0),
    (60, 2.75, 3.0),
    (64, 2.75, 3.0),
    (53, 3.75, 4.0),    # F7 on 2
    (58, 3.75, 4.0),
    (60, 3.75, 4.0),
    (64, 3.75, 4.0),
    (53, 4.75, 5.0),    # F7 on 4
    (58, 4.75, 5.0),
    (60, 4.75, 5.0),
    (64, 4.75, 5.0)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, Ab, F (with some rhythmic space)
sax_notes = [
    (53, 1.5, 1.625),   # F
    (55, 1.625, 1.75),  # G
    (57, 1.75, 1.875),  # Ab
    (53, 1.875, 2.0),   # F
    (53, 2.5, 2.625),   # F
    (55, 2.625, 2.75),  # G
    (57, 2.75, 2.875),  # Ab
    (53, 2.875, 3.0)    # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Bar 2
    drum_notes = [
        (36, start + 0.0, 1.0),     # Kick on 1
        (42, start + 0.125, 0.875), # Hihat on 1 & 2
        (38, start + 0.5, 1.0),     # Snare on 2
        (42, start + 0.625, 0.875), # Hihat on 2 & 3
        (36, start + 1.0, 1.5),     # Kick on 3
        (42, start + 1.125, 1.375), # Hihat on 3 & 4
        (38, start + 1.5, 1.5),     # Snare on 4
        (42, start + 1.625, 1.875)  # Hihat on 4
    ]
    for note, start_t, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_t, end=start_t + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
