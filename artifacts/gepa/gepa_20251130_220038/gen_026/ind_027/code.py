
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
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.375, 0.1875),
    (42, 0.75, 0.1875),
    (42, 1.125, 0.1875),
    (36, 1.5, 0.375),  # Kick on beat 3
    (38, 1.875, 0.375),# Snare on beat 4
    (42, 1.5, 0.1875), # Hihat on 3 & 4
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E
bass_notes = [
    (53, 1.5, 0.375),  # G (chromatic approach to F)
    (55, 1.875, 0.375),# A
    (57, 2.25, 0.375), # Bb (chromatic approach to B)
    (58, 2.625, 0.375),# B
    (55, 2.625, 0.375),# A
    (53, 2.625, 0.375),# G
    (50, 2.625, 0.375),# F
    (52, 2.625, 0.375),# G
    (55, 3.0, 0.375),  # A
    (57, 3.375, 0.375),# Bb
    (58, 3.75, 0.375), # B
    (55, 3.75, 0.375), # A
    (53, 4.125, 0.375),# G
    (50, 4.5, 0.375),  # F
    (52, 4.875, 0.375),# G
    (55, 5.25, 0.375), # A
    (57, 5.625, 0.375),# Bb
    (58, 6.0, 0.375)   # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875),  # F7 (F, A, C, E)
    (69, 1.5, 0.1875),
    (67, 1.5, 0.1875),
    (69, 1.5, 0.1875),
    (64, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    # Bar 3
    (64, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (67, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (64, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    (67, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    # Bar 4
    (64, 3.0, 0.1875),
    (69, 3.0, 0.1875),
    (67, 3.0, 0.1875),
    (69, 3.0, 0.1875),
    (64, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (64, 3.75, 0.1875),
    (69, 3.75, 0.1875),
    (67, 3.75, 0.1875),
    (69, 3.75, 0.1875),
    (64, 4.125, 0.1875),
    (69, 4.125, 0.1875),
    (67, 4.125, 0.1875),
    (69, 4.125, 0.1875),
    (64, 4.5, 0.1875),
    (69, 4.5, 0.1875),
    (67, 4.5, 0.1875),
    (69, 4.5, 0.1875),
    (64, 4.875, 0.1875),
    (69, 4.875, 0.1875),
    (67, 4.875, 0.1875),
    (69, 4.875, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (66, 1.5, 0.375),  # F
    (69, 2.25, 0.375), # A
    (67, 3.0, 0.375),  # Bb
    (69, 3.75, 0.375), # B
    (66, 4.5, 0.375),  # F
    (69, 5.25, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on beat 1
    (38, 1.875, 0.375),# Snare on beat 2
    (42, 1.5, 0.1875), # Hihat on 1 & 2
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (36, 2.25, 0.375), # Kick on beat 3
    (38, 2.625, 0.375),# Snare on beat 4
    (42, 2.25, 0.1875), # Hihat on 3 & 4
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    # Bar 3
    (36, 3.0, 0.375),  # Kick on beat 1
    (38, 3.375, 0.375),# Snare on beat 2
    (42, 3.0, 0.1875), # Hihat on 1 & 2
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (36, 3.75, 0.375), # Kick on beat 3
    (38, 4.125, 0.375),# Snare on beat 4
    (42, 3.75, 0.1875), # Hihat on 3 & 4
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    # Bar 4
    (36, 4.5, 0.375),  # Kick on beat 1
    (38, 4.875, 0.375),# Snare on beat 2
    (42, 4.5, 0.1875), # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (36, 5.25, 0.375), # Kick on beat 3
    (38, 5.625, 0.375),# Snare on beat 4
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_piece.mid")
