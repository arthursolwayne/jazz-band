
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
    (36, 0.0, 0.75),     # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1 & 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.75),    # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3 & 4
    (42, 1.125, 0.375),  # Hihat on 4
    (38, 1.5, 0.75)      # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (36, 1.5, 0.375),    # D (1st beat)
    (37, 1.875, 0.375),  # D# (2nd beat)
    (38, 2.25, 0.375),   # E (3rd beat)
    (39, 2.625, 0.375),  # F (4th beat)
    (41, 3.0, 0.375),    # G (1st beat)
    (42, 3.375, 0.375),  # G# (2nd beat)
    (43, 3.75, 0.375),   # A (3rd beat)
    (44, 4.125, 0.375),  # A# (4th beat)
    (45, 4.5, 0.375),    # B (1st beat)
    (47, 4.875, 0.375),  # C# (2nd beat)
    (48, 5.25, 0.375),   # D (3rd beat)
    (49, 5.625, 0.375)   # D# (4th beat)
]
for note, start, duration in bass_notes:
    nb = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nb)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (45, 1.875, 0.375),  # B7 (2nd beat)
    (49, 1.875, 0.375),
    (50, 1.875, 0.375),
    (52, 1.875, 0.375),
    # Bar 3
    (45, 3.375, 0.375),  # B7 (2nd beat)
    (49, 3.375, 0.375),
    (50, 3.375, 0.375),
    (52, 3.375, 0.375),
    # Bar 4
    (45, 4.875, 0.375),  # B7 (2nd beat)
    (49, 4.875, 0.375),
    (50, 4.875, 0.375),
    (52, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    np = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(np)

# Sax (Dante) - motif in F
sax_notes = [
    # Bar 2: Start the motif
    (53, 1.5, 0.375),    # F (1st beat)
    (55, 1.875, 0.375),  # G (2nd beat)
    (57, 2.25, 0.375),   # A (3rd beat)
    (58, 2.625, 0.375),  # A# (4th beat)
    # Bar 3: Let it hang
    (53, 3.0, 0.375),    # F (1st beat)
    (55, 3.375, 0.375),  # G (2nd beat)
    (57, 3.75, 0.375),   # A (3rd beat)
    (58, 4.125, 0.375),  # A# (4th beat)
    # Bar 4: Resolve it
    (60, 4.5, 0.375),    # C (1st beat)
    (58, 4.875, 0.375),  # A# (2nd beat)
    (57, 5.25, 0.375),   # A (3rd beat)
    (55, 5.625, 0.375)   # G (4th beat)
]
for note, start, duration in sax_notes:
    ns = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(ns)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.75),     # Kick on 1
    (42, 1.5, 0.375),    # Hihat on 1 & 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.75),    # Kick on 3
    (42, 2.25, 0.375),   # Hihat on 3 & 4
    (42, 2.625, 0.375),  # Hihat on 4
    (38, 3.0, 0.75),     # Snare on 4
    # Bar 3
    (36, 3.0, 0.75),     # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1 & 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.75),    # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3 & 4
    (42, 4.125, 0.375),  # Hihat on 4
    (38, 4.5, 0.75),     # Snare on 4
    # Bar 4
    (36, 4.5, 0.75),     # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1 & 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.75),    # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3 & 4
    (42, 5.625, 0.375),  # Hihat on 4
    (38, 6.0, 0.75)      # Snare on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
