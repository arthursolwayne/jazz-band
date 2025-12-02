
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
    (42, 0.1875, 0.1875), # Hihat on 1 &
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),# Hihat on 2 &
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.9375, 0.1875),# Hihat on 3 &
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (53, 1.5, 0.375),    # F (root)
    (51, 1.875, 0.375),  # D (chromatic approach to Eb)
    (55, 2.25, 0.375),   # G (5th)
    (50, 2.625, 0.375),  # C (chromatic approach to Bb)
    (53, 2.999, 0.375),  # F
    (51, 3.374, 0.375),  # D
    (55, 3.749, 0.375),  # G
    (50, 4.124, 0.375),  # C
    (53, 4.499, 0.375),  # F
    (51, 4.874, 0.375),  # D
    (55, 5.249, 0.375),  # G
    (50, 5.624, 0.375)   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (47, 1.875, 0.375),  # Bb7 (Bb, D, F, Ab)
    (49, 1.875, 0.375),
    (50, 1.875, 0.375),
    (53, 1.875, 0.375),
    # Bar 3
    (47, 3.375, 0.375),  # Bb7
    (49, 3.375, 0.375),
    (50, 3.375, 0.375),
    (53, 3.375, 0.375),
    # Bar 4
    (47, 4.875, 0.375),  # Bb7
    (49, 4.875, 0.375),
    (50, 4.875, 0.375),
    (53, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 8):
        start_time = start + (i * 0.1875)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.1875))

# Sax: Your motif, one short phrase, make it sing
# Start with F (53) on beat 1 of bar 2
sax_notes = [
    (53, 1.5, 0.375),    # F
    (55, 1.875, 0.375),  # G
    (53, 2.25, 0.375),   # F
    (50, 2.625, 0.375),  # C
    (53, 2.999, 0.375),  # F
    (55, 3.374, 0.375),  # G
    (53, 3.749, 0.375),  # F
    (50, 4.124, 0.375),  # C
    (53, 4.499, 0.375),  # F
    (55, 4.874, 0.375),  # G
    (53, 5.249, 0.375),  # F
    (50, 5.624, 0.375)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
