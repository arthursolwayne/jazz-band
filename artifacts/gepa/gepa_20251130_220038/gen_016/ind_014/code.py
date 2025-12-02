
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus's walking bass line (Dm7 - G7 - Cm7 - F7)
bass_notes = [
    (50, 1.5, 0.375),   # D (root)
    (52, 1.875, 0.375), # Eb (chromatic approach)
    (49, 2.25, 0.375),  # C (3rd)
    (51, 2.625, 0.375), # Db (chromatic approach)
    (53, 2.875, 0.375), # E (5th)
    (55, 3.25, 0.375),  # G (root)
    (52, 3.625, 0.375), # Eb (chromatic approach)
    (50, 4.0, 0.375),   # D (root)
    (48, 4.375, 0.375), # Bb (chromatic approach)
    (50, 4.75, 0.375),  # D (root)
    (52, 5.125, 0.375), # Eb (chromatic approach)
    (51, 5.5, 0.375),   # Db (chromatic approach)
    (49, 5.875, 0.375)  # C (3rd)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane's piano comping (Dm7 - G7 - Cm7 - F7)
piano_notes = [
    # Bar 2: Dm7 (2 and 4)
    (62, 1.875, 0.375), # F
    (64, 1.875, 0.375), # G
    (67, 1.875, 0.375), # Bb
    (69, 1.875, 0.375), # D
    (64, 2.625, 0.375), # G
    (67, 2.625, 0.375), # Bb
    (71, 2.625, 0.375), # F
    (72, 2.625, 0.375), # G
    # Bar 3: G7 (2 and 4)
    (67, 3.375, 0.375), # Bb
    (71, 3.375, 0.375), # D
    (72, 3.375, 0.375), # E
    (76, 3.375, 0.375), # G
    (72, 4.125, 0.375), # E
    (76, 4.125, 0.375), # G
    (78, 4.125, 0.375), # A
    (71, 4.125, 0.375), # D
    # Bar 4: Cm7 (2 and 4)
    (60, 4.875, 0.375), # C
    (62, 4.875, 0.375), # D
    (64, 4.875, 0.375), # E
    (67, 4.875, 0.375), # G
    (64, 5.625, 0.375), # E
    (67, 5.625, 0.375), # G
    (69, 5.625, 0.375), # Bb
    (71, 5.625, 0.375), # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray's drums (Bars 2-4)
drum_notes_bar2 = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.375),    # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.375),   # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

drum_notes_bar3 = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

drum_notes_bar4 = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante's saxophone motif (Bar 2: Dm7)
sax_notes = [
    (62, 1.5, 0.375),    # F
    (64, 1.875, 0.375),  # G
    (67, 2.25, 0.375),   # Bb
    (69, 2.625, 0.375),  # D
    (67, 3.0, 0.375),    # Bb (restatement)
    (64, 3.375, 0.375),  # G
    (62, 3.75, 0.375),   # F
    (67, 4.125, 0.375),  # Bb (leave it hanging)
    (69, 4.5, 0.375),    # D (return)
    (67, 4.875, 0.375),  # Bb
    (64, 5.25, 0.375),   # G
    (62, 5.625, 0.375)   # F (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
