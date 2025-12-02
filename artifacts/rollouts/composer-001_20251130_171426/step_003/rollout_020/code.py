
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.1875), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.1875), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875)   # Hihat on 4 (end of bar)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (24, 1.5, 0.375),   # F
    (25, 1.875, 0.375), # Gb
    (23, 2.25, 0.375),  # E
    (22, 2.625, 0.375), # D
    (24, 2.625, 0.375), # F
    (25, 2.625, 0.375), # Gb
    (23, 2.625, 0.375), # E
    (22, 2.625, 0.375), # D
    (24, 3.0, 0.375),   # F
    (25, 3.375, 0.375), # Gb
    (23, 3.75, 0.375),  # E
    (22, 4.125, 0.375), # D
    (24, 4.125, 0.375), # F
    (25, 4.125, 0.375), # Gb
    (23, 4.125, 0.375), # E
    (22, 4.125, 0.375), # D
    (24, 4.5, 0.375),   # F
    (25, 4.875, 0.375), # Gb
    (23, 5.25, 0.375),  # E
    (22, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (22, 1.5, 0.1875), # F7 - Bb
    (29, 1.5, 0.1875), # F7 - E
    (26, 1.5, 0.1875), # F7 - Ab
    (24, 1.5, 0.1875), # F7 - F
    (22, 1.875, 0.1875), # F7 - Bb
    (29, 1.875, 0.1875), # F7 - E
    (26, 1.875, 0.1875), # F7 - Ab
    (24, 1.875, 0.1875), # F7 - F
    (22, 2.25, 0.1875), # F7 - Bb
    (29, 2.25, 0.1875), # F7 - E
    (26, 2.25, 0.1875), # F7 - Ab
    (24, 2.25, 0.1875), # F7 - F
    (22, 2.625, 0.1875), # F7 - Bb
    (29, 2.625, 0.1875), # F7 - E
    (26, 2.625, 0.1875), # F7 - Ab
    (24, 2.625, 0.1875), # F7 - F
    (22, 3.0, 0.1875), # F7 - Bb
    (29, 3.0, 0.1875), # F7 - E
    (26, 3.0, 0.1875), # F7 - Ab
    (24, 3.0, 0.1875), # F7 - F
    (22, 3.375, 0.1875), # F7 - Bb
    (29, 3.375, 0.1875), # F7 - E
    (26, 3.375, 0.1875), # F7 - Ab
    (24, 3.375, 0.1875), # F7 - F
    (22, 3.75, 0.1875), # F7 - Bb
    (29, 3.75, 0.1875), # F7 - E
    (26, 3.75, 0.1875), # F7 - Ab
    (24, 3.75, 0.1875), # F7 - F
    (22, 4.125, 0.1875), # F7 - Bb
    (29, 4.125, 0.1875), # F7 - E
    (26, 4.125, 0.1875), # F7 - Ab
    (24, 4.125, 0.1875), # F7 - F
    (22, 4.5, 0.1875), # F7 - Bb
    (29, 4.5, 0.1875), # F7 - E
    (26, 4.5, 0.1875), # F7 - Ab
    (24, 4.5, 0.1875), # F7 - F
    (22, 4.875, 0.1875), # F7 - Bb
    (29, 4.875, 0.1875), # F7 - E
    (26, 4.875, 0.1875), # F7 - Ab
    (24, 4.875, 0.1875), # F7 - F
    (22, 5.25, 0.1875), # F7 - Bb
    (29, 5.25, 0.1875), # F7 - E
    (26, 5.25, 0.1875), # F7 - Ab
    (24, 5.25, 0.1875), # F7 - F
    (22, 5.625, 0.1875), # F7 - Bb
    (29, 5.625, 0.1875), # F7 - E
    (26, 5.625, 0.1875), # F7 - Ab
    (24, 5.625, 0.1875)  # F7 - F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (24, 1.5, 0.375),   # F
    (26, 1.875, 0.375), # G
    (22, 2.25, 0.375),  # E
    (24, 2.625, 0.375), # F
    (26, 3.0, 0.375),   # G
    (22, 3.375, 0.375), # E
    (24, 3.75, 0.375),  # F
    (26, 4.125, 0.375), # G
    (22, 4.5, 0.375),   # E
    (24, 4.875, 0.375), # F
    (26, 5.25, 0.375),  # G
    (22, 5.625, 0.375)  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.1875))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.1875))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.1875))
    # Hihat on 4 (end of bar)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.5 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
