
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
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375),   # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (71, 3.75, 0.375),  # B
    (72, 4.125, 0.375), # C
    (74, 4.5, 0.375),   # D
    (76, 4.875, 0.375), # E
    (77, 5.25, 0.375),  # F
    (79, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.5, 0.1875),  # G7 (Bb)
    (69, 1.5, 0.1875),  # A7 (C)
    (71, 1.5, 0.1875),  # B7 (D)
    (72, 1.5, 0.1875),  # C7 (E)
    # Bar 3
    (67, 2.625, 0.1875), # G7 (Bb)
    (69, 2.625, 0.1875), # A7 (C)
    (71, 2.625, 0.1875), # B7 (D)
    (72, 2.625, 0.1875), # C7 (E)
    # Bar 4
    (67, 3.75, 0.1875),  # G7 (Bb)
    (69, 3.75, 0.1875),  # A7 (C)
    (71, 3.75, 0.1875),  # B7 (D)
    (72, 3.75, 0.1875)   # C7 (E)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875),# Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875),# Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante - Motif: D (62), F (65), G (67), Bb (69), D (62)
# Start at 1.5, then end at 5.5, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),   # D
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375), # Bb
    (62, 5.5, 0.375)    # D (hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
