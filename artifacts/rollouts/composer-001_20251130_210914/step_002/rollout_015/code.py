
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375),  # F
    (67, 3.0, 0.375),  # G
    (69, 3.375, 0.375),  # A
    (71, 3.75, 0.375),  # Bb
    (72, 4.125, 0.375),  # B
    (74, 4.5, 0.375),  # C
    (76, 4.875, 0.375),  # D
    (77, 5.25, 0.375),  # Eb
    (78, 5.625, 0.375),  # E
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375),  # G7
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (72, 1.875, 0.375),
    (67, 3.375, 0.375),  # G7
    (69, 3.375, 0.375),
    (71, 3.375, 0.375),
    (72, 3.375, 0.375),
    (67, 4.875, 0.375),  # G7
    (69, 4.875, 0.375),
    (71, 4.875, 0.375),
    (72, 4.875, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375),  # Kick on 1
        (38, start + 0.375, 0.375),  # Snare on 2
        (42, start + 0.0, 0.1875),  # Hihat on 1
        (42, start + 0.1875, 0.1875),  # Hihat on &
        (42, start + 0.375, 0.1875),  # Hihat on 2
        (42, start + 0.5625, 0.1875),  # Hihat on &
        (42, start + 0.75, 0.1875),  # Hihat on 3
        (42, start + 0.9375, 0.1875),  # Hihat on &
        (42, start + 1.125, 0.1875),  # Hihat on 4
        (36, start + 1.125, 0.375),  # Kick on 3
        (38, start + 1.5, 0.375),  # Snare on 4
    ]
    for note, start_t, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_t, end=start_t + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (66), Bb (71), D (62)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (66, 1.875, 0.375),  # F#
    (71, 2.25, 0.375),  # Bb
    (62, 2.625, 0.375),  # D
    (62, 3.0, 0.375),  # D
    (66, 3.375, 0.375),  # F#
    (71, 3.75, 0.375),  # Bb
    (62, 4.125, 0.375),  # D
    (62, 5.625, 0.375),  # D
    (66, 5.999, 0.375),  # F#
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
