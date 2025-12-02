
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375), # F#
    (44, 2.25, 0.375),  # E
    (45, 2.625, 0.375), # F
    (47, 2.625, 0.375), # G
    (48, 3.0, 0.375),   # G#
    (47, 3.375, 0.375), # G
    (45, 3.75, 0.375),  # F
    (46, 4.125, 0.375), # F#
    (44, 4.5, 0.375),   # E
    (45, 4.875, 0.375), # F
    (47, 5.25, 0.375),  # G
    (48, 5.625, 0.375), # G#
    (47, 6.0, 0.375)    # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.5, 0.1875), # F7 (C, E, G, Bb)
    (53, 1.5, 0.1875),
    (55, 1.5, 0.1875),
    (57, 1.5, 0.1875),
    # Bar 3
    (50, 2.25, 0.1875), # F7
    (53, 2.25, 0.1875),
    (55, 2.25, 0.1875),
    (57, 2.25, 0.1875),
    # Bar 4
    (50, 3.0, 0.1875), # F7
    (53, 3.0, 0.1875),
    (55, 3.0, 0.1875),
    (57, 3.0, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Sax: Motif - F (66), G (67), A (69), back to F (66)
sax_notes = [
    (66, 1.5, 0.375),
    (67, 1.875, 0.375),
    (69, 2.25, 0.375),
    (66, 2.625, 0.375), # End of Bar 2
    (66, 3.0, 0.375), # Start of Bar 3
    (67, 3.375, 0.375),
    (69, 3.75, 0.375),
    (66, 4.125, 0.375), # End of Bar 3
    (66, 4.5, 0.375), # Start of Bar 4
    (67, 4.875, 0.375),
    (69, 5.25, 0.375),
    (66, 5.625, 0.375)  # End of Bar 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
