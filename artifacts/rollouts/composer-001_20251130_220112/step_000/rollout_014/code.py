
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375), (40, 1.875, 0.375), (39, 2.25, 0.375), (37, 2.625, 0.375),  # Bar 2
    (38, 3.0, 0.375), (39, 3.375, 0.375), (37, 3.75, 0.375), (36, 4.125, 0.375),  # Bar 3
    (37, 4.5, 0.375), (38, 4.875, 0.375), (39, 5.25, 0.375), (41, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.875, 0.375), (50, 1.875, 0.375), (53, 1.875, 0.375), (55, 1.875, 0.375),  # F7
    (46, 2.625, 0.375), (48, 2.625, 0.375), (50, 2.625, 0.375), (53, 2.625, 0.375),  # Bb7
    # Bar 3
    (50, 3.375, 0.375), (52, 3.375, 0.375), (55, 3.375, 0.375), (57, 3.375, 0.375),  # D7
    (48, 4.125, 0.375), (50, 4.125, 0.375), (52, 4.125, 0.375), (55, 4.125, 0.375),  # F7
    # Bar 4
    (52, 4.875, 0.375), (54, 4.875, 0.375), (57, 4.875, 0.375), (59, 4.875, 0.375),  # G7
    (50, 5.625, 0.375), (52, 5.625, 0.375), (54, 5.625, 0.375), (57, 5.625, 0.375)   # C7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F (Ab, Bb) -> E (B, C) -> D (Ab, Bb) -> C (B, A)
# Start at 1.5s, end at 3.0s
sax_notes = [
    (53, 1.5, 0.375), (55, 1.5, 0.375), (50, 1.5, 0.375), # F -> Ab -> Bb
    (51, 2.25, 0.375), (52, 2.25, 0.375), (50, 2.25, 0.375), # E -> B -> C
    (55, 3.0, 0.375), (50, 3.0, 0.375), (51, 3.0, 0.375), # D -> Ab -> B
    (50, 3.75, 0.375), (48, 3.75, 0.375), (51, 3.75, 0.375) # C -> B -> A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: Fill the bar (Bars 2-4)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375), (38, start + 0.375, 0.375), (42, start + 0.0, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
