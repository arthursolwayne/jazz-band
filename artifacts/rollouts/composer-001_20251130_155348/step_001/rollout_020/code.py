
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.375),     # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.375),   # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.375),    # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line in D, chromatic approaches
bass_notes = [
    (65, 1.5, 0.375),     # D (1st beat)
    (66, 1.875, 0.375),   # Eb (2nd beat)
    (64, 2.25, 0.375),    # C (3rd beat)
    (65, 2.625, 0.375),   # D (4th beat)
    (67, 3.0, 0.375),     # E (1st beat)
    (68, 3.375, 0.375),   # F (2nd beat)
    (67, 3.75, 0.375),    # E (3rd beat)
    (69, 4.125, 0.375),   # F# (4th beat)
    (69, 4.5, 0.375),     # F# (1st beat)
    (71, 4.875, 0.375),   # G# (2nd beat)
    (70, 5.25, 0.375),    # G (3rd beat)
    (69, 5.625, 0.375)    # F# (4th beat)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.125),   # C7 (2nd beat)
    (62, 2.625, 0.125),   # C7 (4th beat)
    (62, 3.375, 0.125),   # C7 (2nd beat)
    (62, 4.125, 0.125),   # C7 (4th beat)
    (62, 4.875, 0.125),   # C7 (2nd beat)
    (62, 5.625, 0.125)    # C7 (4th beat)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - Motif: D - F# - C - E (The question)
sax_notes = [
    (62, 1.5, 0.25),      # D (1st beat)
    (67, 1.75, 0.25),     # F# (2nd beat)
    (60, 2.0, 0.25),      # C (3rd beat)
    (64, 2.25, 0.25),     # E (4th beat)
    (62, 3.0, 0.25),      # D (1st beat)
    (67, 3.25, 0.25),     # F# (2nd beat)
    (60, 3.5, 0.25),      # C (3rd beat)
    (64, 3.75, 0.25),     # E (4th beat)
    (62, 4.5, 0.25),      # D (1st beat)
    (67, 4.75, 0.25),     # F# (2nd beat)
    (60, 5.0, 0.25),      # C (3rd beat)
    (64, 5.25, 0.25)      # E (4th beat)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes_bars2_4 = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.375),     # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.375),   # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.375),    # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.375),   # Hihat on 4

    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.375),     # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.375),   # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.375),    # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.375),   # Hihat on 4

    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.375),     # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.375),   # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.375),    # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes_bars2_4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
