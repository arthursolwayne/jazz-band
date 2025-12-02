
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # Eb
    (65, 2.25, 0.375),  # E
    (67, 2.625, 0.375), # F
    (69, 3.0, 0.375),   # G
    (71, 3.375, 0.375), # A
    (72, 3.75, 0.375),  # A#
    (74, 4.125, 0.375), # B
    (76, 4.5, 0.375),   # C
    (77, 4.875, 0.375), # C#
    (79, 5.25, 0.375),  # D
    (81, 5.625, 0.375)  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375), # F7 on 2
    (72, 2.25, 0.375),  # A7 on 3
    (74, 2.625, 0.375), # B7 on 4
    (67, 3.375, 0.375), # F7 on 2
    (72, 3.75, 0.375),  # A7 on 3
    (74, 4.125, 0.375), # B7 on 4
    (67, 4.875, 0.375)  # F7 on 2
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - Motif
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # Eb
    (65, 2.25, 0.375),  # E
    (62, 2.625, 0.375), # D (hanging)
    (62, 3.0, 0.375),   # D (return)
    (64, 3.375, 0.375), # Eb
    (65, 3.75, 0.375),  # E
    (67, 4.125, 0.375), # F
    (69, 4.5, 0.375),   # G
    (67, 4.875, 0.375), # F
    (65, 5.25, 0.375),  # E
    (62, 5.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
