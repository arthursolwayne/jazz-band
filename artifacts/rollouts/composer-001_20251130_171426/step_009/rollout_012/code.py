
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
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (37, 1.5, 0.375),  # F root
    (38, 1.875, 0.375),  # F# chromatic up
    (36, 2.25, 0.375),  # E chromatic down
    (37, 2.625, 0.375),  # F
    (39, 3.0, 0.375),  # G
    (40, 3.375, 0.375),  # G#
    (38, 3.75, 0.375),  # F#
    (37, 4.125, 0.375),  # F
    (39, 4.5, 0.375),  # G
    (41, 4.875, 0.375),  # A
    (40, 5.25, 0.375),  # G#
    (39, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (42, 2.25, 0.375),  # F7: F, A, C, E
    (46, 2.25, 0.375),
    (48, 2.25, 0.375),
    (50, 2.25, 0.375),
    (44, 3.0, 0.375),  # G7: G, B, D, F
    (48, 3.0, 0.375),
    (50, 3.0, 0.375),
    (52, 3.0, 0.375),
    (42, 4.5, 0.375),  # F7: F, A, C, E
    (46, 4.5, 0.375),
    (48, 4.5, 0.375),
    (50, 4.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in F
sax_notes = [
    (53, 1.5, 0.375),  # F#
    (55, 1.875, 0.375),  # A
    (58, 2.25, 0.375),  # C
    (53, 2.625, 0.375),  # F#
    (55, 3.0, 0.375),  # A
    (60, 3.375, 0.375),  # D
    (58, 3.75, 0.375),  # C
    (55, 4.125, 0.375),  # A
    (53, 4.5, 0.375),  # F#
    (55, 4.875, 0.375),  # A
    (60, 5.25, 0.375),  # D
    (58, 5.625, 0.375),  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
