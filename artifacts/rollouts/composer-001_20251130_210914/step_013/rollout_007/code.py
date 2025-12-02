
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &4
    (36, 1.5, 0.375),   # Kick on 3
    (38, 1.5, 0.375),   # Snare on 4 (overlap with kick)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# Starting on D (2nd inversion of D7), walking down
# D C# B A G F# E D C B A G F# E D
bass_notes = [
    (62, 1.5, 0.375),   # D
    (61, 1.875, 0.375), # C#
    (60, 2.25, 0.375),  # B
    (59, 2.625, 0.375), # A
    (57, 3.0, 0.375),   # G
    (56, 3.375, 0.375), # F#
    (55, 3.75, 0.375),  # E
    (53, 4.125, 0.375), # D
    (52, 4.5, 0.375),   # C
    (51, 4.875, 0.375), # B
    (50, 5.25, 0.375),  # A
    (49, 5.625, 0.375), # G
    (48, 6.0, 0.375),   # F#
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# D7 (D F# A C) on 1
# Bm7 (B D F# A) on 2
# G7 (G B D F) on 3
# Cm7 (C Eb G Bb) on 4

# Bar 2
piano_notes = [
    # D7 on 1
    (62, 1.5, 0.375),  # D
    (66, 1.5, 0.375),  # F#
    (69, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # C
    # Bm7 on 2
    (66, 1.875, 0.375), # B
    (69, 1.875, 0.375), # D
    (72, 1.875, 0.375), # F#
    (74, 1.875, 0.375), # A
    # G7 on 3
    (67, 2.25, 0.375),  # G
    (71, 2.25, 0.375),  # B
    (74, 2.25, 0.375),  # D
    (76, 2.25, 0.375),  # F
    # Cm7 on 4
    (60, 2.625, 0.375), # C
    (63, 2.625, 0.375), # Eb
    (67, 2.625, 0.375), # G
    (69, 2.625, 0.375), # Bb
    # Bar 3
    # D7 on 1
    (62, 3.0, 0.375),  # D
    (66, 3.0, 0.375),  # F#
    (69, 3.0, 0.375),  # A
    (64, 3.0, 0.375),  # C
    # Bm7 on 2
    (66, 3.375, 0.375), # B
    (69, 3.375, 0.375), # D
    (72, 3.375, 0.375), # F#
    (74, 3.375, 0.375), # A
    # G7 on 3
    (67, 3.75, 0.375),  # G
    (71, 3.75, 0.375),  # B
    (74, 3.75, 0.375),  # D
    (76, 3.75, 0.375),  # F
    # Cm7 on 4
    (60, 4.125, 0.375), # C
    (63, 4.125, 0.375), # Eb
    (67, 4.125, 0.375), # G
    (69, 4.125, 0.375), # Bb
    # Bar 4
    # D7 on 1
    (62, 4.5, 0.375),  # D
    (66, 4.5, 0.375),  # F#
    (69, 4.5, 0.375),  # A
    (64, 4.5, 0.375),  # C
    # Bm7 on 2
    (66, 4.875, 0.375), # B
    (69, 4.875, 0.375), # D
    (72, 4.875, 0.375), # F#
    (74, 4.875, 0.375), # A
    # G7 on 3
    (67, 5.25, 0.375),  # G
    (71, 5.25, 0.375),  # B
    (74, 5.25, 0.375),  # D
    (76, 5.25, 0.375),  # F
    # Cm7 on 4
    (60, 5.625, 0.375), # C
    (63, 5.625, 0.375), # Eb
    (67, 5.625, 0.375), # G
    (69, 5.625, 0.375), # Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, start on bar 2, leave it hanging, come back and finish
# D, F#, A, C
# D on 1
# F# on &2
# A on 3
# C on &4
# Then repeat in bar 4, ending on A

sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),   # D
    (66, 1.875, 0.375), # F#
    (69, 2.25, 0.375),  # A
    (64, 2.625, 0.375), # C
    # Bar 3 (repeat motif but end on A)
    (62, 3.0, 0.375),   # D
    (66, 3.375, 0.375), # F#
    (69, 3.75, 0.375),  # A
    # Bar 4
    (62, 4.5, 0.375),   # D
    (66, 4.875, 0.375), # F#
    (69, 5.25, 0.375),  # A
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
