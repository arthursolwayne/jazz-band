
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    (42, 1.5, 0.375), # F
    (43, 1.875, 0.375), # F#
    (44, 2.25, 0.375), # G
    (45, 2.625, 0.375), # G#
    (46, 3.0, 0.375), # A
    (47, 3.375, 0.375), # A#
    (48, 3.75, 0.375), # Bb
    (49, 4.125, 0.375), # B
    (50, 4.5, 0.375), # C
    (51, 4.875, 0.375), # C#
    (52, 5.25, 0.375), # D
    (53, 5.625, 0.375), # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.5, 0.375), # F7 (F, A, C, E)
    (53, 1.5, 0.375),
    (55, 1.5, 0.375),
    (57, 1.5, 0.375),
    (53, 1.875, 0.375), # F7
    (55, 1.875, 0.375),
    (57, 1.875, 0.375),
    (50, 1.875, 0.375),
    (50, 2.25, 0.375), # F7
    (53, 2.25, 0.375),
    (55, 2.25, 0.375),
    (57, 2.25, 0.375),
    (53, 2.625, 0.375), # F7
    (55, 2.625, 0.375),
    (57, 2.625, 0.375),
    (50, 2.625, 0.375),
    (50, 3.0, 0.375), # F7
    (53, 3.0, 0.375),
    (55, 3.0, 0.375),
    (57, 3.0, 0.375),
    (53, 3.375, 0.375), # F7
    (55, 3.375, 0.375),
    (57, 3.375, 0.375),
    (50, 3.375, 0.375),
    (50, 3.75, 0.375), # F7
    (53, 3.75, 0.375),
    (55, 3.75, 0.375),
    (57, 3.75, 0.375),
    (53, 4.125, 0.375), # F7
    (55, 4.125, 0.375),
    (57, 4.125, 0.375),
    (50, 4.125, 0.375),
    (50, 4.5, 0.375), # F7
    (53, 4.5, 0.375),
    (55, 4.5, 0.375),
    (57, 4.5, 0.375),
    (53, 4.875, 0.375), # F7
    (55, 4.875, 0.375),
    (57, 4.875, 0.375),
    (50, 4.875, 0.375),
    (50, 5.25, 0.375), # F7
    (53, 5.25, 0.375),
    (55, 5.25, 0.375),
    (57, 5.25, 0.375),
    (53, 5.625, 0.375), # F7
    (55, 5.625, 0.375),
    (57, 5.625, 0.375),
    (50, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.4999)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.6875)
    # Add all
    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), # G
    (64, 1.875, 0.375), # A
    (66, 2.25, 0.375), # Bb
    (67, 2.625, 0.375), # B
    (66, 3.0, 0.375), # Bb
    (64, 3.375, 0.375), # A
    (62, 3.75, 0.375), # G
    (60, 4.125, 0.375), # F
    (62, 4.5, 0.375), # G
    (64, 4.875, 0.375), # A
    (66, 5.25, 0.375), # Bb
    (67, 5.625, 0.375), # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
