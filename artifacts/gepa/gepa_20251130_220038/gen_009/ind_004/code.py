
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
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    (45, 1.5, 0.375),  # F
    (44, 1.875, 0.375), # Eb
    (46, 2.25, 0.375),  # F#
    (42, 2.625, 0.375), # D
    (43, 2.625, 0.375), # Eb
    (45, 3.0, 0.375),   # F
    (44, 3.375, 0.375), # Eb
    (46, 3.75, 0.375),  # F#
    (42, 4.125, 0.375), # D
    (43, 4.125, 0.375), # Eb
    (45, 4.5, 0.375),   # F
    (44, 4.875, 0.375), # Eb
    (46, 5.25, 0.375),  # F#
    (42, 5.625, 0.375), # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (53, 1.5, 0.375),  # F
    (58, 1.5, 0.375),  # A
    (55, 1.5, 0.375),  # C
    (50, 1.5, 0.375),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (50, 2.625, 0.375), # Bb
    (55, 2.625, 0.375), # D
    (53, 2.625, 0.375), # F
    (48, 2.625, 0.375), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    (50, 3.75, 0.375),  # Eb
    (55, 3.75, 0.375),  # G
    (52, 3.75, 0.375),  # Bb
    (47, 3.75, 0.375),  # Db
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums - Little Ray (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = 1.5 * (bar - 1)
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5))

# Sax - Dante (short motif, make it sing)
sax_notes = [
    (62, 1.5, 0.375),    # G (Fm scale: F, Gb, G, Ab, A, Bb, B)
    (60, 1.875, 0.375),  # E
    (62, 2.25, 0.375),   # G
    (65, 2.625, 0.375),  # B
    (62, 3.0, 0.375),    # G
    (65, 3.375, 0.375),  # B
    (63, 3.75, 0.375),   # A
    (65, 4.125, 0.375),  # B
    (62, 4.5, 0.375),    # G
    (65, 4.875, 0.375),  # B
    (63, 5.25, 0.375),   # A
    (65, 5.625, 0.375),  # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_piece.mid')
