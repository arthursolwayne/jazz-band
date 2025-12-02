
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
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    (36, bar1_start + 0.0, 0.375),
    (36, bar1_start + 0.75, 0.375),
    # Snare on 2 and 4
    (38, bar1_start + 0.375, 0.375),
    (38, bar1_start + 0.75 * 3, 0.375),
    # Hihat on every eighth
    (42, bar1_start + 0.0, 0.125),
    (42, bar1_start + 0.125, 0.125),
    (42, bar1_start + 0.25, 0.125),
    (42, bar1_start + 0.375, 0.125),
    (42, bar1_start + 0.5, 0.125),
    (42, bar1_start + 0.625, 0.125),
    (42, bar1_start + 0.75, 0.125),
    (42, bar1_start + 0.875, 0.125),
    (42, bar1_start + 1.0, 0.125),
    (42, bar1_start + 1.125, 0.125),
    (42, bar1_start + 1.25, 0.125),
    (42, bar1_start + 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bar2_start = 1.5
bass_notes = [
    # Bar 2: Dm7
    (62, bar2_start + 0.0, 0.375),  # D
    (60, bar2_start + 0.375, 0.375),  # C
    (62, bar2_start + 0.75, 0.375),  # D
    (64, bar2_start + 1.125, 0.375),  # F
    # Bar 3: Dm7
    (62, bar2_start + 1.5, 0.375),  # D
    (60, bar2_start + 1.875, 0.375),  # C
    (62, bar2_start + 2.25, 0.375),  # D
    (64, bar2_start + 2.625, 0.375),  # F
    # Bar 4: Dm7
    (62, bar2_start + 3.0, 0.375),  # D
    (60, bar2_start + 3.375, 0.375),  # C
    (62, bar2_start + 3.75, 0.375),  # D
    (64, bar2_start + 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, bar2_start + 0.375, 0.375),  # D
    (67, bar2_start + 0.375, 0.375),  # G
    (69, bar2_start + 0.375, 0.375),  # Bb
    (64, bar2_start + 0.375, 0.375),  # F
    # Bar 3: Dm7
    (62, bar2_start + 1.875, 0.375),  # D
    (67, bar2_start + 1.875, 0.375),  # G
    (69, bar2_start + 1.875, 0.375),  # Bb
    (64, bar2_start + 1.875, 0.375),  # F
    # Bar 4: Dm7
    (62, bar2_start + 3.375, 0.375),  # D
    (67, bar2_start + 3.375, 0.375),  # G
    (69, bar2_start + 3.375, 0.375),  # Bb
    (64, bar2_start + 3.375, 0.375)   # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Full quarter
bar2_drums = [
    # Kick on 1 and 3
    (36, bar2_start + 0.0, 0.375),
    (36, bar2_start + 0.75, 0.375),
    (36, bar2_start + 1.5, 0.375),
    (36, bar2_start + 2.25, 0.375),
    (36, bar2_start + 3.0, 0.375),
    (36, bar2_start + 3.75, 0.375),
    # Snare on 2 and 4
    (38, bar2_start + 0.375, 0.375),
    (38, bar2_start + 1.125, 0.375),
    (38, bar2_start + 1.875, 0.375),
    (38, bar2_start + 2.625, 0.375),
    (38, bar2_start + 3.375, 0.375),
    # Hihat on every eighth
    (42, bar2_start + 0.0, 0.125),
    (42, bar2_start + 0.125, 0.125),
    (42, bar2_start + 0.25, 0.125),
    (42, bar2_start + 0.375, 0.125),
    (42, bar2_start + 0.5, 0.125),
    (42, bar2_start + 0.625, 0.125),
    (42, bar2_start + 0.75, 0.125),
    (42, bar2_start + 0.875, 0.125),
    (42, bar2_start + 1.0, 0.125),
    (42, bar2_start + 1.125, 0.125),
    (42, bar2_start + 1.25, 0.125),
    (42, bar2_start + 1.375, 0.125),
    (42, bar2_start + 1.5, 0.125),
    (42, bar2_start + 1.625, 0.125),
    (42, bar2_start + 1.75, 0.125),
    (42, bar2_start + 1.875, 0.125),
    (42, bar2_start + 2.0, 0.125),
    (42, bar2_start + 2.125, 0.125),
    (42, bar2_start + 2.25, 0.125),
    (42, bar2_start + 2.375, 0.125),
    (42, bar2_start + 2.5, 0.125),
    (42, bar2_start + 2.625, 0.125),
    (42, bar2_start + 2.75, 0.125),
    (42, bar2_start + 2.875, 0.125),
    (42, bar2_start + 3.0, 0.125),
    (42, bar2_start + 3.125, 0.125),
    (42, bar2_start + 3.25, 0.125),
    (42, bar2_start + 3.375, 0.125),
    (42, bar2_start + 3.5, 0.125),
    (42, bar2_start + 3.625, 0.125),
    (42, bar2_start + 3.75, 0.125),
    (42, bar2_start + 3.875, 0.125)
]
for note, start, duration in bar2_drums:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif in Dm, one short phrase
sax_notes = [
    # Bar 2: Start of motif
    (65, bar2_start + 0.0, 0.375),  # E
    (64, bar2_start + 0.375, 0.375),  # D
    (66, bar2_start + 0.75, 0.375),  # F
    # Bar 3: Continue motif
    (67, bar2_start + 1.125, 0.375),  # G
    (65, bar2_start + 1.5, 0.375),  # E
    (64, bar2_start + 1.875, 0.375),  # D
    (66, bar2_start + 2.25, 0.375),  # F
    # Bar 4: End of motif
    (67, bar2_start + 2.625, 0.375),  # G
    (66, bar2_start + 3.0, 0.375),  # F
    (64, bar2_start + 3.375, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
