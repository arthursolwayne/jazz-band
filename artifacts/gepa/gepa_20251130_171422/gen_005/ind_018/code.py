
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    (30, 1.5, 0.375),   # Bb
    (31, 1.875, 0.375), # B
    (29, 2.25, 0.375),  # A
    (28, 2.625, 0.375), # Ab
    (27, 2.625, 0.375), # G
    (28, 3.0, 0.375),   # Ab
    (29, 3.375, 0.375), # A
    (30, 3.75, 0.375),  # Bb
    (31, 4.125, 0.375), # B
    (32, 4.5, 0.375),   # C
    (31, 4.875, 0.375), # B
    (30, 5.25, 0.375),  # Bb
    (31, 5.625, 0.375), # B
    (32, 6.0, 0.375),   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (40, 1.875, 0.375), # Fm7 (F, Ab, C, Eb) - F
    (43, 1.875, 0.375), # Fm7 - Eb
    (44, 1.875, 0.375), # Fm7 - C
    (41, 1.875, 0.375), # Fm7 - Ab
    # Bar 3
    (40, 3.375, 0.375), # Fm7 - F
    (43, 3.375, 0.375), # Fm7 - Eb
    (44, 3.375, 0.375), # Fm7 - C
    (41, 3.375, 0.375), # Fm7 - Ab
    # Bar 4
    (40, 4.875, 0.375), # Fm7 - F
    (43, 4.875, 0.375), # Fm7 - Eb
    (44, 4.875, 0.375), # Fm7 - C
    (41, 4.875, 0.375), # Fm7 - Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante) - One short motif, make it sing
sax_notes = [
    (46, 1.5, 0.75),    # G (start of motif)
    (44, 2.25, 0.75),   # E (end of first phrase)
    (46, 2.625, 0.75),  # G (restatement)
    (47, 3.375, 0.75),  # A (end of motif)
    (46, 3.75, 0.75),   # G (repeat)
    (44, 4.5, 0.75),    # E (repeat)
    (46, 4.875, 0.75),  # G (repeat)
    (47, 5.625, 0.75)   # A (end)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
