
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: C - Eb - F - G (1.5 - 2.25s), leave it hanging
sax_notes = [
    (60, 1.5, 0.375),  # C
    (62, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # F
    (65, 2.625, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line (chromatic approaches, no repeated notes)
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (64, 1.875, 0.375),  # C7 (C, E, B)
    (67, 1.875, 0.375),  # E
    (71, 1.875, 0.375),  # B
    (64, 2.625, 0.375),  # C7 (C, E, B)
    (67, 2.625, 0.375),  # E
    (71, 2.625, 0.375)   # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: repeat from 1.5s, but end on Bb (3.0 - 3.375s)
sax_notes = [
    (60, 3.0, 0.375),  # C
    (62, 3.375, 0.375),  # Eb
    (64, 3.75, 0.375),  # F
    (66, 4.125, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line (chromatic approaches, no repeated notes)
bass_notes = [
    (60, 3.0, 0.375),  # C
    (61, 3.375, 0.375),  # C#
    (62, 3.75, 0.375),  # D
    (63, 4.125, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (64, 3.375, 0.375),  # C7 (C, E, B)
    (67, 3.375, 0.375),  # E
    (71, 3.375, 0.375),  # B
    (64, 4.125, 0.375),  # C7 (C, E, B)
    (67, 4.125, 0.375),  # E
    (71, 4.125, 0.375)   # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: resolve the hanging phrase on Bb (4.5 - 5.25s)
sax_notes = [
    (60, 4.5, 0.375),  # C
    (62, 4.875, 0.375),  # Eb
    (64, 5.25, 0.375),  # F
    (66, 5.625, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line (chromatic approaches, no repeated notes)
bass_notes = [
    (60, 4.5, 0.375),  # C
    (61, 4.875, 0.375),  # C#
    (62, 5.25, 0.375),  # D
    (63, 5.625, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (64, 4.875, 0.375),  # C7 (C, E, B)
    (67, 4.875, 0.375),  # E
    (71, 4.875, 0.375),  # B
    (64, 5.625, 0.375),  # C7 (C, E, B)
    (67, 5.625, 0.375),  # E
    (71, 5.625, 0.375)   # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
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
midi.write("dante_intro.mid")
