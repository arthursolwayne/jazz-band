
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

# Bar 1
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
    (36, 1.125, 0.375)  # Kick on 3
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375),  # F
    (67, 3.0, 0.375),  # G
    (69, 3.375, 0.375),  # A
    (71, 3.75, 0.375),  # Bb
    (72, 4.125, 0.375),  # B
    (71, 4.5, 0.375),  # Bb
    (69, 4.875, 0.375),  # A
    (67, 5.25, 0.375),  # G
    (65, 5.625, 0.375)  # F
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),  # D7: D, F#, A, C
    (67, 1.5, 0.375),
    (72, 1.5, 0.375),
    (64, 1.5, 0.375),
    (67, 1.875, 0.375),  # D7
    (72, 1.875, 0.375),
    (64, 1.875, 0.375),
    (66, 1.875, 0.375),
    (67, 2.25, 0.375),  # G7
    (71, 2.25, 0.375),
    (76, 2.25, 0.375),
    (69, 2.25, 0.375),
    (67, 2.625, 0.375),  # G7
    (71, 2.625, 0.375),
    (76, 2.625, 0.375),
    (69, 2.625, 0.375),
    (62, 3.0, 0.375),  # D7
    (67, 3.0, 0.375),
    (72, 3.0, 0.375),
    (64, 3.0, 0.375),
    (67, 3.375, 0.375),  # D7
    (72, 3.375, 0.375),
    (64, 3.375, 0.375),
    (66, 3.375, 0.375),
    (67, 3.75, 0.375),  # G7
    (71, 3.75, 0.375),
    (76, 3.75, 0.375),
    (69, 3.75, 0.375),
    (67, 4.125, 0.375),  # G7
    (71, 4.125, 0.375),
    (76, 4.125, 0.375),
    (69, 4.125, 0.375),
    (62, 4.5, 0.375),  # D7
    (67, 4.5, 0.375),
    (72, 4.5, 0.375),
    (64, 4.5, 0.375),
    (67, 4.875, 0.375),  # D7
    (72, 4.875, 0.375),
    (64, 4.875, 0.375),
    (66, 4.875, 0.375),
    (67, 5.25, 0.375),  # G7
    (71, 5.25, 0.375),
    (76, 5.25, 0.375),
    (69, 5.25, 0.375),
    (67, 5.625, 0.375),  # G7
    (71, 5.625, 0.375),
    (76, 5.625, 0.375),
    (69, 5.625, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62) -> F# (67) -> A (72) -> D (62)
# Start on 1.5s, repeat on 3.0s, end on 4.5s

sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375),  # F#
    (72, 2.25, 0.375),  # A
    (62, 2.625, 0.375),  # D
    (62, 3.0, 0.375),  # D
    (67, 3.375, 0.375),  # F#
    (72, 3.75, 0.375),  # A
    (62, 4.125, 0.375),  # D
    (62, 4.5, 0.375),  # D
    (67, 4.875, 0.375),  # F#
    (72, 5.25, 0.375),  # A
    (62, 5.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
