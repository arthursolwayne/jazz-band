
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0, 0.375), # Kick on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on 2
    (42, 0.375, 0.1875), # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 0.75, 0.375), # Kick on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), # D
    (63, 1.875, 0.375), # Eb
    (60, 2.25, 0.375), # C
    (62, 2.625, 0.375), # D

    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375), # E
    (62, 3.375, 0.375), # D
    (60, 3.75, 0.375), # C
    (59, 4.125, 0.375), # Bb

    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375), # D
    (60, 5.625, 0.375) # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # G
    (64, 1.875, 0.375), # Bb
    (69, 1.875, 0.375), # D

    # Bar 3 (3.0 - 4.5s)
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # G
    (64, 3.375, 0.375), # Bb
    (69, 3.375, 0.375), # D

    # Bar 4 (4.5 - 6.0s)
    (62, 4.875, 0.375), # D
    (67, 4.875, 0.375), # G
    (64, 4.875, 0.375), # Bb
    (69, 4.875, 0.375) # D
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Dante, motif with a question, leave it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), # D
    (65, 1.875, 0.375), # F
    (62, 2.25, 0.375), # D
    (60, 2.625, 0.375), # C

    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375), # D
    (65, 3.375, 0.375), # F
    (62, 3.75, 0.375), # D
    (60, 4.125, 0.375), # C

    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), # D
    (65, 4.875, 0.375), # F
    (62, 5.25, 0.375), # D
    (60, 5.625, 0.375) # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375), # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on 2
    (42, 1.875, 0.1875), # Hihat on 3
    (42, 2.0625, 0.1875), # Hihat on 4
    (36, 2.25, 0.375), # Kick on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875), # Hihat on 4

    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375), # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on 2
    (42, 3.375, 0.1875), # Hihat on 3
    (42, 3.5625, 0.1875), # Hihat on 4
    (36, 3.75, 0.375), # Kick on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875), # Hihat on 4

    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375), # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on 2
    (42, 4.875, 0.1875), # Hihat on 3
    (42, 5.0625, 0.1875), # Hihat on 4
    (36, 5.25, 0.375), # Kick on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on 4
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
