
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125),
    (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375),  # D -> Eb
    (64, 2.25, 0.375), (65, 2.625, 0.375),  # E -> F
    (67, 3.0, 0.375), (68, 3.375, 0.375),   # G -> G#
    (69, 3.75, 0.375), (70, 4.125, 0.375),  # A -> Bb
    (72, 4.5, 0.375), (73, 4.875, 0.375),   # B -> B#
    (74, 5.25, 0.375), (75, 5.625, 0.375),  # C -> C#
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (64, 1.5, 0.375), (69, 1.5, 0.375), (74, 1.5, 0.375), (76, 1.5, 0.375),
    # Bar 3: F#7 (F#, A#, C#, E)
    (69, 2.625, 0.375), (74, 2.625, 0.375), (76, 2.625, 0.375), (78, 2.625, 0.375),
    # Bar 4: A7 (A, C#, E, G)
    (69, 3.75, 0.375), (74, 3.75, 0.375), (76, 3.75, 0.375), (79, 3.75, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Bars 2-4): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start + 0.0, 0.375), (38, bar_start + 0.375, 0.375),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375),
        (42, bar_start + 0.0, 0.125), (42, bar_start + 0.125, 0.125),
        (42, bar_start + 0.25, 0.125), (42, bar_start + 0.375, 0.125),
        (42, bar_start + 0.5, 0.125), (42, bar_start + 0.625, 0.125),
        (42, bar_start + 0.75, 0.125), (42, bar_start + 0.875, 0.125),
        (42, bar_start + 1.0, 0.125), (42, bar_start + 1.125, 0.125),
        (42, bar_start + 1.25, 0.125), (42, bar_start + 1.375, 0.125),
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D, F#, A, D (motif)
sax_notes = [
    (64, 1.5, 0.375),  # D
    (69, 1.875, 0.375), # F#
    (74, 2.25, 0.375),  # A
    (62, 2.625, 0.375), # D (leave it hanging on the 4th beat)
    (64, 3.0, 0.375),  # D (return with the motif)
    (69, 3.375, 0.375), # F#
    (74, 3.75, 0.375),  # A
    (64, 4.125, 0.375), # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
