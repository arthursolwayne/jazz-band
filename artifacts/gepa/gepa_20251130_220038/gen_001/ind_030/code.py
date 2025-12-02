
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
    (38, 0.75, 0.375), # Snare on 2
    (36, 1.125, 0.375),# Kick on 3
    (38, 1.5, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375), # Fm root (Ab) on 1
    (38, 1.875, 0.375), # Bb on 2
    (36, 2.25, 0.375), # G on 3
    (35, 2.625, 0.375), # F on 4
    (34, 2.625, 0.375), # Eb on 4
    (37, 3.0, 0.375), # F on 1
    (38, 3.375, 0.375), # Bb on 2
    (36, 3.75, 0.375), # G on 3
    (35, 4.125, 0.375), # F on 4
    (34, 4.125, 0.375), # Eb on 4
    (37, 4.5, 0.375), # F on 1
    (38, 4.875, 0.375), # Bb on 2
    (36, 5.25, 0.375), # G on 3
    (35, 5.625, 0.375)  # F on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.375), # Bb7 (Bb, D, F, Ab)
    (53, 1.875, 0.375),
    (55, 1.875, 0.375),
    (57, 1.875, 0.375),
    # Bar 3
    (50, 3.375, 0.375), # Bb7 again
    (53, 3.375, 0.375),
    (55, 3.375, 0.375),
    (57, 3.375, 0.375),
    # Bar 4
    (50, 4.875, 0.375), # Bb7 again
    (53, 4.875, 0.375),
    (55, 4.875, 0.375),
    (57, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375),# Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.25, 0.1875),# Hihat on 3
    (38, 2.625, 0.375),# Snare on 4
    (42, 2.625, 0.1875),# Hihat on 4
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375),# Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.75, 0.1875),# Hihat on 3
    (38, 4.125, 0.375),# Snare on 4
    (42, 4.125, 0.1875),# Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375),# Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.25, 0.1875),# Hihat on 3
    (38, 5.625, 0.375),# Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax melody: One short motif, make it sing
sax_notes = [
    (62, 1.5, 0.375), # E (Fm3)
    (64, 1.875, 0.375), # G (Fm5)
    (60, 2.25, 0.375), # D (Fm7)
    (62, 2.625, 0.375), # E (Fm3)
    (67, 3.0, 0.375), # Bb (Fm9)
    (64, 3.375, 0.375), # G (Fm5)
    (60, 3.75, 0.375), # D (Fm7)
    (62, 4.125, 0.375), # E (Fm3)
    (65, 4.5, 0.375), # A (Fm11)
    (64, 4.875, 0.375), # G (Fm5)
    (60, 5.25, 0.375), # D (Fm7)
    (62, 5.625, 0.375)  # E (Fm3)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
