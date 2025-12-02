
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (42, 1.125, 0.1875),# Hihat on 4
    (38, 1.5, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),   # D on 1
    (64, 1.875, 0.375),  # E on 2
    (63, 2.25, 0.375),   # D# on 3
    (62, 2.625, 0.375),  # D on 4
    (60, 3.0, 0.375),    # Bb on 1
    (62, 3.375, 0.375),  # D on 2
    (61, 3.75, 0.375),   # C on 3
    (60, 4.125, 0.375),  # Bb on 4
    (59, 4.5, 0.375),    # A on 1
    (60, 4.875, 0.375),  # Bb on 2
    (58, 5.25, 0.375),   # Ab on 3
    (59, 5.625, 0.375)   # A on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (60, 1.5, 0.1875),  # Bb on 1 (comp on 2)
    (62, 1.875, 0.1875),# D on 2
    (64, 1.875, 0.1875),# E on 2
    (67, 1.875, 0.1875),# G on 2
    (69, 1.875, 0.1875),# Bb on 2
    (60, 2.25, 0.1875), # Bb on 3
    (62, 2.625, 0.1875),# D on 4
    (64, 2.625, 0.1875),# E on 4
    (67, 2.625, 0.1875),# G on 4
    (69, 2.625, 0.1875),# Bb on 4
    # Bar 3 (3.0 - 4.5s)
    (60, 3.0, 0.1875),  # Bb on 1
    (62, 3.375, 0.1875),# D on 2
    (64, 3.375, 0.1875),# E on 2
    (67, 3.375, 0.1875),# G on 2
    (69, 3.375, 0.1875),# Bb on 2
    (60, 3.75, 0.1875), # Bb on 3
    (62, 4.125, 0.1875),# D on 4
    (64, 4.125, 0.1875),# E on 4
    (67, 4.125, 0.1875),# G on 4
    (69, 4.125, 0.1875),# Bb on 4
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.1875),  # Bb on 1
    (62, 4.875, 0.1875),# D on 2
    (64, 4.875, 0.1875),# E on 2
    (67, 4.875, 0.1875),# G on 2
    (69, 4.875, 0.1875),# Bb on 2
    (60, 5.25, 0.1875), # Bb on 3
    (62, 5.625, 0.1875),# D on 4
    (64, 5.625, 0.1875),# E on 4
    (67, 5.625, 0.1875),# G on 4
    (69, 5.625, 0.1875) # Bb on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm motif: D, F, G, Bb (Dm7) with a chromatic passing tone
sax_notes = [
    (62, 1.5, 0.375),   # D on 1
    (64, 1.875, 0.375), # F on 2
    (65, 2.25, 0.375),  # G on 3
    (69, 2.625, 0.375), # Bb on 4
    (62, 3.0, 0.375),   # D on 1 (repeat)
    (64, 3.375, 0.375), # F on 2
    (65, 3.75, 0.375),  # G on 3
    (69, 4.125, 0.375), # Bb on 4
    (62, 4.5, 0.375),   # D on 1 (third time)
    (64, 4.875, 0.375), # F on 2
    (65, 5.25, 0.375),  # G on 3
    (69, 5.625, 0.375)  # Bb on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875),# Hihat on 2
    (42, 1.875, 0.1875),# Hihat on 3
    (42, 2.0625, 0.1875),# Hihat on 4
    (36, 2.25, 0.375),  # Kick on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.25, 0.1875), # Hihat on 1
    (42, 2.4375, 0.1875),# Hihat on 2
    (42, 2.625, 0.1875),# Hihat on 3
    (42, 2.8125, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875),# Hihat on 2
    (42, 3.375, 0.1875),# Hihat on 3
    (42, 3.5625, 0.1875),# Hihat on 4
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 3.75, 0.1875), # Hihat on 1
    (42, 3.9375, 0.1875),# Hihat on 2
    (42, 4.125, 0.1875),# Hihat on 3
    (42, 4.3125, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),# Hihat on 2
    (42, 4.875, 0.1875),# Hihat on 3
    (42, 5.0625, 0.1875),# Hihat on 4
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.25, 0.1875), # Hihat on 1
    (42, 5.4375, 0.1875),# Hihat on 2
    (42, 5.625, 0.1875),# Hihat on 3
    (42, 5.8125, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
