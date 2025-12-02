
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375),# Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.125, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Bass line - walking, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375),  # F3
    (50, 1.875, 0.375), # Gb3
    (49, 2.25, 0.375),  # G3
    (51, 2.625, 0.375), # Ab3
    (53, 2.625, 0.375), # Bb3
    (55, 3.0, 0.375),   # B3
    (53, 3.375, 0.375), # Bb3
    (51, 3.75, 0.375),  # Ab3
    (50, 4.125, 0.375), # G3
    (48, 4.5, 0.375),   # F3
    (50, 4.875, 0.375), # G3
    (52, 5.25, 0.375),  # A3
    (53, 5.625, 0.375), # Bb3
    (55, 6.0, 0.375)    # B3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (60, 1.5, 0.1875), # F
    (65, 1.5, 0.1875), # A
    (62, 1.5, 0.1875), # C
    (64, 1.5, 0.1875), # Eb

    # Bar 3: D7 (D, F#, A, C)
    (62, 2.25, 0.1875), # D
    (67, 2.25, 0.1875), # F#
    (69, 2.25, 0.1875), # A
    (60, 2.25, 0.1875), # C

    # Bar 4: G7 (G, B, D, F)
    (67, 3.0, 0.1875), # G
    (71, 3.0, 0.1875), # B
    (69, 3.0, 0.1875), # D
    (60, 3.0, 0.1875), # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
    # Add to drums
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)

# Dante: Tenor sax - one short motif, make it sing
# Motif: F (60), Bb (64), F (60), Eb (63)
sax_notes = [
    (60, 1.5, 0.375),  # F
    (64, 1.875, 0.375), # Bb
    (60, 2.25, 0.375),  # F
    (63, 2.625, 0.375), # Eb
    (60, 3.0, 0.375),   # F
    (64, 3.375, 0.375), # Bb
    (60, 3.75, 0.375),  # F
    (63, 4.125, 0.375), # Eb
    (60, 4.5, 0.375),   # F
    (64, 4.875, 0.375), # Bb
    (60, 5.25, 0.375),  # F
    (63, 5.625, 0.375)  # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
