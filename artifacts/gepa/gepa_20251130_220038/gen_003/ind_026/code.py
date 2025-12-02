
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

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (63, 1.875, 0.375), # Eb (chromatic approach)
    (60, 2.25, 0.375),  # Bb (5th)
    (62, 2.625, 0.375), # D
    (65, 2.625, 0.375), # F (7th)
    (63, 3.0, 0.375),   # Eb
    (62, 3.375, 0.375), # D
    (60, 3.75, 0.375),  # Bb
    (62, 4.125, 0.375), # D
    (65, 4.5, 0.375),   # F
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375), # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),  # D7 (D, F#, A, C)
    (69, 1.5, 0.375),  # C
    (66, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # F#

    (62, 2.25, 0.375), # D7
    (69, 2.25, 0.375), # C
    (66, 2.25, 0.375), # A
    (64, 2.25, 0.375), # F#

    (62, 3.0, 0.375),  # D7
    (69, 3.0, 0.375),  # C
    (66, 3.0, 0.375),  # A
    (64, 3.0, 0.375),  # F#

    (62, 3.75, 0.375), # D7
    (69, 3.75, 0.375), # C
    (66, 3.75, 0.375), # A
    (64, 3.75, 0.375), # F#

    (62, 4.5, 0.375),  # D7
    (69, 4.5, 0.375),  # C
    (66, 4.5, 0.375),  # A
    (64, 4.5, 0.375),  # F#

    (62, 5.25, 0.375), # D7
    (69, 5.25, 0.375), # C
    (66, 5.25, 0.375), # A
    (64, 5.25, 0.375), # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Main motif
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375), # F
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375), # Eb
    (62, 3.0, 0.375),   # D
    (65, 3.375, 0.375), # F
    (62, 3.75, 0.375),  # D
    (64, 4.125, 0.375), # Eb
    (62, 4.5, 0.375),   # D
    (65, 4.875, 0.375), # F
    (62, 5.25, 0.375),  # D
    (64, 5.625, 0.375), # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
