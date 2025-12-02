
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (62, 2.25, 0.375), (63, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (66, 3.75, 0.375), (67, 4.125, 0.375),
    (68, 4.5, 0.375), (69, 4.875, 0.375), (70, 5.25, 0.375), (71, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s) - C7 (C, E, B)
    (60, 1.5, 0.375), (64, 1.5, 0.375), (71, 1.5, 0.375),
    # Bar 3 (2.625 - 3.375s) - D7 (D, F#, C#)
    (62, 2.625, 0.375), (67, 2.625, 0.375), (74, 2.625, 0.375),
    # Bar 4 (4.125 - 4.875s) - E7 (E, G#, D)
    (64, 4.125, 0.375), (69, 4.125, 0.375), (76, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.6875)

    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C - E - G - C (C major triad, played as a motif)
sax_notes = [
    (60, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375), (60, 2.625, 0.375),
    (60, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375), (60, 4.125, 0.375),
    (60, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
