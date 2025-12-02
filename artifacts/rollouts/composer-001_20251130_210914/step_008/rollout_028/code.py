
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in F, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375),   # F (37) - root
    (38, 1.875, 0.375),  # F# chromatic
    (39, 2.25, 0.375),   # G
    (40, 2.625, 0.375),  # G#
    (39, 2.875, 0.375),  # G
    (38, 3.25, 0.375),   # F#
    (37, 3.625, 0.375),  # F
    (36, 4.0, 0.375),    # E chromatic
    (37, 4.375, 0.375),  # F
    (38, 4.75, 0.375),   # F#
    (39, 5.125, 0.375),  # G
    (40, 5.5, 0.375)     # G#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, comp on F7
piano_notes = [
    (42, 1.875, 0.1875), # G (F7: F, A, C, E, Bb)
    (46, 1.875, 0.1875), # Bb
    (47, 1.875, 0.1875), # B
    (50, 1.875, 0.1875), # D
    (52, 1.875, 0.1875), # E
    (53, 1.875, 0.1875), # F
    (42, 2.25, 0.1875),  # G
    (46, 2.25, 0.1875),  # Bb
    (47, 2.25, 0.1875),  # B
    (50, 2.25, 0.1875),  # D
    (52, 2.25, 0.1875),  # E
    (53, 2.25, 0.1875),  # F
    (42, 4.125, 0.1875), # G
    (46, 4.125, 0.1875), # Bb
    (47, 4.125, 0.1875), # B
    (50, 4.125, 0.1875), # D
    (52, 4.125, 0.1875), # E
    (53, 4.125, 0.1875), # F
    (42, 4.5, 0.1875),   # G
    (46, 4.5, 0.1875),   # Bb
    (47, 4.5, 0.1875),   # B
    (50, 4.5, 0.1875),   # D
    (52, 4.5, 0.1875),   # E
    (53, 4.5, 0.1875)    # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Motif in F, short and haunting
sax_notes = [
    (42, 1.5, 0.5),     # G
    (43, 2.0, 0.5),     # G#
    (42, 2.5, 0.5),     # G
    (40, 3.0, 0.5),     # E
    (42, 3.5, 0.5),     # G
    (43, 4.0, 0.5),     # G#
    (42, 4.5, 0.5),     # G
    (40, 5.0, 0.5)      # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
