
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.75),  # Snare on 2
    (42, 0.375, 0.75),  # Hihat on 2
    (36, 0.75, 1.125),  # Kick on 3
    (42, 0.75, 1.125),  # Hihat on 3
    (38, 1.125, 1.5),   # Snare on 4
    (42, 1.125, 1.5),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (60, 1.5, 0.375),   # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.375), # C7 (C, E, B)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    # Bar 3
    (60, 3.375, 0.375), # C7
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    # Bar 4
    (60, 4.875, 0.375), # C7
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Bar 2
    drum_notes = [
        (36, bar_start, 0.375),   # Kick on 1
        (42, bar_start, 0.375),   # Hihat on 1
        (38, bar_start + 0.375, 0.75),  # Snare on 2
        (42, bar_start + 0.375, 0.75),  # Hihat on 2
        (36, bar_start + 0.75, 1.125),  # Kick on 3
        (42, bar_start + 0.75, 1.125),  # Hihat on 3
        (38, bar_start + 1.125, 1.5),   # Snare on 4
        (42, bar_start + 1.125, 1.5),   # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C -> E -> B -> C
sax_notes = [
    (60, 1.5, 0.375),   # C
    (64, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # B
    (60, 2.625, 0.375), # C (leave it hanging)
    (60, 4.5, 0.375),   # Return to C
    (64, 4.875, 0.375), # E
    (67, 5.25, 0.375),  # B
    (60, 5.625, 0.375), # C (finish)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
