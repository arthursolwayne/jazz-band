
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.375),     # Hihat on 1
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.125, 0.375),   # Hihat on 3
    (38, 1.5, 0.375),     # Snare on 4
    (42, 1.5, 0.375),     # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (44, 1.5, 0.375),
    (45, 1.875, 0.375),
    (43, 2.25, 0.375),
    (42, 2.625, 0.375),
    (44, 2.875, 0.375),
    (45, 3.25, 0.375),
    (43, 3.625, 0.375),
    (42, 4.0, 0.375),
    (44, 4.25, 0.375),
    (45, 4.625, 0.375),
    (43, 5.0, 0.375),
    (42, 5.375, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.875, 0.375),  # Bb7 (Fm - 2)
    (50, 1.875, 0.375),
    (53, 1.875, 0.375),
    (55, 1.875, 0.375),
    # Bar 3
    (48, 3.25, 0.375),   # Bb7 (Fm - 2)
    (50, 3.25, 0.375),
    (53, 3.25, 0.375),
    (55, 3.25, 0.375),
    # Bar 4
    (48, 4.625, 0.375),  # Bb7 (Fm - 2)
    (50, 4.625, 0.375),
    (53, 4.625, 0.375),
    (55, 4.625, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(dr)
    # Hihat on 1
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    drums.notes.append(dr)
    # Snare on 2
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(dr)
    # Hihat on 2
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(dr)
    # Kick on 3
    dr = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(dr)
    # Hihat on 3
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(dr)
    # Snare on 4
    dr = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(dr)
    # Hihat on 4
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(dr)

# Saxophone (Dante) - short motif starting on 2, leaving it hanging until the end of bar 4
sax_notes = [
    (46, 1.875, 0.375),  # G (Fm)
    (48, 2.25, 0.375),   # Bb
    (46, 2.625, 0.375),  # G
    (44, 3.0, 0.375),    # E♭
    (46, 3.375, 0.375),  # G
    (48, 3.75, 0.375),   # Bb
    (46, 4.125, 0.375),  # G
    (44, 4.5, 0.375),    # E♭
    (46, 4.875, 0.375),  # G
    (48, 5.25, 0.375),   # Bb
    (46, 5.625, 0.375),  # G
    (44, 6.0, 0.375)     # E♭
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
