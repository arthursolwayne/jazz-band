
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: sax starts, everyone joins
# Sax motif: Fm7 -> G7 -> Cm7 -> Bb7 (Fm key)
sax_notes = [
    (64, 1.5, 0.375),  # F
    (67, 1.875, 0.375),  # A
    (60, 2.25, 0.375),  # F
    (65, 2.625, 0.375),  # G
    (64, 2.625, 0.375),  # F
    (62, 3.0, 0.375),  # D
    (58, 3.375, 0.375),  # Bb
    (62, 3.75, 0.375),  # D
    (63, 4.125, 0.375),  # Eb
    (64, 4.5, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in Fm (F, Gb, G, Ab, A, Bb, B, C, C#, D, Eb, E, F, F)
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375),  # Gb
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375),  # Ab
    (71, 3.0, 0.375),  # A
    (72, 3.375, 0.375),  # Bb
    (74, 3.75, 0.375),  # B
    (76, 4.125, 0.375),  # C
    (77, 4.5, 0.375),  # C#
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: comp on 2 and 4, with 7th chords
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, C)
    (64, 1.875, 0.125),  # F
    (69, 1.875, 0.125),  # Ab
    (72, 1.875, 0.125),  # Bb
    (76, 1.875, 0.125),  # C
    # Bar 3: G7 (G, B, D, F)
    (67, 3.0, 0.125),  # G
    (71, 3.0, 0.125),  # B
    (74, 3.0, 0.125),  # D
    (64, 3.0, 0.125),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (76, 4.125, 0.125),  # C
    (71, 4.125, 0.125),  # Eb
    (74, 4.125, 0.125),  # G
    (72, 4.125, 0.125),  # Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 2: Drums continue
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
    (36, 3.0, 0.375),  # Kick on 1 (Bar 3)
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1 (Bar 4)
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
